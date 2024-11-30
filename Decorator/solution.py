def strict(func):
    def wrapper(*args):
        try:
            user_types = []
            for arg in args:
                user_types.append(type(arg))

            prototype_types = []
            for key, value in func.__annotations__.items():
               prototype_types.append(value)

            matches = []
            for i in user_types:
                if i in prototype_types:
                    matches.append(i)

            if len(matches) != len(user_types):
                raise TypeError
            else:
                return func(*args)
        except TypeError:
            return TypeError
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def hello_name(name: str) -> str:
    return f"Hello {name}"
