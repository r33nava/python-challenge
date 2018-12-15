# -*- coding: utf-8 -*-
"""
Author: Reena Desai

Python Homework: PyBank

Description: In this challenge, I am tasked with creating a Python script 
for analyzing the financial records of my company. I will give a set of financial 
data called budget_data.csv. 

The dataset is composed of two columns: Date and Profit/Losses. 

My task is to create a Python script that analyzes the records to calculate each 
of the following:

The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period


"""

#Dependencies
import csv
import os 

#Create empty lists sets for dateslist and revenue amounts
dateslist = []
revenuelist = []

#Open CSV file
with open('budget_data.csv') as budget_data:
  csvreader = csv.reader(budget_data)
  
 
    
#Find number of months in data set
num_of_months = len(dateslist)



#Find sum of revenue 
  
for i in budget_data:
    total_revenue = total_revenue + total_revenue(i)
  
#Find change in revenue per month

monthly_change = []
j = 0

for j in num_of_months:
  if j == 0:
    monthly_change.append(0)
  else: 
    monthly_change.append(revenue(j) - prevous revenue) 

    
#Find average change in monthly revenue
sum_monthly_change = 0
x = 0 

for x in range(num_of_months):
  sum_monthly_change = sum_monthly_change + x
  average_monthly_change = sum_monthly_change/num_of_months


#Find Greatest Increase in Profits
  
greatest_increase = 0
  
y=0
  for y in num_of_months:
  if y == 0:
    revenue_change(y) > greatest_increase
    greatest_increase = revenue_change
  else:  
    y = y+1 
    
#Find Greatest Decrease in Profits

greatest_decrease = 0
  
  for z in num_of_months:
  if z == 0:
    revenue_change(z) > greatest_decrease
    greatest_decrease = revenue_change
  else:  
    z = z+1 


# Export to textfile 
file = ("output.txt","w")
with open(file) as txtfile:
    file.write("Financial Analysis")
    file.write("----------------------")
    file.write("Total Months: " + num_of_months)
    file.write("Total: " + '$' + total_revenue)
    file.write("Average Change: " + '$' + average_monthly_change)
    file.write("Greatest Increase in Profits: " + greatest_increase)  
    file.write("Greatest Decrease in Profits: " + greatest_decrease)  


#Print Results
print("Financial Analysis")
print("----------------------")
print("Total Months: " + num_of_months)
print("Total: " + '$' + total_revenue)
print("Average Change: " + '$' + average_monthly_change)
print("Greatest Increase in Profits: " + " ($" + greatest_increase + ")")  
print("Greatest Decrease in Profits: " + " ($" + greatest_decrease + ")")  