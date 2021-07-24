# This is task 1.

def print_hello() -> str:
    """если введенное число больше 7, то вывести “Привет”"""
    answer = input("Please, enter a number: \n")
    if answer.isdigit():
        num = int(answer)
        if num > 7:
            return "Привет"
    else:
        return "It is not a number!"


# This is task 2.
def name() -> str:
    """если введенное имя совпадает с Вячеслав, то вывести
     “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"
    """
    my_name = "вячеслав"
    answer = input("Please, enter a name: \n")
    if answer.lower() == my_name:
        return "Привет, Вячеслав"
    else:
        return "Нет такого имени"


# This is task 3.
def num_sort():
    """на входе есть числовой массив,
     необходимо вывести элементы массива кратные 3
     """
    print("Please, enter numbers\n(to stop entering numbers write 'stop'):")
    list_num = []
    while True:
        num = input()
        if num.lower() == "stop":
            break
        if num.isdigit():
            num = int(num)
            if num % 3 == 0:
                list_num.append(str(num))
        else:
            print("It is not a number!")
    if len(list_num):
        return " ".join(list_num)
    else:
        return "There are no multiples of 3"


if __name__ == '__main__':
    print(print_hello())
    print("--------------------")
    print(name())
    print("--------------------")
    print(num_sort())
