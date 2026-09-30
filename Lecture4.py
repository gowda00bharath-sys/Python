# # this is lecture 3 for dictionary and sets
# info={
#   "key":"value",
#   "name":"Bharath",
#   "cgpa":7.5,
#   "subject":["Maths","DSA"],
#   "tup":("dic","set"),
#   "marks":32.32
# }
# print(info)
# print(len(info))
# info["name"]="gunda"
# print(info)
# info["surname"]="gowda"
# print(info)

# #Method of dict

# student={
#   "name":"Bharath",
#   "subject":{
#     "DSA":100,
#     "Math":200,
#     "phy":122
#   }
# }
# print(student)
# print(student.keys())
# print(student.values())
# print(student["subject"])
# print(student["subject"]["DSA"])
# print(type(student.items()))
# print(student.get("name"))
# print(student["name"])
# student.update({"name":"gowda"})
# print(student.get("name"))

# Set in python

# collection={1,2,23,4,2,"hello","Hello",4}
# print(type(collection))
# print(len(collection))

# new_col={54,"hello"}
# print(type(new_col))


# #Methods of Set

# new_col.add(22)
# new_col.add(1)
# print(new_col)
# new_col.add(2)
# print(len(new_col))
# print(new_col)
# new_col.pop()
# print(len(new_col))
# print(new_col)

# set1={1,2,3}
# set2={3,4,5}

# print(set1.union(set2))
# print(set1.intersection(set2))

# program 1

# dict1={
#   "table":["a peice of furniture","list of fact and figure"],
#   "cat":"a small animal"
# }
# print(dict1)

# # #program 2

# # st1={"python","java","c++","java","python","c","c++","java","pyhton"}
# # print(len(st1))

# #program 3

# dict1={
#   "phy":input("enter the marks of phy"),
#   "chem":input("enter the marks of chem"),
#   "math":input("enter the marks of maths")
# }

# dict2={}
# print(type(dict2))

# dict2.update({"math":input("enter the marks of maths ")})
# dict2.update({"phy":input("enter the marks of phy")})
# dict2.update({"chem":input("enter the marks of chem")})
# print(dict2)

# program4

# set1=set()

# set1.add(9)
# set1.add("9.0")
# print(set1)
