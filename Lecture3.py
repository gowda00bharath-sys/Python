# # Lectuer Three in which we learn List and Tuples

# marks=[24.2,32.32,32.32,244.3,23,12]
# print(marks)
# marks.remove(32.32)
# print(marks)
# print(marks.pop(2))
# print(marks)

# student=["Bharath","Placed",1000000,8.07]
# print(len(student))
# print(type(student))
# student[0]="divya"
# print(student)


# # print(student[3])

# # Slicing

# # str="apna college"
# # print(str[1:4])
# # print(str[:5])
# # print(str[3:])
# # print(str[1:len(str)])


# #List Methods()

# student.append("Skilled")
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# student.reverse
# student.insert(3,"working")
# print(student)


#tuples

# tup=(1,"String")# this are tuples that are packed with parantesis
# print(type(tup))
# print(tup.index("String"))
# print(len(tup))


# Program 1

# movies=[]
# movies.append(input(" enter the 1st movie "))
# movies.append(input(" enter the 2nd movie"))
# movies.append(input(" enter the 3rd movie"))
# print(movies)


#program 2

# pal1=[1,2,1]

# pal2=[1,"abc","abd",1]

# copy_pal=pal2.copy()
# copy_pal.reverse()
# if(copy_pal==pal2):
#     print("Plaindrom")
# else:
#     print("NOT palindrom")


#PROGRAM 3
student=["A","B","C","A","B","A","B","A","A"]
print(student.count("A"))