import timeit

def measuring(n):
    lst = list(range(n))
    st = set(range(n))
    exists, absent = n // 2, -1

    t_lst_hit  = timeit.timeit(lambda: exists in lst, number=10_000)
    t_lst_miss = timeit.timeit(lambda: absent  in lst, number=10_000)
    t_set_hit  = timeit.timeit(lambda: exists in st,  number=10_000)
    t_set_miss = timeit.timeit(lambda: absent  in st,  number=10_000)
    return t_lst_hit, t_lst_miss, t_set_hit, t_set_miss

print(f"{'n':>8} | {'list with':>10} | {'list without':>12} | {'set with':>10} | {'set without':>10}")
for n in (1_000, 10_000, 100_000):
    r = measuring(n)
    print(f"{n:>8} | {r[0]:>10.4f} | {r[1]:>12.4f} | {r[2]:>10.4f} | {r[3]:>10.4f}")