# Read N from the user.
n = int(input("Enter the length of fibonnaci sequence (N):"))

 #Check for the valid input.
 if n <= 0:
    print("Please enter a postive integer.")

else:
    #Initialize the first two fibbonaci numbers.
    a,b = 0,1
    print("Fibbonaci sequence:")
    for i in range(n):
        print(a, end=' ')
        #Update values of a and b.
        a,b = b, a + b

