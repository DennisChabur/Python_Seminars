import ui_c
from calculations import sum_c, sub_c, mult_c, div_c


inputed_sign = ui_c.input_c
converted_to_list_of_complex = list(map(complex, filter(lambda x:
                                x not in '+-*/', inputed_sign())))


def check_action(inputed_sign):
    if inputed_sign[1] == '+': return sum_c
    elif inputed_sign[1] == '-': return sub_c
    elif inputed_sign[1] == '*': return mult_c
    elif inputed_sign[1] == '/': return div_c


def check_c(list_of_complex):
    if (type(list_of_complex[0]) == complex) and \
            list_of_complex[1] in '+-*/' and \
            (type(list_of_complex[2]) == complex):
        return True
    else:
        print("Некорректный ввод")
        return False
