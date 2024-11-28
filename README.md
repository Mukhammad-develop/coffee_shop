# Coffee Shop Backend

A backend system for managing a coffee shop's operations, including user registration, authentication, product management, cart functionality, and order processing.

---


## Features
- **User Authentication**:
  - Registration (`/registration`)
  - Login (`/authentication`)
  - Verification (`/verification`)
  - Fetch Current User Details (`/me`)

- **Product Management**:
  - CRUD operations for products and categories.

- **Cart Management**:
  - Add, update, view, and delete cart items.

- **Order Management**:
  - Place and manage user orders.

---

## Technologies
- **Framework**: Django Rest Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (via `rest_framework_simplejwt`)
- **Deployment**: Docker with Docker Compose

---

## Setup
### Prerequisites
- Python 3.11+
- PostgreSQL
- Docker and Docker Compose

### Start
1. Clone the repository:
   ```bash
   git clone git@github.com:Mukhammad-develop/coffee_shop.git
   cd coffee_shop_backend

# Endpoints

## User Authentication

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| POST   | `/registration`    | Register a new user.           |
| POST   | `/authentication`  | Authenticate a user (JWT).     |
| POST   | `/verification`    | Verify user identity.          |
| GET    | `/me`              | Get current user details.      |

## Product Management

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| GET    | `/products`        | Get all products.              |
| POST   | `/products`        | Add a new product.             |
| PUT    | `/products/<id>`   | Update a product.              |
| DELETE | `/products/<id>`   | Delete a product.              |

## Category Management

| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| GET    | `/categories`         | Get all categories.             |
| POST   | `/categories`         | Add a new category.             |
| PUT    | `/categories/<id>`    | Update a category.              |
| DELETE | `/categories/<id>`    | Delete a category.              |

## Cart Management

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| GET    | `/cart`            | Get the user's cart.           |
| POST   | `/cart`            | Add an item to the cart.       |
| PUT    | `/cart/<id>`       | Update a cart item.            |
| DELETE | `/cart/<id>`       | Remove a cart item.            |

## Order Management

| Method | Endpoint           | Description                    |
|--------|--------------------|--------------------------------|
| GET    | `/orders`          | Get all orders for the user.   |
| POST   | `/orders`          | Place a new order.             |
| GET    | `/orders/<id>`     | Get details of a specific order.|
| DELETE | `/orders/<id>`     | Cancel a specific order.        |
