def analyzer():
  marks = list(map(int, input("enter the marks : ").split()))
  #finding maximum and the minimum marks
  maximum = marks[0]
  minimum = marks[0]
  
  for m in marks:
    if m < minimum:
      minimum = m
    if m > maximum:
      maximum = m
      
    print("Highest marks:", highest)
    print("Lowest marks:", lowest)
    
marks_analyzer()
