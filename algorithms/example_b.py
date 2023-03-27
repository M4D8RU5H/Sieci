from .ialgorithm import IAlgorithm
import math

class ExampleB(IAlgorithm):
    _name = "Przykład B"
    _spaces_on = False

    def encrypt(self, input: str, key: str):
        key = key.replace('\n', '')
        key = key.replace(' ', '')
        input = input.replace('\n', '')

        if not self._spaces_on:
            input = input.replace(' ', '')

        input_length = float(len(input))
        input_list = list(input)
        key_list = sorted(list(key))

        cols_num = len(key)
        rows_num = int(math.ceil(input_length / cols_num))

        missing_chars_count = int((rows_num * cols_num) - input_length)
        input_list.extend('*' * missing_chars_count)

        matrix = [input_list[i: i + cols_num] for i in range(0, len(input_list), cols_num)]

        result = ""
        for i in range(cols_num):
            index = key.index(key_list[i])
            key = key[:index] + "*" + key[index+1:]

            for row in matrix:
                if row[index] != '*':
                    result += row[index]

            if not self._spaces_on:
                result += ' '

        return result

    def decrypt(self, input: str, key: str):
        key = key.replace('\n', '')
        key = key.replace(' ', '')
        input = input.replace('\n', '')

        input_length = float(len(input))
        input_list = list(input)

        cols_num = len(key)
        rows_num = int(math.ceil(input_length / cols_num))

        missing_chars_count = int((rows_num * cols_num) - input_length)
        input_list.extend('*' * missing_chars_count)

        matrix = [input_list[i: i + rows_num] for i in range(0, len(input_list), rows_num)]
        if not self._spaces_on:
            for row in matrix:
                if ' ' in row:
                    row.remove(' ')
                    row.extend('*' * (rows_num - len(row)))

        result = ""
        for row in range(rows_num):
            key_list = sorted(list(key))

            for c in range(cols_num):
                index = key_list.index(key[c])
                key_list[index] = '*'

                char = matrix[index][row]
                if char != '*':
                    result += char

        return result

    def get_name(self):
        return self._name
