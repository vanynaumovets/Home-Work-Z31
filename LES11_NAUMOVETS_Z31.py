def geop_rogress(N):
    count = 1
    p = 0
    for i in range (2, N+1):
        count += 1
        p = i+count
        yield count+p
it  =  (geop_rogress(10))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
