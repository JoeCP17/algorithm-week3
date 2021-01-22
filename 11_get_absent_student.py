#해시 문제


# Q. 오늘 수업에 많은 학생들이 참여했습니다.
# 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때,
# 출석하지 않은 학생의 이름을 반환하시오.


all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    student_dict = {} # 딕셔너리를 생성한 후
    for key in all_array: # 모든 학생들을 딕셔너리에 넣어준다.
        student_dict[key] = True

    for key in present_array: # 모든 학생이름을 알고있는 key가 present_array를 돌면서
        del student_dict[key] #present_array에 있는 학생 이름을 하나씩 지운다.

    for key in student_dict.keys(): #그후 키를 다시 반복해서
        return key #남아있는 학생 반환


#시간복잡도 : O(N)
print(get_absent_student(all_students, present_students))

#해쉬테이블은 , 시간 복잡도는 극소화 할수있지만, 공간을 많이사용한다.