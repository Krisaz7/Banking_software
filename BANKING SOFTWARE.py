import random
import re

###NEW CUSTOMER ###
def New_user_details():
 Balance=0
 n = input("Enter Full Name : " )
 global Name
 Name = n.replace(" ", "")
 if Name.isalpha() == False:
      print("Enter a valid Name ")
 Age=int(input("Enter the age : "))
 global Aadhar_number
 Aadhar_number=int(input("Enter the Aadhar number : "))
 if len(str(Aadhar_number))!=12:
        	print("Enter a valid Aadhar_number")

 global Mobile_number
 Mobile_number = int(input("Enter the Mobile Number : "))
 if len(str(Mobile_number))>10:
   	print("Enter a valid Mobile Number:  ")

 Address = input("Enter your residential Address : ")

 global Account_number
 Account_number = random.randrange(9000000,9999999)
 print("Your Account Number is ", Account_number)

 print("The Password should contain a capital Value ",
	  	"\nThe Password should contain a Special charecter ",
	  	" \nThe password should contain a numeric Value",
	  	" \nThe password should be 8 charecters long "
	  	)
 global Password
 Password = input("Enter the Password")
 flag = 0
 while True:
  if (len(Password)<=8):
   flag = -1
   break
  elif not re.search("[a-z]", Password):
   flag = -1
   break
  elif not re.search("[A-Z]", Password):
   flag = -1
   break
  elif not re.search("[0-9]", Password):
   flag = -1
   break
  elif not re.search("[_@$!#%&*]" , Password):\
   flag = -1
  break
 else:
   flag = 0
   print("Valid Password")

 if flag == -1:
			print("Not a Valid Password ")

 global userdetails
 userdetails = {Account_number: [Name, Age, Aadhar_number, Mobile_number, Address, Password]}

 print("Welcome to SWQT Bank ")
 Ans=input("Do you want to deposit cash")

 if Ans=='Yes'or 'YES' or 'yes':
		global New_amount
		New_amount=int(input("Enter the Amount to be depositted "))
		New_balance = Balance+New_amount
		print("Your Updated balance is ",New_balance)


global Balance
Balance=25000
def withdrawal():

	global amt
	amt=int(input("Enter the amount to be withdrawn"))
	if amt > Balance:
		print("You dont have sufficient balance ")
	else:
		print("You have succesfully withdrawn ",amt ," from your account and your balance is ", Balance - amt)
		return Balance

def deposit():

	amt=int(input("Enter the amount to be Deposited "))
	new_balance=amt+Balance
	print("Your Updated balance is ",new_balance)
	return new_balance

def baalance():
	Balance = 25000
	print("your balance is ",Balance)
	return Balance

###Existing Customer###
def existing_customer():
	AccountDetails=dict(username="User1" ,password="Asdfgh!")
	Accno=input("Enter the Account Number : ")
	if len(Accno) !=7 or Accno.isnumeric()==False:
		print("Please Enter a valid Account number ")
	else:
		username=input("Enter your username : ")
		password=input("Enter your password : ")
		if username!="User1" and password!="Asdfgh!":
			print("Please enter valid Credentials ")
		else:
			print("Login Succesfull")
	choice=int(input("1.withdrawal "
				 "\n2.Deposit "
				 "\n3.Balance "
				 "\n"))
	if choice==1:
 	 balance=withdrawal()
	elif choice==2:
	  balance=deposit()
	elif choice == 3:
	  balance = baalance()
	else:
 	 print("Please chose an option from above ")



#Main Program

print("Welcome to SWQT Bank ")
CHoice=int(input("Please select an option from below "
	  "\n 1. New customer "
	  "\n 2. Existing Customer "
				 "\n "))
if CHoice==1:
	New_user_details()
elif CHoice==2:
	existing_customer()
else:
	print("Please choose from above ")
