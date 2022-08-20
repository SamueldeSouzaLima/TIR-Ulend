from ast import NotIn
from investments import investments
from installments import installments
from datetime import datetime
from datetime import timedelta
import numpy_financial as npf

cashflows = {}

for investment in investments:
    
    date_time_obj = datetime.strptime(investment["created_at"], '%Y-%m-%d')
    investmentAmount=(-float(investment["amount"]))
    
    if date_time_obj in cashflows:
        cashflows[date_time_obj]+=investmentAmount
    else:
        cashflows[date_time_obj]=investmentAmount

for installment in installments:

    date_time_obj = datetime.strptime(installment["due_date"], '%Y-%m-%d') 
    installmentAmount=(float(installment["amount"]))

    if date_time_obj in cashflows:
        cashflows[date_time_obj]+=installmentAmount
    else:
        cashflows[date_time_obj]=installmentAmount

minDay=min(cashflows.keys())
maxDay=max(cashflows.keys())

currentDay=minDay
while currentDay < maxDay:
    if currentDay not in cashflows:
        cashflows[currentDay]=0.0
    currentDay +=timedelta(days=1)

cashflows=dict(sorted(cashflows.items()))

def calc_irr():
    data = []
    
    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 6)
    print("TIR:%.6f"% irr)

if __name__ == "__main__":
    calc_irr()