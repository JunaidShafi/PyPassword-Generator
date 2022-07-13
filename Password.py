import random
l= int(input("How many letters would you like in your password"))
s= int(input("How many symbols would you like?"))
n= int(input("How many numbers would you like?"))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
string = []
num =[]
sym=[]
for i in range(0,l):
        q= random.randint(0,51)
        st=alphabets[q]
        string.insert(i,st)
for j in range(0,n):
        q= random.randint(0,9)
        nem= numbers[q]
        num.insert(j,nem)
for k in range(0,s):
        q= random.randint(0,8)
        sem= symbols[q]
        sym.insert(k,sem)
password= sym + num + string
length= len(password)
broad=''
for l in range(0,length):
    broad+=password[l]
random.shuffle(password)
broke=''
for se in range(0,length):
    broke+=password[se]
print(f"Your Randomized password is {broke}\n Have Fun!")
