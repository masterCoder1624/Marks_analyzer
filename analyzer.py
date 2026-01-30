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

   #finding the average of all the marks
  total = 0
  count = 0
  for m in marks:
    total = total + m
    count += 1
  average = total / count
  print("the average of the marks is : " , average)

  #searching an element
  target = int(input("Enter the marks to search: "))
  for i in range(len(marks)):
    if marks[i] == target:
      print(f"Marks {target} found at index {i}")
          break
    else:
      print(f"Marks {target} not found in the list.")
    
marks_analyzer()
