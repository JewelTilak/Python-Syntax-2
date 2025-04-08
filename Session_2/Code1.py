while True:
    try:
        number = int(input("Enter number: "))
        result = 10/number
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    else:
        print(f"The result is {result}")

    finally:
        print("Thank You")