# cofffee-shop-code-challenge
# ☕ Coffee Shop Domain Modeling Challenge



A Python implementation of a coffee shop domain with three models: `Coffee`, `Customer`, and `Order`, demonstrating object-oriented programming principles and many-to-many relationships.

## 🏗️ Project Structure
coffee-shop-challenge/
├── lib/
│ ├── init.py
│ ├── coffee.py # Coffee model implementation
│ ├── customer.py # Customer model implementation
│ └── order.py # Order model implementation
├── tests/
│ ├── init.py
│ ├── test_coffee.py
│ ├── test_customer.py
│ └── test_order.py
├── debug.py # Sandbox for manual testing
├── Pipfile # Dependency management
└── README.md


🛠️ Implementation Details
Key Features:
Proper Data Encapsulation with getters/setters

Type Validation for all attributes

Immutable Properties where required

Relationship Methods to navigate object graph

Business Logic Methods like average_price()

Validation Rules:
☕ Coffee names: 3+ character strings (immutable)

👤 Customer names: 1-15 character strings

💲 Order prices: floats between 1.0-10.0 (immutable)


🚀 Getting Started
Clone the repository:

bash
git clone https://github.com/BakariJuma1/cofffee-shop-code-challenge
cd coffee-shop-challenge
Set up environment:

bash
pipenv install
pipenv shell
Run tests:

bash
python -m pytest tests/
Experiment in debug console:

bash
python debug.py
