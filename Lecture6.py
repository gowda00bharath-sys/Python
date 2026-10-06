
#fountion decleartion
# def cla_sum(a,b): #argumnet
#   return a+b

# sum=cla_sum(1,2) #calling the function
# print(sum)

# count=cla_sum(5,6) #calling the function
# print(count)


# def print_hel(): # without parameter
#   print("hello")

# output=print_hel()

# print(output)

# print_hel()#no argument

# print_hel()

#program

# def avg(a,b,c):
#   avg_num=(a+b+c)/3
#   return avg_num

# call=avg(1,2,3)
# print(call)

#default constructor

# def calu_pro(a=1,b=1):#default paramter
#     print(a*b)
#     return a*b


# calu_pro(2,2)#argumnet passed

#program

# def length(list):
#     print(len(list))
#     return len(list)

# list=["student","100","81.92","muway"]
# print(list)

# tup=("student","100","81.92","muway","100")
# print(tup)

# length(tup)

#program

# def line(listaaa):
#     for i in listaaa:
#         print(i,end=" ")

# tup=("student","100","81.92","muway","100")

# line(tup)

#program

# def fac(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial*=i

#     print(factorial)
#     return factorial

# fac(3)

# def ruppee_con():
#     usd=int(input("enter the usd amoount"))
#     print(usd*96)
#     return usd*96

# ruppee_con()

#program

# def guess(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")

# guess(3)

#programm 

# def rec(n):
#   if(n==0):
#     return
#   print(n,end=" ")
#   rec(n-1)

# rec(5)

# factorial recursion

# def fac(n):
#   if(n==0):
#     return 1
#   return n*fac(n-1)

# print(fac(5))

# list =["bharath","100","placed","working","software engineer"]

# def recu(sow,n):
#   if(n==-1):
#     return
#   print(sow[n]) 
#   recu(sow,n-1)

# recu(list,4)
 #

#program recursion


# def sum(n):
#   if(n==0):
#     return 0
#   return sum(n-1) + n

# summ=sum(5)

# print(summ)