-- ==============================================================================
-- SQL MOCK INTERVIEW QUESTIONS: PRACTICAL SQL CODE & QUERY REFERENCE
-- Magnate Academy - Technical Round Preparation
-- Contains practical SQL solutions, schemas, and queries for Scenario Questions
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- Q24, Q25, Q26: Table Creation, Alteration, and Constraints
-- ------------------------------------------------------------------------------
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dept_id INT,
    salary DECIMAL(10, 2) NOT NULL DEFAULT 30000.00,
    hire_date DATE NOT NULL,
    manager_id INT,
    CONSTRAINT chk_salary CHECK (salary > 0)
);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

-- Adding Foreign Key constraint
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
ON DELETE SET NULL;

-- Adding a new column
ALTER TABLE employees ADD email VARCHAR(100) UNIQUE;

-- ------------------------------------------------------------------------------
-- Q65: Total salary paid by each department
-- ------------------------------------------------------------------------------
SELECT 
    d.dept_name,
    SUM(e.salary) AS total_department_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- ------------------------------------------------------------------------------
-- Q66: Find departments with more than 5 employees
-- ------------------------------------------------------------------------------
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS total_employees
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 5;

-- ------------------------------------------------------------------------------
-- Q70: Highest, lowest, and average salary for each department
-- ------------------------------------------------------------------------------
SELECT 
    d.dept_name,
    MAX(e.salary) AS highest_salary,
    MIN(e.salary) AS lowest_salary,
    ROUND(AVG(e.salary), 2) AS average_salary
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- ------------------------------------------------------------------------------
-- Q85: Employees along with their department names (INNER JOIN)
-- ------------------------------------------------------------------------------
SELECT 
    e.emp_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- ------------------------------------------------------------------------------
-- Q86: Customers who have never placed an order (LEFT JOIN with IS NULL)
-- ------------------------------------------------------------------------------
-- Schema assumption: customers(customer_id, customer_name), orders(order_id, customer_id)
SELECT 
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- ------------------------------------------------------------------------------
-- Q87 & Q88: Self Join - Employees who earn more than their managers
-- ------------------------------------------------------------------------------
SELECT 
    e.first_name AS employee_name,
    e.salary AS employee_salary,
    m.first_name AS manager_name,
    m.salary AS manager_salary
FROM employees e
INNER JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;

-- ------------------------------------------------------------------------------
-- Q111: Find the 2nd highest salary using window functions
-- ------------------------------------------------------------------------------
WITH RankedSalaries AS (
    SELECT 
        emp_id,
        first_name,
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT salary
FROM RankedSalaries
WHERE salary_rank = 2
LIMIT 1;

-- ------------------------------------------------------------------------------
-- Q112: Top 3 salaries in each department
-- ------------------------------------------------------------------------------
WITH DeptRankedSalaries AS (
    SELECT 
        e.emp_id,
        e.first_name,
        d.dept_name,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rnk
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
)
SELECT dept_name, first_name, salary, rnk
FROM DeptRankedSalaries
WHERE rnk <= 3;

-- ------------------------------------------------------------------------------
-- Q115: Compare each month's sales with previous month's sales (LAG)
-- ------------------------------------------------------------------------------
-- Schema assumption: monthly_sales(sale_month DATE, total_amount DECIMAL)
SELECT 
    sale_month,
    total_amount AS current_month_sales,
    LAG(total_amount, 1) OVER (ORDER BY sale_month) AS previous_month_sales,
    ROUND(total_amount - LAG(total_amount, 1) OVER (ORDER BY sale_month), 2) AS mom_growth
FROM monthly_sales;

-- ------------------------------------------------------------------------------
-- Q116: Running total of sales
-- ------------------------------------------------------------------------------
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM sales_records;

-- ------------------------------------------------------------------------------
-- Q117: 3-Period Moving Average
-- ------------------------------------------------------------------------------
SELECT 
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3_periods
FROM sales_records;

-- ------------------------------------------------------------------------------
-- Q120: Identify duplicate records using ROW_NUMBER()
-- ------------------------------------------------------------------------------
WITH CTE_Duplicates AS (
    SELECT 
        emp_id,
        email,
        ROW_NUMBER() OVER (
            PARTITION BY email 
            ORDER BY emp_id ASC
        ) AS row_num
    FROM employees
)
SELECT * 
FROM CTE_Duplicates 
WHERE row_num > 1;

-- To delete duplicate rows safely:
-- DELETE FROM employees WHERE emp_id IN (
--     SELECT emp_id FROM CTE_Duplicates WHERE row_num > 1
-- );

-- ------------------------------------------------------------------------------
-- Q144: Recursive CTE - Generate sequence or Org Hierarchy
-- ------------------------------------------------------------------------------
-- Generating numbers 1 to 10
WITH RECURSIVE NumberSequence AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM NumberSequence WHERE n < 10
)
SELECT * FROM NumberSequence;

-- Org Chart Hierarchy level traversal
WITH RECURSIVE OrgHierarchy AS (
    SELECT emp_id, first_name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.first_name, e.manager_id, o.level + 1
    FROM employees e
    JOIN OrgHierarchy o ON e.manager_id = o.emp_id
)
SELECT * FROM OrgHierarchy ORDER BY level, manager_id;

-- ------------------------------------------------------------------------------
-- Q145: Find gaps in a sequence of IDs
-- ------------------------------------------------------------------------------
WITH SequenceWithNext AS (
    SELECT 
        emp_id AS curr_id,
        LEAD(emp_id) OVER (ORDER BY emp_id) AS next_id
    FROM employees
)
SELECT 
    curr_id + 1 AS gap_start,
    next_id - 1 AS gap_end
FROM SequenceWithNext
WHERE next_id - curr_id > 1;

-- ------------------------------------------------------------------------------
-- Q150: Complete E-Commerce Database Schema & Sample Analytics Query
-- ------------------------------------------------------------------------------
CREATE TABLE ecommerce_customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ecommerce_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50)
);

CREATE TABLE ecommerce_inventory (
    product_id INT PRIMARY KEY,
    stock_quantity INT NOT NULL DEFAULT 0,
    last_restocked TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES ecommerce_products(product_id)
);

CREATE TABLE ecommerce_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_status ENUM('PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED', 'CANCELLED') DEFAULT 'PENDING',
    total_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (customer_id) REFERENCES ecommerce_customers(customer_id)
);

CREATE TABLE ecommerce_order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price_at_purchase DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ecommerce_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES ecommerce_products(product_id)
);

CREATE TABLE ecommerce_payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method ENUM('CREDIT_CARD', 'PAYPAL', 'BANK_TRANSFER', 'UPI') NOT NULL,
    payment_status ENUM('PENDING', 'COMPLETED', 'FAILED', 'REFUNDED') DEFAULT 'PENDING',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount_paid DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ecommerce_orders(order_id)
);

-- Analytics Query: Top 5 Customers by Revenue with order counts
SELECT 
    c.customer_id,
    c.full_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.unit_price_at_purchase) AS total_revenue
FROM ecommerce_customers c
JOIN ecommerce_orders o ON c.customer_id = o.customer_id
JOIN ecommerce_order_items oi ON o.order_id = oi.order_id
JOIN ecommerce_payments p ON o.order_id = p.order_id
WHERE o.order_status = 'DELIVERED' 
  AND p.payment_status = 'COMPLETED'
GROUP BY c.customer_id, c.full_name
ORDER BY total_revenue DESC
LIMIT 5;
