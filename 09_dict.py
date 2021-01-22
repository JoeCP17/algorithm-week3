class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)  # index = 해쉬를통한 key값 처리한 값에서 iteems의 최대 길이의 나머지 값
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index]



my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
