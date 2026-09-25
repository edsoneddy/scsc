from sys import stdin, stdout
t,x = map(str,stdin.readline().split('\n'))
t = int(t)
for i in range(t):
    q,x = map(str,stdin.readline().split('\n'))
    flag = True
    v = [] 
    for j in range(len(q)):
        c = q[j]
        if flag and q[j]!=' ':
            flag = False
            if ord(q[j])>ord('Z'):
                c = chr(ord(q[j])-32)
        elif q[j]!=' ':
            flag = True
            if ord(q[j])>=ord('A') and ord(q[j])<=ord('Z'):
                c = chr(ord(q[j])+32)
        v.append(c)
    for j in range(len(v)):
        stdout.write(v[j])
    stdout.write('\n')