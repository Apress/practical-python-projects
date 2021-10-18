f=open("D:\plaintext.txt","w")
L=["I live in delhi"]
f.writelines(L)
f.close()

f=open("D:\plaintext.txt","a")
f.write("\nIndia")
f.close()

f=open("D:\plaintext.txt","r")
print(f.read())
print()
f.close()