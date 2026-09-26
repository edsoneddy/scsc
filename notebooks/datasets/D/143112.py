n=int (input ())
for i in range (n):
 x=input ()
 cont=1
 nc=""
 for j in x:
  letra=j
  if letra == " ":
   nc=nc+letra
  else:
   if cont%2!=0:
    nc=nc+letra.upper ()
    cont=cont+1
   else:
    nc=nc+letra.lower ()
    cont=cont+1
 print (nc)
