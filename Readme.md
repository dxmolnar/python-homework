# PyBank

## What is PyBank

In this project, a Python script is created to analyze financial records from a company's dataset (`budget_data.csv`). The dataset contains two columns: Date and Profit/Losses. The script performs the following calculations:

1. Determines the total number of months included in the dataset.
2. Calculates the net total amount of Profit/Losses over the entire period.
3. Computes the average of the changes in Profit/Losses over the entire period.
4. Identifies the greatest increase in profits, including the date and the corresponding amount.
5. Identifies the greatest decrease in losses, including the date and the corresponding amount.

## The final output of the PyBank.py file is as follows: 

> ### Financial Analysis
>  Total Months: 86  
>  Total: $38382578  
>  Average  Change: $-2315.12  
>  Greatest Increase in Profits: Feb-2012 ($1926159)  
>  Greatest Decrease in Profits: Sep-2013 ($-2196167)  

-----------------------------  
# PyRamen

## What is PyRamen?

PyRamen is a python script that evaluate the financial performance of the business.
The data in the sales_data.csv file is cross-referenced with internal menu data to perform calculations. The calculations of interest include total revenue and costs, and on a per-product basis to understand which products are doing well, which are doing poorly, and which products need to be removed.
In the main.py script pathlib and csv libraries were imported to read in the sales and menu data files. Then lists were created to hold the menu and sales data as objects in python. After this a dictionary was initialized to hold the future aggregated per-product results:

After running the script the results were saved in a .txt file.

> PyRamen
> ----------------------------
> spicy miso ramen {'01-count': 9238, '02-revenue': 110856.0, '03-cogs': 46190.0, '04-profit': 64666.0}
> tori paitan ramen {'01-count': 9156, '02-revenue': 119028.0, '03-cogs': 54936.0, '04-profit': 64092.0}
> truffle butter ramen {'01-count': 8982, '02-revenue': 125748.0, '03-cogs': 62874.0, '04-profit': 62874.0}
> tonkotsu ramen {'01-count': 9288, '02-revenue': 120744.0, '03-cogs': 55728.0, '04-profit': 65016.0}
> vegetarian spicy miso {'01-count': 9216, '02-revenue': 110592.0, '03-cogs': 46080.0, '04-profit': 64512.0}
> shio ramen {'01-count': 9180, '02-revenue': 100980.0, '03-cogs': 45900.0, '04-profit': 55080.0}
> miso crab ramen {'01-count': 8890, '02-revenue': 106680.0, '03-cogs': 53340.0, '04-profit': 53340.0}
> nagomi shoyu {'01-count': 9132, '02-revenue': 100452.0, '03-cogs': 45660.0, '04-profit': 54792.0}
> soft-shell miso crab ramen {'01-count': 9130, '02-revenue': 127820.0, '03-cogs': 63910.0, '04-profit': 63910.0}
> burnt garlic tonkotsu ramen {'01-count': 9070, '02-revenue': 126980.0, '03-cogs': 54420.0, '04-profit': 72560.0}
> vegetarian curry + king trumpet mushroom ramen {'01-count': 8824, '02-revenue': 114712.0, '03-cogs': 61768.0, '04-profit': 52944.0}




