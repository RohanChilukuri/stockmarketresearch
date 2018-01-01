#Analyze 150 years of stock market data to determine whether active trading
#using any market-timing strategies would have beaten a passive buy-and-hold strategy

#MAIN PROGRAM

import csv
import math
import os.path
import statistics
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import rules
import formulas
import typical_investor
import time_plot_xaxis

#Read in stock market data from 1871 to 2017

#Specify path to csv file (not needed if the file is in the same directory) - remove # in following two lines
#userhome = os.path.expanduser('~')
#csvfile = os.path.join(userhome, 'Desktop', 'StockMarketResearch', 'Stock Market Data.csv')
with open('stock_market_data.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = {}
    for row in reader:
        for header, value in row.items():
            if value == '':
                continue
            else:
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
dates = data['Date']
spcomp = data['S&P Comp']
dividend = data['Dividend']
earnings = data['Earnings']
GS10 = data['GS10']

#Convert annual GS10 to a percentage
annualGS10 = formulas.Percentage(GS10)

#Calculate monthly GS10 from annual GS10
monthlyGS10 = formulas.AnnualtoMonth(annualGS10)

#Calculate annual yield (Dividend / S&P Comp)
annualyield = formulas.DivideNumbers(dividend, spcomp)

#Calculate monthly yield from annual yield
monthlyyield = formulas.AnnualtoMonth(annualyield)

#Calculate earnings yield (Earnings/S&P Comp)
earningsyield = formulas.DivideNumbers(earnings, spcomp)

#Calculate annualP/E ratio (S&P Comp per year/earnings per year)
annualpe = formulas.DivideNumbers(spcomp, earnings)

#Calculate monthly return (monthly yield + delta of S&P Comp)
monthlyreturn = formulas.MonthlyReturn(monthlyyield, spcomp)

#Calculate median of yield and P/E ratio for computations
medianyield = statistics.median(annualyield)
medianpe = statistics.median(annualpe)

#Ask for inital investment, monthly investment, investent horizon, and start and end date
initialinvestment = input("How much for initial investment (in dollars)? ")
while (not(initialinvestment.isnumeric())):
    print ("Please enter a positive or 0 dollar value.")
    initialinvestment = input("How much for initial investment (in dollars)? ")
monthlyinvestment = input("Amount for monthly investment (in dollars)? ")
while (not(monthlyinvestment.isnumeric())):
    print ("Please enter a positive or 0 dollar value.")
    monthlyinvestment = input("Amount for monthly investment (in dollars)? ")
startdate = input("Start in what year and month(1871.02 - 2017.03)? ")
while (startdate not in dates or startdate == '1871.01'):
    print ("Outside range or need to place in format yryr.mm")
    startdate = input("Start in what year and month(1871.02 - 2017.03)? ")
enddate = input("End in what year and month(1871.02 - 2017.03)? ")
while (enddate not in dates or enddate == '1871.01'):
    print ("Outside range or need to place in format yryr.mm")
    enddate = input("End in what year and month(1871.02 - 2017.03)? ")
while (enddate <= startdate):
    print ("End date must be after start date")
    startdate = input("Start in what year and month(1871.02 - 2017.03)? ")
    enddate = input("End in what year and month(1871.02 - 2017.03)? ")
investmenthorizon = input("What is your typical investment horizon (years)? ")
while (not(investmenthorizon.isnumeric()) or int(investmenthorizon) > 146 or int(investmenthorizon) == 0):
    print ("Please enter a positive integer value less than 147 and greater than 0.")
    investmenthorizon = input("What is your typical investment horizon (years)? ")


#Store index of start and end date in dates, investment period, and totalinvestment
startdate = dates.index(startdate)
enddate = dates.index(enddate)+1
period = enddate-startdate-1
totalinvestment = int(initialinvestment) + int(monthlyinvestment)*int(period)

#Call each function to calculate balances of investment stategies
buyandholdspcomprule = rules.BuyAndHold(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment)
buyandholdGS10rule = rules.BuyAndHold(initialinvestment, startdate, enddate, monthlyGS10, monthlyinvestment)
perule = rules.PERule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualpe, medianpe, monthlyGS10)
yieldrule = rules.YieldRule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualyield, medianyield, monthlyGS10)
yieldandGS10rule = rules.YieldAndGS10Rule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualyield, medianyield, annualGS10, monthlyGS10)
peandyieldrule = rules.PEAndYieldRule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualpe, medianpe, annualyield, medianyield, monthlyGS10)
peoryieldrule = rules.PEORYieldRule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualpe, medianpe, annualyield, medianyield, monthlyGS10)
peandyieldandGS10rule = rules.PEAndYieldAndGS10Rule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualpe, medianpe, annualyield, medianyield, annualGS10, monthlyGS10)
fedrule = rules.FedRule(initialinvestment, startdate, enddate, monthlyreturn, monthlyinvestment, annualGS10, monthlyGS10, earningsyield)

#Return end balance for each investment strategy
buyandholdspcompruleendbalance = round(buyandholdspcomprule[len(buyandholdspcomprule)-1], 2)
buyandholdGS10ruleendbalance = round(buyandholdGS10rule[len(buyandholdGS10rule)-1], 2)
peruleendbalance = round(perule[len(perule)-1], 2)
yieldruleendbalance = round(yieldrule[len(yieldrule)-1], 2)
yieldandGS10ruleendbalance = round(yieldandGS10rule[len(yieldandGS10rule)-1], 2)
peandyieldruleendbalance = round(peandyieldrule[len(peandyieldrule)-1], 2)
peoryieldruleendbalace = round(peoryieldrule[len(peoryieldrule)-1], 2)
peandyieldandGS10ruleendbalance = round(peandyieldandGS10rule[len(peandyieldandGS10rule)-1], 2)
fedruleendbalance = round(fedrule[len(fedrule)-1], 2)

