import psycopg2
import matplotlib.pyplot as plt

# Connect to your postgres DB
conn = psycopg2.connect(dbname ='SQL_2_1', user='Test', password='bQNxVzJL4g6u', host='ep-noisy-flower-846766.us-east-2.aws.neon.tech',sslmode='require')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM ba_aircraft WHERE manufacturer = 'Boeing' LIMIT 15")

# Retrieve query results
records = cur.fetchall()

company_names=[]
company_revenues=[]
for row in records:
    id, name, money = row
    company_names.append(name)
    company_revenues.append(money)

print(company_revenues)
print(company_names)

sum_of_revenues = 0
for revenue in company_revenues:
    sum_of_revenues = sum_of_revenues + revenue
mean_revenue = sum_of_revenues /10

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
fruits = ['Apple', 'banana', 'cherry']
counts = [40, 100, 30]
ax.xaxis.set_tick_params(rotation=45)
ax.set_title('companies & revenues')
ax.set_xlable('fruits')
ax.set_ylable('company')
ax.axvline(mean_revenue)
ax.barh(fruits, counts)

ax.set_title('Company')
fig.savefig('sample1.png')