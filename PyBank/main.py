
#import modules
import os
import csv



#define functions
def pybank(profitloss, inpCttotalmonths, inpTotalamount, inpaverageamount, greatestincamount, greatestincdate, greatestdecamount, greatestdecdate):
    
      
#    outTotalamount = inpTotalamount + int(profitloss[1])
    
    
    
#    #The total number of months included in the dataset
    outCttotalmonths = inpCttotalmonths + 1  
    
#    #The net total amount of "Profit/Losses" over the entire period
    outTotalamount = inpTotalamount + int(profitloss[1])

#    #The average of the changes in "Profit/Losses" over the entire period
    outaverageamount= (int(outTotalamount) / int(outCttotalmonths))
    
    #The greatest increase in profits (date and amount) over the entire period
#    while max(budgetCSV):
#        greatestincdate=budgetCSV[0]
#        greatestincamount=budgetCSV[1]
        
     
    if int(profitloss[1]) > greatestincamount:
        greatestincamount=int(profitloss[1])
        greatestincdate=profitloss[0]
           
    #outgreatestincamount=max(listThing[1])
    
    #The greatest decrease in losses (date and amount) over the entire period
#    while min(budgetCSV):
#        greatestdecamount=budgetCSV[1]
#        greatestdecdate=budgetCSV[0]

    if int(profitloss[1]) < greatestdecamount :
        greatestdecamount=int(profitloss[1])
        greatestdecdate=profitloss[0]

    
    return [outCttotalmonths, outTotalamount,outaverageamount,greatestincdate,greatestincamount,greatestdecamount,greatestdecdate]
#    print("Financial Analysis")
#    print("----------------------------")
#    print(f"Total Months: " (totalmonths= + str(outCttotalmonths)))
#    print(f"Profit/Loss Total:  str(outTotalamount)")
#    print(f"Average  Change:  str(averageamount)")
#    print(f"Greatest Increase in Profits: str(max(cttotalmonths))  str(max(greatestincamount))")
#    print(f"Greatest Decrease in Profits: str()")


#init variables
budgetCSV = "C:/Users/lorib/Desktop/python-challenge/PyBank/budget_data.csv"

cttotalmonths = 0
totalamount = 0
averageamount = 0.0
greatestincamount=0
greatestincdate=""
greatestdecamount=0
greatestdecdate=""



#do stuff
with open (budgetCSV ,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        listThing = pybank(row, cttotalmonths,totalamount,averageamount,greatestincamount,greatestincdate, greatestdecamount, greatestdecdate)
        cttotalmonths = listThing[0]
        totalamount = listThing[1]
        averageamount= listThing[2]
        greatestincdate=listThing[3]
        greatestincamount=listThing[4]
        greatestdecamount=listThing[5]
        greatestdecdate=listThing[6]
        
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:   {cttotalmonths}")
print(f"Profit/Loss Total:  {totalamount}")
print(f"Average  Change:  {averageamount}")
print(f"Greatest Increase in Profits: {greatestincdate} ${greatestincamount}")
print(f"Greatest Decrease in Profits: {greatestdecdate} ${greatestdecamount}")


