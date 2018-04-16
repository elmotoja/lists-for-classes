cars = {}
line = input("Car: ")
while line:
  if line in cars:
    cars[line] +=1
  else:
    cars[line]=1
  line = input("Car: ")
  
for car in cars:
  print("Cars that are " +str(car) +":", cars[car])
