# Candy Database Management Project (Python)

A Python project to manage, filter, and visualize a database of candies. 
This project demonstrates key data processing and visualization techniques using `pandas` and `matplotlib`.

## Features

1. **Candy Data Import and Processing**  
- Reads candy data from a file (`candies.txt`) and organizes it into a `pandas` DataFrame.
- Automatically calculates the `Total` column (`Price/kg * Quantity purchased`).

2. **Interactive Filtering**
- Filter candies interactively based on flavor and price. User inputs the flavor and a minimum price to display matching results.

3. **Interactive Deletion**
- Remove candies from the database by specifying their name via user input.

4. **Data Visualization**  
- Create and display two different types of graphs to visualize the candy data:
  **Graph 1**: Line chart showing the amount of candies by flavor.
  **Graph 2**: Bar chart comparing the price and quantity of candies.

## Files in the Repository

- **`candies.txt`**: Input file containing candy data.
- **Graphs**: Graphs are displayed in the program and can be saved if needed.
- **Script File**: Python script implementing all functionalities.

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/candy-database-management.git
    cd candy-database-management
    ```
    
2. Prepare the Input File:
- Ensure the **`candies.txt`** file is present in the project directory
- Format: A CSV-style text file with the columns: `Name, Flavor, Price, Quantity`.

4. Run the script:
   
    ```bash
    python candy_database_management.py
    ```
    
5. Follow the Prompts:
- Filter candies by flavor and price.
- Delete candies by name.
- Visualize candy data with interactive graphs.

## Key Skills Demonstrated

- Data Manipulation: Using Python's `pandas` library for cleaning, filtering, and analyzing data.
- Interactive Features: Console-based user inputs for a dynamic experience.
- Data Visualization: Creating and customizing graphs with `matplotlib`.

## Why This Project?

This project highlights my ability to:
- Work with data files and process information efficiently.
- Design interactive, user-friendly scripts.
- Generate clear, insightful visualizations for data analysis.
