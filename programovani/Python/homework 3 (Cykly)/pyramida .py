high_pyramid = int(input("enter the desired height of the pyramid"))
i = 1
while i < high_pyramid:
  print((high_pyramid-i)*" ", (1+2*(i-1))*"*")
  i += 1
