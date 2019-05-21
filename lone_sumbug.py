def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c

print(lone_sum(1,1,1))

print(lone_sum(2,2,3))

print(lone_sum(1,2,1))

print(lone_sum(1,2,2))

print(lone_sum(1,2,3))
