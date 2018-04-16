count={}
line = input("Enter line: ")
while line:
  words = line.split()
  for w in words:
    if w in count:
      count[w] +=1
    else:
      count[w] = 1
  line = input("Enter line: ")
  
for word in sorted(count): # here sorted() is used 
  print(word, count[word])