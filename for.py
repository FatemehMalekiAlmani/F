from os import system
system('cls')
for i in range(1,10):
    print(i,i*i,i**2)
    if i==5:
        print('i reached 5')
        break