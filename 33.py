a, b = map(int, input().split())
saram = list(map(int, input().split()))

party = a * b

for i in saram:
    print(i - party)
