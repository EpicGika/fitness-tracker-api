# API Authentication

This API uses JWT (JSON Web Tokens) for authentication. Below are the steps to authenticate and access protected endpoints.

## Obtaining a Token

To authenticate, send a POST request to the `/api/token/` endpoint with your username and password:

### Request
- **URL**: `/api/token/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
