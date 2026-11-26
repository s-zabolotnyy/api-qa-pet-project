# REST API Test Automation (Python + Pytest)

A lightweight API test automation framework built with Python, `requests`, and `pytest`. This project demonstrates Object-Oriented Programming (OOP) principles applied to QA automation for testing public RESTful endpoints.

## Key Features & Architecture
* **OOP & Inheritance:** Uses a `BaseApiClient` parent class to handle HTTP connections and a `UserApiClient` child class for endpoint-specific logic.
* **REST API Testing:** Covers positive scenarios (`200 OK`), JSON response parsing, and negative edge cases (`404 Not Found`).
* **Clean Assertions:** Uses Python list comprehensions and `pytest` assertions for readable data validation.

## Tech Stack
* **Language:** Python 3
* **Libraries:** `requests`, `pytest`

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip install requests pytest
   ```
3. Run the tests:
   ```bash
   pytest -v
   ```
