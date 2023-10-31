def F(s):
    s_1 = ''
    M = []
    N = []
    for i in range(len(s)):
        if s[i].isalpha():
            s_1 += s[i]
        elif s[i - 1].isalpha():
            if s_1 in M:
                N.append(s_1)
            else:
                M.append(s_1)
            s_1 = ''
    if s_1 in M:
        N.append(s_1)
    else:
        M.append(s_1)
    for i in N:
        if i !=' ':
            s = s.replace(i, '', 1)
    while '  ' in s:
        s = s.replace('  ', ' ')

    print(s)

s = input('Введите строку: ')
F(s)
