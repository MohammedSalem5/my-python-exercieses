##Python strings


print("Hello")
print('hello')


print("It's alright ")
print("He is called ' johnny' ")
print('He is called "Johnny" ')


 #Slicing strings 
a = " Hello , world  "
print(a)

x = ''' Messi is the world ,  
the best in history ,
No !! one can be near him in the top 
so " MESSI " is number one 
'''
print(x)

print(a[1 : 5 ])
print(a[1])



for x in "Banana" : 
    print(x)





print(len(a))




txt = " The best things in life are free !" 
if " Messi " not in txt : 
    print ("Messi is not in txt " )

b= "Hello, World!"
print(b[:5])
print(b[2:])

print(b[5 : 10])

print(b[-5 : -2])

#Modify strings 
l = " Hello , World! "
print(l.upper())
print(l.lower())
print(l.strip())
print(l.replace("H" , "J"))
print(l.split(" , "))



 ## String Concatenation

m = "Hello mfs"
M= " World!"
n = m +  " " + M
print(n)

##Format - Strings


#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

AGE = 36
text = f"My name is Mohammed , I am {AGE}"
print(text)

price = 59
texti = f"the price is {20 * 59} dollars "
#texti = f"the price is {price} dollars "
#texti = f"the price is {price: .1f} dollars "
print(texti)

#Escape Character
#txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Python String Methods
tt= "hello world "
print(tt.capitalize())
print(tt.casefold())
print(tt.center(10))
print(tt.count("hello"))
print(tt.encode())
print(tt.endswith("."))
print(tt.expandtabs(4))