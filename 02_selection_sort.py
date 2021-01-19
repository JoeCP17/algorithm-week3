# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 선택 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]


# 배열의 크기만큼 반복했다가 -1씩 줄어듬

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(5 - i):  # 한개씩 줄어드는 구조
            if array [ i + j ] < array[min_index]:
                min_index = i + j
                array[i] , array[min_index] = array[min_index] , array[i]
            print(i + j)
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
