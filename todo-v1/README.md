
## Todo Application

This is a basic Todo API using Django Rest Framework. We can view (***get***) existing todo items, add (***post***) new todo item, modify (***patch***) todo item and remove (***delete***) todo item.

Project has been deployed on [***Heroku***](https://django-todo-v1.herokuapp.com/)


### 🔗 Content

* [Overview](#todo-application)
* [Content](#-content)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [API Reference](#-api-reference)
* [Run Locally](#-run-locally)
* [Documentation](#-documentation)
* [Demo](#-demo)
* [Screen-Shots](#-screen-shots)
* [Author](#-author)


### 📋 Features

- **GET**  --> View All Todos items
- **POST** --> Add new Todo item
- **PATCH** --> Modify Todo item
- **DELETE** --> Delete Todo item


### 🧰 Tech Stack

Django, Django REST Framework *(Python)*


### 🛠 API Reference

**Postman Endpoints** : https://www.getpostman.com/collections/36777afb47097b8bb1eb

![ENV file](docs/ss.png)

**API Endpoints JSON file** (for importing into thunderclient / postman) is available in the docs folder or click [here](docs/endpoints.json) 


### 💻 Run Locally

***Step#1 : Clone Project Repository***

```bash
git clone https://github.com/atharvparkhe/todo-v1.git && cd todo-v1
```

***Step#2 : Create Virtual Environment***

* If *virtualenv* is not istalled :
```bash
pip install virtualenv && virtualenv env
```
* **In Windows :**
```bash
env/Scripts/activate
```
* **In Linux or MacOS :**
```bash
source env/bin/activate
```

***Step#3 : Install Dependencies***

```bash
pip install --upgrade pip -r requirements.txt
```

***Step#4 : Run Server***

```bash
python manage.py runserver
```

*Check the terminal if any error.*


### 📄 Documentation

The docs folder contain all the project documentations and screenshots of the project.

**Remote Server Base Link :** https://django-todo-v1.herokuapp.com/

**Local Server Base Link :** http://localhost:8000/

**Admin Pannel :**
- ***Username :*** "admin"
- ***Email :*** "admin@admin.com"
- ***Password :*** "password"


### 🧑🏻‍💻 Demo

![Implementation](docs/abc.gif)

YouTube Link : https://youtu.be/cRNKxHO3O2g


### 🌄 Screen-Shots

![Get All Todos](docs/project/get-todo.png)
![Add new Todo](docs/project/post-todo.png)
![Edit Todo](docs/project/patch-todo.png)
![Delete Todo](docs/project/delete-todo.png)


### 🙋🏻‍♂️ Author

**🤝 Connect with Atharva Parkhe**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/atharvparkhe/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/atharvparkhe/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/atharvparkhe/)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/patharv777/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UChimOJO64hOqtE7HCgtiIig)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8WNC43Xsfc)
