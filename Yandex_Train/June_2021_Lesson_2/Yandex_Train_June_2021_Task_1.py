def check_array(arr: list) -> str:
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(check_array(arr))
