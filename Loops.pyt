# Loops in python - while & for loop

# while loop

count = 0

while count < 5:
    print(count)             #1
    count = count + 1 




count_ = 5
while count_ > 0:
    print(count_)          #2
    count_ -= 1




count1 = 5
while count1 > 0:
    print(count1)
    count1 -= 1             #3
else:
    print("while loop endel")




password = ""

while password != "1234":
    password = input("Enter password: ")     #4

print("Access Granted")


#_________________________________ for loop



language = 'python'
for x in language:
    print(x)



for p in range(5):
    print(p)
          


for y in range(5,10):
    print(y)



for u in range(1,10,2):
    print(u)



for e in range(5):
    print(e)
else:
    print("for loop ended")



#_________________________________ loop control statements    # pass statement
                                  

for j in range(5):
   pass




count5 = 5
while count5 > 0 :
    if count == 3:
       pass
    else:
        print(count5)
    count5 -= 1


#__________________________________Loop control - break statement

for t in range(5):
    if t == 5:
        break
    print(t)


#____________________________________Loop control - continue statement


for m in range(10):
    if m == 5:
        continue
    print(m)




count9 = 5
while count9 > 0:
    if count9 == 3:
        continue
    else:
        print(count9)
    count9 -= 1

    


while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
       print("congarts! you guessed it right") 
       break
    print("sorry , you entered:",user_input)