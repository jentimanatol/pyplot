import matplotlib.pyplot as plt
import seaborn as sns

# Data stored in a list of dictionaries
data = [
    {"category": "Auto Services", "date": "09/19", "description": "MERCEDES-BENZ OF BURLI", "amount": 292.81},
    {"category": "Auto Services", "date": "10/11", "description": "FRANKS AUTO INSPECTION", "amount": 35.00},
    {"category": "Auto Supplies", "date": "05/28", "description": "AUTOZONE #5138", "amount": 37.18},
    {"category": "Education", "date": "06/03", "description": "Pearsonplus.com", "amount": 7.43},
    {"category": "Education", "date": "08/05", "description": "Pearsonplus.com", "amount": 7.43},
    {"category": "Education", "date": "09/06", "description": "Pearsonplus.com", "amount": 7.43},
    {"category": "Electronics", "date": "09/12", "description": "BEST BUY", "amount": 28.68},
    {"category": "Electronics", "date": "10/23", "description": "BEST BUY", "amount": 89.35},
    {"category": "Fees", "date": "04/15", "description": "SEC OF MA EXPEDITED FE", "amount": 10.00},
    {"category": "Fees", "date": "04/15", "description": "SEC OF MA FILING FEE", "amount": 100.00},
    {"category": "Fees", "date": "11/18", "description": "ICI*FEE BOSTON WEB PMT", "amount": 1.10},
    {"category": "Fees", "date": "11/18", "description": "ICI*FEE BOSTON WEB PMT", "amount": 1.10},
    {"category": "Government Services", "date": "05/27", "description": "CITY OF NEWBURYPORT", "amount": 1.50},
    {"category": "Government Services", "date": "07/25", "description": "TBI", "amount": 290.70},
    {"category": "Government Services", "date": "11/18", "description": "RMV E-SERVICES", "amount": 60.00},
    {"category": "Home Improvement", "date": "09/23", "description": "LOWES #02723", "amount": 32.08},
    {"category": "Home Improvement", "date": "09/27", "description": "LOWES #02723", "amount": 110.87},
    {"category": "Home Improvement", "date": "09/30", "description": "LOWES #02723", "amount": 109.40},
    {"category": "Home Improvement", "date": "10/04", "description": "THE HOME DEPOT #2614", "amount": 33.09},
    {"category": "Home Improvement", "date": "11/06", "description": "LOWES #01914", "amount": 190.19},
    {"category": "Home Improvement", "date": "11/25", "description": "THE HOME DEPOT #2674", "amount": 2.56},
    {"category": "Insurance", "date": "07/12", "description": "ASI / PROGRESSIVE", "amount": 877.00},
    {"category": "Insurance", "date": "07/15", "description": "HARTFORD INS. PREMIUM", "amount": 1813.00},
    {"category": "Insurance", "date": "08/19", "description": "GEICO *AUTO", "amount": 1119.15},
    {"category": "Legal Services", "date": "11/18", "description": "AFP*Tsizer Law P C", "amount": 185.40},
    {"category": "Office Supplies", "date": "01/15", "description": "STAPLES", "amount": 19.11},
    {"category": "Online Shopping", "date": "07/03", "description": "AMZN Mktp US", "amount": 112.63},
    {"category": "Online Shopping", "date": "08/07", "description": "p.com", "amount": 127.49},
    {"category": "Online Shopping", "date": "09/10", "description": "AMZN Mktp US", "amount": 52.12},
    {"category": "Online Shopping", "date": "09/10", "description": "AMAZON MKTPL", "amount": 16.22},
    {"category": "Parking", "date": "04/18", "description": "PARKING METERS PILOT P", "amount": 4.25},
    {"category": "Parking", "date": "04/25", "description": "PARKING METERS PILOT P", "amount": 4.25},
    {"category": "Parking", "date": "07/02", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "07/09", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "07/09", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "07/22", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "07/29", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "08/05", "description": "OPS*52 MAIN ST", "amount": 6.00},
    {"category": "Parking", "date": "08/12", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "08/26", "description": "PARKWHIZ, INC.", "amount": 90.00},
    {"category": "Parking", "date": "08/30", "description": "OPS*52 MAIN ST", "amount": 6.00},
    {"category": "Parking", "date": "09/03", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "09/09", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "09/16", "description": "OPS*52 MAIN ST", "amount": 6.00},
    {"category": "Parking", "date": "09/16", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "09/30", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "10/14", "description": "PARKING METERS PILOT P", "amount": 4.00},
    {"category": "Parking", "date": "10/18", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Parking", "date": "10/21", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "10/21", "description": "PARKING METERS PILOT P", "amount": 4.25},
    {"category": "Parking", "date": "10/28", "description": "OPS*52 MAIN ST", "amount": 6.00},
    {"category": "Parking", "date": "10/31", "description": "LAZ PKG L05236-FLOWBIR", "amount": 4.00},
    {"category": "Parking", "date": "11/04", "description": "OPS*52 MAIN ST", "amount": 2.00},
    {"category": "Parking", "date": "11/18", "description": "BOSTON PARKING TICKETS", "amount": 40.00},
    {"category": "Parking", "date": "11/18", "description": "BOSTON PARKING TICKETS", "amount": 40.00},
    {"category": "Parking", "date": "11/18", "description": "OPS*52 MAIN ST", "amount": 6.00},
    {"category": "Parking", "date": "11/19", "description": "LAZ PKG L05236-FLOWBIR", "amount": 2.00},
    {"category": "Parking", "date": "12/11", "description": "OPS*52 MAIN ST", "amount": 4.00},
    {"category": "Postage", "date": "04/15", "description": "USPS PO", "amount": 0.68},
    {"category": "Recreation", "date": "07/08", "description": "NH STATE PARKS METERS", "amount": 9.25},
    {"category": "Retail", "date": "06/10", "description": "FIVE BELOW 8050", "amount": 5.31},
    {"category": "Retail", "date": "07/24", "description": "DOLLAR TREE", "amount": 5.31},
    {"category": "Retail", "date": "08/19", "description": "DOLLAR TREE", "amount": 5.31},
    {"category": "Retail", "date": "08/26", "description": "DOLLAR TREE", "amount": 2.66},
    {"category": "Retail", "date": "09/09", "description": "DOLLAR TREE", "amount": 5.31},
    {"category": "Retail", "date": "09/09", "description": "DOLLAR TREE", "amount": 3.98},
    {"category": "Retail", "date": "09/16", "description": "BUNKER-HILL-CC-BKSTORE", "amount": 57.18},
    {"category": "Retail", "date": "09/16", "description": "DOLLAR TREE", "amount": 3.98},
    {"category": "Retail", "date": "11/11", "description": "DOLLAR TREE", "amount": 3.98},
    {"category": "Shipping", "date": "11/19", "description": "THE UPS STORE 4423", "amount": 25.32},
    {"category": "Transportation", "date": "02/08", "description": "UBER", "amount": 33.38},
    {"category": "Transportation", "date": "05/03", "description": "LYFT", "amount": 33.99},
    {"category": "Travel", "date": "02/05", "description": "DELTA", "amount": 232.60},
    {"category": "Travel", "date": "02/12", "description": "Trip.com", "amount": 87.06},
    {"category": "Travel", "date": "02/12", "description": "DELTA", "amount": 183.10},
    {"category": "Utilities", "date": "04/29", "description": "G MELLO DISPOSAL CORP", "amount": 258.00},
    {"category": "Web Services", "date": "12/05", "description": "DNH*GODADDY#3448568724", "amount": 22.17},
]

# Convert the list of dictionaries to a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Group by category and calculate the total amount for each category
category_totals = df.groupby('category')['amount'].sum().reset_index()

# Sort the categories by total amount (descending)
category_totals = category_totals.sort_values(by='amount', ascending=False)

# Set up the visualization
plt.figure(figsize=(12, 8))
sns.barplot(x='amount', y='category', data=category_totals, palette='viridis')

# Add labels and title
plt.xlabel('Total Amount ($)', fontsize=14)
plt.ylabel('Category', fontsize=14)
plt.title('Total Expenses by Category', fontsize=16)

# Add value labels on the bars
for index, value in enumerate(category_totals['amount']):
    plt.text(value, index, f'${value:,.2f}', va='center', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()