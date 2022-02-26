#Question 4:
#We have a list of numbers given below. Write a Python function to print all the odd-indexed items from the list.
test_list = [2, 3, 5, 6, 8, 9]

odd_i = []
even_i = []
for i in range(0, len(test_list)):
  if i % 2:
    even_i.append(test_list[i])
  else:
    odd_i.append(test_list[i])

res = even_i

# print result
print(res)
