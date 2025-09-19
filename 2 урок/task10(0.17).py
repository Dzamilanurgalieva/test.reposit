num = input()
numl = list(num)
numl1 = numl
count = 0
if "-" in numl:
    numl1 = numl[1:]

while numl1:
    count += 1
    print(count)
    numl1 = numl1[1:]

print(count)

