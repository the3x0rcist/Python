# A simple python WebScraper


import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error

# Function to fetch data from Scrapethissite
def fetch_country_data():
    url = 'https://scrapethissite.com/pages/simple'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    countries = []
    rows = soup.select('div.container > div.row > div.col-md-12 > table > tbody > tr')

    for row in rows[:20]:  # Only take the first 20 countries
        cols = row.find_all('td')
        country = cols[0].text.strip()
        capital = cols[1].text.strip()
        population = cols[2].text.strip().replace(',', '')
        area = cols[3].text.strip().replace(',', '')

        countries.append((country, capital, int(population), float(area)))

    return countries

# Function to save data to MySQL database
def save_to_db(data):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',        # Replace with your MySQL host
            user='your_username',    # Replace with your MySQL username
            password='your_password',# Replace with your MySQL password
            database='your_database' # Replace with your MySQL database name
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS countries (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    country VARCHAR(100),
                    capital VARCHAR(100),
                    population INT,
                    area FLOAT
                )
            ''')

            # Insert data into the table
            cursor.executemany('''
                INSERT INTO countries (country, capital, population, area)
                VALUES (%s, %s, %s, %s)
            ''', data)

            connection.commit()
            print("Data has been successfully saved to the database.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function to execute the script
if __name__ == "__main__":
    data = fetch_country_data()
    save_to_db(data)
