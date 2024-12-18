#Imports
import datetime
import tkinter as tk
from tkinter.messagebox import showinfo

#Global variables
product_list = []
bills = 0
d = {}

#Custom class for invalid inputs
class InvalidInputError(Exception):
    def __init__(self):
        self.message = 'ERROR: Invalid Input :(\n'
        super().__init__(self.message)


class Feedback:
    def feedback(self):
        try:
            #Main Window
            a = tk.Tk()
            a.geometry('500x420')
            a.title("Feedback")
            a.lift()                       #To show the window on front
            a.attributes('-topmost', True)
            #Heading
            head = tk.Label(a, text = 'CUSTOMER FEEDBACK', height=2, width=40, font=('Times New Roman', 25, 'bold'), bg='Light Blue')
            head.pack()
            #Name Entry Widget
            l1 = tk.Label(a, text = 'Name')
            l1.place(x=15, y=90)
            e1 = tk.Entry(a, width=30)
            e1.place(x=15, y=115)
            #Email Entry Widget
            l2 = tk.Label(a, text = 'Email')
            l2.place(x=15, y=150)
            e2 = tk.Entry(a, width=30)
            e2.place(x=15, y=175)
            #Rating Widget
            l3 = tk.Label(a, text = 'Rate your experience:')
            l3.place(x=15, y=210)
            rating_scale = tk.Scale(a, from_=1, to=5, orient=tk.HORIZONTAL, length=200)
            rating_scale.place(x=15,y=235)
            #Comment Entry Widget
            l3 = tk.Label(a, text = 'Comments (if any):')
            l3.place(x=15, y= 290)
            e3 = tk.Entry(a, width=50)
            e3.place(x=15, y=315)
            #Submit Button Function
            def sub():
                showinfo('Message', 'Thank You for your feedback :)')
                a.destroy()
            #Saving feedback
            def save():
                fb = open('Feedbacks.txt', 'a')
                fb.write(f'Name: {e1.get()}\nEmail: {e2.get()}\nRating: {str(rating_scale.get())}\nComment: {e3.get()}\n\n')
                fb.close()
            #Submit Button
            submit = tk.Button(a, text = 'Submit', bg='Light Blue', relief=tk.RAISED, command=lambda:[save(),sub()])
            submit.place(x=250, y=370, anchor='center')
            #Event listener
            a.mainloop()
        except Exception as e:
            showinfo('ERROR', 'Unexpected error occurred :(')
            Menu().menu()


class History:
    def write_history(self):          #Save history
        try:
            file_name = f"{login_user}"
            file = open(f"Shopping History/{file_name}.txt", 'a')
            current_datetime = datetime.datetime.now()
            file.write(f"Products: {product_list}\nTotal Bill: Rs.{bills}\nCheckout completed at {current_datetime}\n")
        except FileNotFoundError:
            print('ERROR: File Error. History not saved')
            Menu().menu()
        except Exception as e:
            print(f'ERROR: Unexpected error occurred :( - {e}')
            Menu().menu()
        finally:
            file.close()

    def read_history(self):           #View History
        try:
            file_name = f"{login_user}"
            file1 = open(f"Shopping History/{file_name}.txt")
            print("\nShopping History\n----------------")
            print(file1.read())
        except FileNotFoundError:
            print(f'ERROR: File Not Found')
            Menu().menu()
        except Exception as e:
            print(f'ERROR: Unexpected error occurred :( - {e}')
            Menu().menu()
        finally:
            file1.close()
            Menu().menu()


class Checkout:
    def checkout(self):
        try:
            print(f'Items in your cart:{product_list}')
            print(f'Total bill of all items:{bills}')
            print(f'Items with their prices:{d}\n')
            ch = input("Confirm checkout? [Y/N]\n=> ")
            ch = ch.strip().lower()
            if ch == 'y':
                print("Enter your card details\n----------------------")
                ck = input("Enter credit card number: ")
                cl = input("Enter card PIN: ")
                print("Payment successful :)\nYour order will be delivered in 2 hours\n")

                #File write (Shopping history)
                History().write_history()

                #Asking for feedback
                a = input('Do you want to give us a feedback? Feedback helps us to improve :)\na) Yes\nb) No\n=> ')
                a = a.strip().lower()
                if a == 'a':
                    Feedback().feedback()
                    Menu().menu()
                elif a == 'b':
                    Menu().menu()
                else:
                    raise InvalidInputError

            #No checkout
            elif ch == 'n':
                cg = input("1. Go to cart\n2. Go back to menu\n=> ")
                if cg == '1':
                    Cart().view_cart()
                elif cg == '2':
                    Menu().menu()
                else:
                    raise InvalidInputError
            else:
                raise InvalidInputError

        except InvalidInputError as ie:
            print(ie)
            Menu().menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Menu().menu()

