from classes import *


def main():
    strands = [Strand(value=1.0 * j) for j in range(1, 5)]

    def f1(e: E):
        return strands[e.value]

    def f2(e: E):
        return strands[2 + e.value]

    def f3(e: E):
        return Strand(value=100.0 + e.value)

    t1 = Tassel(func=f1)
    t2 = Tassel(func=f2)
    t3 = Tassel(func=f3)

    strands[1].next_tassel = t2
    strands[3].next_tassel = t3

    for s in t1:
        print(s)


if __name__ == "__main__":
    main()
