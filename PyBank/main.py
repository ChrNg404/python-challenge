#Alright, let's program. Here are the things I need to do:
import pandas as pd
#Now we just need to save the path and put it to a variable

budget_data = "Resources/budget_data.csv"

#Then we read the file

budget_data_pd = pd.read_csv(budget_data)

#Let's call the head just to make sure it's the right file
print(budget_data_pd.head())

#Alright, now for the actual assignment:
# -The total number of months included in the dataset
#Ask for total months, or run individual calculation of each month
#Wait I'm dumb, the question is the total number of months in the entire dataset. I should just run a length

#count = budget_data_pd["Date"].value_counts()
#count
#This is code for moments where I want to count the number of times each date appears. 

len(budget_data_pd)
#This is code for the actual number of months in the entire dataset.


#-The total net amount of "Profit/Losses" over the entire period
# Let's just use the sum total of the profit column. I think we can add the already negative numbers to to the positive ones and it'll work.

total = budget_data_pd["Profit/Losses"].sum()
total


#-The greatest increase in profits (date and amount) over the entire period
#So let's just run a function for max and a function for min. Then print it.

minval = budget_data_pd.min()
maxval = budget_data_pd.max()
print(minval, maxval)

#The benefit is that we get the biggest loss and the biggest profit. However, the date is meaningless.
#If we wanted to change that, we would probably sort the data from highest to lowest.