class Cart:
    def products(self):
        try:
            with open('products list.txt', 'r') as fl:
                print(fl.read())
                pl = input('\na) Add products to cart\nb) Back to menu\n=> ')
                if pl == 'a':
                    Cart().add_to_cart()
                elif pl == 'b':
                    Menu().menu()
                else:
                    raise InvalidInputError()
            fl.close()
        except FileNotFoundError:
            print("ERROR: File not found.")
            Menu().menu()
        except InvalidInputError as ie:
            print(ie)
            Menu().menu()
        except Exception as e:
            print(f'Unexpected error occurred - {e}')

    def add_to_cart(self):
        global product_list, bills, d
        while True:
            try:
                item = int(input("Enter your choice number (Enter '0' to go back): "))
                if item == 0:
                    break
                elif item == 1:
                    bill = 200
                    d['Apples'] = bill
                    bills += bill
                    product_list.append('Apples')
                elif item == 2:
                    bill = 150
                    d['Bananas'] = bill
                    bills += bill
                    product_list.append('Bananas')
                elif item == 3:
                    bill = 120
                    d['Potatoes'] = bill
                    bills += bill
                    product_list.append('Potatoes')
                elif item == 4:
                    bill = 150
                    d['Tomatoes'] = bill
                    bills += bill
                    product_list.append('Tomatoes')
                elif item == 5:
                    bill = 200
                    d['Milk'] = bill
                    bills += bill
                    product_list.append('Milk')
                elif item == 6:
                    bill = 300
                    d['Eggs'] = bill
                    bills += bill
                    product_list.append('Eggs')
                elif item == 7:
                    bill = 80
                    d['Butter'] = bill
                    bills += bill
                    product_list.append('Butter')
                elif item == 8:
                    bill = 100
                    d['Cheese'] = bill
                    bills += bill
                    product_list.append('Cheese')
                elif item == 9:
                    bill = 50
                    d['Bread'] = bill
                    bills += bill
                    product_list.append('Bread')
                elif item == 10:
                    bill = 100
                    d['Cupcakes'] = bill
                    bills += bill
                    product_list.append('Cupcakes')
                elif item == 11:
                    bill = 100
                    d['Muffins'] = bill
                    bills += bill
                    product_list.append('Muffins')
                elif item == 12:
                    bill = 100
                    d['Rusk'] = bill
                    bills += bill
                    product_list.append('Rusk')
                else:
                    raise InvalidInputError
            except InvalidInputError as ie:
                print(ie)
                Menu().menu()
        print("Item(s) added to cart.")
        Menu().menu()

    def remove_from_cart(self):
        global product_list, bills, d
        if not product_list:
            print('No items in cart.')
            Menu().menu()

        print("Products:", product_list)
        bills = bills
        print("Total cost:", bills)
        print("Items with prices:", d)

        while True:
            item = input("Enter item name to remove (Enter 'n' to go back): ").strip().capitalize()
            if item == 'N':
                break
            elif item in d:
                bill = d[item]
                del d[item]
                product_list.remove(item)
                bills -= bill
                print(f"{item} removed from cart.")
            else:
                print("Item not found in cart.")
        print(f'Item(s) removed from cart')
        Menu().menu()

    def view_cart(self):
        try:
            print('\nYour Cart\n---------')
            print('Products:', product_list)
            print('Your total bill is Rs.', bills)
            print('Items with prices:', d)
            #Taking customer response
            print('1. Remove items from cart\n2. Checkout now\n3. Back to menu')
            k = input('Enter your response: ')
            if k == '1':
                Cart().remove_from_cart()
            elif k == '2':
                Checkout().checkout()
            elif k == '3':
                Menu().menu()
            else:
                raise InvalidInputError
        except InvalidInputError as ie:
            print(ie)
            Menu().menu()


class Menu:
    def menu(self):               #Second menu after login
         global login_user        #Declaring global to use in view profile method
         print("Select an option:\n1. Your Profile\n2. Shop Now\n3. View Cart and Checkout\n4. Your Shopping History\n5. Logout\n6. Logout and Exit Application")
         option = int(input('Enter your choice (1-6): '))
         if option == 1:
             profile = Profile()                 #Creating an object of Profile class
             profile.username = login_user       #Using username
             profile.view_profile()              #Calling view profile method
         elif option == 2:
             Cart().products()
         elif option == 3:
             Cart().view_cart()
         elif option == 4:
             History().read_history()
         elif option == 5:
             Main_Menu().main_menu()
         elif option == 6:
             print("Thank You! :)")
         else:
             print("ERROR: Invalid choice. Enter '6' to exit application.\n")
             Menu().menu()


