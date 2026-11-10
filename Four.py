import sys

users = {101: "Алиса", 102: "Женя", 103: "Анна", 104: "Дима", 105: "Егор"}
print(users[103])

n = 1000
lst  = list(range(n))
tpl = tuple(range(n))
st   = set(range(n))
dct  = {i: i for i in range(n)}

print(sys.getsizeof(lst))
print(sys.getsizeof(tpl))
print(sys.getsizeof(st))
print(sys.getsizeof(dct))

x = ["x" * 1000 for _ in range(10)]
print(sys.getsizeof(x))
print(sum(sys.getsizeof(s) for s in x))