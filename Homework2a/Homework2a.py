#Task 10: There are n coins on the table. Some of them are tails up, and some are coats of arms.
#Determine the minimum number of coins that need to be turned over so that all the coins are turned up with the same side.
#Print the minimum number of coins to flip



#n = int(input('Enter a number of coins: '))
#heads = tails = 0
#for i in range(n):
#    x = int(input('Heads(1) or tails(0)?: '))
#    if x == 1:
#        heads += 1
#    else:
#        tails += 1
#if heads < tails:
#    print(f'Flip the {heads} coins to tails')
#elif heads == tails:
#    print(f'A number of heads and tails are equal, each is {heads}')
#else:
#    print((f'Flip the {tails} coins to the heads'))






#Task 12
#Petya and Katya are brother and sister. Petya is a student, and Katya is a schoolgirl. Petya
#helps Katya in math. He conceives two natural numbers X and Y
#(X,Y≤1000), and Katya has to guess them. To do this, Petya makes two hints.
#He calls the sum of these numbers S and their product P. Help Katya to guess
#the numbers conceived by Petya



#x = int(input("Enter X from 1 to 1000: "))
#y = int(input("Enter Y from 1 to 1000: "))
#for i in range(x):
#    for j in range(y):
#        if x == i + j and y == i * j:
#            print(i, j)





#Task 14: It is required to output all integer powers of two (i.e. numbers of the form 2k) that do not exceed the number N.

#N = abs(int(input('Enter the number N: ')))
#stop = 0
#P = 2
#for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end=' ')
#             P = 2
#         else:
#             stop = 1
#     else:
#        i = N
