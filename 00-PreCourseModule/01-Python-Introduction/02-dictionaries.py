# # user = {
# #     "name" : "Rahul Mishra" , 
# #     "age" : 25  , 
# #     "address" : "Bangalore"
# # }

# # name = user["name"]

# # print(type(name))

# # age = user.get("age" , "Not Found")
# # print(type(age))
# # print(age)


# data = {
#     "a" : 1 , 
#     "b" : 2 
# }

# data["c"] = data.get("c" , 0) + 1 # 0 + 1 = 1 
# print(data) 

# """
# data = {
#     "a" : 1 , 
#     "b" : 2 , 
#     "c" : 1 
# }

# """

# Itarating over the dictionary : 

person = {
    "name" : "Rahul Mishra" , 
    "age" : 25 , 
    "gender" : "Male", 
    "address" : "Bangalore"
}

for key in person : 
    print(f"Key : {key}")
print("\n")
for val in person.values() :
    print(f"value : {val}")

print("\n")

#printing both 
for key , val in person.items() : 
    print(f"{key} : {val}")
