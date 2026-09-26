n=int (input ())
for i in range (n):
 a=input ()
 cont=1
 nc=""
 for j in a:
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