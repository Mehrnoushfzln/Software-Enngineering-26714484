import tkinter as tk

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

button_account = tk.Button(root, text="create an account", )
button_account.pack()

button_withdraw_cash = tk.Button(root, text="withdraw_cash", )
button_withdraw_cash.pack()

button_deposit_cash = tk.Button(root, text="deposit_cash", )
button_deposit_cash.pack()

button_transfer = tk.Button(root, text="transfer from different accounts", )
button_transfer.pack()

button_account_detail = tk.Button(root, text="view account detail", command=open_page)
button_account_detail.pack()
        
root.mainloop()