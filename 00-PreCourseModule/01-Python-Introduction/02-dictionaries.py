# # # user = {
# # #     "name" : "Rahul Mishra" , 
# # #     "age" : 25  , 
# # #     "address" : "Bangalore"
# # # }

# # # name = user["name"]

# # # print(type(name))

# # # age = user.get("age" , "Not Found")
# # # print(type(age))
# # # print(age)


# # data = {
# #     "a" : 1 , 
# #     "b" : 2 
# # }

# # data["c"] = data.get("c" , 0) + 1 # 0 + 1 = 1 
# # print(data) 

# # """
# # data = {
# #     "a" : 1 , 
# #     "b" : 2 , 
# #     "c" : 1 
# # }

# # """

# # Itarating over the dictionary : 

# person = {
#     "name" : "Rahul Mishra" , 
#     "age" : 25 , 
#     "gender" : "Male", 
#     "address" : "Bangalore"
# }

# for key in person : 
#     print(f"Key : {key}")
# print("\n")
# for val in person.values() :
#     print(f"value : {val}")

# print("\n")

# #printing both 
# for key , val in person.items() : 
#     print(f"{key} : {val}")

#Nested dictionary 
users = {
    "alice": {
        "email": "alice@example.com",
        "age": 30
    },
    "bob": {
        "email": "bob@example.com",
        "age": 25
    }
}

age = users["alice"]["age"]
print(age)

alice = users.get("alice" , {})
alice_age = alice.get("age" , {})
print(alice_age)