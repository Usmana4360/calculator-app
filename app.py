from cal_func import do_addition,do_subtraction,do_diviion
from multipy import do_multipication
def main():
    print("welcome to calculator app")
    print("""Please select 1 number you want to do
          1=do_addition
          2=do_subtraction""")
    
    user_input=input("Select a Number")

    a=int(input('Enter first number'))
    b=int(input("Enter second number"))

    if user_input =="1":
        result=do_addition(a,b)
    elif user_input=="2":
        result=do_subtraction(a,b)
    elif user_input=="3":
        result=do_multipication(a,b)
    elif user_input=="4":
        result=do_diviion(a,b)
    print("result",result)
    

if __name__=="__main__":
    main()