# 📝 Blogging System

A full-stack Blogging System built using Django that allows users to register, create blogs, edit posts, like articles, search blogs, categorize content, and manage user authentication.

## 🚀 Features

- 🔐 User Authentication
  - User Registration
  - Login
  - Logout

- ✍️ Blog Management
  - Create Blog
  - Edit Blog
  - Delete Blog
  - View Blog Details

- ❤️ Like System
  - Like/Unlike Blogs

- 📂 Categories
  - Category-wise Blog Listing

- 🔍 Search Blogs

- 👤 User Profile

- 📱 Responsive UI using Bootstrap

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## 📁 Project Structure

```
blogging-system/
│
├── blog_main/
│
├── blogs/
│
├── category/
│
├── users/
│
├── templates/
│
├── static/
│
├── media/
│
├── db.sqlite3
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/blogging-system.git
```

### 2. Move into Project Folder

```bash
cd blogging-system
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Login Page
- Register Page
- Create Blog
- Blog Details
- Categories
- Search Result
- User Profile
- Admin Panel

---

## 🔑 Admin Panel

Visit

```
http://127.0.0.1:8000/admin/
```

Login using your superuser credentials.

---

## 📌 Future Improvements

- Comments System
- Rich Text Editor
- Email Verification
- Password Reset
- Bookmark Blogs
- User Following
- Dark Mode
- REST API
- JWT Authentication
- Image Compression
- Blog Analytics

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 🐞 Known Issues

- SQLite is used for development.
- Media files require proper configuration in production.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Harsh Raj**

- GitHub: https://github.com/harsh-raj-14

---

## ⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork it

📢 Share it with others

Happy Coding! 🚀