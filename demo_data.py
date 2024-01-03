# import sqlite3

# create_demo_table = """
#     CREATE TABLE demo(
#         s VARCHAR(1),
#         x INT,
#         y INT
#     );
# """

# with sqlite3.connect('demo_data.sqlite3') as sl_conn:
#     sl_curs = sl_conn.cursor()

#     sl_curs.execute(create_demo_table)

#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);")
#     sl_conn.commit()

#     sl_curs.execute('SELECT * FROM demo;')
#     all_rows = sl_curs.fetchall()

#     sl_curs.execute('SELECT * FROM demo WHERE x >= 5 AND y >= 5;')
#     xy_at_least_5 = sl_curs.fetchall()

#     sl_curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
#     unique_y = sl_curs.fetchall()


# print("All rows:", all_rows)
# print("Rows with both x and y at least 5:", xy_at_least_5)
# print("Number of unique values of y:", unique_y)
# import sqlite3

# create_demo_table = """
#     CREATE TABLE IF NOT EXISTS demo(
#         s VARCHAR(1),
#         x INT,
#         y INT
#     );
# """

# with sqlite3.connect('demo_data.sqlite3') as sl_conn:
#     sl_curs = sl_conn.cursor()

#     sl_curs.execute(create_demo_table)

#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);")
#     sl_conn.commit()

#     sl_curs.execute('SELECT * FROM demo;')
#     row_count = sl_curs.fetchall()

#     sl_curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;')
#     xy_at_least_5 = sl_curs.fetchall()

#     sl_curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
#     unique_y = sl_curs.fetchall()

# print("All rows:", row_count)
# print("Rows with both x and y at least 5:", xy_at_least_5)
# print("Number of unique values of y:", unique_y)
# import sqlite3
# import os

# Check if the database file exists, and delete it if it does
# if os.path.exists('demo_data.sqlite3'):
#     os.remove('demo_data.sqlite3')

# drop_existing_table = """
#     DROP TABLE IF EXISTS demo;
# """
# create_demo_table = """
#     CREATE TABLE IF NOT EXISTS demo(
#         s VARCHAR(1),
#         x INT,
#         y INT
#     );
# """

# with sqlite3.connect('demo_data.sqlite3') as sl_conn:
#     sl_curs = sl_conn.cursor()

#     sl_curs.execute(create_demo_table)

#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);")
#     sl_curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);")
#     sl_conn.commit()

#     sl_curs.execute('SELECT COUNT(*) FROM demo;')
#     row_count = sl_curs.fetchall()

#     sl_curs.execute('SELECT * FROM demo WHERE x >= 5 AND y >= 5;')
#     xy_at_least_5 = sl_curs.fetchall()

#     sl_curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
#     unique_y = sl_curs.fetchall()

# print("Row count:", row_count)
# print("Rows with both x and y at least 5:", xy_at_least_5)
# print("Number of unique values of y:", unique_y)

# import sqlite3
# import pandas as pd

# drop_existing_table = """
#     DROP TABLE IF EXISTS demo;
# """
# create_demo_table = """
#     CREATE TABLE IF NOT EXISTS demo(
#         s VARCHAR(1),
#         x INT,
#         y INT
#     );
# """

# sl_conn = sqlite3.connect('demo_data.sqlite3')
# sl_curs = sl_conn.cursor()

# sl_curs.execute(drop_existing_table)
# sl_curs.execute(create_demo_table)

# sl_curs.execute("INSERT INTO demo (s,x,y) Values ('g',3,9);")
# sl_curs.execute("INSERT INTO demo (s,x,y) Values ('v',5,7);")
# sl_curs.execute("INSERT INTO demo (s,x,y) Values ('f',8,7);")

# sl_curs.close()
# sl_conn.commit()

# sl_conn = sqlite3.connect('demo_data.sqlite3')
# sl_curs = sl_conn.cursor()

# sl_curs.execute('SELECT * FROM demo;').fetchall()
# sl_curs.execute('SELECT COUNT(*) FROM demo;')
# row_count = sl_curs.fetchall()

# sl_curs.execute('SELECT * FROM demo WHERE x >= 5 AND y >= 5;')
# xy_at_least_5 = sl_curs.fetchall()

# sl_curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
# unique_y = sl_curs.fetchall()

# print(row_count, "<<< row count")
# print(xy_at_least_5, "<<<< atleast 5")
# print(unique_y, "<<< Unique")
# # assert [('v', 5, 7), ('f', 8, 7)] == [(2,)]
# db = [('v', 5, 7), ('f', 8, 7)]

# db1 = pd.DataFrame(db)
# print(len(db1.columns))


import sqlite3

drop_existing_table = """
    DROP TABLE IF EXISTS demo;
"""
create_demo_table = """
    CREATE TABLE IF NOT EXISTS demo(
        s VARCHAR(1),
        x INT,
        y INT
    );
"""
conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()
curs.execute(drop_existing_table)
curs.execute(create_demo_table)
conn.commit()

curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)")
conn.commit()

curs.execute("SELECT COUNT(*) from demo")
row_count_result = curs.fetchone()
row_count = [(row_count_result[0],)] if row_count_result else [(0,)]
print("Num rows in table:", row_count)

curs.execute("""SELECT COUNT(*)
                FROM demo
                WHERE (x >= 5) AND (y >= 5)""")
xy_at_least_5_result = curs.fetchone()
xy_at_least_5 = (
    [(xy_at_least_5_result[0],)] if xy_at_least_5_result else [(0,)]
)
print("Num rows where x and y are both at least 5:", xy_at_least_5)

curs.execute("""SELECT COUNT(DISTINCT y)
                FROM demo""")
unique_y_result = curs.fetchone()
unique_y = [(unique_y_result[0],)] if unique_y_result else [(0,)]
print("Num distinct y values:", unique_y)
