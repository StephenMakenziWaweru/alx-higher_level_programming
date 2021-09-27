#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = [0] * list_length

    while i < list_length:
        try:
            res[i] = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")

        finally:
            i += 1
    return res
