import sys 
import time
print("\033[1;32;40m .::::        .:::::::    .::          .::.::::::: .::")
print("\033[1;32;40m.:    .::    .::    .::  .::    .::   .:::        .::")  
print("\033[1;32;40m.::         .::    .::  .::.  :: .:: . .::       .::")   
print("\033[1;32;40m.::          .: .::      .::  .::  .::   .::     .::")     
print("\033[1;32;40m.::   .:::: .::  .::    .::  .::   .:   .::    .::")      
print("\033[1;32;40m.::    .:  .::    .::   .::  .::         .::   .::")        
print("\033[1;32;40m.:::::   .::      .::  .::  .::         .::  .:::::::::::")
print("Welcome To Grimz Fam Db")
print("Created By J4CKR4BB17")
a = False 
file = False
a = input("1.Start 2.Help:")
if a == "2" :print("Help: to acces anything said in this menu restart the db info: when the program asks for name always add a .py at the end and use the same name in both inputs or ELSE it will not work:For the input once the file is created use tab and space to skip lines and the suggestion bar to complete do not press enter unless you are done with the db!!! if you have any more questions ask kik:J4CKR4BB17_")
if a == "2" :sys.exit("please restart Grimzdb")
if a == "1" :a = input("Welcome To GrimzFaM to create a file press 1:")
if a == "1" :file = input("What would You like to Name Your file")
print("New File Named "+file+" Created")
filename = input ("filename: ");
with open (filename, "w") as f:
  f.write (input ());
fobj = open(""+file+"", "r")
print('Type python3 [file you created] to open the file')  





