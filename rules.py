#Calculate monthly balances for nine common investment strategies

#Buy-and-Hold Stocks
#Buy-and-Hold GS10
def BuyAndHold(initial, date1, date2, recurringreturn, recurringinvestment):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
        new_list.append(balance)
        j += 1
    return new_list

#If PE at the end of the month > median PE, invest in GS10  for following month; otherwise stocks.
def PERule(initial, date1, date2, recurringreturn, recurringinvestment, pe, pemedian, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (pe[i-1] > pemedian):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If Yield at the end of the month < median Yield, invest  in GS10 for following month; otherwise stocks.
def YieldRule(initial, date1, date2, recurringreturn, recurringinvestment, yields, yieldmedian, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (yields[i-1] < yieldmedian):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If Yield too low (Yield Rule) AND GS10 Rate higher than Yield, invest in GS10 for following month; otherwise stocks.
def YieldAndGS10Rule(initial, date1, date2, recurringreturn, recurringinvestment, yields, yieldmedian, GS10, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (yields[i-1] < yieldmedian and GS10[i-1] > yields[i-1]):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If PE too high (P/E Rule) AND Yield too low (Yield Rule), invest in GS10 for following month; otherwise stocks.
def PEAndYieldRule(initial, date1, date2, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (pe[i-1] > pemedian and yields[i-1] < yieldmedian):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If PE is too high (P/E Rule) OR Yield too low (Yield Rule), invest in GS10 for following month; otherwise stocks.
def PEORYieldRule(initial, date1, date2, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (pe[i-1] > pemedian or yields[i-1] < yieldmedian):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If PE too high (P/E Rule) AND Yield too low (Yield Rule) AND GS10 Rate higher than Yield, invest in GS10 for following month; otherwise stocks.
def PEAndYieldAndGS10Rule(initial, date1, date2, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, GS10, recurringreturnGS10):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (pe[i-1] > pemedian and yields[i-1] < yieldmedian and GS10[i-1] > yields[i-1]):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list

#If earnings yield is greater than treasury yield, invest in stocks; otherwise GS10
def FedRule(initial, date1, date2, recurringreturn, recurringinvestment, GS10, recurringreturnGS10, yieldsearnings):
    new_list = []
    balance = float(initial)
    j = date1-1
    for i in range(date1, date2):
        if (yieldsearnings[i-1] < GS10[i-1]):
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturnGS10[j]))
            new_list.append(balance)
            j += 1
        else:
            balance = (balance + float(recurringinvestment)) * (1.0 + float(recurringreturn[j]))
            new_list.append(balance)
            j += 1
    return new_list
