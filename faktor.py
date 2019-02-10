from math import ceil
A,I = map(int,input().split())

aux=A*I
while ceil(aux/A)>=I:aux-=1  """La funcion ceil() Devuelve el valor mas"""

print(aux+1)	