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

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:Mukhammad-develop/coffee_shop.git
   cd coffee_shop_backend
