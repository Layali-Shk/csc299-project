def inc(n: int) -> int:
    return n + 1

def main():
    print("Testing inc function:")
    print("inc(5) =", inc(5))
    print("inc(0) =", inc(0))
    print("inc(-3) =", inc(-3))

#  only run main when called directly
if __name__ == "__main__":
    main()

