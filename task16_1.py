import re

def F(s):
    s = s.upper()
    s = re.sub(r'\B\w', '', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = s.replace(' ', '')
    return s
print(F('Институт, точной+ механики оптики!'))