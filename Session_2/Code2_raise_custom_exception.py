while True:
    name = input("Enter the name of the file: ")
    try:
        f = open(name + '.txt')
        if f.name ==  'test.txt':
            raise Exception("Do not open the file") # Custom Error
        
    except FileNotFoundError as e:
        print(f"File not found: {e}")

    except Exception as e:  
        print(e)

    else:
        data = f.read()
        print(data)

    finally:
        try:
            f.close()
        except NameError:
            pass