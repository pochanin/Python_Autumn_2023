import re

def F(s, n):
    p = r"\b[0-9]\b|\b{}[0-{}]\b|\b[0-{}][0-9]\b|\b{}\b".format(n // 10, n % 10, n // 10 - 1, n)
    s = re.findall(p, s)
    return s

n = int(input('Введите двузначное число: '))
print(F('12 1 3534 35 57 58 43 38', n))