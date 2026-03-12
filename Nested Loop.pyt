# Loops in python - Nested Loop



for i in range(3):
    for num in range(1,4):   #1
        print(num)   
    print("___")
 


hj = 1
while i < 4:
    for j in range(1,4):     #2
        print(j)
    print("---")
    i += 1




# print prime numbers between range of 2 to 10 using nested loop :

for back in range(2,10):
    for common in range(2,back):
        if back % common == 0:
           break  
    else:   
        print(back)  


