# 1. Create a table Candies with columns: Name, Flavor, Price/kg, Quantity purchased, Total.
# 2. Fill the candy database with data from the text file candies.txt.
# 3. Fill in the Price column by adding the calculated amount values to the corresponding candy.

import pandas as pd

pd.set_option('display.max_rows', None)
df = pd.read_csv('candies.txt', delimiter=',', encoding='utf8')
df['Total'] = df.Price * df.Amount
print(df)

# 4. Print only those candies whose type is entered using the keyboard,
# e.g. "Chocolate" and price > 5 eur - entered using the keyboard.

print()
print('Printing of selected candies\n')

while True:
    flavor = input('Choose a candy flavor: ')
    price = int(input('Specify the lowest price for candies: '))
    selected_candies = df.loc[(df['Flavor'].str.contains(flavor, case=False)) & (df['Price'] > price)]
    if selected_candies.empty:
        print('There are no candies matching your selected criteria.')
    else:
        print(selected_candies)
        break

# 5. Delete the data of the candy name entered using input -
# delete the entire row in the table about that candy.

print()
print('Deleting selected candies')

while True:
    delete = input('Which candy would you like to delete? (Specify name): ').lower()
    deleted_lines = df[df['Name'].str.lower() == delete]
    if deleted_lines.empty:
        print('There are no candies matching your selected criteria.')
    else:
        df = df.drop(deleted_lines.index)
        print(f"The candy '{delete}' has been deleted.")
        break

print(df)

# 6. Using the Seaborn or Matplotlib Python libraries, display at least two graphs
# (of different types - linear, columnar, dotted, etc.).
# Change the graph parameters, e.g. color palette.
# Graphs must have axis names, values on the axes, a title.
# They can also have a legend or other selected info.

print()
print('Graph Nr. 1')

amount_by_flavor = df['Flavor'].value_counts()
print('Amount by flavor:')
print(amount_by_flavor)

from matplotlib import pyplot as plt

plt.plot(amount_by_flavor.index, amount_by_flavor, color='tab:orange')

plt.xlabel('Flavor')
plt.ylabel('Amount')
plt.title('Amount by flavor')

for i, amount in enumerate(amount_by_flavor):
    plt.text(i, amount + 1, str(amount), ha='center')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print()
print('Graph Nr. 2')

import numpy as np

sorted_df = df.sort_values(by='Price', ascending=False)

fig, ax = plt.subplots()

width = 0.25
index = np.arange(len(sorted_df))
column_1 = ax.bar(index, sorted_df['Price'], width, color='tab:orange', label='Price')

column_2 = ax.bar(index + width, sorted_df['Amount'], width, color='tab:blue', label='Amount')

ax.set_xlabel('Name')
ax.set_ylabel('Price(€), Amount')
ax.set_title('Price and amount')
ax.set_xticks(index + width / 2)
ax.set_xticklabels(sorted_df['Name'], rotation=90, ha='right')
ax.legend()

for columns in [column_1, column_2]:
    for column in columns:
        height = column.get_height()
        ax.annotate('{}'.format(height),
                    xy=(column.get_x() + column.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.set_facecolor('aliceblue')

plt.tight_layout()
plt.show()