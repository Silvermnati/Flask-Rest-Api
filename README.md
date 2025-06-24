# 🌙 Late Show API

A Flask-based RESTful API for managing Late Night TV show guests, episodes, and appearances.

---

## ✅ Features

- MVC architecture
- PostgreSQL database (no SQLite)
- JWT-based authentication (Flask-JWT-Extended)
- Token-protected endpoints
- SQLAlchemy ORM with Flask-Migrate
- Fully tested via Postman collection
- Clean and modular folder structure

---

## 🗂 Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   └── appearance.py
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   └── appearance_controller.py
├── .env
├── .flaskenv
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
├── challenge-4-lateshow.postman_collection.json
```

---

## 🛠️ Setup Instructions

### 🔧 Environment Setup

1. **Clone the repo** (or create your own):

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

2. **Install dependencies**:

```bash
pipenv install
pipenv shell
```

3. **Create the PostgreSQL database**:

```sql
CREATE DATABASE late_show_db;
```

4. **Configure environment variables** in `.env`:

```env
DATABASE_URI=postgresql://<username>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=supersecretjwtkey
```

5. **Add `.flaskenv`**:

```env
FLASK_APP=server.app:create_app
FLASK_ENV=development
```

---

## 🔃 Database Migration + Seeding

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python -m server.seed
```

---

## 🚀 Run the Server

```bash
flask run
```

API will run on: `http://127.0.0.1:5000`

---

## 🔐 Authentication Flow

### 🔹 Register

```http
POST /register
Content-Type: application/json

{
  "username": "admin",
  "password": "adminpass"
}
```

### 🔹 Login

```http
POST /login
Content-Type: application/json

{
  "username": "admin",
  "password": "adminpass"
}
```

Response:
```json
{
  "access_token": "<JWT token>"
}
```

### 🔐 Using the Token

For protected routes, add this header:

```http
Authorization: Bearer <your-token>
```

---

## 📮 API Endpoints

| Route | Method | Auth? | Description |
|-------|--------|-------|-------------|
| `/register` | POST | ❌ | Create user |
| `/login` | POST | ❌ | Log in & get JWT |
| `/guests` | GET | ❌ | List guests |
| `/episodes` | GET | ❌ | List episodes |
| `/episodes/<id>` | GET | ❌ | Get single episode with appearances |
| `/episodes/<id>` | DELETE | ✅ | Delete episode |
| `/appearances` | POST | ✅ | Create new appearance |

---

## 🧪 Postman Collection

1. Open Postman
2. Click **Import**
3. Upload `challenge-4-lateshow.postman_collection.json`
4. Use requests:
   - Register
   - Login
   - Add JWT to protected routes
   - Test all endpoints

---

## 🧼 Sample Appearance Request (Protected)

```http
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

---

## 🧪 Testing Instructions

- Seeded users, episodes, and guests using `python -m server.seed`
- All routes tested using Postman
- JWT-protected routes tested with login token
- Appearance and episode deletion confirmed working

---

## 🛑 Known Limitations

- No pagination on large datasets
- Simple date format (can be improved to ISO 8601)

---

## 📜 License

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in     
all copies or substantial portions of the Software.                            

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```

---

## 📎 Author

**Silvester**  
Built with ❤️ using Flask, PostgreSQL, and Postman.
