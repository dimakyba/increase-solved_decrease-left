def mod_exp(a, m, c):
    counter = 0;
    b = a
    res = 1.0
    print(f"{counter}) b = {b}, m = {m}, res = {res} (Before loop start)")
    counter += 1

    while m > 0:
        if m % 2 == 1:
            res *= b
            res %= c
            print(f"{counter}) b = {b}, m = {m}, res = {res} (Odd m, update res)")
            counter += 1
        m //= 2
        b *= b
        b %= c
        print(f"{counter})b = {b}, m = {m}, res = {res}")
        counter += 1

    return res

# a = 5377
# m = 6200
# c = 6296

a = 5860
m = 6802
c = 6331

result = mod_exp(a, m, c)
print(f"Main result: ({a}^{m}) mod {c} = {result}")
