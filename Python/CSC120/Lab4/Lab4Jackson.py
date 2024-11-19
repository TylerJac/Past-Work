# ===============================================================

# Name: Tyler Jackson

# Date: 3/25/2024

# Course: CSC 120 NLE01

# Algorithm:Connect to Database Function,
# Display Cities by Population in Ascending Order Function,
# Display Cities by Population in Descending Order Function,
# Display Cities by Name Function,
# Display Total Population Function,
# Display Average Population Function,
# Display City with Highest Population Function,
# Display City with Lowest Population Function,
# Main Function


# References: in class, W3Schools

# ===============================================================

# Import the sqlite3 module for database operations
import sqlite3


def connect_to_database():
    """
    Connects to the 'cities.db' database.

    Returns:
        sqlite3.Connection: Connection object representing the database connection.
    """
    # Establish connection to the database
    conn = sqlite3.connect('cities.db')
    return conn


def display_cities_by_population_ascending():
    """
    Displays a list of cities sorted by population in ascending order.

    Returns: A list of tuples representing city information (CityID, CityName, Population).
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute the SQL query to select cities sorted by population in ascending order
    cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
    # Fetch all rows from the result set
    cities = cursor.fetchall()
    # Close the database connection
    conn.close()
    return cities


def display_cities_by_population_descending():
    """
    Displays a list of cities sorted by population in descending order.

    Returns: A list of tuples representing city information (CityID, CityName, Population).
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute the SQL query to select cities sorted by population in descending order
    cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
    # Fetch all rows from the result set
    cities = cursor.fetchall()
    # Close the database connection
    conn.close()
    return cities


def display_cities_by_name():
    """
    Displays a list of cities sorted by name.

    Returns: A list of tuples representing city information (CityID, CityName, Population).
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute SQL query to select all columns from the 'Cities' table sorted by CityName
    cursor.execute("SELECT * FROM Cities ORDER BY CityName")
    # Fetch all rows from the result set
    cities = cursor.fetchall()
    # Close the database connection
    conn.close()
    return cities


def display_total_population():
    """
    Displays the total population of all the cities.

    Returns: Total population of all cities.
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute SQL query to calculate the sum of population from the 'Cities' table
    cursor.execute("SELECT SUM(Population) FROM Cities")
    # Fetch the result of the SQL query and extract the total population
    total_population = cursor.fetchone()[0]
    # Close the database connection
    conn.close()
    return total_population


def display_average_population():
    """
    Displays the average population of all the cities.

    Returns: Average population of all cities.
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute SQL query to calculate the average population of all cities
    cursor.execute("SELECT AVG(Population) FROM Cities")
    # Fetch the result of the SQL query and access the first element (average population)
    average_population = cursor.fetchone()[0]
    # Close the database connection
    conn.close()
    return average_population


def display_city_with_highest_population():
    """
    Displays the city with the highest population.

    Returns: A tuple representing city information (CityID, CityName, Population).
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute SQL query to select all columns from the 'Cities' table,
    # ordering the result by population in descending order, and limit the result to 1 row
    cursor.execute("SELECT * FROM Cities ORDER BY Population DESC LIMIT 1")
    # Fetch the next row from the result set
    city = cursor.fetchone()
    # Close the database connection
    conn.close()
    return city


def display_city_with_lowest_population():
    """
    Displays the city with the lowest population.

    Returns: A tuple representing city information (CityID, CityName, Population).
    """
    # Connect to the database
    conn = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute SQL query to select all columns from the 'Cities' table, ordered by Population in ascending order,
    # limiting the result to one row.
    cursor.execute("SELECT * FROM Cities ORDER BY Population ASC LIMIT 1")
    # Fetch the next row from the result set
    city = cursor.fetchone()
    # Close the database connection
    conn.close()
    return city


def main():
    """
    Main function to handle user input and display results.
    """
    while True:
        print("\nMenu:")
        print("1. Display a list of cities sorted by population, in ascending order.")
        print("2. Display a list of cities sorted by population, in descending order.")
        print("3. Display a list of cities sorted by name.")
        print("4. Display the total population of all the cities.")
        print("5. Display the average population of all the cities.")
        print("6. Display the city with the highest population.")
        print("7. Display the city with the lowest population.")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Handling user menu choice
        if choice == '1':
            # Display cities sorted by population in ascending order
            cities = display_cities_by_population_ascending()
            for city in cities:
                print(city)
        elif choice == '2':
            # Display cities sorted by population in descending order
            cities = display_cities_by_population_descending()
            for city in cities:
                print(city)
        elif choice == '3':
            # Display cities sorted by name
            cities = display_cities_by_name()
            for city in cities:
                print(city)
        elif choice == '4':
            # Display total population of all cities
            total_population = display_total_population()
            print("Total population of all cities:", total_population)
        elif choice == '5':
            # Display average population of all cities
            average_population = display_average_population()
            print("Average population of all cities:", average_population)
        elif choice == '6':
            # Display the city with the highest population
            city = display_city_with_highest_population()
            print("City with the highest population:", city)
        elif choice == '7':
            # Display the city with the lowest population
            city = display_city_with_lowest_population()
            print("City with the lowest population:", city)
        elif choice == '8':
            # Exit the program
            print("")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
