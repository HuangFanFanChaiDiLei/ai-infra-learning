# 形参名前面加*，可以接收任意数量的位置参数，并打包成一个元组
def test1(*args): # arguments
    print(args)
    print(type(args))
    print(len(args))
    for i in args:
        print(i, end=' ')

# 形参名前面加**，可以接收任意数量的关键字参数，并打包成一个字典
def test2(**kwargs): # keyword arguments
    print(kwargs)
    print(type(kwargs))
    print(len(kwargs))
    for k, v in kwargs.items():
        print(f'{k}: {v}')

def test3(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

test1('Tim', 'male', 1.75, 70)
print()
print()
test2(name='Tim', gender='male', height=1.75, weight=70)
print()
test3('Tim', 'male', 1.75, weight = 70, age = 18)