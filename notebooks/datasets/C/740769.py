def jeneraxd(abiertas, cerradas, n, metele_nomas):
    if abiertas == n and cerradas == n:
        print(metele_nomas)
        return
    if abiertas < n:
        jeneraxd(abiertas + 1, cerradas, n, metele_nomas + "(")
    if cerradas < abiertas:
        jeneraxd(abiertas, cerradas + 1, n, metele_nomas + ")")
try:
    while True:
        deuna = input().strip()
        if deuna == "":
            break
        enie = int(deuna)
        jeneraxd(0, 0, enie, "")
except EOFError:
    pass