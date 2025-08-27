def main():
    interval_first = int(input())
    interval_second = int(input())
    train_first = int(input())
    train_second = int(input())

    min_time_first = train_first * (interval_first + 1) - interval_first
    max_time_first = train_first * (interval_first + 1) + interval_first

    min_time_second = train_second * (interval_second + 1) - interval_second
    max_time_second = train_second * (interval_second + 1) + interval_second

    min_time = max(min_time_first, min_time_second)
    max_time = min(max_time_first, max_time_second)

    if min_time > max_time:
        print(-1)
    else:
        print(min_time, max_time)


if __name__ == "__main__":
    main()
