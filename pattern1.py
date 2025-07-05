#

# row = int(input("Enter number of row: "))   #no of line to print
# for i in range(1,row+1):                     #current row no.
#     for j in range(i):                       #colum index- how many stars to print
#         print("*", end="")
#     print()                                  #NEXT LINE

# row =int(input("enter no. of rows : "))
# for i in range (1,row+1):
#     spaces= row - i
#     stars= i* 2 - 1
#     print(" "* spaces + "*"* stars)

rows =int(input("enter no. of rows :"))
i =1
while i<=rows:
    #printing spaces
    space=1
    while space<=rows-i:
        print(" ",end ="")
        space+=1
    
    #printing stars
    star =1
    while star<= i*2-1:
        print("*",end="")
        star+=1
    
    #new line
    print()
    i+=1
