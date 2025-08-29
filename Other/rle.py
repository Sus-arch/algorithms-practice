def rle(s):
    new_s = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count != 1:
                new_s.append(s[i - 1] + str(count))
                count = 1
            else:
                new_s.append(s[i - 1])

    if count != 1:
        new_s.append(s[i] + str(count))
    else:
        new_s.append(s[i])

    return "".join(new_s)


if __name__ == "__main__":
    print(rle(input()))

