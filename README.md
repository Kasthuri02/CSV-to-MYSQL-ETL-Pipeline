<h1 align="center">CSV to MySQL ETL Pipeline using python and pandas</h1>

  

<h2>📌 Project Overview</h2>

This project demonstrates an ETL (Extract, Transform, Load) pipeline that processes raw order data from a CSV file and stores the cleaned data in a MySQL database.
The pipeline uses Python and Pandas to perform data cleaning and transformation, ensuring data quality and consistency before loading it into MySQL.

<h2>🏗️ Project Architecture</h2>





**1. Extract Data**

- Read order data from a CSV file.
- Load the data into a Pandas DataFrame.
- Understand the data structure and identify data quality issues.

**2. Transform Data**

- Remove duplicate records.
- Handle missing values using appropriate default values.
- Replace missing customer and product details.
- Remove records with invalid quantities.
- Calculate the total order amount using quantity and price.
- Save the cleaned data into a new CSV file.

**3. Load Data**

- Establish a connection to the MySQL database.
- Create the required database table.
- Insert the cleaned records into MySQL.
- Use environment variables to manage database credentials securely.

<h2>🛠️ Tools & Technologies</h2>



- **Programming Language:** Python
- **Data Processing:** Pandas
- **Database:** MySQL
- **Query Language:** SQL
- **Environment Management:** python-dotenv
- **Development Tools:** VS Code, MySQL Workbench

## 📂 Project Structure

```text
CSV-to-MySQL-ETL-Pipeline/
│
├── data/
│   ├── orders.csv
│   └── cleaned_orders.csv
│
├── scripts/
│   ├── read_data.py
│   └── load_data.py
│
├── sql/
│   └── create_table.sql
│
├── .env
├── .gitignore
└── README.md
```

<h2>📊 Project Outcome</h2>

- Successfully processed approximately 520 raw order records.
- Cleaned and transformed the data using Pandas.
- Loaded 495 cleaned records into the MySQL database.
- Eliminated duplicate records and handled missing values.
- Created a structured dataset ready for further SQL analysis.

<h2>👩‍💻 Author</h2>

Name:Kasthuri P

Role:Data Engineering                   





