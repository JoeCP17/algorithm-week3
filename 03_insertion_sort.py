#Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 삽입 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break


insertion_sort(input)
print(input)