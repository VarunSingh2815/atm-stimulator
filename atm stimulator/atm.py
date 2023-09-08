import tkinter as tk
from tkinter import messagebox
import pickle

input_file = open('atm_sim_accounts.pickle', 'rb')
acc = pickle.load(input_file)

# GLOBAL VARIABLES FOR COLORS
w = '#98F5FF'
g = '#76EE00'
lg = '#F8F8FF'
r = '#FF3030'
f = '#FFFFE0'

class ATMLogin(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg=w, **kwargs)

        # SETTING UP WINDOW
        master.title('ATM- by Varun Singh')
        master.config(bg=w)
        master.geometry('250x385')
        master.resizable(False, False)

        # VARIABLES
        self.log = tk.StringVar()
        self.pin = tk.IntVar()
        self.pin.set('')
        self.reg_log = tk.StringVar()
        self.reg_pin = tk.IntVar()
        self.reg_pin.set('')
        self.reg_pin1 = tk.IntVar()
        self.reg_pin1.set('')
        self.reg_bal = tk.IntVar()

        # HEADINGS
        self.head = tk.Label(self, text=' WELCOME TO THE ATM ', justify='center', bg='#FFDEAD',fg='black', font='Courier 13')
        self.head.grid(row=0, column=0, pady=6)

        self.log_head = tk.Label(self, text=f"{11 * '-'} LOGIN {11 * '-'}", justify='center', bg=w, font='Courier 10')
        self.log_head.grid(row=1, column=0, pady=6)

        self.sig_head = tk.Label(self, text=f"{11 * '-'} SIGNUP {11 * '-'}", justify='center', bg=w, font='Courier 10')
        self.sig_head.grid(row=6, column=0, pady=6)

        # LOGIN SECTION
        self.log_name = tk.Label(self, text='Acc Name', bg=w, font='Courier 10')
        self.log_name.grid(row=2, column=0, sticky='w')
        self.log_box1 = tk.Entry(self, bg=lg, textvariable=self.log, width=22)
        self.log_box1.grid(row=2, column=0, sticky='e', padx=2)

        self.log_pin = tk.Label(self, text='Acc Pin', bg=w, font='Courier 10')
        self.log_pin.grid(row=3, column=0, sticky='w')
        self.log_box2 = tk.Entry(self, bg=lg, textvariable=self.pin, show='*', width=22)
        self.log_box2.grid(row=3, column=0, sticky='e', padx=2)

        self.log_btn = tk.Button(self, text='Login', bg=g, relief='flat', width=18, command=self.login)
        self.log_btn.grid(row=4, column=0, columnspan=2, pady=6, padx=2, sticky='e')

        self.log_out = tk.Label(self, text='', bg=w, font='Courier 9', width=19)
        self.log_out.grid(row=5, column=0, sticky='e')

        # SIGNUP SECTION
        self.reg_name = tk.Label(self, text='New Name', bg=w, font='Courier 9')
        self.reg_name.grid(row=7, column=0, sticky='w')
        self.log_box3 = tk.Entry(self, bg=lg, textvariable=self.reg_log, width=22)
        self.log_box3.grid(row=7, column=0, sticky='e', padx=2)

        self.sin_pin = tk.Label(self, text='New Pin', bg=w, font='Courier 9')
        self.sin_pin.grid(row=8, column=0, sticky='w')
        self.log_box4 = tk.Entry(self, bg=lg, textvariable=self.reg_pin, show='*', width=22)
        self.log_box4.grid(row=8, column=0, sticky='e', padx=2)

        self.sin_pin1 = tk.Label(self, text='Confirm Pin', bg=w, font='Courier 9')
        self.sin_pin1.grid(row=9, column=0, sticky='w')
        self.confirm_box = tk.Entry(self, bg=lg, textvariable=self.reg_pin1, show='*', width=22)
        self.confirm_box.grid(row=9, column=0, sticky='e', padx=2)

        self.sin_bal = tk.Label(self, text='Balance', bg=w, font='Courier 9')
        self.sin_bal.grid(row=10, column=0, sticky='w')
        self.log_box5 = tk.Entry(self, bg=lg, textvariable=self.reg_bal, width=22)
        self.log_box5.grid(row=10, column=0, sticky='e', padx=2)

        self.sin_btn = tk.Button(self, text='SignUp', bg=g, relief='flat', width=18, command=self.signup)
        self.sin_btn.grid(row=11, column=0, columnspan=2, pady=6, padx=2, sticky='e')

        self.sin_out = tk.Label(self, text='', bg=w, font='Courier 9', width=19)
        self.sin_out.grid(row=12, column=0, sticky='e')

        self.quit_btn = tk.Button(self, text='Quit', bg=r, relief='flat', command=lambda:
        [self.save(), self.quit()])
        self.quit_btn.grid(row=13, column=0, sticky='w', padx=4)

    def login(self):
        # CHECKING AUTHENTICITY
        name_var = self.log.get().capitalize()
        if name_var in acc:
            pin_var = self.pin.get()
            if acc[name_var]['pin'] == pin_var:
                self.log_out.config(text='Logging in...')
                self.pack_forget()
                ATMAction(name_var, self.master).pack()
            else:
                self.log_out.config(text='Incorrect pin.')
                self.log_box2.delete(0, 'end')
        else:
            self.log_out.config(text='Invalid Name!')
            self.log_box1.delete(0, 'end')
            self.log_box2.delete(0, 'end')

    def signup(self):
        # REGISTERING
        new_name = self.reg_log.get().capitalize()
        new_pin = self.reg_pin.get()
        new_pin1 = self.reg_pin1.get()
        s_balance = self.reg_bal.get()

        if new_pin == new_pin1:
            # SAVING USER CREDENTIALS
            acc.update({new_name: {'money': s_balance, 'pin': new_pin}})
            self.sin_out.config(text='Registered')

            # CLEARING BOXES
            self.log_box3.delete(0, 'end')
            self.log_box4.delete(0, 'end')
            self.confirm_box.delete(0, 'end')
            self.log_box5.delete(0, 'end')

        else:
            self.sin_out.config(text='Different pins!')

        # UPDATING TO DICTIONARY[WITHIN]
        output_file = open('atm_sim_accounts.pickle', 'wb')
        pickle.dump(acc, output_file)
        output_file.close()

    def save(self):
        # UPDATING TO DICTIONARY[SEPARATELY]
        output_file = open('atm_sim_accounts.pickle', 'wb')
        pickle.dump(acc, output_file)
        output_file.close()


