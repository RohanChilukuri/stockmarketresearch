#Create a list contatining the values for the x-axis of a time plot
def TimePlotXAxis(period, nextmark, date1, date2, date, dateyr):
    new_list = []
    new_list.append(dateyr[date1])
    if (not ((date2-date1) == 0)):
        for i in range(date1+1, date2):
            if (period == 1):
                new_list.append(date[i])
            elif (i == nextmark):
                new_list.append(dateyr[i])
                nextmark = nextmark + period
            else:
                new_list.append('')
    return new_list
