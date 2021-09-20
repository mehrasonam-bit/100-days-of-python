import random


# def shuffle(string):
#   tempList = list(string)
#   random.shuffle(tempList)
#   return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90)) #generate random uppercase letter as per ASCII code

uppercaseLetter2=chr(random.randint(65,90)) 

digit1=chr(random.randint(48,57)) #generate random digit
digit2=chr(random.randint(48,57)) 

lowercaseLetter1=chr(random.randint(97,122)) #generate random lowercase letter as per ASCII code
lowercaseLetter2=chr(random.randint(97,122)) 

symbols=chr(random.randint(21,46)) #generate symbols as per ASCII code

password=[]
password.append(uppercaseLetter1)
password.append(uppercaseLetter2)
password.append(lowercaseLetter1)
password.append(lowercaseLetter2)
password.append(digit1)
password.append(digit2)
password.append(symbols)

#shuffle(password)

random.shuffle(password)
for p in range(7):
  print(password[p],end="")