class Account:
    def create_account(self):
        try:
            self.fh = open("Accounts/accounts.txt", "a")
            self.fhh = open("Accounts/account holders name.txt", "a")
            print('\nEnter Your Information\n----------------------')
            self.first_name = input("Enter first name: ")
            self.last_name = input("Enter last name: ")
            self.email = input('Enter your email (optional): ')
            self.phone = input('Enter phone no (optional): ')
            self.address = input('Enter your home address (optional): ')
            self.username = input("Choose a username: ")
            print("NOTE: Password must be between 7 and 12 characters and should also include at least one digit.")
            self.password = input("Choose your password: ")

            #Password validity check for digit
            number = 0
            for i in self.password:
                if i.isdigit():
                    number += 1

            #Password validity check for length
            if len(self.password) >= 7 and len(self.password) <= 12 and number >= 1:
                #Saving username and password
                user_pass = {self.username:self.password}
                self.fh.write(f'{user_pass}\n')
                self.fhh.write(f'- {self.first_name} {self.last_name}\n')
                print("Account created successfully. You can login now :)\n")
                self.fh.flush()
                self.fhh.flush()

                profile = Profile()    #Creating Profile object to pass attributes
                profile.username = self.username  #Passing all attributes to save in profile
                profile.first_name = self.first_name
                profile.last_name = self.last_name
                profile.email = self.email
                profile.phone = self.phone
                profile.address = self.address
                profile.save_profile()  # Save profile details

                Main_Menu().main_menu()      #Going back to menu
            else:
                print("ERROR: Your password does not meet the requirements. Try again!")
                Main_Menu().main_menu()
        except InvalidInputError as ie:
            print(ie)
            Main_Menu().main_menu()
        except IOError as ioe:
            print(f'ERROR: File Error - {ioe}')
            Main_Menu().main_menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Main_Menu().main_menu()
        finally:
            self.fh.close()                 #Closing files
            self.fhh.close()


    #Login function
    def login(self):
        try:
            with open('Accounts/accounts.txt') as file:           #Opening accounts file
                #Taking login credentials from user
                print('\nEnter your credentials\n----------------------')
                global login_user                        #Global variable to use in profile and history
                login_user = input("Enter your username: ")
                login_password = input("Enter your password: ")

                #Checking for valid id
                self.user_pass = {login_user:login_password}
                count = 0
                for line in file:
                    line = eval(line.strip())
                    if line == self.user_pass:
                        count += 1
                file.close()
                if count >= 1:
                    print("Login successful. You can shop now :)\n")
                    #Opening file for shopping history (in case of no previous history)
                    self.file_name = f"{login_user}"
                    self.file1 = open(f"Shopping History/{self.file_name}.txt", 'a')
                    self.file1.close()
                    Menu().menu()         #Second menu function call (when login is successful)
                else:
                    print("ERROR: Either account does not exist or invalid username/password. Try again!\n")
                    Main_Menu().main_menu()
        except IOError as ioe:
            print(f'ERROR: File Error - {ioe}')
            Main_Menu().main_menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Main_Menu().main_menu()

    def save_profile(self):
        pass

    def view_profile(self):
        pass


#Profile class (inheriting from Account class)
class Profile(Account):
    def save_profile(self):           #Saving profile after account creation
        try:
            f = open(f'Profiles/{self.username}.txt', 'w')
            f.write(f'Name: {self.first_name} {self.last_name}\nUsername: {self.username}\n')
            f.write(f'Email: {self.email}\nPhone No: {self.phone}\nAddress: {self.address}\n')
            f.close()
        except IOError as ioe:
            print(f'ERROR: File Error - {ioe}')
            Main_Menu().main_menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Main_Menu().main_menu()

    def view_profile(self):             #Viewing profile
        try:
            f = open(f'Profiles/{login_user}.txt')
            print('\nYour Profile\n------------')
            print(f.read())
            f.seek(0)
            f.close()

            #options after viewing profile
            ch = input('Options:\na) Back to menu\nb) Logout\n=> ')     #options
            ch = ch.strip().lower()
            if ch == 'a':
                Menu().menu()
            elif ch == 'b':
                Main_Menu().main_menu()
            else:
                raise InvalidInputError()
        except FileNotFoundError:
            print(f'ERROR: Profile not found')
            Menu().menu()
        except IOError as ioe:
            print(f'ERROR: File Error - {ioe}')
            Menu().menu()
        except InvalidInputError as ie:
            print(ie)
            Menu().menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Menu().menu()


class Main_Menu:
    def main_menu(self):            #Main menu for signup and login
        try:
            print("Welcome to SuperMart!\nHappy Shopping :)\n---------------------")
            choice = input("Choose:\na) Sign Up\nb) Login and Shop\nc) Exit the application\n=> ")
            choice = choice.strip().lower()
            if choice == 'a':
                Account().create_account()
            elif choice == 'b':
                Account().login()
            elif choice == 'c':
                print("Thank you! :)")
            else:
                raise InvalidInputError()
        except InvalidInputError as ie:
            print(ie)
            Main_Menu().main_menu()
        except Exception as e:
            print('ERROR:', f'Unexpected error occurred - {e}')
            Main_Menu().main_menu()

