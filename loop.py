# i=0
# while i<6:
#     print("Bangladesh")
#     break
#     if i==5:
#         i+=1


# a=[10,5,12,"Bangla"]

# for i in a :
#     print(i)

# for i in range(0,100,2):
#     print(i)

# a=8
# for i in range(0,a):
#     for j in range(0,i+1):
#         print("*", end='')
#     print('\r')

a=8
for i in range(a,0,a-1):
    for j in range(0,i-1):
        print("*", end=' ')
    print('\r')