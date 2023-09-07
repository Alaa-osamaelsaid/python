#task1.1
#method1

#a= [1,2,3,2,7,2,2,8,9]
#count = 0
#for i in a:
   #if i == 2: 
       #count+=1
#print('number of occurence of number 2 is:',count)

#method2
#a = [1,2,3,2,3,2,2,8,9]
#search = 2
#def checkoccurence(a,number):
    #count = 0
    #for i in a:
        #if(i == number):
            #count+=1
    #return count

#result = checkoccurence(a,search)
#print('count is:',result)

#method3
a = [1,2,3,2,7,2,2,8,9]
#print("The number is repeated:",a.count(2),"times") #list.count(i) function that counts the reapeate number in the list
b= a.count(2)
print('The number is repeated: {}'.format(b),'times')