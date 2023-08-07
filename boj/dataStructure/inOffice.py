import sys
input = sys.stdin.readline

office = set()

n = int(input().strip())

for _ in range(n):
    name, log = input().split()

    if log == "enter":
        office.add(name)
    else:
        office.remove(name)

office = list(office)
office.sort(reverse=True)
for name in office:
    print(name)