import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbol=[ '!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to the Py Password Generator!")
n_letters=input(f"How many letters would you like in your password?\n")
n_symbols=input(f"How many symbols would you like in your password?\n")
n_numbers=input(f"How many numbers would you like in your password?\n")

password=""
for char in range(1,int(n_letters)+1):
  char=random.choice(letters)
  password=password + char
  print(password)


for i in range(1,int(n_symbols)+1):
  i=random.choice(symbol)
  password=password + i
  print(password)

for j in range(1,int(n_numbers)+1):
  j=random.choice(numbers)
  password=password + j
  print(password)


print(password)
