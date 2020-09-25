name=input("Enter Your Name To Enter:- ")
print("HELLO " + name + "!!!")
print("THIS PROGRAM IS MADE TO FIND THE NTH TERM OF A PARTICULAR SEQUENCE.")
print("RULES FOR IT IS AS FOLLOWS:- \n (1) IT IS COMPULSORY TO GIVE THE FIRST TWO NUMBERS OF YOUR SEQUENCE.  \n (2) IT WILL ASK YOU TO INPUT 4 NUMBERS WHICH SHOULD BE IN THE CORRECT FORMAT OF ARITHEMATIC PROGRESSION OTHERWISE IT WOULD GIVE AN ERROR AND YOU NEED TO START IT AGAIN. \n (3) IF YOU WANT TO FIND THE THIRD OR THE FOURTH TERM THEN JUST ENTER 0 IN THE INPUT AND YOU WILL GET YOUR ANSWER. ")
print("I HOPE YOU ARE READY!!!!\n LETS BEGIN\n\n")

def arithematic_progression():
    
    while True:
        number1=float(input("Enter The First Number:- "))
        number2=float(input("Enter The Second Number:- "))
        
        a=number1
        d=number2-number1
        
        number3=float(input("Enter The Third Number:- "))
        if number3==0:
            number_to_find=3
            break

        number4=float(input("Enter The Fourth Number:- "))

        if number4==0:
            number_to_find=4
            break
        if d!=number3-number2 or d!=number4-number3 :
            print("ERROR:- ")
            print("PLEASE WRITE IN THE CORRECT FORMAT OF ARITHEMATIC PROGRESSION!!!")
            continue
        number_to_find=int(input("Enter The Number Of Term Which You Want To Know:- "))
        
        if d==number3-number2 or d==number4-number3:
            break
    
        number_to_find=int(input("Enter The Number Of Term Which You Want To Know:- "))
    arithematic_progression()
to_continue = input("Do you want to continue the write continue else write quit. (Anything else would not be allowed)")
        
def re_run():
    if to_continue == "continue":
        #printing_the_answers()
        arithematic_progression()
    elif to_continue == "quit":
        printing_the_answers()
    else:
        print("Write in Correct syntax!!")
        arithematic_progression()
re_run()
def printing_the_answers():
    print ("The First Term Of The Sequence Is:- ",a)
            
    print ("The Number Of Term Which You Want To Find Is:- ",number_to_find)
            
    print ("The Common Differnce Of Your Sequence Is:- ",d)
            
    print("The" ,number_to_find,"th term Is:- ",(a + (number_to_find - 1) * d))
        
                

