import os

start=int(input("enter range ( first number ) =>"))
end=int(input("enter range ( last number ) =>"))

if os.path.exists("Tables from"+str(start)+"to"+str(end) + ".txt"):
  os.remove(str(start)+"to"+str(end) + ".txt")
  
f = open("Tables from" + str (start) + "to" + str (end) + ".txt", "a")
ran=range(start,end+1,1)
tables = [1,2,3,4,5,6,7,8,9,10]
for x in ran:
    for y in tables:
        content = (str(x) + " * " + str(y)+ " = " + str(x * y))
        content=content.replace("'", "")
        f.write(str(content)+"\n")
f.close()

