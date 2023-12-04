#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista = []
    for i in range(my_list):
        lista.append(my_list[i] % 2 == 0)
    return lista
