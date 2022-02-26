#Question 3:
#Create a function in Python that displays the name and results of a candidate. The function should accept the candidate's name and his/her results as "Pass/Fail." If the result is missing in the function call, show it as "Pass."

def my_function(result1, result2):
  print("Sam is " + result1)
  print("Judy is " + result2)

my_function(result1 = "Pass", result2 = "Fail")