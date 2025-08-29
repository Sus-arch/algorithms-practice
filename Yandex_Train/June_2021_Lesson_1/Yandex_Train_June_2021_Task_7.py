def main():
    alloy, workpiece, detail = map(int, input().split())

    def get_count_details(alloy_rest):
        if alloy_rest < workpiece or workpiece < detail:
            return 0

        workpiece_count = alloy_rest // workpiece
        alloy_rest %= workpiece
        detail_count = (workpiece // detail) * workpiece_count
        alloy_rest += (workpiece % detail) * workpiece_count

        return detail_count + get_count_details(alloy_rest)

    print(get_count_details(alloy))


if __name__ == '__main__':
    main()
