# 링크드리스트를 이용한 중복값 대처

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:  # items for문을 돌렸을때
            if key == k:  # 내가 찾고자 하는값이 동일할경우
                return v  # 해당 값을 반환해라


# 충돌방지

class LinkedDict:
    def __init__(self):
        self.items = []  # [Linked Tuple() 이 8개 들어가있음 ]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items) #이전에 했던것처럼 index값을 먼저 생성
        self.items[index].add(key,value) #이미 Linkedtuple에서 .add 메소드를 생성

    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index].get(key)

