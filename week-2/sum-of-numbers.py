n=int(input("Enter the number upto which you want sum?"))
s=0
for i in range(0,n+1):
    s=s+i
    print("First {} numbers when added gives {} as sum".format(i,s))