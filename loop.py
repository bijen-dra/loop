### complex variable 
nameList = ["Ram", "shyam", "sita"]


print ( " My name is ", nameList)

# for i in nameList:
#     print("My name is "+ i)
#     print("working in loop")


print(nameList[0])

## to add to a list
nameList.append("bjn")
print(nameList[3])



## add to distinct place
nameList.insert(1,"ram")
print(nameList)


## remove to a list 
nameList.pop()
print(nameList)


### calculate 
totalNumberOfRam = nameList.count("ram")
print(totalNumberOfRam)

## counting
total = len(nameList)
print("total item", total)

### Control flow statement

## if - elif - else

for i in nameList:
    if i.lower() == "sita":
        print ("Yes there is sita")
    elif i.lower() == "ram":
        print ("Yes there is ram")
    else:
        print("")

