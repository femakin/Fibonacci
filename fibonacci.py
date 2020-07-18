#  fibonacci_numbers = [0, 1]
#for i in range(2,10):
 # print(i)
 # fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
#print(fibonacci_numbers)
try:
    N = int(input("Please Enter Length of fibonacci series: ")) # User Input the Length of fibonacci series they want

    fibo = [0, 1] 
    a = fibo[0]
    b = fibo[1]
    total = 0
    for i in range(2, N):
        c = a + b
        a, b = b, c
        fibo.append(c)
    #print(fibo[:N])
    print(fibo)  
# Try and Except
    for j in range(len(fibo)):
        if(fibo[j] % 2 == 0):
           total = total + fibo[j] 
    print("The sum of the even Fibonacci seq above is:", total)
    
except ValueError:
    print('Wrong Input!')   



   
