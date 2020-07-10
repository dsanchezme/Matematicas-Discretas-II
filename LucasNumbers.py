#Lucas Numbers Generation
#by Diego Sanchez

#Defining the function
def Lucas(n):
  if(n==0):
    return 2
  elif(n==1):
    return 1
  return Lucas(n-1)+Lucas(n-2)

#Solving first question
#What is the eighteenth Lucas number?

print("El 18-th número de Lucas: ", Lucas(17))


#Solving second question
#What is the nearest Lucas number to 1000?

n=0

while(Lucas(n)<1000):
  n+=1

if(abs(Lucas(n-1)-1000)>abs(Lucas(n)-1000)):
  ans = Lucas(n)
else:
  ans = Lucas(n-1)

print("El número de Lucas más cercano a 1000: ", ans)


#Solving third question
#What is the first Lucas number greater than 1000?

n=0

while(Lucas(n)<100):
  n+=1

print("El primer número de Lucas más grande que 100: ", Lucas(n))
