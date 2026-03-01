name = "aadi"
print(name[0])         




my_name = "aadi"    

print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[3])




name2 = "Hello World" 
print(name2[9])




name3 = "Hello World"
print(name3[5])
print(name3[-1])




name4 = "Hello World"
print(name4[5])
print(name4[-1])
print(name4[-4])




#_______________________________string slicing


name_ = "aadi"
print(name_[0:3])




name__ = "aadi"
print(name__[0:2:1])




name6 = "Electronic"
print(name6[0:3])
print(name6[0:3:1])
print(name6[0:5:1])
print(name6[3:5:2])
print(name6[0:5:3])
print(name6[0:0:9])




name0 =  "python"
print(name0[0:2])
print(name0[0:3])
print(name0[2:5])
print(name0[1:4])
print(name0[-1:])
print(name0[5:])
print(name0[-2:])
print(name0[-3:])
print(name0[0::2])
print(name0[:])
print(name0[::])
print(name0[::-1])



#______________________________________string Methode



word = "Hello,Madhav"      #  len() 1
print(len(word))



word_ = "Hello,Madhav"
print(word.upper())        #   upper() 2



word__ = "Hello,Madhav"    #    lower() 3
print(word__.lower())




word0 = "Hello,Madhav"       
print(word__.count('H'))   #  count() 4




word1 = "Hello,Madhav"     #  find()  5  
print(word1.find('e'))




word3 = "Hello,Madhav"       
print(word3.split(','))   #split()    6



word4= "Hello,Madhav"       
print(word1.replace("Hello","aadi"))  # replace() 7




word5= "my name is aadi"       
print(word5.title())  # title() 8




js = ("python","java","c++")   #join()9
print(" ".join(js))