def get_conanic_number(number: str):
    number = number.replace("-", "").replace("(", "").replace(")", "")
    if number.startswith("8"):
        number = number[1:]
    elif number.startswith("+7"):
        number = number[2:]
    if len(number) != 10:
        number = "495" + number
    return number

new_number = input()
new_conanic_number = get_conanic_number(new_number)
for _ in range(3):
    if get_conanic_number(input()) == new_conanic_number:
        print("YES")
    else:
        print("NO")