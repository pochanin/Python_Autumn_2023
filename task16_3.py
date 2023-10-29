def lower(func):
    def F1(*args, **kwargs):
        s_1 = func(*args, **kwargs)
        if isinstance(s_1, str):
            s_1 = s_1.lower()
        return s_1

    return F1


@lower
def F(s):
    return s


print(F('Hello, MY FRiend'))
