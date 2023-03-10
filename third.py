import tkinter as tk

        
root = tk.Tk()

button_account = tk.Button(root, text="create an account")
button_account.pack()

button_withdraw_cash = tk.Button(root, text="withdraw_cash", )
button_withdraw_cash.pack()

button_deposit_cash = tk.Button(root, text="deposit_cash", )
button_deposit_cash.pack()

button_transfer = tk.Button(root, text="transfer from different accounts", )

root.mainloop()