def main():
 A=int(input(""))
 temp=A
 rev=0
 while(A>0):
    dig=A%10
    rev=rev*10+dig
    A=A//10
 if(temp==rev):
    print("yes")
 else:
    print("no")

if __name__ == '__main__':
    main()
