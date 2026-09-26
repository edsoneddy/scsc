def parentesis(n, abi=0, cer=0, sec="", res=None):
    if res is None:
        res = []
    
    if len(sec) == 2 * n:
        res.append(sec)
        return

    if abi < n:
        parentesis(n, abi + 1, cer, sec + "(", res)
    
    if cer < abi:
        parentesis(n, abi, cer + 1, sec + ")", res)
    
    return res

def main():
    try:
        while True:
            n = int(input())
            sec = parentesis(n)
            for secu in sec:
                print(secu)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
