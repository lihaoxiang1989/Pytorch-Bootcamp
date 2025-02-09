import sys


def show_sizeof(x, level=0):

    print("\t" * level, x.__class__, sys.getsizeof(x), x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


if __name__ == "__main__":
    # show_sizeof(None)  # 16
    # show_sizeof(3)  # 28
    # show_sizeof(2**63)  # 36
    # show_sizeof(102947298469128649161972364837164)  # 40
    # show_sizeof(918659326943756134897561304875610348756384756193485761304875613948576297485698417)  # 60

    show_sizeof("")
    show_sizeof("My hovercraft is full of eels")
