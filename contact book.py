Contacts ={}
def creating():
    store_name = input("enter your store name:")
    phone_number = int(input("enter your phone number:"))
    email = input("enter your email id")
    address = input("enter your address")
    Contacts[store_name]={
        "phone number":phone_number,
        "email":email,
        "address":address
    }
    print(f"{store_name}s details saved")
def view():
    name = input("enter the store name yo wanna view:")
    if name in Contacts:
        print(f"{name}s details:")
        for key, value in Contacts[name].items():
            print(f"{key}:{value}")
    else:
        print("store details not present\n")
def edit():
    name = input("enter the store name yo wanna edit:")
    if name in Contacts:
        print(f"{name}s current details:")
        for key, value in Contacts[name].items():
            print(f"{key}:{value}")
        field = input("enter the field you wanna change(phone number,email,address)")
        if field in Contacts[name]:
            new_value = input("enter the new value ")
            Contacts[name][field]= new_value
        else:
            print("error")
    else:
        print("store details not present\n")
def delete():
    name = input("enter the shop name you wanna delete")
    Contacts.pop(name)
    print(f"{name} has been deleted")
def show_all():
    if not Contacts:
        print("No data is present")
    else:
        print("\nAll data present")
        for name,detail in Contacts.items():
            print(name)
            for key,values in detail.items():
                print(f"{name}:{values}")
while True:
    print("1. Add Shop")
    print("2. Search shop")
    print("3. Upadte Shop")
    print("4. Delete shop details")
    print("5. Show all shop")
    print("6. Exit")
    
    choice = input("enter your choice")
    if choice =="1":
        creating()
    elif choice =="2":
        view()
    elif choice == "3":
        edit()
    elif choice =="4":
        delete()
    elif choice == "5":
        show_all()
    elif choice=="6":
        print("exiting the program")
        break
    else:
        print("invalid entry")



    