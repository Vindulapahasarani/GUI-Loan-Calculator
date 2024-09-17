import tkinter as tk
import customtkinter as ck
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

app = ck.CTk()
ck.set_appearance_mode('dark-blue')
ck.set_default_color_theme('blue')
app.geometry('1200x600')
app.title('Loan Calculator')

#left frame
left_frame = ck.CTkFrame(master = app,
                         width = 350,
                         height = 580,
                         fg_color='#573CFA'
                         )
left_frame.place(x =10 ,y= 10)

title = ck.CTkLabel(master = left_frame, text = "Loan Calculator",
                    font = ("Arial",20))
title.pack(padx = 60,pady=50,fill="both", expand="True")

loan_amt_label= ck.CTkLabel(master = left_frame, text = "Enter Loan Amount",
                    font = ("Arial",20))
loan_amt_label.pack(padx = 30,pady=10,fill="both", expand="True")
loan_amt_entry= ck.CTkEntry(master = left_frame, font = ("Arial",20),
                            fg_color='white',text_color="black",corner_radius=20)
loan_amt_entry.pack(padx = 30,pady=10,fill="both", expand="True")

loan_int_label= ck.CTkLabel(master = left_frame, text = "Enter Loan Interest Rate ",
                    font = ("Arial",20))
loan_int_label.pack(padx = 30,pady=10,fill="both", expand="True")
loan_int_entry= ck.CTkEntry(master = left_frame, font = ("Arial",20),
                            fg_color='white',text_color="black",corner_radius=20)
loan_int_entry.pack(padx = 30,pady=10,fill="both", expand="True")

loan_tenure_label= ck.CTkLabel(master = left_frame, text = "Enter Loan Tenure",
                    font = ("Arial",20))
loan_tenure_label.pack(padx = 30,pady=10,fill="both", expand="True")
loan_tenure_entry= ck.CTkEntry(master = left_frame, font = ("Arial",20),
                            fg_color='white',text_color="black")
loan_tenure_entry.pack(padx = 30,pady=10,fill="both", expand="True")

submit_btn = ck.CTkButton(master=left_frame,text= "Submit",
                          font = ("Arial",20),corner_radius=20,
                          fg_color="black", hover_color="black",
                          command=lambda : submit())
submit_btn.pack(padx=30, pady=50, fill="both")


#Right frame
right_frame = ck.CTkFrame(master = app,
                         width = 800,
                         height = 580)
right_frame.place(x =370 ,y= 10)


#Submit Button
def submit():
    principal = float(loan_amt_entry.get())
    interest = float(loan_int_entry.get())
    tenure = int(loan_tenure_entry.get())
    data = calculations(principal,interest,tenure)
    interest_payable = table_display(data)
    chart_display(principal,interest_payable)

def chart_display():
    fig = plt.Figure(figsize=(3,3),dpi=100)
    plot = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig,master=right_frame)
    canvas.get_tk_widget().grid(row=0, column=1)
    x = [55,45]
    mylabels = ['Principal', 'Interest']
    myexplode = [0.0,0.1]
    plt.pie(x, labels=mylabels, autopct='%1.1f%%',explode=myexplode)
def table_display(data):

    table = ttk.Treeview(master=right_frame,
                         columns=('month','interest','principal','emi','balprinciple'),
                         show="headings")
    table.heading('month',text="Month", anchor='nw')
    table.heading('interest',text="Interest Payable", anchor='nw')
    table.heading('principal',text="Principal Payable", anchor='nw')
    table.heading('emi',text="EMI", anchor='nw')
    table.heading('balprinciple',text="Balance Principal", anchor='nw')
    interest_payable = 0.00
    for k in range(len(data)):
        table.insert(parent="", index=k,          
                    values= (data[k]['Month'],
                            data[k]['Interest_payable'],
                            data[k]['Principle Payable'],
                            data[k]['EMI'],
                            data[k]['Balance Principle'])
                )
        interest_payable = interest_payable + data[k]['Interest_payable']
    table.grid(row = 1, column=1, columnspan=2)



#Calculations
def calculations(p,i,t):
    roi_per_mon = i/12/100
    tenure_in_mon = t*12

    emi = round((p*roi_per_mon*pow(1+roi_per_mon,tenure_in_mon))/(pow(1+roi_per_mon,tenure_in_mon)-1))
    balance = p
    schedule = []
    for mon in range(tenure_in_mon):
        interest_montly_payable = round(balance * roi_per_mon)
        remain_emi_bal = round(emi - interest_montly_payable)
        balance = round(balance - remain_emi_bal)
        schedule.append({
            'Month':mon+1,
            'Interest_payable': interest_montly_payable,
            'Principle Payable': remain_emi_bal,
            'EMI': emi,
            'Balance Principle':balance
        })
    return schedule


app.mainloop()