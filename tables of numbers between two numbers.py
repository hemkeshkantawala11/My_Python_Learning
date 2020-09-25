start=int(input("enter range ( first number ) =>"))
end=int(input("enter range ( last number ) =>"))
ran=range(start,end+1)
tables = [1,2,3,4,5,6,7,8,9,10]
for x in ran:
    for y in tables:
        content = (str(x) + " * " + str(y)+ " = " + str(x * y))
       
        print(content)