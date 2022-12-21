from rectangle import rectangle
from circle import circle
from square import square


def main():
    r = rectangle("синего", 3, 2)
    c = circle("зеленого", 5)
    s = square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()