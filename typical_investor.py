import numpy as np
import rules

#Confirm validity of Buy-and-Hold S&P Comp rule for the typical investor that invests for their investment horizon
def TypicalInvestor(initial, date, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, GS10, recurringreturnGS10, yieldsearnings, time):
    time = int(time)*12
    horizon = len(date)-time
    new_array = np.zeros((horizon, 9))
    endbalances = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(date)-time):
        rules_list = [rules.BuyAndHold(initial, i, i+time, recurringreturn, recurringinvestment),
                 rules.BuyAndHold(initial, i, i+time, recurringreturnGS10, recurringinvestment),
                 rules.PERule(initial, i, i+time, recurringreturn, recurringinvestment, pe, pemedian, recurringreturnGS10),
                 rules.YieldRule(initial, i, i+time, recurringreturn, recurringinvestment, yields, yieldmedian, recurringreturnGS10),
                 rules.YieldAndGS10Rule(initial, i, i+time, recurringreturn, recurringinvestment, yields, yieldmedian, GS10, recurringreturnGS10),
                 rules.PEAndYieldRule(initial, i, i+time, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, recurringreturnGS10),
                 rules.PEORYieldRule(initial, i, i+time, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, recurringreturnGS10),
                 rules.PEAndYieldAndGS10Rule(initial, i, i+time, recurringreturn, recurringinvestment, pe, pemedian, yields, yieldmedian, GS10, recurringreturnGS10),
                 rules.FedRule(initial, i, i+time, recurringreturn, recurringinvestment, GS10, recurringreturnGS10, yieldsearnings)]
        for j in range(len(rules_list)):
            endbalances[j] = round(rules_list[j][len(rules_list[j])-1], 2)
            new_array[i-1, j] = endbalances[j]
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    for i in range(1, horizon):
        compare = new_array[i, 0]
        index = 0
        for j in range(1, len(rules_list)):
            if (compare < new_array[i, j]):
                index = j
                compare = new_array[i, j]
        if (index == 0):
            print (str(date[i]) + "-" + str(date[i+time]) + ": Buy-and-Hold S&P Comp")
            count0 += 1
        elif (index == 1):
            print (str(date[i]) + "-" + str(date[i+time]) + ": Buy-and-Hold GS10")
            count1 += 1
        elif (index == 2):
            print (str(date[i]) + "-" + str(date[i+time]) + ": P/E Rule")
            count2 += 1
        elif (index == 3):
            print (str(date[i]) + "-" + str(date[i+time]) + ": Yield Rule")
            count3 += 1
        elif (index == 4):
            print (str(date[i]) + "-" + str(date[i+time]) + ": Yield & GS10 Rule")
            count4 += 1
        elif (index == 5):
            print (str(date[i]) + "-" + str(date[i+time]) + ": P/E & Yield Rule")
            count5 += 1
        elif (index == 6):
            print (str(date[i]) + "-" + str(date[i+time]) + ": P/E or Yield Rule")
            count6 += 1
        elif (index == 7):
            print (str(date[i]) + "-" + str(date[i+time]) + ": P/E & Yield & GS10 Rule")
            count7 += 1
        elif (index == 8):
            print (str(date[i]) + "-" + str(date[i+time]) + ": Fed Rule")
            count8 += 1
        else:
            print ("Error")
    print ("Buy-and-Hold S&P Comp wins: " + str(count0) + " (" + str(round((count0/horizon)*100, 2)) + "%)")
    print ("Buy-and-Hold GS10 wins: " + str(count1) + " (" + str(round((count1/horizon)*100, 2)) + "%)")
    print ("P/E Rule wins: " + str(count2) + " (" + str(round((count2/horizon)*100, 2)) + "%)")
    print ("Yield Rule wins: " + str(count3) + " (" + str(round((count3/horizon)*100, 2)) + "%)")
    print ("Yield & GS10 Rule wins: " + str(count4) + " (" + str(round((count4/horizon)*100, 2)) + "%)")
    print ("P/E & Yield Rule wins: " + str(count5) + " (" + str(round((count5/horizon)*100, 2)) + "%)")
    print ("P/E or Yield Rule wins: " + str(count6) + " (" + str(round((count6/horizon)*100, 2)) + "%)")
    print ("P/E & Yield & GS10 Rule wins: " + str(count7) + " (" + str(round((count7/horizon)*100, 2)) + "%)")
    print ("Fed Rule wins: " + str(count8) + " (" + str(round((count8/horizon)*100, 2)) + "%)")
    return new_array