class ATMAction(tk.Frame):

    def __init__(self, name_var, master=None, **kwargs):
        super().__init__(master, bg=w, **kwargs)

        # SETTING UP WINDOW
        master.title('ATM')
        master.config(bg=w)
        master.geometry('320x380')
        master.resizable(False, False)

        # VARIABLES
        self.name_var = name_var
        self.cb = acc[name_var]['money']
        self.w = tk.IntVar()
        self.w.set('')
        self.d = tk.IntVar()
        self.d.set('')

        # MAIN GREETING
        self.head = tk.Label(self, text=f'   Welcome Mr./Mrs. {name_var}   ', justify='center', bg=w, font='Courier 12')
        self.head.grid(row=0, column=0, columnspan=2, pady=4)

        # ACTION BUTTONS, LABELS AND ENTRIES
        self.bal_lab = tk.Label(self, text=f'Your current balance\nis Rs. {self.cb}', bg=w, font='Courier 11',
                                justify='center')
        self.bal_lab.grid(row=1, column=0, columnspan=2, pady=5, padx=4)

        self.withdraw = tk.Button(self, text='Withdraw', bg='#EE7AE9', font='Courier 12', relief=tk.RAISED, width=10, height=4,
                                  command=self.withdraw)
        self.withdraw.grid(row=2, column=0, sticky='w', pady=5)

        self.drawe = tk.Entry(self, bg=lg, justify='center', textvariable=self.w)
        self.drawe.grid(row=2, column=1, pady=5, padx=4, sticky='n')

        self.drawl = tk.Label(self, text=f'', bg=w, font='Courier 10')
        self.drawl.grid(row=2, column=1, pady=5, padx=4, sticky='s')

        self.deposit = tk.Button(self, text='Deposit', bg='#FF83FA', font='Courier 12', relief=tk.RAISED, width=10, height=4,
                                 command=self.deposit)
        self.deposit.grid(row=3, column=0, sticky='w', pady=5)

        self.depe = tk.Entry(self, bg=lg, justify='center', textvariable=self.d)
        self.depe.grid(row=3, column=1, pady=5, padx=4, sticky='n')

        self.depl = tk.Label(self, text=f'', bg=w, font='Courier 10')
        self.depl.grid(row=3, column=1, pady=5, padx=4, sticky='s')

        self.logout = tk.Button(self, text=f'Logout', bg='#FF4500', font='Courier 12', relief=tk.RAISED, command=self.logout)
        self.logout.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete = tk.Button(self, text=f'Delete Account', bg=r, font='Courier 12', relief=tk.RAISED, command=self.remove)
        self.delete.grid(row=5, column=0, columnspan=2, pady=6)

    def withdraw(self):
        with_amt = self.w.get()  # GETTING USER INPUT FROM ENTRY
        # CHECKING AMOUNT AGAINST BALANCE
        if with_amt > acc[self.name_var]['money']:
            self.drawl.config(text=f'Amount exceeds\ncurrent balance')
            self.drawe.delete(0, 'end')
        elif with_amt == '':
            self.drawl.config(text=f'Invalid amount!')
        else:
            acc[self.name_var]['money'] -= with_amt
            self.drawl.config(text=f'You successfully\nwithdrawal Rs. {with_amt}')
            self.drawe.delete(0, 'end')  # CLEARING ENTRY BOX

        # UPDATING TO DICTIONARY[WITHIN]
        output_file = open('atm_sim_accounts.pickle', 'wb')
        pickle.dump(acc, output_file)
        output_file.close()

        # DYNAMICALLY REFRESHING BALANCE
        self.cb = acc[self.name_var]['money']
        self.bal_lab.config(text=f'Your current balance\nis Rs. {self.cb}')

    def deposit(self):
        dep_amt = self.d.get()  # GETTING USER INPUT FROM ENTRY
        # CHECKING AMOUNT AGAINST BALANCE
        if dep_amt <= 0:
            self.depl.config(text=f'Invalid amount!')
            self.depe.delete(0, 'end')
        else:
            acc[self.name_var]['money'] += dep_amt
            self.depl.config(text=f'You successfully\ndeposited Rs. {dep_amt}')
            self.depe.delete(0, 'end')  # CLEARING ENTRY BOX

        # UPDATING TO DICTIONARY[WITHIN]
        output_file = open('atm_sim_accounts.pickle', 'wb')
        pickle.dump(acc, output_file)
        output_file.close()

        # DYNAMICALLY REFRESHING BALANCE
        self.cb = acc[self.name_var]['money']
        self.bal_lab.config(text=f'Your current balance\nis Rs. {self.cb}')

    def logout(self):
        if messagebox.askyesno('ATM', 'Are you sure you want to Logout?'):
            self.destroy()
            ATMLogin(self.master).pack()
        else:
            return

    def remove(self):
        if messagebox.askyesno('ATM', 'Are you sure you want to delete your account?'):
            acc.pop(self.name_var)
            self.destroy()
            ATMLogin(self.master).pack()

            # UPDATING TO DICTIONARY[WITHIN]
            output_file = open('atm_sim_accounts.pickle', 'wb')
            pickle.dump(acc, output_file)
            output_file.close()
        else:
            return


def main():
    root = tk.Tk()
    run = ATMLogin(root)
    run.pack()
    root.mainloop()


if __name__ == '__main__':
    main()