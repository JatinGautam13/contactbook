contact={}
def  add_contact(name,phone,e_mail):
     contact[name]={"phone":phone,"e-mail":e_mail}
     for name,info in contact.items():
            f=open("text.txt","a")
            f.write(f"(Name: {name}\nPhone: {info['phone']}\nE-mail: {info['e-mail']})\n\n")
            f.close()

     print("contact saved successfully\n")

def show_all_contact():
    print("CONTACT APP LIST\n")
    f=open("text.txt")
    print(f.read())
    f.close()
   

def delete_contact(file_name,name):
    file=open(file_name,"r")
    lines=file.readlines()
    new_lines = [i for i in lines if name.lower() not in i.lower()]
    file=open(file_name,"w")
    file.writelines(new_lines)
        # else:
        #     print("contact not found\n")

def search_name(name):
    if name in contact:
        print(contact[name])

def edit_contact(name,phone,e_mail):
     if name in contact:
           contact[name]["phone"] = phone
           contact[name]["e-mail"] = e_mail
           print("contact edit successfully\n")
     else:
         print("contact does not exited\n")





# def Contact_App():
while True:
        print("\nCONTACT APP\n")
        print("PRESS 1 TO ADD CONTACT")
        print("PRESS 2 TO SHOW ALL CONTACT")
        print("PRESS 3 TO DELETE CONTACT")
        print("PRESS 4 TO SEARCH CONTACT")
        print("PRESS 5 TO EDIT CONTACT")
        print("PRESS 6 TO EXIT\n")

        user=input("ENTER YOUR QUERRY:")
        if user=="1":
            name=input("Enter Name :").lower()
            phone=input("Enter Phone : ")
            e_mail=input("Enter E-Mail :")
            add_contact(name,phone,e_mail)

        elif user=="2":
            show_all_contact()

        elif user=="3":
            name=input("enter name\n").lower()
            delete_contact("text.txt",name)
        
        elif user=="4":
            name=input("enter name\n")
            search_name(name)
        
        elif user=="5":
            name=input("enter name :").lower()
            phone=input("enter phone : ")
            e_mail=input("enter mail :")
            edit_contact(name,phone,e_mail)
        
        elif user=="6":
            print("EXIT")
            break
        else:
            print("INVALID INPUT")
        


# Contact_App()