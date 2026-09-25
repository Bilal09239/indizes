import sqlite3

connection = sqlite3.connect("indizes.db")

cursor = connection.cursor() 

verteilung = """
    WITH cte_name AS(
        SELECT first_name, COUNT(*) AS count
        FROM PERSON
        GROUP BY first_name 
        ORDER BY count DESC
    )

    SELECT MIN(count), MAX(count), AVG(count)
    FROM cte_name ;
"""

cursor.execute(verteilung)
print(cursor.fetchone())

index_loeschen = """
    DROP INDEX idx_first_name; 
"""

cursor.execute(index_loeschen)

ohne_index = """
        SELECT * FROM PERSON WHERE first_name = 'Michael'
        LIMIT(10);
    """
for x in range(20):
    cursor.execute(ohne_index)
    time = cursor.fetchall()

index_erstellen = """
    CREATE INDEX idx_first_name ON PERSON(first_name);
"""
cursor.execute(index_erstellen)

mit_index = """
        SELECT * FROM PERSON WHERE first_name = 'Michael';
    """

for x in range(20):
    cursor.execute(mit_index)
    time = cursor.fetchall()


connection.commit()
connection.close()