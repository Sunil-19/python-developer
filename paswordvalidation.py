import re
f=0
passwrd=input("enter password ")
if not  re.search('[a-z]',passwrd):
    f=1
if  not  re.search('[A-Z]',passwrd):
    f=1
if not re.search('[0-9]',passwrd):
    f=1
if not re.search('[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', passwrd):
    f=1
if  len(passwrd)<6:
    f=1
if  len(passwrd)>20:
    f=1
if (f==0):
    print('password is valid')
else:
    print('password invalid')