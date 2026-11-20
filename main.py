def find_first_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] == 0:
                return i, j

    return None


def main():
    m = int(input("Введите количество строк: "))
    n = int(input("Введите количество столбцов: "))

    if m <= 0 or n <= 0:
        print("Размеры матрицы должны быть положительными.")
        return

    matrix = []

    for i in range(m):
        while True:
            try:
                row = list(map(float, input(
                    f"Введите элементы строки {i + 1}: "
                ).split()))

                if len(row) != n:
                    print(f"Необходимо ввести ровно {n} элементов.")
                    continue

                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: вводите только числа.")

    result = find_first_zero(matrix)

    if result is None:
        print("Нулевых элементов в матрице нет.")
    else:
        i, j = result
        print(f"Индексы первого нуля: [{i}][{j}]")
        print(f"Строка: {i + 1}, столбец: {j + 1}")


if __name__ == "__main__":
    main()