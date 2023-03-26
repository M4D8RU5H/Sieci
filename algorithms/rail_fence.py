from .ialgorithm import IAlgorithm


class RailFence(IAlgorithm):
    _name = "Rail Fence"

    def encrypt(self, input: str, key: str):
        if len(input) <= 1:
            raise ValueError("This input value is not allowed")

        if len(key) < 1:
            raise ValueError("This key value is not allowed")

        try:
            key = int(key)
        except Exception as e:
            raise e

        input = input.replace('\n', '')

        fence = [""] * key
        row = 0
        direction = 1

        for char in input:
            fence[row] += char
            row += direction
            if row == 0 or row == key - 1:
                direction = -direction

        return "".join(fence)

    def decrypt(self, input: str, key: str):
        if len(input) <= 1:
            raise ValueError("This input value is not allowed")

        if len(key) < 1:
            raise ValueError("This key value is not allowed")

        try:
            key = int(key)
        except Exception as e:
            raise e

        input = input.replace('\n', '')

        fence = [""] * key
        row = 0
        direction = 1

        for i in range(len(input)):
            fence[row] += "*"
            row += direction
            if row == 0 or row == key - 1:
                direction = -direction

        index = 0
        for i in range(key):
            for j in range(len(fence[i])):
                if fence[i][j] == "*":
                    fence[i] = fence[i][:j] + input[index] + fence[i][j+1:]
                    index += 1

        result = ""
        row = 0
        direction = 1
        for i in range(len(input)):
            result += fence[row][0]
            fence[row] = fence[row][1:]
            row += direction
            if row == 0 or row == key - 1:
                direction = -direction

        return result

    def get_name(self):
        return self._name


