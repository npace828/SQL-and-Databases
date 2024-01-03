import sqlite3


conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()


expensive_items_query = """
SELECT * FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""


avg_hire_age_query = """
SELECT AVG(HireDate - BirthDate) AS avg_age FROM Employee;
"""


ten_most_expensive_query = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""


largest_category_query = """
SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName)
AS num_products
FROM Category
INNER JOIN Product ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY num_products DESC
LIMIT 1;
"""


cursor.execute(expensive_items_query)
expensive_items = cursor.fetchall()

cursor.execute(avg_hire_age_query)
avg_hire_age = cursor.fetchall()

cursor.execute(ten_most_expensive_query)
ten_most_expensive = cursor.fetchall()

cursor.execute(largest_category_query)
largest_category = cursor.fetchall()


conn.close()


query_strings = {
    'expensive_items': expensive_items_query,
    'avg_hire_age': avg_hire_age_query,
    'ten_most_expensive': ten_most_expensive_query,
    'largest_category': largest_category_query
}

# Print the results (optional, for submission)
print("Ten most expensive items (Part 1):\n", expensive_items)
print("Average age of hiring employees (Part 2):\n", avg_hire_age)
print("Ten most expensive items and their suppliers (Part 3):\n",
      ten_most_expensive)
print("Largest category by number of unique products (Part 4):\n",
      largest_category)
