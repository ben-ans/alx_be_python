def display_menu():
    print("Shopping List Manager")
    print("1, Add Item")
    print("2, Remove Item")
    print("3, View Item")
    print("4, Exit")


def main():
    shopping_list = ["makola","mayoka"]
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if  choice == '1':
            #Prompt for add item
            item = input("The name of the item you want to add: ")
            shopping_list.append(item)

        elif choice == '2':
            #Prompt for removing shopping list
            item = str(input("The name of the item you want to remove: "))
            shopping_list.remove(item)

        elif choice == '3':
            #Display shopping list
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
                

        elif choice == '4':
            #Prompt for exit
            print("GOodbye!!")
            break
        else:
            print("Ivalid Choice, please try again")

if __name__ == "__main__":
    main()