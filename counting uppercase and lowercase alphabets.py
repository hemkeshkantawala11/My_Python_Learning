"""def alphabet_style():
    #ande=input("Enter The Sentence:- ")
    s = ("The Geek King")
    l,u = 0,0
for i in s: 
    if (i>='a'and i<='z'): 
        l=l+1                  #counting lower case 
    if (i>='A'and i<='Z'): 
        u=u+1                  #counting upper case
        
print("The number of upper case alphabets are:- ",u)
print("The number of lower case alphabets are:- ",l)
alphabet_style()"""
def upperlower(string): 
  
    upper = 0
    lower = 0
  
    for i in range(len(string)): 
          
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122): 
            lower += 1
  
        
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90): 
            upper += 1
  
    print('Lower case characters = %s' %lower, 
          'Upper case characters = %s' %upper)  
string = input('Enter The Sentence:- ')
upperlower(string) 