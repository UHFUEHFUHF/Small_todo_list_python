def guess():
    items = set()
    while True:
        x = input("Enter the number the task :")
        
        y = input("do you want to add more items :")
        if(y == "y" or y == "Y"):
            items.add(x)
        else:
            print(list(items))
            check = input("Do you want to delete any items :")
            if(check == "y"):
                items_to_delete = input("Enter the name you want to delete :")

                if items_to_delete in items:
                    items.remove(items_to_delete)
                    print(list(items))
                    break
            if(check == "n"):
                break





guess()