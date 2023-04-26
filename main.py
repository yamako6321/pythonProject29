A = int(input())
B = int(input())
R = int(input())
M = int(input())
if A < B:
    d = B
    k = A
else:
    d = A
    k = B
if R < d - R:
    x = R
else:
    x = d - R
if M < d - M:
    y = M
else:
    y = d - M
if x < y:
    print(x)
else:
    print(y)
