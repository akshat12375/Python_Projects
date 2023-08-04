import random
print("HELLO\nHOPE YOU WILL ENJOY THE GAME\n    DEVELOPER-AKSHAT SRIVASTAVA")
print("___________________________________")
user=int(input("YOUR CHANCE \n1-FOR ROCK\n2-FOR PAPER\n3-FOR SCISSOR"))
comp=random.randint(1,3)
a=["ROCK","PAPER","SCISSOR"]
if user==1:
     if(comp==1):
          print(f"COMPUTER DECISION {a[comp-1]}\nDRAW")
     elif(comp==2):
          print(f"COMPUTER DECISION {a[comp-1]}\nCOMPUTER WINS")
     else:
          print(f"COMPUTER DECISION {a[comp-1]}\nUSER  WINS")
elif user==2:
     if(comp==1):
          print(f"COMPUTER DECISION {a[comp-1]}\nUSER WINS")
     elif(comp==2):
          print(f"COMPUTER DECISION {a[comp-1]}\nDRAW")
     else:
          print(f"COMPUTER DECISION {a[comp-1]}\nCOMPUTER  WINS")
else :
     if(comp==1):
          print(f"COMPUTER DECISION {a[comp-1]}\nUSER WINS")
     elif(comp==2):
          print(f"COMPUTER DECISION {a[comp-1]}\nCOMPUTER WINS")
     else:
          print(f"COMPUTER DECISION {a[comp-1]}\nDRAW")
print("THANK YOU ")

    