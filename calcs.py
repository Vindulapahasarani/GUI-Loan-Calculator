import pandas as pd
principal = 100000
aroi = 12
tenure = 1
def calculations(p,i,t):
    roi_per_mon = i/12/100
    tenure_in_mon = t*12

    emi = round((p*roi_per_mon*pow(1+roi_per_mon,tenure_in_mon))/(pow(1+roi_per_mon,tenure_in_mon)-1))
    print('Emi Amount is '+str(emi))
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
    
print(pd.DataFrame(calculations(principal, aroi, tenure)))