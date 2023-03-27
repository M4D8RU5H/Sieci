from .ialgorithm import IAlgorithm
import math

class ExampleC(IAlgorithm):
    _name = "Przykład C"

    def encrypt(self, input: str, key: str):
        key = key.replace('\n', '')
        key = key.replace(' ', '')
        input = input.replace('\n', '')
        input = input.replace(' ', '')

        input_list = list(input)
        key_list = sorted(list(key))

        cols_num = len(key)

        matrix = []
        key_cp = key
        i = 0
        start_index = key_cp.index(key_list[0])
        while len(input_list) > 0:
            index = key_cp.index(key_list[i])
            key_cp = key_cp[:index] + '*' + key_cp[index + 1:]

            matrix += [['*'] * cols_num]

            if index == start_index:
                matrix[i][index] = input_list[0]
                chars_to_delete = 1

            elif start_index < index:
                matrix[i] = matrix[i][:start_index] + input_list[start_index: index+1] + matrix[i][index+1:]
                chars_to_delete = index - start_index + 1

            elif index < start_index:
                matrix[i] = matrix[i][:index] + input_list[index: start_index + 1] + matrix[i][start_index + 1:]
                chars_to_delete = start_index - index + 1

            input_list = input_list[chars_to_delete:]
            i += 1

        key_cp = key
        result = ""
        for i in range(cols_num):
            index = key_cp.index(key_list[i])
            key_cp = key_cp[:index] + '*' + key_cp[index + 1:]

            for row in matrix:
                char = row[index]
                if char != '*':
                    result += char

            result += ' '

        return result

    def decrypt(self, encrypted: str, key: str):
        return "Nie zaimplementowano"

    def get_name(self):
        return self._name