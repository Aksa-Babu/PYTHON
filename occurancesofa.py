Astr=input("enter the string\n")
char=input("enter the character\n")
print("Given string:\n",Astr)
("Given character:\n",char)
res=0
for i in range(len(Astr)):
    if(Astr[i]==char):
            res=res+1
print("Number of time character is present in string:\n",res)