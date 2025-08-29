def main():
    length_first, width_first, length_second, width_second = map(int, input().split())

    size_one = size_two = 1001
    min_squeare = 2 * size_one * size_two

    if length_first < width_first:
        length_first, width_first = width_first, length_first
    if length_second < width_second:
        length_second, width_second = width_second, length_second

    # Горизонтально поставить правее
    if (max(width_first, width_second) * (length_first + length_second)) < min_squeare:
        min_squeare = (max(width_first, width_second) * (length_first + length_second))
        size_one = max(width_first, width_second)
        size_two = length_first + length_second

    # Вертикально поставить правее
    if (max(width_first, length_second) * (length_first + width_second)) < min_squeare:
        min_squeare = (max(width_first, length_second) * (length_first + width_second))
        size_one = max(width_first, length_second)
        size_two = length_first + width_second

    # Горизонтально поставит ниже
    if (max(length_first, length_second) * (width_first + width_second)) < min_squeare:
        min_squeare = (max(length_first, length_second) * (width_first + width_second))
        size_one = max(length_first, length_second)
        size_two = width_first + width_second

    # Вертикально поставить ниже
    if (max(length_first, width_second) * (width_first + length_second)) < min_squeare:
        size_one = max(length_first, width_second)
        size_two = width_first + length_second

    print(size_one, size_two)


if __name__ == '__main__':
    main()
