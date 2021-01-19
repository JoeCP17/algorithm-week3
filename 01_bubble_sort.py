# 그러면 이제 한 번 구현하러 가볼게요!
#
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 버블 정렬을 이용해서 정렬하시오.


input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    length = len(array)

    for i in range(length): # n의 길이
        for j in range(length - i - 1): # n 의 길이
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!


#시간 복잡도 : O(N2) <- O의 N제곱
