# E-Commerce Order Management System

This is a backend system built with **FastAPI** to manage and process orders in an e-commerce platform. The system provides RESTful APIs for order management, asynchronous order processing using an in-memory queue, and metrics reporting.

---

## Features

- **Order Management**:
  - Create new orders with fields like `user_id`, `order_id`, `item_ids`, and `total_amount`.
  - Check the status of orders (`Pending`, `Processing`, `Completed`).

- **Asynchronous Order Processing**:
  - Uses an in-memory queue (`queue.Queue`) with a worker thread to process orders asynchronously.

- **Metrics Reporting**:
  - Fetch key metrics such as:
    - Total number of orders processed.
    - Average processing time for orders.
    - Count of orders in each status (`Pending`, `Processing`, `Completed`).

- **Database**:
  - Uses **MySQL** with **SQLAlchemy** for order storage.
  - Auto-incremental `order_id` for unique order identification.

---

## Technologies Used

- **Python** (FastAPI, SQLAlchemy, Pydantic)
- **MySQL** (Database)
- **Queue.Queue** (Asynchronous task processing with worker threads)

---

## Setup Instructions

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed on your system.
2. **MySQL**: Install and set up a MySQL server.
3. **Dependencies**: Install the required Python packages.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sajaljain077/ecommerce-order-system.git
   cd ecommerce-order-system
   ```
2. **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```
3. **Set Up the Database**:
  Find all of the sql queries in the sql_query.txt file
  DATABASE_URL = "mysql+pymysql://{{username}}:{{password}}@localhost/order_db"

4. **Run the Application**:
  ```bash
  uvicorn app.main:app --reload
  ```
