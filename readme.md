# Challenge

## Database Schema

| Table Name | Description |
|------------|-------------|
| products   | Contains information about products, including name, price, and unit measure ID. |
| unit_measures | Contains information about unit measures, including name and abbreviation. |

### products

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | integer  | Unique identifier for the product. |
| name        | string   | Name of the product. |
| price       | decimal  | Price of the product. |
| unit_measure_id | integer | Foreign key referencing the unit_measures table. |

### unit_measures

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | integer  | Unique identifier for the unit measure. |
| name        | string   | Name of the unit measure. |
| abbreviation | string  | Abbreviation for the unit measure. |

### sales

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | integer  | Unique identifier for the sale. |
| date        | date     | Date of the sale. |
| quantity    | integer  | Quantity of the product sold. |
| product_id  | integer  | Foreign key referencing the products table. |



### SQL scripts to create the tables

```sql
    CREATE TABLE unit_measure (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );

    CREATE TABLE product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        unit_measure_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (unit_measure_id) REFERENCES unit_measure (id)
    );

    CREATE TABLE sale (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        quantity INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product (id)
    );
```
