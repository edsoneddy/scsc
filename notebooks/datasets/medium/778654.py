for i in range(int(input())):
  palabra=input()
  contador=0
  nuevapalabra=""
  for j in palabra:
    if j ==" ":
      nuevapalabra += " "
      continue
    contador+=1
    if contador%2==0:
      nuevapalabra+= j.lower()
    else:
      nuevapalabra+= j.upper()
  print(nuevapalabra)