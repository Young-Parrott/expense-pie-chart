# This program will generate a pie chart that contains expenses for the last month.
# The categories will be: rent, gas, food, clothing, car payment, and misc.
# The program will accept values for these from input, and place them into a text file.
# The program will then take the values, either read from the file, or from input and display them
# in a pie chart, also will track: total spent.

import matplotlib.pyplot as plt
import numpy as np
import datetime

# creates a file with the name of the current month_expenses.txt
# adds input gathered to file.
def add_to_file(lst):
    now = datetime.date.today()
    month = now.strftime('%B')
    #open text file for storage
    f = open(f'{month}_expenses.txt','w')
    
    #add values to file
    for value in lst:
        f.write(str(value))
        
    #close file
    f.close()

    

def main():
    now = datetime.date.today()
    #gather input
    month = now.strftime('%B')
    rent = input('Enter the amount you paid for rent this month: $')
    gas = input('Enter the amount you paid for gas this month: $')
    food = input('Enter the amount you paid for food this month: $')
    clothing = input('Enter the amount you paid for clothing this month: $')
    car = input('Enter the amount you paid for you vehicle this month: $')
    misc = input('Enter the amount you spent for miscellaneous purchases: $')
    total = float(rent) + float(gas) + float(food) + float(clothing) + float(car) + float(misc)
    total = str(total)
    #place values into list
    lst = [rent, gas, food, clothing, car, misc]
    myLabels =["Rent", "Gas", "Food", "Clothing", "Car", "Misc"]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    
    #call add to file
    add_to_file(lst)
        
    #generate pie chart
    #convert list into numpy array
    data = np.asarray(lst)

    #plot the pie chart
    plt.pie(data, autopct='%1.1f%%', startangle=90, colors=colors, labels=myLabels)
    plt.title(month + ' Expenses', loc='center')
    plt.text(-2, 1, f'Total Expenses: ${total}')
    plt.text(-2, .90, f'Rent: ${rent}')
    plt.text(-2, .80, f'Gas: ${gas}')
    plt.text(-2, .70, f'Food: ${food}')
    plt.text(-2, .60, f'Clothing: ${clothing}')
    plt.text(-2, .50, f'Car: ${car}')
    plt.text(-2, .40, f'Misc: ${misc}')
    plt.show()

if __name__ == '__main__':
    main()
    
