import tkinter as tk
from tkinter import messagebox


def msg_show_transfer():
    messagebox.showinfo("Account Created", "Your money has been transfered.")

def transfer():
    transfer = tk.Toplevel()
    transfer.title("Transfer from diffrent account")
    
    frame = tk.Frame(transfer)
    frame.pack()

    label_transfer_name = tk.Label(frame, text="Payee name")
    label_transfer_name.pack()
    
    textbox_name = tk.Entry(frame)
    textbox_name.pack()
    
    label_sortcode = tk.Label(frame, text="Sort Code")
    label_sortcode.pack()
    
    textbox_sortcode = tk.Entry(frame)
    textbox_sortcode.pack()
    
    
    label_account_number_transfer = tk.Label(frame, text="Account Number")
    label_account_number_transfer.pack()
    
    textbox_account_numbrt = tk.Entry(frame)
    textbox_account_numbrt.pack()
    
    label_t_amount = tk.Label(frame, text="amount")
    label_t_amount.pack()
    
    textbox_amount = tk.Entry(frame)
    textbox_amount.pack()
    
    Submit_transfer_button = tk.Button(frame, text="submit",command=msg_show_transfer)
    Submit_transfer_button.pack()
    
    exit_transfer_button = tk.Button(frame, text="Close", command=transfer.destroy)
    exit_transfer_button.pack()
    
    
root = tk.Tk()
root.title("Transfer from diffrent account")

frame = tk.Frame(root)
frame.pack()



def location_Withdraw():
    location_Withdraw = tk.Toplevel()
    location_Withdraw.title("Withdraw Cash")
    
    frame = tk.Frame(location_Withdraw)
    frame.pack()

    label_Withdraw_street = tk.Label(frame, text="there is a list of streets 26714484Bank has branch and ATM there.")
    label_Withdraw_street.pack()
    
    label_Withdraw_money = tk.Label(frame, text="Cash can be withdrawn there")
    label_Withdraw_money.pack()
    
    label_Withdraw_branch = tk.Label(frame, text="West Broadway, Main Street, Taylor Street, High Street")
    label_Withdraw_branch.pack()
    
    exit_Withdraw_button = tk.Button(frame, text="exit", command=location_Withdraw.destroy)
    exit_Withdraw_button.pack()
    
    
root = tk.Tk()
root.title("Withdraw Cash")

frame = tk.Frame(root)
frame.pack()


def location():
    location = tk.Toplevel()
    location.title("Deposit Cash")
    
    frame = tk.Frame(location)
    frame.pack()

    label_street = tk.Label(frame, text="there is a list of streets 26714484Bank has branch and ATM there.")
    label_street.pack()
    
    label_deposit_money = tk.Label(frame, text="you can deposit money into your account in there")
    label_deposit_money.pack()
    
    label_branch = tk.Label(frame, text="West Broadway, Main Street, Taylor Street, High Street")
    label_branch.pack()
    
    exit_location_button = tk.Button(frame, text="exit", command=location.destroy)
    exit_location_button.pack()
    
    
root = tk.Tk()
root.title("Deposit Cash")

frame = tk.Frame(root)
frame.pack()



def msg_show():
    messagebox.showinfo("Account Created", "Your account has been created. Please log in.")

def Create_account():
    new_account = tk.Toplevel()
    new_account.title("Create new accounnt")
    
    frame = tk.Frame(new_account)
    frame.pack()

    label_id = tk.Label(frame, text="Enter your ID")
    label_id.pack()
    
    textbox_id = tk.Entry(frame)
    textbox_id.pack()
    
    label_password = tk.Label(frame, text="Enter your password")
    label_password.pack()
    
    textbox_password = tk.Entry(frame)
    textbox_password.pack()
    
    Submit_button = tk.Button(frame, text="submit",command=msg_show)
    Submit_button.pack()
    
    exit_button = tk.Button(frame, text="Close", command=new_account.destroy)
    exit_button.pack()
    
    
root = tk.Tk()
root.title("Create new accounnt")

frame = tk.Frame(root)
frame.pack()

def open_page():
    new_window = tk.Toplevel()
    new_window.title("Account Detail")

    frame = tk.Frame(new_window)
    frame.pack()

    label = tk.Label(frame, text="Name: Mehrnoush Fazlollah Nejad")
    label.pack()
    
    label_number = tk.Label(frame, text="Account Number: 12345")
    label_number.pack()
    
    label_sort_code = tk.Label(frame, text="Account Sort Code: 12 45 78")
    label_sort_code.pack()
    
    label_amount = tk.Label(frame, text="Account Balance: 5678 GBP")
    label_amount.pack()
    
    label_c_address = tk.Label(frame, text="Address: Lincoln, United Kingdom")
    label_c_address.pack()
    
    close_button = tk.Button(frame, text="Close", command=new_window.destroy)
    close_button.pack()

root = tk.Tk()
root.title("Account Detail")

frame = tk.Frame(root)
frame.pack()



root = tk.Tk()
root.title("Main Page")

button_account = tk.Button(root, text="create an account", command=Create_account)
button_account.pack()

button_withdraw_cash = tk.Button(root, text="withdraw_cash",command=location_Withdraw)
button_withdraw_cash.pack()

button_deposit_cash = tk.Button(root, text="deposit_cash",command=location )
button_deposit_cash.pack()

button_transfer = tk.Button(root, text="transfer from different accounts",command=transfer )
button_transfer.pack()

button_account_detail = tk.Button(root, text="view account detail", command=open_page)
button_account_detail.pack()
        
root.mainloop()