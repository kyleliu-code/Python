"""
fibonacci sequence principle:

F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) n >=2 int
1,1,2,3...
"""
# 10 以内的fibonacci seqence
# a, b = 0, 1
# while b < 10 :
#     print(b)
#     a, b = b, a + b


# 求对应位置的 fibonacci seqence

def fibonacci (n) :
    if n <=2:
        print("当前n 为：",n,1)
    else:
        a, b, i = 1, 1,0
        while i < n-2:
            i += 1
            a, b = b, a+b
            # print(b)
        print("当前n 为：", n, b)
# fibonacci(1)
# fibonacci(2)
# fibonacci(3)
# fibonacci(4)
# fibonacci(5)
# fibonacci(6)
# fibonacci(7)


# fibanacci 的 第二种写法

def fibonacci_for(n):
    if n <= 2:
        print('当前n为： ', n,1)
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b ,a+b
        print("当前n为：",n,b)


fibonacci_for(1)
fibonacci_for(2)
fibonacci_for(3)
fibonacci_for(4)
fibonacci_for(5)
fibonacci_for(6)
fibonacci_for(7)