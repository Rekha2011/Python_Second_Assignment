#Question 2:
#Write a Python function that accepts two arguments and calculates the addition and subtraction of it. Also, print both the arithmetic results in a single return call.
Input1 = [30]
Input2 = [50]
Output = []

for i in range(len(Input1)):
    if Input1[i] > Input2[i]:
        Output.append(Input1[i] - Input2[i])
    else:
        Output.append(Input1[i])

print("\nOutput list is")
print(Output)