while True:
    print("\n====Dream File Manger====")
    print("\n1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    if choice == "1":
        file = open("Dream.txt","r")
        content = file.read()
        file.close()
        print(content)
    elif choice == "2":
        file = open("Dream.txt","a")
        new = input("Enter your new inspiring line: ")
        file.write(new +"\n")
        file.close()
        print("Your inspiration has been added!")
    elif choice == "3":
        print("Warning: This will overwrite the file.")
        proceed = input("Do you want to continue?(Yes or No): ").lower()
        while True:
            if proceed == "yes":
                file = open("Dream.txt","w")
                rewrite = input("Write your new set of inspiring messages: ")
                file.write(rewrite)
                file.close()
                print("File has been overwritten \n")
                break
            else:
                break
    elif choice == "4":
        break
    else:
        print("INVALID INPUT!! Try Again")
        continue