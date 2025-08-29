def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    def check_size():
        if (a <= d and (b <= e or c <= e)) or (a <= e and (b <= d or c <= d)):
            return "YES"
        elif (b <= d and (a <= e or c <= e)) or (b <= e and (a <= d or c <= d)):
            return "YES"
        elif (c <= d and (a <= e or b <= e)) or (c <= e and (a <= d or b <= d)):
            return "YES"
        return "NO"

    print(check_size())


if __name__ == "__main__":
    main()
