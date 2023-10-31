import itertools

for i in range(1, 7):
    for j in itertools.combinations([50, 100, 200, 500, 1000, 5000], i):
        print(sum(j))