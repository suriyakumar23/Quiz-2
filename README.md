

 📊 Employee Data Generator & API Analytics Platform

A Django REST Framework-based application to generate synthetic employee data, store it in a PostgreSQL database, and expose secure REST APIs for analytics and visualization.

---

 🚀 Features

* ✅ Generate fake employee data using `Faker`
* 🗃️ Store and manage data with **PostgreSQL** (or SQLite for local use)
* 🔐 Token-based authentication (DRF TokenAuth)
* 🔎 Filtering, pagination, and throttling on API endpoints
* 📄 Interactive API documentation with **Swagger UI**
* 📊 Optional frontend integration for data visualization with **Chart.js**

---

 🛠️ Tech Stack

| Category            | Tools/Frameworks                      |
| ------------------- | ------------------------------------- |
| Backend             | Python 3.8+, Django 4.x               |
| API Layer           | Django REST Framework, Django Filters |
| Docs                | drf-yasg (Swagger UI)                 |
| Database            | PostgreSQL (SQLite fallback)          |
| Data Gen            | Faker (for synthetic employee data)   |

---

 📁 Project Structure

```
quiz-2/
│
├── api/                  # Core app with views, serializers, models
├── core/                 # Project settings and URLs
├── utils/                # Custom functions for data generation
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation (you’re here)
```

---

🧪 API Endpoints (Sample)

| Endpoint          | Method | Description                       |
| ----------------- | ------ | --------------------------------- |
| `/api/employees/` | GET    | List all employees (with filters) |
| `/api/employees/` | POST   | Create new employee data          |
| `/api/token/`     | POST   | Obtain token for auth             |
| `/swagger/`       | GET    | API documentation via Swagger UI  |

✅ **Supports filtering**, e.g. `?department=HR&min_salary=50000`
✅ **Pagination and throttling** enabled

---

 🔐 Authentication

This project uses **Token-based authentication**.
To use secured endpoints:

1. Get your token via `/api/token/` by posting credentials.
2. Include it in headers:
   `Authorization: Token <your_token_here>`

---

 📈 Optional Visualization

Integrate a simple frontend (HTML + Chart.js) to display:

* Number of employees by department
* Average salary breakdown
* Gender distribution



---

 ⚙️ Setup Instructions

 1. Clone the repo

```bash
git clone https://github.com/suriyakumar23/Quiz-2.git
cd Quiz-2
```

 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

 3. Install dependencies

```bash
pip install -r requirements.txt
```

 4. Configure database (PostgreSQL recommended)

Edit `settings.py` to connect your PostgreSQL database.
For quick testing, SQLite will also work.

 5. Run migrations and start server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---
📌 Future Improvements

* Add JWT authentication
* Deploy on Heroku or Render
* Add unit tests and CI/CD
* Integrate full frontend (React, Vue)

---
 👨‍💻 Author

Suriya Kumar
GitHub: [@suriyakumar23](https://github.com/suriyakumar23)
LinkedIn: [linkedin.com/in/suriya-kumar-6647562a7](https://linkedin.com/in/suriya-kumar-6647562a7)

---
 📄 License

This project is licensed under the [MIT License](LICENSE).


