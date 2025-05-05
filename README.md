 JobSphere

JobSphere is a dynamic job portal web application where job seekers and employers can meet, connect, and engage. This platform helps job seekers search for jobs and apply, while employers can post jobs and manage applications easily.

---

🚀 Features

- 👨‍💼 Separate roles for **Job Seekers**, **Employers**, and **Admin**
- 🔍 Job search integration using a **3rd-party Job API**
- 📄 Employers can **post**, **edit**, and **manage job listings**
- 📥 Job seekers can **search**, **apply**, and **track applications**
- 🔐 User authentication and role-based access
- 🗃️ Admin panel to manage users and jobs

---

🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **API Integration**: 3rd-party Job Search API

---

📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/JobSphere.git
   cd JobSphere
2. **Create virtual environment**
    python -m venv env
    source env/bin/activate # On Windows:  env\Scripts\activate 
    
3. **Install dependencies**
    pip install -r requirements.txt
4. **Apply migrations**
    python manage.py migrate
5. **Run the server**
    python manage.py runserver
6. **Open in browser**
    http://127.0.0.1:8000/
    

