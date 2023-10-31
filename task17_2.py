def up(func):
    def remake(*args, **kwargs):
        up_args = [arg.upper() for arg in args if isinstance(arg,str)]
        up_kwargs = {key: value.upper() for key, value in kwargs.items() if isinstance(value,str)]}

        return func(*up_args, **up_kwargs)

    return remake

@up
def F(*args, **kwargs):
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

F(14,'aaa', 'Hello World', count='bbb', count_1=1)