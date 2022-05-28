def main():
    try:
        number1,number2 = eval(input("Enter two numbers, seperated by a comma: "))
        result = number1/number2
        print("Result is", result)
    except ZeroDivisionError:
        print("Division by Zero!")
    except SyntaxError:
        print("A comma may be missing in the input")
    except:
        print("Somthing wrong in the input")
    else:
        print("No exceptions")
    finally:
        print("The final clause is excecuted")

main()

    