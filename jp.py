rep = int(input("Enter seconds:")) 
hour = rep // 3600
minute = (rep % 3600)// 60
second = rep%60
print (rep, "is equal" , hour , "hours" , minute , "minutes" , second, "seconds" )