#Confirm validity of Buy-and-Hold S&P Comp rule for the typical investor that invests for their investment horizon
typicalinvestor = typical_investor.TypicalInvestor(initialinvestment, dates, monthlyreturn, monthlyinvestment, annualpe, medianpe, annualyield, medianyield, annualGS10, monthlyGS10, earningsyield, investmenthorizon)
#Output array to csv file if desired (remove # in next line)
#np.savetxt("Stock Research.csv", typicalinvestor, delimiter=",")

#Print total investment, end balances, and CAGR of each rule
print ("Total investment: $" + str(totalinvestment))
print ("Buy-and-Hold S&P Comp - End Balance:" + ' ${:,.0f}'.format(buyandholdspcompruleendbalance) + " / CAGR: " + str(formulas.CAGR(buyandholdspcompruleendbalance, totalinvestment, period)) + "%")
print ("Buy-and-Hold GS10 - End Balance:" + ' ${:,.0f}'.format(buyandholdGS10ruleendbalance) + " / CAGR: " + str(formulas.CAGR(buyandholdGS10ruleendbalance, totalinvestment, period)) + "%")
print ("P/E Rule - End Balance:" + ' ${:,.0f}'.format(peruleendbalance) + " / CAGR: " + str(formulas.CAGR(peruleendbalance, totalinvestment, period)) + "%")
print ("Yield Rule - End Balance:" + ' ${:,.0f}'.format(yieldruleendbalance) + " / CAGR: " + str(formulas.CAGR(yieldruleendbalance, totalinvestment, period)) + "%")
print ("Yield & GS10 Rule - End Balance:" + ' ${:,.0f}'.format(yieldandGS10ruleendbalance) + " / CAGR: " + str(formulas.CAGR(yieldandGS10ruleendbalance, totalinvestment, period)) + "%")
print ("P/E & Yield Rule - End Balance:" + ' ${:,.0f}'.format(peandyieldruleendbalance ) + " / CAGR: " + str(formulas.CAGR(peandyieldruleendbalance, totalinvestment, period)) + "%")
print ("P/E or Yield Rule - End Balance:" + ' ${:,.0f}'.format(peoryieldruleendbalace) + " / CAGR: " + str(formulas.CAGR(peoryieldruleendbalace, totalinvestment, period)) + "%")
print ("P/E & Yield & GS10 Rule - End Balance:" + ' ${:,.0f}'.format(peandyieldandGS10ruleendbalance) + " / CAGR: " + str(formulas.CAGR(peandyieldandGS10ruleendbalance, totalinvestment, period)) + "%")
print ("Fed Rule - End Balance:" + ' ${:,.0f}'.format(fedruleendbalance) + " / CAGR: " + str(formulas.CAGR(fedruleendbalance, totalinvestment, period)) + "%")

#Create a bar graph that plots the end balance of each investment strategy
ind = ['Buy-and-Hold S&P Comp', 'Buy-and-Hold GS10', 'P/E Rule', 'Yield Rule',
       'Yield & GS10 Rule', 'P/E & Yield Rule', 'P/E or Yield Rule', 'P/E & Yield & GS10 Rule', 'Fed Rule']
indaxis = np.arange(len(ind))
depaxis = (buyandholdspcompruleendbalance, buyandholdGS10ruleendbalance,
           peruleendbalance, yieldruleendbalance, yieldandGS10ruleendbalance,
           peandyieldruleendbalance, peoryieldruleendbalace, peandyieldandGS10ruleendbalance,
           fedruleendbalance)
fig, ax = plt.subplots(1, figsize=(12,8))
bars = ax.bar(indaxis, depaxis)
ax.set_ylabel('End Balance ($)')
ax.set_xlabel('Investment Strategy')
ax.set_xticks(indaxis)
ax.set_xticklabels(ind, fontsize=8, weight='bold', rotation=15)
ax.set_title('End Balance vs. Investment Strategy')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2, height*1.002, '${:,.0f}'.format(height), weight='bold', ha='center', va='bottom')

#Create a time plot that plots the change in balance of investment strategies over time
plt.figure(2, figsize=(12,8))
colors = ['#000000', '#ff0000', '#008080', '#0000ff', '#00ff00', '#ff00ff', '#00ffff', '#ffa500', '#800000']
rules = [buyandholdspcomprule, buyandholdGS10rule, perule, yieldrule, yieldandGS10rule,
         peandyieldrule, peoryieldrule, peandyieldandGS10rule, fedrule]
datesyears = [x[:-3] for x in dates]
interval = math.ceil((enddate-startdate)/12)
nexttick = startdate + interval
timeplotxaxis = time_plot_xaxis.TimePlotXAxis(interval, nexttick, startdate, enddate, dates, datesyears)
xaxis = np.arange(len(timeplotxaxis))
for i in range(len(ind)):
    plt.plot(xaxis, rules[i], colors[i], label=ind[i])
plt.xticks(xaxis, timeplotxaxis)
plt.xlabel('Date')
plt.ylabel('Balance ($)')
plt.title('Balance vs. Date')
plt.legend()
plt.show()
