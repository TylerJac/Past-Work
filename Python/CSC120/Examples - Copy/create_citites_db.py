import sqlite3


def main():
    # connect to the database
    connection = sqlite3.connect('cities.db')

    # get a database cursor
    cursor = connection.cursor()

    # initialize Cities table
    initialize_table(cursor)

    # add records to Cities table
    add_cities(cursor)

    # commit changes
    connection.commit()

    # display the cities
    display_cities(cursor)

    # close the connection
    connection.close()


def initialize_table(cursor):
    """
    Adds the Cities table to the database
    :param cursor: Database cursor object
    :return: None
    """
    # drop table if it already exists
    cursor.execute("DROP TABLE IF EXISTS Cities")

    # create table
    cursor.execute("""CREATE TABLE Cities(CityID INTEGER PRIMARY KEY NOT NULL,
                                          CityName TEXT,
                                          Population REAL)""")


def add_cities(cursor):
    """
    Adds 20 city records to Cities table
    :param cursor: Database cursor object
    :return: None
    """
    cities_population = [(1, "Tokyo", 38001000),
                         (2, "Delhi", 25703168),
                         (3, "Shanghai", 23740778),
                         (4, "Sao Paulo", 21066245),
                         (5, "Mumbai", 21042538),
                         (6, "Mexico City", 20998543),
                         (7, "Beijing", 20383994),
                         (8, "Osaka", 20237645),
                         (9, "Cairo", 18771769),
                         (10, "New York", 18593220),
                         (11, "Dhaka", 17598228),
                         (12, "Karachi", 16617644),
                         (13, "Buenos Aires", 15180176),
                         (14, "Kolkata", 14864919),
                         (15, "Istanbul", 14163989),
                         (16, "Chongqing", 13331579),
                         (17, "Lagos", 13122829),
                         (18, "Manila", 12946263),
                         (19, "Rio de Janeiro", 12902306),
                         (20, "Guangzhou", 12458130)]

    for row in cities_population:
        cursor.execute("""INSERT INTO Cities(CityID, CityName, Population)
                          VALUES(?, ?, ?)""", (row[0], row[1], row[2]))


def display_cities(cursor):
    """
    Displays the contents of the Cities table
    :param cursor: Database cursor object
    :return: None
    """
    print("Contents of cities.db/Cities table:")
    cursor.execute("SELECT * FROM Cities")
    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]:<3}{row[1]:<20}{row[2]:,.0f}")


if __name__ == '__main__':
    main()
