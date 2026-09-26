n_max = int(input())
crible = {}
for k in range(2, n_max + 1):
    crible[k] = True

i = 2
while i * i <= n_max:
    if crible.get(i, False):
        j = i * i
        while j <= n_max:
            crible[j] = False
            j += i
    i += 1

encontrados = [str(k) for k, v in sorted(crible.items()) if v]
print(" ".join(encontrados))
