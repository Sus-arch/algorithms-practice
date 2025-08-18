temp_room, temp_cond = map(int, input().split())
mode = input()
match mode:
    case "freeze":
        if temp_cond > temp_room:
            print(temp_room)
        else:
            print(temp_cond)
    case "heat":
        if temp_cond < temp_room:
            print(temp_room)
        else:
            print(temp_cond)
    case "auto":
        print(temp_cond)
    case "fan":
        print(temp_room)