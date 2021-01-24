# Q. 괄호가 바르게 짝지어졌다는 것은 '('
# 문자로 열렸으면 반드시 짝지어서 ')'
# 문자로 닫혀야 한다는 뜻이다. 예를 들어

# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.

# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

# 짝수 = True
# 거짓 = False 반환

# ( , )의 개수가 각각 몇개인지 파악해야한다.
# 스택으로한다면?


s = "(())()"


def is_correct_parenthesis(string):
    stack_string = []  # 괄호를 저장할 빈 스택 지정

    for char in range(len(string)):  # string의 범위만큼 반복
        if string[char] == '(':  # 만약 (가 있다면
            stack_string.append(char)  # 스택에 하나씩 저장
        elif string[char] == ')':  # )가 들어오게된다면
            if len(stack_string) == 0:  # if를 통해 만약 스택에 아무것도 들어있지않으면
                return False
            stack_string.pop()

    if len(stack_string) == 0:  # 지정한 스택이 0과 일치할시
        return True
    else:  # 그게 아닐시
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
