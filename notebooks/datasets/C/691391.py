import sys
def genParent(n):
    def Backtracking(s="", l=0, r=0):
        if len(s) == 2 * n:
            parentsis.append(s)
            return
        if l < n:
            Backtracking(s + "(", l + 1, r)
        if r < l:
            Backtracking(s + ")", l, r + 1)
    parentsis = []
    Backtracking()
    return parentsis

for i in sys.stdin:
     if i == "\n":
          break
     n = int(i)
     secs = genParent(n)
     for sec in secs:
            print(sec)