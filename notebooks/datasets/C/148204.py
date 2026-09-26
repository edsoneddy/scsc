def print_all_parens(n):
    def print_parens(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            print_parens(left + 1, right, s + "(")
        if right < left:
            print_parens(left, right + 1, s + ")")
 
    print_parens(0, 0, "")
while(True):
    n= int(input())
    print_all_parens(n)