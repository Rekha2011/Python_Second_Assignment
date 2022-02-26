#Question 7:
#Write a Python function to find 'Mall' from the dictionary 'map_details' given below.
map_details = {101:'Park', 102:'Zoo', 103:'Mall'}

key_list = list(map_details.keys())
val_list = list(map_details.values())

print(list(map_details.keys())[list(map_details.values()).index('Mall')])
