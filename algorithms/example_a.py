from .ialgorithm import IAlgorithm


class ExampleA(IAlgorithm):
    _name = "Przykład A"

    def encrypt(self, input: str, key: str):
        input = input.replace('\n', '')
        key = self.__convert_key_to_list(key)

        columns = [''] * len(key)

        for i, char in enumerate(input):
            column_index = i % len(key)
            columns[column_index] += char

        sorted_columns = [columns[i - 1] for i in key]

        result = ""
        column_index = 0
        i = 0
        while i != len(input):
            if sorted_columns[column_index] != "":
                result += sorted_columns[column_index][0]
                sorted_columns[column_index] = sorted_columns[column_index][1:]
                i += 1
            column_index = (column_index + 1) % 4

        return result

    def decrypt(self, input: str, key: str):
        input = input.replace('\n', '')
        key = self.__convert_key_to_list(key)

        columns = [""] * len(key)
        for char_count in range(len(input)):
            columns[char_count % 4] += "*"

        char_count = 0
        i = 0
        while char_count != len(input):
            column_index = key[i % 4] - 1
            if columns[column_index][0] == "*":
                columns[column_index] = columns[column_index][1:]
                columns[column_index] += input[char_count]
                char_count += 1
            i += 1

        result = ""
        char_count = 0
        while char_count != len(input):
            column_index = char_count % 4
            result += columns[column_index][0]
            columns[column_index] = columns[column_index][1:]
            char_count += 1

        return result

    @staticmethod
    def __convert_key_to_list(key: str):
        numbers = key.split("-")
        numbers = [int(num) for num in numbers]

        return numbers

    def get_name(self):
        return self._name
