def main():
    def find_entrance_and_floor():
        apps_first, floor_count, apps_second, entrance_second, floor_second = map(int, input().split())
        if floor_second > floor_count:
            return "-1 -1"

        if entrance_second == 1 and floor_second == 1:
            if apps_first <= apps_second:
                return "1 1"
            floor_first = 0
            if floor_count == 1:
                floor_first = 1
            entrance_first = 0
            if apps_first <= floor_count * apps_second:
                entrance_first = 1
            return f"{entrance_first} {floor_first}"

        valid_apps_per_floor = []
        know_flat_floor = (entrance_second - 1) * floor_count + floor_second

        for apps_per_floor in range(1, apps_second + 1):
            computed_floor = (apps_second - 1) // apps_per_floor + 1
            if computed_floor == know_flat_floor:
                valid_apps_per_floor.append(apps_per_floor)

        if not valid_apps_per_floor:
            return "-1 -1"

        candidate_floors = list(set((apps_first - 1) // apps_per_floor + 1 for apps_per_floor in valid_apps_per_floor))
        candidate_entrances = [(floor - 1) // floor_count + 1 for floor in candidate_floors]
        adjusted_floors = [floor - (entrance - 1) * floor_count for floor, entrance in zip(candidate_floors, candidate_entrances)]

        entrance_result = candidate_entrances[0] if len(set(candidate_entrances)) == 1 else 0
        floor_result = adjusted_floors[0] if len(set(adjusted_floors)) == 1 else 0

        return f"{entrance_result} {floor_result}"

    print(find_entrance_and_floor())


if __name__ == '__main__':
    main()
