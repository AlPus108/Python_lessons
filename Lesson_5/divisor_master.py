# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:

# if __name__ == '__main__':

# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);

def prime_num(n):
    div = 2
    while n % div != 0:
        div += 1
    if div == n:
        print(f'Число {n} простое')
    else:
        print(f'Число {n} составное')
    # return res



# 2) выводит список всех делителей числа;

def div_list(n):
    d_list = []
    for i in range(1, n + 1, 1):
        if n % i == 0:
            d_list.append(i)
    return d_list


# 3) выводит самый большой простой делитель числа.

# def max_div(n):
#     max_num = 0
#     for i in div_list(n):
#         if i > max_num:
#             max_num = i
#     return max_num

def max_div(n):
    max_num = div_list(n)
    return max_num[-1]