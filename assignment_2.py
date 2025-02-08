# Import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open URL
url = "https://versionsof.net/core/8.0/8.0.0/"
driver.get(url)
time.sleep(2)  # Adjust delay based on page loading time

# Locate all tables
tables = driver.find_elements(By.XPATH, "//table")

all_data = []  # List to store table data

for table in tables:
    rows = table.find_elements(By.XPATH, ".//tr")

    table_data = []
    
    for row in rows:
        cells = row.find_elements(By.XPATH, ".//td | .//th")  # Handle both headers & data
        cell_texts = [cell.text.strip() if cell.text.strip() else "-" for cell in cells]  # Replace null with "-"

        # If header row, store separately
        if row == rows[0]:
            headers = cell_texts
        else:
            # Handle multiple values in a single cell
            max_splits = max(len(cell.split("\n")) for cell in cell_texts)
            split_rows = [cell.split("\n") + ["-"] * (max_splits - len(cell.split("\n"))) for cell in cell_texts]

            for i in range(max_splits):
                table_data.append([row[i] for row in split_rows])

    # Append table data with headers
    if table_data:
        all_data.extend([[headers] + table_data])

# Convert to DataFrame and save to CSV
if all_data:
    final_df = pd.concat([pd.DataFrame(data[1:], columns=data[0]) for data in all_data], ignore_index=True)
    final_df.to_csv("scraped_tables.csv", index=False)

    print("Scraping successful! Data saved to scraped_tables.csv")
else:
    print("No tables found!")

# Close the driver
driver.quit()
