l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(word,key):
    new=''
    for i in word:
        if(i==' '):
            new=new+' '
            
        else:
            po=l.index(i)
            pos=(po+key)%26
            new=new+l[pos]
            
    print(new)
def decryption(word,key):
    new=''
    for i in word:
        if(i==' '):
            new=new+' '
            
        else:
            po=l.index(i)
            pos=(po-key)%26
            new=new+l[pos]
            
    print(new)
choice=input("what would you like to do [encrypt]for encryption or [decrpt]for decryption\n")
sen=input("enter the sentence\n")
keyw=int(input("enter the key "))
if choice=="encrypt":
    encryption(word=sen,key=keyw)

elif choice =="decrypt":
    decryption(word=sen,key=keyw)
ch=input("would you like to do again")
while(ch=='yes'):
    choice=input("what would you like to do [encrypt]for encryption or [decrpt]for decryption\n")
    sen=input("enter the sentence\n")
    keyw=int(input("enter the key "))
    if choice=="encrypt":
        encryption(word=sen,key=keyw)

    elif choice =="decrypt":
        decryption(word=sen,key=keyw)
    ch=input("would you like to do again\n")
print("THANK YOU")
