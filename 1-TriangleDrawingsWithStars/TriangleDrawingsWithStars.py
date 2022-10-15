rows=5
print("\n1.\n")

for i in range(1,rows+1):
  print("*"*i)

print("\n2.\n")
 
for i in range(rows,0,-1):
  print(i*"*")

print("\n3.\n")


for i in range(0,rows):
  for j in range(0,i+1):
    if j==0:
      print(" "*(rows-i)+"*",end="")
    else:
      print("*",end="")
  print()

print("\n4.\n")


for i in range(rows-1,-1,-1):
  for j in range(0,i+1):
    if j==0:
      print(" "*(rows-i)+"*",end="")
    else:
      print("*",end="")
  print()

print("\n5.\n")


for i in range(0,rows):
  for j in range(0,i+1):
    if j==0:
      print(" "*(rows-i)+"**",end="")
    else:
      print("*"*2,end="")
  print()

print("\n6.\n")


for i in range(rows,0,-1):
  for j in range(0,i):
    if j==0:
      print(" "*(rows-i)+"**",end="")
    else:
      print("*"*2,end="")
  print()

#shortcut to the 6. question
#rows = 5
#for i in range(rows, 0, -1):
#  print(" "*(rows-i), "*"*(i*2))

print("\n7.\n")

for i in range(1, rows + 1):
  print("*"*i +" "*((rows-i)*2) +"*"*i)
