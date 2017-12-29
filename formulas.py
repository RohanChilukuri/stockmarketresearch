from decimal import Decimal
import math
import numpy as np

#Collection of formulas used in main program

#Convert each member of a list to a percentage
def Percentage(old_list):
    new_list = []
    for i in range(len(old_list)):
        new_list.append(float(old_list[i])/100.0)
    return new_list

#Convert annual data to montly data for a list
def AnnualtoMonth(old_list):
    new_list = []
    for i in range(len(old_list)):
        new_list.append(float(old_list[i]/12.0))
    return new_list

#Formula for dividing members of two lists by each other
def DivideNumbers(numerator, divisor):
    new_list = []
    for i in range(len(numerator)):
        new_list.append(float(numerator[i])/float(divisor[i]))
    return new_list

#Calculate monthly return (monthly yield + delta of S&P Comp)
def MonthlyReturn(numerator, divisor):
    new_list = []
    for i in range(1, len(divisor)):
        new_list.append(float(numerator[i]) + ((float(divisor[i])-float(divisor[i-1]))/float(divisor[i-1])))
    return new_list

#Calculate Compound Annual Growth Rate
def CMGR(endvalue, total, time):
    return np.round(((math.pow(Decimal(endvalue)/Decimal(total), 1/time) - 1)*100), 2)
    
def CAGR(endvalue, total, time):
    return CMGR(endvalue, total, time)*12
