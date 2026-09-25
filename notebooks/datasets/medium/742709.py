def solve(cases):
    for case in cases:
        #case=case.replace(' ','')
        ans=''
        T=1
        for e in case:
            if e==' ':
                ans=ans+e
            else:
                if T==1:
                    if not 65<=ord(e)<=90:
                        ans=ans+str(chr(ord(e)-32))
                    else:
                        ans=ans+e
                else:
                    if not 97<=ord(e)<=122:
                        ans=ans+str(chr(ord(e)+32))
                    else:
                        ans=ans+e
                T=1-T
        print(ans)    

l=[]
for _ in range(int(input())):
    l.append(str(input()))
solve(l)
