#program to display students names and marks obtained by them
#and to find out the first,second,third ranks of the class



pair={}
main=[]
num=eval(input("enter the number of students in a class"))
if num>3:
     i=1
     while i<=num:
        name=(input("enter the name of the student"))
        marks=eval(input("enter the marks of the student"))
        pair[name]=marks
        i=i+1
     print(pair)
     print("name of the student" ,"\t" ,"marks")
     for x in pair:
        print(x, "\t" "\t" "\t" ,pair[x])
     #for x in pair:    
        #print("student {} secured {} marks".format(x,pair[x]))# remove x for for loop to see formated type pf output
     for x in pair:
        main.append(pair[x])

     main1=sorted(main)
     k=main[len(main1)-1]
     z=[key for (key,value) in pair.items() if value==k]#this command got it from internet
     print(" {} secured first rank with {} marks".format(z,k))
     q=main[len(main1)-2]
     e=[key for (key,value) in pair.items() if value==q]
     print(" {} secured second  rank with {} marks".format(e,q))
     w=main[len(main1)-3]
     x=[key for (key,value) in pair.items() if value==w]
     print(" {} secured third  rank with {} marks".format(x,w))             
     print("congratulations  ",z,e,x)      
else:
    print(" students in a class can't be less than 3")
    
