# SQL INTERVIEW QUESTIONS: COMPREHENSIVE MASTER SOLUTIONS (150 QUESTIONS)

**Course:** Data Science & Analytics  
**Module:** SQL & Relational Database Management Systems  
**Database Dialect Reference:** ANSI SQL & MySQL 8.0+

---

## TABLE OF CONTENTS
1. [Section 1: SQL Fundamentals (Q1 – Q30)](#section-1-sql-fundamentals-q1--q30)
2. [Section 2: Filtering and Constraints (Q31 – Q55)](#section-2-filtering-and-constraints-q31--q55)
3. [Section 3: Aggregate Functions and Grouping (Q56 – Q70)](#section-3-aggregate-functions-and-grouping-q56--q70)
4. [Section 4: Joins and Relationships (Q71 – Q90)](#section-4-joins-and-relationships-q71--q90)
5. [Section 5: Subqueries and Set Operations (Q91 – Q105)](#section-5-subqueries-and-set-operations-q91--q105)
6. [Section 6: Window Functions and Ranking (Q106 – Q120)](#section-6-window-functions-and-ranking-q106--q120)
7. [Section 7: Database Design, Transactions and Performance (Q121 – Q140)](#section-7-database-design-transactions-and-performance-q121--q140)
8. [Section 8: MySQL Internals and Real-World Problem Solving (Q141 – Q150)](#section-8-mysql-internals-and-real-world-problem-solving-q141--q150)

---

# SECTION 1: SQL FUNDAMENTALS (Q1 – Q30)

### 1. What is SQL, and why is it used?
**Answer:**  
SQL (Structured Query Language) is the standard declarative programming language used to interact with, manage, and manipulate relational databases. It is used to create schemas, query tabular data, insert, update, delete records, and enforce security, integrity constraints, and transactional consistency.

### 2. What is a database?
**Answer:**  
A database is an organized, structured collection of digital data stored and accessed electronically from a computer system. Databases are designed to facilitate efficient data insertion, querying, updating, administration, and concurrent access.

### 3. What is a Database Management System (DBMS)?
**Answer:**  
A DBMS is system software that serves as an interface between end-users/applications and the underlying physical database. It provides programmatic tools to define, create, maintain, secure, and control data access (e.g., SQLite, Microsoft Access, MongoDB).

### 4. What is a Relational Database Management System (RDBMS)?
**Answer:**  
An RDBMS is an advanced DBMS based on Edgar F. Codd's relational model. Data is stored in structured tables (relations) comprising rows (tuples) and columns (attributes), where relationships between entities are established and enforced through Primary and Foreign Keys (e.g., MySQL, PostgreSQL, Oracle, SQL Server).

### 5. What is the difference between DBMS and RDBMS?
**Answer:**

| Feature | DBMS | RDBMS |
| :--- | :--- | :--- |
| **Data Storage** | Files, hierarchical structures, or key-value pairs. | Tabular format (rows and columns). |
| **Relationships** | No native relational integrity or foreign key support. | Enforces entity and referential integrity via foreign keys. |
| **Normalization** | Not inherently supported. | Fully supported to eliminate data redundancy. |
| **ACID Compliance** | Rarely guarantees full ACID properties. | Strictly enforces ACID compliance for transactions. |
| **Data Volume / Users** | Small datasets, single or few users. | Enterprise-scale datasets, massive concurrent access. |

### 6. What is a table in a database?
**Answer:**  
A table is a database object organized in a grid of vertical columns (fields/attributes) and horizontal rows (records/tuples) representing a distinct business entity (such as `Customers`, `Orders`, or `Products`).

### 7. What are rows and columns in a table?
**Answer:**
- **Row (Tuple / Record):** A single horizontal entry in a table that represents one unique instance of an entity with specific values for each attribute.
- **Column (Field / Attribute):** A vertical structure containing a single category of data with a specified name and data type (e.g., `birth_date DATE`, `salary DECIMAL`).

### 8. What is a SQL query?
**Answer:**  
A SQL query is a declarative instruction or statement sent to an RDBMS engine requesting data retrieval (`SELECT`), data modification (`INSERT`, `UPDATE`, `DELETE`), schema definition (`CREATE`, `ALTER`), or access permission changes.

### 9. What are the different categories of SQL commands?
**Answer:**  
SQL commands are categorized into five sub-languages:
1. **DDL (Data Definition Language)**
2. **DML (Data Manipulation Language)**
3. **DQL (Data Query Language)**
4. **DCL (Data Control Language)**
5. **TCL (Transaction Control Language)**

### 10. What is the difference between DDL, DML, DQL, DCL, and TCL?
**Answer:**
- **DDL (Data Definition Language):** Defines, modifies, and drops database schema structures.  
  *Commands:* `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`.
- **DML (Data Manipulation Language):** Modifies the actual row data stored within tables.  
  *Commands:* `INSERT`, `UPDATE`, `DELETE`.
- **DQL (Data Query Language):** Retrieves data from tables without altering underlying state.  
  *Commands:* `SELECT`.
- **DCL (Data Control Language):** Manages user authentication, permissions, and security privileges.  
  *Commands:* `GRANT`, `REVOKE`.
- **TCL (Transaction Control Language):** Controls multi-step database transactions to ensure consistency.  
  *Commands:* `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

### 11. What is the purpose of the `SELECT` statement?
**Answer:**  
The `SELECT` statement is the primary DQL command used to query and extract specific records, columns, expressions, or aggregated metrics from one or more database tables or views.

### 12. How do you retrieve all columns from a table?
**Answer:**  
Using the asterisk wildcard (`*`):
```sql
SELECT * FROM employees;
```
*(Best practice in production is to explicitly enumerate required column names to avoid unnecessary network I/O and prevent breaking dependent applications when schemas change).*

### 13. What is the purpose of the `WHERE` clause?
**Answer:**  
The `WHERE` clause specifies row-level filtering conditions. It restricts the rows returned by a query or affected by `UPDATE`/`DELETE` statements to only those where the condition evaluates to `TRUE`. It executes **before** any `GROUP BY` aggregation takes place.

### 14. What is the difference between `WHERE` and `HAVING`?
**Answer:**

| Feature | `WHERE` Clause | `HAVING` Clause |
| :--- | :--- | :--- |
| **Execution Point** | Filters individual records **before** grouping occurs. | Filters aggregated groups **after** `GROUP BY` executes. |
| **Aggregate Functions** | **Cannot** contain aggregate functions (`WHERE SUM(x) > 10` is invalid). | **Can** filter on aggregate functions (`HAVING SUM(x) > 10`). |
| **Applied To** | Rows (records). | Groups of rows. |
| **Usage Context** | Used with `SELECT`, `UPDATE`, `DELETE`. | Used almost exclusively with `SELECT` and `GROUP BY`. |

### 15. How do you retrieve unique values using `DISTINCT`?
**Answer:**  
By prefixing the column list with the `DISTINCT` keyword. It evaluates the tuple of selected columns and filters out duplicate rows from the final result set:
```sql
SELECT DISTINCT department_id FROM employees;
SELECT DISTINCT country, city FROM customers;
```

### 16. What is the purpose of the `ORDER BY` clause?
**Answer:**  
`ORDER BY` sorts the result set returned by a query by one or more columns in either ascending (`ASC`, default) or descending (`DESC`) order:
```sql
SELECT first_name, salary FROM employees ORDER BY salary DESC, first_name ASC;
```

### 17. What is the difference between ascending and descending order?
**Answer:**
- **Ascending (`ASC`):** Arranges values from lowest to highest (numbers: $1 \rightarrow 100$, text: $A \rightarrow Z$, dates: oldest to newest). Default sorting in SQL.
- **Descending (`DESC`):** Arranges values from highest to lowest (numbers: $100 \rightarrow 1$, text: $Z \rightarrow A$, dates: newest to oldest).

### 18. What is the purpose of the `LIMIT` clause in MySQL?
**Answer:**  
`LIMIT` constrains the maximum number of rows returned by a query. It often accepts an optional `OFFSET` for pagination:
```sql
-- Retrieve the top 5 highest paid employees:
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- Pagination: Skip first 20 records and retrieve the next 10:
SELECT * FROM employees ORDER BY emp_id LIMIT 10 OFFSET 20;
```

### 19. What are SQL aliases, and how do you use `AS`?
**Answer:**  
Aliases provide temporary, readable names for table columns or table identifiers during query execution using the `AS` keyword:
```sql
SELECT 
    first_name AS given_name, 
    salary * 12 AS annual_compensation 
FROM employees AS emp;
```

### 20. What is the difference between `DELETE`, `DROP`, and `TRUNCATE`?
**Answer:**

| Feature | `DELETE` | `TRUNCATE` | `DROP` |
| :--- | :--- | :--- | :--- |
| **Category** | DML | DDL | DDL |
| **Operation** | Removes specified or all rows one by one. | Empties the entire table by deallocating data pages. | Deletes the table data **and** the schema definition. |
| **`WHERE` clause** | Supported (can delete specific rows). | Not supported (removes all rows). | Not applicable. |
| **Speed** | Slower (logs each row deletion). | Extremely fast (minimal logging). | Fast. |
| **Rollback** | Can be rolled back inside a transaction. | Cannot be rolled back in MySQL (auto-commits DDL). | Cannot be rolled back. |
| **Identity Reset**| Does not reset `AUTO_INCREMENT`. | Resets `AUTO_INCREMENT` back to 1. | Table ceases to exist. |

### 21. What is the purpose of the `INSERT INTO` statement?
**Answer:**  
`INSERT INTO` adds new rows of data into an existing database table:
```sql
INSERT INTO departments (dept_id, dept_name) VALUES (101, 'Engineering');
```

### 22. How do you modify existing records using `UPDATE`?
**Answer:**  
Using the `UPDATE` statement with the `SET` keyword:
```sql
UPDATE employees 
SET salary = salary * 1.10, dept_id = 101 
WHERE emp_id = 45;
```

### 23. What happens if you execute an `UPDATE` statement without a `WHERE` clause?
**Answer:**  
**Every single row in the entire table will be updated** to the specified value(s). In production environments, this can lead to catastrophic data corruption. (MySQL provides `SET sql_safe_updates = 1;` to block updates without key-based `WHERE` clauses).

### 24. What is the purpose of the `CREATE TABLE` statement?
**Answer:**  
`CREATE TABLE` is a DDL command that defines a new table structure, specifying column names, data types, lengths, default values, and integrity constraints:
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) CHECK (price > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 25. How do you add a new column to an existing table?
**Answer:**  
Using `ALTER TABLE ... ADD`:
```sql
ALTER TABLE employees ADD email VARCHAR(100) UNIQUE;
```

### 26. What is the purpose of the `ALTER TABLE` statement?
**Answer:**  
`ALTER TABLE` modifies an existing table structure without dropping it. It is used to add, modify, rename, or drop columns, as well as add or remove table constraints (primary keys, foreign keys, indexes).

### 27. What is the difference between `CHAR` and `VARCHAR`?
**Answer:**
- **`CHAR(M)`:** **Fixed-length** string storage ($0$ to $255$ characters). If the inserted text is shorter than $M$, it is right-padded with spaces to length $M$. Best for constant-length data (e.g., country codes `'US'`, MD5 hashes, phone numbers).
- **`VARCHAR(M)`:** **Variable-length** string storage ($0$ to $65,535$ characters). Stores only the actual characters plus a 1- or 2-byte prefix length indicator. Conserves disk and memory for strings of varying length (e.g., names, addresses).

### 28. What are the common numeric, string, and date data types in MySQL?
**Answer:**
- **Numeric:** `TINYINT`, `INT`, `BIGINT`, `DECIMAL(p, s)` (exact financial math), `FLOAT`, `DOUBLE`.
- **String:** `CHAR`, `VARCHAR`, `TEXT`, `ENUM`.
- **Date & Time:** `DATE` (`YYYY-MM-DD`), `TIME`, `DATETIME`, `TIMESTAMP` (timezone-aware), `YEAR`.

### 29. What is the difference between `NULL`, zero, and an empty string?
**Answer:**
- **`NULL`:** Represents the **absence of a value**, unknown, or unassigned data. It does not occupy a numeric zero or string value and requires ternary logic evaluation (`IS NULL`).
- **Zero (`0`):** A defined, precise numerical integer value equal to the absence of quantity.
- **Empty String (`''`):** A defined character string of length zero containing no characters.

### 30. What is the purpose of the `IS NULL` and `IS NOT NULL` operators?
**Answer:**  
Because `NULL` represents an unknown value, standard comparison operators (`= NULL` or `<> NULL`) always evaluate to `UNKNOWN` (falsy in boolean contexts). The dedicated operators `IS NULL` and `IS NOT NULL` must be used to test whether an attribute contains a null value:
```sql
SELECT * FROM employees WHERE commission_pct IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
```

---

# SECTION 2: FILTERING AND CONSTRAINTS (Q31 – Q55)

### 31. What is the difference between the `WHERE` and `ORDER BY` clauses?
**Answer:**  
- `WHERE`: Filters data by evaluating row-level boolean predicates. Determines **which rows** are included.
- `ORDER BY`: Sequences the filtered output rows. Determines **in what order** the returned rows are presented.

### 32. How do you filter records using comparison operators?
**Answer:**  
Using standard operators: `=`, `!=` (or `<>`), `>`, `<`, `>=`, `<=`:
```sql
SELECT * FROM employees WHERE salary >= 50000 AND dept_id != 10;
```

### 33. What are the logical operators `AND`, `OR`, and `NOT`?
**Answer:**
- `AND`: Evaluates to `TRUE` if **all** joined conditions are true.
- `OR`: Evaluates to `TRUE` if **at least one** condition is true.
- `NOT`: Inverts the boolean truth value of a condition.

### 34. What is the difference between `AND` and `OR`?
**Answer:**  
`AND` narrows down the result set by enforcing that multiple conditions must all be satisfied simultaneously, whereas `OR` broadens the result set by matching rows satisfying any of the specified conditions. `AND` has higher operator precedence than `OR` in SQL evaluation.

### 35. What is the purpose of the `BETWEEN` operator?
**Answer:**  
Filters values within a specified inclusive range: `val BETWEEN low AND high` is logically equivalent to `(val >= low AND val <= high)`.
```sql
SELECT * FROM orders WHERE order_date BETWEEN '2026-01-01' AND '2026-03-31';
```

### 36. How does the `IN` operator work?
**Answer:**  
The `IN` operator checks whether a candidate value matches any value in a discrete list of literals or values returned by a subquery:
```sql
SELECT * FROM customers WHERE country IN ('Canada', 'Germany', 'Japan');
```

### 37. What is the purpose of the `LIKE` operator?
**Answer:**  
Performs pattern-matching searches on text strings using wildcard characters.

### 38. What is the difference between the `%` and `_` wildcards in SQL?
**Answer:**
- **`%` (Percent):** Matches **zero, one, or multiple** characters of arbitrary length.
- **`_` (Underscore):** Matches **exactly one single** character at that specific position.

### 39. How do you search for values that begin with a specific character?
**Answer:**  
By placing the target character before the `%` wildcard:
```sql
SELECT * FROM customers WHERE customer_name LIKE 'A%';
```

### 40. How do you search for values that contain a particular substring?
**Answer:**  
By wrapping the substring inside two `%` wildcards:
```sql
SELECT * FROM products WHERE product_name LIKE '%phone%';
```

### 41. What is a primary key?
**Answer:**  
A primary key is a column (or combination of columns) that uniquely identifies each individual record in a database table. It must contain unique values and can **never contain `NULL`** values. Each table can have at most one primary key.

### 42. What is a foreign key?
**Answer:**  
A foreign key is a column (or set of columns) in one table that references the primary key (or a unique key) of another table. It establishes and enforces a referential link between related entities.

### 43. What is the difference between a primary key and a unique key?
**Answer:**

| Feature | Primary Key | Unique Key |
| :--- | :--- | :--- |
| **Number per Table** | Exactly **one** per table. | **Multiple** unique constraints allowed per table. |
| **`NULL` Acceptance** | Never permits `NULL` values (`NOT NULL` enforced). | Permits `NULL` values (one or multiple depending on RDBMS). |
| **Default Index** | Automatically creates a **clustered index** (in InnoDB/SQL Server). | Creates a **non-clustered index**. |
| **Purpose** | Uniquely identifies the entity record. | Prevents duplicate values across specific alternative attributes. |

### 44. What is a composite primary key?
**Answer:**  
A primary key composed of two or more columns combined together to guarantee uniqueness when no single column alone is unique:
```sql
CREATE TABLE order_items (
    order_id INT,
    item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, item_id)
);
```

### 45. What is a candidate key?
**Answer:**  
Any column or minimal set of columns that satisfies the conditions of uniqueness and non-nullability, qualifying it as a candidate to be chosen as the primary key.

### 46. What is a super key?
**Answer:**  
Any set of one or more columns within a table that uniquely identifies a row. A candidate key is a minimal super key (having no redundant attributes).

### 47. What is a surrogate key?
**Answer:**  
An artificial, system-generated identifier with no business meaning (e.g., auto-incrementing integer or UUID) created specifically to serve as a simple, stable primary key.

### 48. What are SQL constraints, and why are they important?
**Answer:**  
Constraints are rules enforced on data columns to restrict the types of data that can be inserted, updated, or deleted. They ensure **data integrity, accuracy, consistency, and reliability** at the database engine level.

### 49. What is the purpose of the `NOT NULL` constraint?
**Answer:**  
Enforces that a column must always be assigned a valid value; attempts to insert or update a row with `NULL` will be rejected.

### 50. What is the purpose of the `UNIQUE` constraint?
**Answer:**  
Ensures that all non-null values stored in a column (or combination of columns) are distinct across the table.

### 51. What is the purpose of the `DEFAULT` constraint?
**Answer:**  
Provides a fallback default value for a column when an `INSERT` statement does not explicitly provide one:
```sql
ALTER TABLE users ALTER status SET DEFAULT 'active';
```

### 52. What is the purpose of the `CHECK` constraint?
**Answer:**  
Validates that values entered into a column satisfy a specific boolean expression:
```sql
ALTER TABLE employees ADD CONSTRAINT chk_age CHECK (age >= 18);
```

### 53. What is referential integrity?
**Answer:**  
A database state where all foreign key references are completely valid: every foreign key value must either point to an existing primary key in the referenced parent table or be explicitly `NULL`. It prevents "orphan records".

### 54. What is the difference between `ON DELETE CASCADE` and `ON DELETE SET NULL`?
**Answer:**
- **`ON DELETE CASCADE`:** When a parent record is deleted, all matching child rows in the referencing table are **automatically deleted**.
- **`ON DELETE SET NULL`:** When a parent record is deleted, the foreign key column in all matching child rows is **automatically set to `NULL`** (requires foreign key column to be nullable).

### 55. Can a table have multiple foreign keys? Explain with an example.
**Answer:**  
**Yes.** Tables frequently contain multiple foreign keys to establish relationships with different parent entities.  
*Example:* An `orders` table referencing both `customers` and `employees`:
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    employee_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(emp_id)
);
```

---

# SECTION 3: AGGREGATE FUNCTIONS AND GROUPING (Q56 – Q70)

### 56. What are aggregate functions in SQL?
**Answer:**  
Mathematical functions that perform a computation on a set of values across multiple rows and return a single summary value (e.g., `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

### 57. What is the difference between `COUNT(*)` and `COUNT(column_name)`?
**Answer:**
- **`COUNT(*)`:** Counts the total number of rows in the table/group, **including rows with `NULL` values and duplicate rows**.
- **`COUNT(column_name)`:** Counts only the number of rows where `column_name` is **strictly not `NULL`**.

### 58. What is the purpose of the `SUM()` function?
**Answer:**  
Calculates the total numeric sum of all non-null values in a given column across a table or group.

### 59. How does the `AVG()` function work?
**Answer:**  
Calculates the arithmetic mean by dividing the sum of non-null values by the count of non-null values. `NULL` values are excluded from both numerator and denominator.

### 60. What is the difference between `MIN()` and `MAX()`?
**Answer:**
- `MIN()`: Finds the smallest value in a column (lowest number, earliest date, or first alphabetical string).
- `MAX()`: Finds the largest value in a column (highest number, latest date, or last alphabetical string).

### 61. What is the purpose of the `GROUP BY` clause?
**Answer:**  
Collapses rows that have matching values in specified columns into summary rows, enabling aggregate functions (`SUM`, `AVG`, `COUNT`) to be computed for each distinct group.

### 62. What happens when you use `GROUP BY` with multiple columns?
**Answer:**  
Rows are grouped into distinct subsets based on the **unique combination of all specified columns**:
```sql
SELECT department_id, job_title, COUNT(*) 
FROM employees 
GROUP BY department_id, job_title;
```

### 63. What is the purpose of the `HAVING` clause?
**Answer:**  
Provides a condition to filter groups produced by the `GROUP BY` clause based on aggregate calculations.

### 64. Why is `HAVING` commonly used with aggregate functions?
**Answer:**  
Because the `WHERE` clause filters individual records before grouping occurs and cannot evaluate aggregate expressions. `HAVING` is executed after the grouping and aggregation phase.

### 65. How do you find the total salary paid by each department?
**Answer:**
```sql
SELECT 
    dept_id, 
    SUM(salary) AS total_department_salary 
FROM employees 
GROUP BY dept_id;
```

### 66. How do you find departments with more than five employees?
**Answer:**
```sql
SELECT 
    dept_id, 
    COUNT(emp_id) AS employee_count 
FROM employees 
GROUP BY dept_id 
HAVING COUNT(emp_id) > 5;
```

### 67. How do you count the number of distinct values in a column?
**Answer:**  
Combine `COUNT` with `DISTINCT`:
```sql
SELECT COUNT(DISTINCT country) AS distinct_country_count FROM customers;
```

### 68. How do aggregate functions handle `NULL` values?
**Answer:**  
All aggregate functions (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT(col)`) **ignore `NULL` values**, treating them as if they do not exist. The only exception is `COUNT(*)`, which counts rows regardless of null content. If all values in a column are `NULL`, `SUM()` and `AVG()` evaluate to `NULL`.

### 69. What is the difference between filtering rows before grouping and filtering groups after aggregation?
**Answer:**
- **Filtering before grouping (`WHERE`):** Eliminates unneeded rows prior to aggregation, improving performance by reducing data volume in memory.
- **Filtering after aggregation (`HAVING`):** Evaluates computed summary values across groups after all rows have been scanned and grouped.

### 70. How would you find the highest, lowest, and average salary for each department?
**Answer:**
```sql
SELECT 
    dept_id,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY dept_id;
```

---

# SECTION 4: JOINS AND RELATIONSHIPS (Q71 – Q90)

### 71. What is a join in SQL?
**Answer:**  
A join is an operation that combines rows from two or more tables based on a related common column between them.

### 72. Why are joins used in relational databases?
**Answer:**  
Relational databases normalize data into separate, specialized tables to minimize redundancy. Joins allow applications to reconstruct complete composite business views on demand.

### 73. What is an `INNER JOIN`?
**Answer:**  
Returns only the records that have **matching values in both tables**. Rows with no match in either table are excluded.

### 74. What is a `LEFT JOIN`?
**Answer:**  
Returns **all records from the left table**, along with matched records from the right table. For left-table rows with no match in the right table, right-table columns return `NULL`.

### 75. What is a `RIGHT JOIN`?
**Answer:**  
Returns **all records from the right table**, along with matched records from the left table. For right-table rows with no match, left-table columns return `NULL`.

### 76. What is a `CROSS JOIN`?
**Answer:**  
Produces the **Cartesian product** of two tables, pairing every row from the first table with every row from the second table. If Table A has $M$ rows and Table B has $N$ rows, the result contains $M \times N$ rows.

### 77. What is a self join?
**Answer:**  
A regular join in which a table is joined with **itself**, typically using distinct table aliases. Commonly used to query hierarchical data (e.g., matching employees to their managers).

### 78. What is the difference between `INNER JOIN` and `LEFT JOIN`?
**Answer:**  
`INNER JOIN` discards rows that do not have a match in both tables. `LEFT JOIN` preserves all rows from the left table regardless of whether a matching record exists in the right table.

### 79. What is the difference between `LEFT JOIN` and `RIGHT JOIN`?
**Answer:**  
They are mirror images of one another: `LEFT JOIN` keeps all rows from the first (left) table, while `RIGHT JOIN` keeps all rows from the second (right) table. Any `RIGHT JOIN` can be rewritten as a `LEFT JOIN` by reversing table order.

### 80. What is the difference between a join condition in `ON` and a filter in `WHERE`?
**Answer:**
- In **`INNER JOIN`**, conditions placed in `ON` and `WHERE` produce identical results.
- In **`LEFT JOIN`**, conditions in `ON` dictate how the right table matches; if unmatched, left rows still appear with `NULL`s. Conditions in `WHERE` are applied after the join, filtering out rows and potentially turning the `LEFT JOIN` into an unintended `INNER JOIN`.

### 81. What is an equi join?
**Answer:**  
Any join that uses the equality comparison operator (`=`) in its join predicate:
```sql
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.customer_id;
```

### 82. What is a non-equi join?
**Answer:**  
A join that uses comparison operators other than equality (`<`, `>`, `<=`, `>=`, `BETWEEN`):
```sql
SELECT e.first_name, e.salary, g.grade_level 
FROM employees e 
JOIN salary_grades g ON e.salary BETWEEN g.min_salary AND g.max_salary;
```

### 83. What is a natural join, and why should it be used cautiously?
**Answer:**  
A `NATURAL JOIN` automatically joins two tables based on all columns that share the exact same column name.  
*Caution:* If someone adds or renames a column in either table, the join condition silently changes, producing incorrect results or zero rows.

### 84. How do you join three or more tables in a single query?
**Answer:**  
Chain consecutive join clauses:
```sql
SELECT 
    c.customer_name, o.order_id, p.product_name, oi.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```

### 85. How do you retrieve employees along with their department names?
**Answer:**
```sql
SELECT 
    e.emp_id, e.first_name, e.last_name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;
```

### 86. How do you find customers who have never placed an order?
**Answer:**
```sql
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

### 87. How do you find employees who earn more than their managers?
**Answer:**
```sql
SELECT 
    e.first_name AS employee_name,
    e.salary AS employee_salary,
    m.first_name AS manager_name,
    m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```

### 88. How can a self join be used to represent an employee-manager relationship?
**Answer:**  
By referencing the same table twice with aliases `e` (employee) and `m` (manager), joining on `e.manager_id = m.emp_id`:
```sql
SELECT 
    e.first_name AS employee, 
    COALESCE(m.first_name, 'Top Executive') AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```

### 89. What happens when join columns contain duplicate values?
**Answer:**  
Every matching row in Table A joins with every matching row in Table B, generating an **$M \times N$ row multiplication (fan-out)** for those keys, which can inflate row counts and distort aggregate calculations.

### 90. How can you identify and prevent unexpected duplicate rows after joining tables?
**Answer:**
- **Identify:** Compare `COUNT(*)` against `COUNT(DISTINCT primary_key)` or inspect data with `GROUP BY join_key HAVING COUNT(*) > 1`.
- **Prevent:** Ensure join conditions join on unique/primary keys; pre-aggregate the child table using a CTE or subquery before joining.

---

# SECTION 5: SUBQUERIES AND SET OPERATIONS (Q91 – Q105)

### 91. What is a subquery in SQL?
**Answer:**  
A subquery (nested query / inner query) is a `SELECT` statement enclosed in parentheses embedded within another SQL query (`SELECT`, `INSERT`, `UPDATE`, or `DELETE`).

### 92. What is the difference between a subquery and a join?
**Answer:**  
- Joins combine columns from multiple tables into a single output row in memory; modern query optimizers usually optimize joins better than subqueries.
- Subqueries isolate retrieval logic, returning a single value or list of values for filtering or conditional evaluation.

### 93. What is a single-row subquery?
**Answer:**  
A subquery that returns exactly one row with one column. Used with scalar operators (`=`, `>`, `<`):
```sql
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 94. What is a multiple-row subquery?
**Answer:**  
A subquery that returns multiple rows. Evaluated using set operators (`IN`, `ANY`, `ALL`):
```sql
SELECT * FROM employees WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'London');
```

### 95. What is a correlated subquery?
**Answer:**  
A subquery that references one or more columns from the outer query. It cannot be executed independently and is re-evaluated for each candidate row processed by the outer query:
```sql
SELECT e.first_name, e.salary, e.dept_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE dept_id = e.dept_id
);
```

### 96. What is the difference between correlated and non-correlated subqueries?
**Answer:**
- **Non-Correlated:** Independent of the outer query; executes once, and its result is reused by the outer query.
- **Correlated:** Dependent on outer query values; executes repeatedly for each candidate row in the outer query.

### 97. What is the purpose of the `EXISTS` operator?
**Answer:**  
Tests for the existence of rows in a subquery. It returns `TRUE` as soon as the inner query finds at least one matching row, short-circuiting further evaluation for high efficiency:
```sql
SELECT c.customer_name 
FROM customers c 
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

### 98. What is the difference between `EXISTS` and `IN`?
**Answer:**
- `IN`: Evaluates all values returned by the subquery into an in-memory list and checks for membership.
- `EXISTS`: Returns a boolean based on whether any row matches. It stops scanning as soon as the first match is found.

### 99. What is the difference between `NOT EXISTS` and `NOT IN`, especially when `NULL` values are present?
**Answer:**  
- If a subquery returns even a single `NULL` value, `NOT IN (SELECT col ...)` evaluates to `UNKNOWN` for all rows, causing the outer query to return **zero rows**.
- `NOT EXISTS` uses boolean row presence checks, so it is **completely immune to `NULL` values** in subquery results and reliably returns non-matching rows.

### 100. What is a scalar subquery?
**Answer:**  
A subquery that returns exactly one single value (1 row, 1 column). It can appear anywhere a scalar literal or expression is valid (such as the `SELECT` column list).

### 101. What is a derived table?
**Answer:**  
A subquery placed in the `FROM` clause of a query that functions as a temporary in-memory table. It must always be assigned an alias:
```sql
SELECT dept_id, avg_sal 
FROM (SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id) AS dept_summary
WHERE avg_sal > 60000;
```

### 102. What is a Common Table Expression (CTE)?
**Answer:**  
A temporary named result set defined using the `WITH` clause that exists only for the duration of the execution of a single primary query:
```sql
WITH HighEarners AS (
    SELECT emp_id, first_name, salary 
    FROM employees 
    WHERE salary > 80000
)
SELECT * FROM HighEarners WHERE emp_id < 100;
```

### 103. What is the difference between a CTE and a subquery?
**Answer:**  
- CTEs are declared at the top of the query, making complex queries significantly more readable and modular.
- A CTE can be referenced multiple times within the same statement and supports recursion (`WITH RECURSIVE`).
- Subqueries must be duplicated if needed in multiple locations.

### 104. What is the difference between `UNION` and `UNION ALL`?
**Answer:**
- **`UNION`:** Combines result sets and performs an automatic deduplication sort, removing duplicate rows.
- **`UNION ALL`:** Combines result sets **without deduplication**, preserving all rows. It is significantly faster because it avoids sorting overhead.

### 105. What are the requirements for combining query results using set operations?
**Answer:**
1. Both queries must select the **exact same number of columns**.
2. Corresponding columns must have **compatible data types** in the same position.
3. Column names and aliases are determined by the first `SELECT` statement.

---

# SECTION 6: WINDOW FUNCTIONS AND RANKING (Q106 – Q120)

### 106. What is a window function in SQL?
**Answer:**  
A window function performs calculations across a set of table rows related to the current row without collapsing the individual rows into a single summary output.

### 107. How does a window function differ from an aggregate function used with `GROUP BY`?
**Answer:**  
`GROUP BY` collapses grouped rows into a single summary record. Window functions calculate aggregations or rankings while **retaining the original identity and row count** of every individual row in the result set.

### 108. What is the purpose of the `OVER()` clause?
**Answer:**  
Defines the window partitioning, ordering, and framing specifications over which the window function operates:
```sql
SELECT emp_id, salary, AVG(salary) OVER () AS company_avg_salary FROM employees;
```

### 109. What is the difference between `PARTITION BY` and `GROUP BY`?
**Answer:**  
`GROUP BY` changes the granularity of the query output by collapsing rows. `PARTITION BY` divides rows into logical partitions for computation within the `OVER()` clause while maintaining row-level detail.

### 110. What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?
**Answer:**
Given duplicate values `[100, 90, 90, 80]`:
- **`ROW_NUMBER()`:** Assigns sequential, strictly unique integers: `1, 2, 3, 4`.
- **`RANK()`:** Assigns identical rank to ties, but **skips subsequent ranks**: `1, 2, 2, 4`.
- **`DENSE_RANK()`:** Assigns identical rank to ties **without gaps**: `1, 2, 2, 3`.

### 111. How do you find the second-highest salary using a window function?
**Answer:**
```sql
WITH RankedSalaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT salary FROM RankedSalaries WHERE rnk = 2 LIMIT 1;
```

### 112. How do you find the top three salaries in each department?
**Answer:**
```sql
WITH RankedDeptSalaries AS (
    SELECT 
        first_name, dept_id, salary,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM RankedDeptSalaries WHERE rnk <= 3;
```

### 113. What is the purpose of the `LAG()` function?
**Answer:**  
Accesses data from a previous row in the same result set without using a self-join:
```sql
SELECT order_date, amount, LAG(amount, 1) OVER (ORDER BY order_date) AS prev_amount FROM sales;
```

### 114. What is the purpose of the `LEAD()` function?
**Answer:**  
Accesses data from a subsequent (following) row in the same result set without using a self-join:
```sql
SELECT order_date, amount, LEAD(amount, 1) OVER (ORDER BY order_date) AS next_amount FROM sales;
```

### 115. How can you compare each month's sales with the previous month's sales?
**Answer:**
```sql
SELECT 
    sale_month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY sale_month) AS prev_month_revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY sale_month) AS mom_difference
FROM monthly_sales;
```

### 116. What is a running total, and how can you calculate it?
**Answer:**  
A running total is a cumulative sum of a numeric measure across sequential rows:
```sql
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM sales;
```

### 117. What is a moving average in SQL?
**Answer:**  
An average computed over a rolling window of recent preceding rows:
```sql
SELECT 
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS 3_day_moving_average
FROM sales;
```

### 118. What is the purpose of `FIRST_VALUE()` and `LAST_VALUE()`?
**Answer:**
- `FIRST_VALUE(col)`: Returns the value of `col` from the first row of the window frame.
- `LAST_VALUE(col)`: Returns the value of `col` from the last row of the window frame (requires `RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING` to avoid defaulting to current row).

### 119. What is a window frame, and how do `ROWS` and `RANGE` differ?
**Answer:**  
A window frame specifies the exact subset of rows within a partition evaluated by the window function:
- **`ROWS`:** Defines window offsets by physical row counts (e.g., `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`).
- **`RANGE`:** Defines window offsets by logical value boundaries based on the `ORDER BY` expression, treating ties identically.

### 120. How would you identify duplicate records using `ROW_NUMBER()`?
**Answer:**
```sql
WITH DuplicateCTE AS (
    SELECT 
        emp_id, email,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY emp_id) AS row_num
    FROM employees
)
SELECT * FROM DuplicateCTE WHERE row_num > 1;
```

---

# SECTION 7: DATABASE DESIGN, TRANSACTIONS AND PERFORMANCE (Q121 – Q140)

### 121. What is database normalization?
**Answer:**  
Database normalization is the systematic design process of organizing tables and attributes in a relational database to minimize data redundancy and prevent data anomalies (insertion, update, and deletion anomalies).

### 122. What is the difference between 1NF, 2NF, and 3NF?
**Answer:**
- **First Normal Form (1NF):** Each column contains atomic (indivisible) values, no repeating groups or arrays, and each record has a primary key.
- **Second Normal Form (2NF):** Satisfies 1NF and contains **no partial dependencies** (every non-key attribute must depend on the whole primary key, not a part of a composite key).
- **Third Normal Form (3NF):** Satisfies 2NF and contains **no transitive dependencies** (non-key attributes must not depend on other non-key attributes).

### 123. What is Boyce–Codd Normal Form (BCNF)?
**Answer:**  
A stricter version of 3NF (often called 3.5NF). A table is in BCNF if and only if for every functional dependency $X \rightarrow Y$, the determinant $X$ is a **super key**.

### 124. What is denormalization, and when is it useful?
**Answer:**  
Denormalization is the intentional introduction of controlled redundancy into a normalized schema by combining tables or storing pre-aggregated metrics. It is used in read-heavy analytical databases and data warehouses (e.g., Star Schema) to reduce expensive multi-table joins and boost query read performance.

### 125. What is a functional dependency?
**Answer:**  
A relationship between attributes where the value of one attribute (or set of attributes) $X$ uniquely determines the value of another attribute $Y$, denoted as $X \rightarrow Y$.

### 126. What is an index in SQL?
**Answer:**  
An index is an auxiliary data structure (typically a B+ Tree) that stores ordered references to table rows, allowing the database engine to locate records quickly without performing a full table scan.

### 127. How does a database index improve query performance?
**Answer:**  
Without an index, the database must execute a Full Table Scan ($\mathcal{O}(N)$), reading every page on disk. With a B+ Tree index, searches navigate a balanced tree hierarchy in $\mathcal{O}(\log N)$ disk I/O operations.

### 128. What is the difference between clustered and nonclustered indexes?
**Answer:**
- **Clustered Index:** Dictates the physical storage order of the actual rows on disk. A table can have **only one** clustered index (usually the Primary Key in InnoDB). Leaf nodes contain the actual row data.
- **Non-Clustered (Secondary) Index:** A separate structure containing indexed keys and pointers back to the primary key/clustered index. A table can have **multiple** non-clustered indexes.

### 129. What is a composite index and why does column order matter?
**Answer:**  
A composite index covers multiple columns: `INDEX (col_a, col_b)`.  
*Column order matters:* The index can only be utilized if queries filter on the **leftmost prefix** (e.g., filtering on `col_a` or `col_a AND col_b` uses the index, but filtering solely on `col_b` cannot utilize the composite index).

### 130. What is a covering index?
**Answer:**  
An index that contains all the columns requested by a query (in `SELECT`, `WHERE`, `ORDER BY`). The engine retrieves the data directly from the index structure without reading the underlying table data pages, eliminating secondary lookups.

### 131. What are the disadvantages of creating too many indexes?
**Answer:**
1. **Slows Down DML:** Every `INSERT`, `UPDATE`, and `DELETE` must update both the table and all associated index trees.
2. **Storage Overhead:** Indexes consume significant disk space and buffer pool RAM.
3. **Optimizer Overhead:** Increases query planning time as the optimizer evaluates more index paths.

### 132. What is a query execution plan?
**Answer:**  
The step-by-step operational strategy generated by the query optimizer detailing how it will execute a query (which indexes will be used, join algorithms chosen, table scan methods, and cost estimates).

### 133. How do you use `EXPLAIN` in MySQL?
**Answer:**  
Prefix any `SELECT`, `UPDATE`, or `DELETE` statement with `EXPLAIN` (or `EXPLAIN ANALYZE`):
```sql
EXPLAIN SELECT * FROM employees WHERE dept_id = 10;
```
Key output fields include `type` (e.g., `ALL` = full scan, `ref`/`range` = index lookup), `possible_keys`, `key`, `rows`, and `Extra`.

### 134. What are transactions in SQL?
**Answer:**  
A transaction is a single logical unit of work consisting of one or more SQL operations that must either succeed completely as a whole or fail completely with no partial changes applied.

### 135. What are the ACID properties of a transaction?
**Answer:**
- **Atomicity:** All operations within the transaction succeed, or all are rolled back ("all or nothing").
- **Consistency:** Transactions transition the database from one valid state to another, preserving all integrity constraints.
- **Isolation:** Concurrent transactions execute without interfering with one another.
- **Durability:** Once committed, transaction results are permanently saved on disk, surviving system crashes.

### 136. What is the difference between `COMMIT` and `ROLLBACK`?
**Answer:**
- `COMMIT`: Permanently saves all changes made during the current transaction to disk.
- `ROLLBACK`: Cancels all changes made in the transaction, reverting data back to its pre-transaction state.

### 137. What is a savepoint, and how is it used?
**Answer:**  
A savepoint creates an intermediate marker within a transaction, allowing partial rollbacks without aborting the entire transaction:
```sql
START TRANSACTION;
INSERT INTO accounts VALUES (1, 100);
SAVEPOINT sp1;
INSERT INTO accounts VALUES (2, 200);
ROLLBACK TO sp1; -- Reverts second insert, keeps first
COMMIT;
```

### 138. What are dirty reads, non-repeatable reads, and phantom reads?
**Answer:**
- **Dirty Read:** A transaction reads uncommitted changes written by another concurrent transaction (which might subsequently be rolled back).
- **Non-Repeatable Read:** A transaction reads the same row twice and observes **different values** because another transaction updated and committed that row in between.
- **Phantom Read:** A transaction re-executes a range query and finds **new or missing rows** because another transaction inserted or deleted records and committed.

### 139. What is the difference between optimistic and pessimistic locking?
**Answer:**
- **Optimistic Locking:** Assumes conflicts are rare; allows transactions to proceed without locking rows, verifying version numbers (`version = version + 1`) at commit time. If modified, the transaction is rejected and retried.
- **Pessimistic Locking:** Assumes conflicts are frequent; locks the target rows upfront (`SELECT ... FOR UPDATE`), forcing concurrent transactions to wait until the lock is released.

### 140. What is a deadlock and how can it be prevented or handled?
**Answer:**  
A deadlock occurs when two or more transactions hold locks on resources that each other needs, creating a circular wait where neither can proceed.  
**Prevention & Handling:**
1. Access resources and tables in the same predictable order across all application code.
2. Keep transactions short and commit promptly.
3. Use lowest necessary isolation levels.
4. Database engines detect deadlocks via Wait-For Graphs and automatically abort/rollback the transaction with lower cost, signaling the client to retry.

---

# SECTION 8: MYSQL INTERNALS AND REAL-WORLD PROBLEM SOLVING (Q141 – Q150)

### 141. What is the difference between a stored procedure and a stored function?
**Answer:**
- **Stored Procedure:** Compiled routine executed with `CALL procedure_name()`. Can return zero, one, or multiple values via `OUT` parameters; can execute DDL, DML, and transaction statements; cannot be called inside a `SELECT` statement.
- **Stored Function:** Routine executed directly within SQL expressions (`SELECT func(col)`). Must return a **single scalar value** via a `RETURN` statement; cannot contain transaction control statements (`COMMIT`).

### 142. What is a database trigger, and when should you use one?
**Answer:**  
A trigger is a stored program that executes automatically in response to a specific DML event (`BEFORE` or `AFTER` an `INSERT`, `UPDATE`, or `DELETE`) on a specified table.  
*When to use:* Maintaining comprehensive audit trails, enforcing complex cross-table business validation rules, and maintaining derived denormalized counter caches.

### 143. What is a view, and how does it differ from a table?
**Answer:**  
A view is a virtual table defined by a saved SQL query. It does not store physical data on disk (unless materialized); instead, it executes its underlying query dynamically whenever queried. It is used to simplify complex joins, enhance security by exposing only selected columns, and present clean abstractions.

### 144. What is a recursive CTE and where can it be useful?
**Answer:**  
A CTE that references its own name using `UNION ALL`, consisting of an **anchor member** (base case) and a **recursive member** that repeats until an empty set is produced.  
*Where useful:* Querying organizational employee hierarchies, bills of materials (part-subpart trees), file system folder trees, and generating date/number sequences.

### 145. How do you find gaps in a sequence of IDs or dates using SQL?
**Answer:**  
Using the `LEAD()` window function to inspect the gap between consecutive rows:
```sql
WITH SequenceWithNext AS (
    SELECT 
        id AS current_id, 
        LEAD(id) OVER (ORDER BY id) AS next_id
    FROM transactions
)
SELECT 
    current_id + 1 AS gap_start, 
    next_id - 1 AS gap_end
FROM SequenceWithNext
WHERE next_id - current_id > 1;
```

### 146. How would you optimize a slow query involving multiple joins and millions of records?
**Answer:**
1. **Analyze Execution Plan:** Run `EXPLAIN ANALYZE` to identify full table scans (`type: ALL`), temporary table creations, and filesorts.
2. **Indexing Strategy:** Create composite or covering indexes on join keys (`ON`) and filter columns (`WHERE`).
3. **Filter Early:** Push filtering conditions into subqueries/CTEs before performing joins to reduce join cardinality.
4. **Avoid `SELECT *`:** Select only the required columns to enable index-only scans.
5. **Optimize Hardware & Buffers:** Increase `innodb_buffer_pool_size` so working datasets reside in memory.
6. **Partitioning:** Implement range or list partitioning on high-volume date columns.

### 147. What is the difference between partitioning and sharding?
**Answer:**
- **Partitioning:** Splitting a single large table into smaller physical partitions on the **same single database server instance**. The partition logic is managed transparently by the RDBMS engine.
- **Sharding:** Horizontally distributing table data across **multiple independent physical database servers/nodes**. Requires application-level routing or distributed proxy layers.

### 148. How does MySQL's InnoDB storage engine differ from the MyISAM storage engine?
**Answer:**

| Feature | InnoDB | MyISAM |
| :--- | :--- | :--- |
| **Transactions & ACID** | Full ACID support (`COMMIT`, `ROLLBACK`). | No transaction support. |
| **Locking Granularity** | **Row-level locking** (high concurrency). | **Table-level locking** (low write concurrency). |
| **Crash Recovery** | Automatic crash recovery via Redo Log. | Prone to corruption; requires `REPAIR TABLE`. |
| **Foreign Keys** | Fully supported and enforced. | Not supported (parsed but ignored). |
| **Data Storage** | Clustered index on primary key. | Heap data files (`.MYD`) with separate index (`.MYI`). |

### 149. How would you safely update millions of rows without causing excessive locking or downtime?
**Answer:**  
Updating millions of rows in a single query locks large numbers of rows, floods the undo/redo logs, and causes replication lag.  
**Best Practice Solution:** Break the operation into **chunked batches** executed in a loop with a small sleep delay:
```sql
SET @rows_updated = 1;
WHILE @rows_updated > 0 DO
    UPDATE orders 
    SET status = 'ARCHIVED'
    WHERE order_date < '2023-01-01' AND status != 'ARCHIVED'
    LIMIT 5000;
    
    SET @rows_updated = ROW_COUNT();
    -- Allow concurrent transactions to process between batches
    DO SLEEP(0.1);
END WHILE;
```

### 150. How would you design and query a database for an e-commerce system involving customers, products, orders, order items, payments, and inventory?
**Answer:**

#### Relational Schema Architecture:
1. **`customers`:** `customer_id (PK)`, `full_name`, `email (UNIQUE)`, `created_at`
2. **`products`:** `product_id (PK)`, `product_name`, `unit_price`, `category`
3. **`inventory`:** `product_id (PK, FK)`, `stock_quantity`, `last_restocked`
4. **`orders`:** `order_id (PK)`, `customer_id (FK)`, `order_date`, `order_status`, `total_amount`
5. **`order_items`:** `order_item_id (PK)`, `order_id (FK)`, `product_id (FK)`, `quantity`, `unit_price_at_purchase`
6. **`payments`:** `payment_id (PK)`, `order_id (FK)`, `payment_method`, `payment_status`, `amount_paid`

#### Analytical Query Example: Top 5 Customers by Revenue
```sql
SELECT 
    c.customer_id,
    c.full_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.unit_price_at_purchase) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'DELIVERED' 
  AND p.payment_status = 'COMPLETED'
GROUP BY c.customer_id, c.full_name
ORDER BY total_revenue DESC
LIMIT 5;
```
