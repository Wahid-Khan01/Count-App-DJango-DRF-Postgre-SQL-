Despite time constraints due to heavy workload at the office, I've endeavored to provide the best possible solution within the limited time available. If you encounter any difficulties while running the application, please feel free to connect with me for assistance.


Project Summary: Catalyst

Overview:
Catalyst is a robust web application designed to streamline data management tasks by allowing users to register, upload CSV files, filter data based on keywords. Built on a powerful stack including Python, Django, Django Rest Framework (DRF), PostgreSQL, JavaScript, HTML, CSS, Bootstrap, AJAX, and Django-allauth, Catalyst offers a seamless user experience coupled with advanced functionality.

Key Features:

User Registration and Authentication:
Users can easily register on the platform and securely authenticate themselves using Django-allauth.
Admins have the authority to manage user accounts, including adding, deleting, and viewing user details.

File Upload and Management:
Registered users can upload CSV files containing their data.
Catalyst efficiently manages and stores uploaded files in a PostgreSQL database.

Data Filtering:
Users have the capability to filter data within uploaded CSV files based on specific keywords.
The application utilizes AJAX to ensure seamless and responsive filtering functionality.

Technologies Used:
Python, Django, Django Rest Framework (DRF), PostgreSQL, JavaScript, HTML & CSS, Bootstrap, AJAX, Django-allauth, Chunked-upload

Instructions for Setup
1. First, create the environment.
2. After creating the environment, install the required modules from the requirement.txt file.
3. Next, create a Django project.
4. Create a .env file within the project to store sensitive information securely.
5. You'll need to create five Django apps since each part is divided into small apps.
6. Load relevant configurations in the project's settings.
7. Finally, load the created apps in the INSTALLED_APPS list within the project settings.

Project Name - catalyst_count
Total 5 Apps - authentication, uploader, count_api, query_builder, user_management

Important Instruction 
1. Virtual Environment should be created because the css(designing) of allauth(inbuilt signup and inbuilt login) templates is done in inbuilt templates only which you will get in virtual environment directory. I will share those templates in the end of this document
2. Url of filter api - 127.0.0.1:8000/filter/?name=enter_name&industry=enter_industry&year_founded=enter_year_founded&locality=enter_locality&country=enter_country
3. All the modules with their appropriate versions are available in the reuirements.txt dont forget to install it once the virtual environment created
4. Docker is also used with this but just because the auth template is having its css in virtual environment, css will fade away if the application is running on a docker container and for reducing the complexity i am not providing it. But if needed i will add it in the repo
5.Secret key and database info is save in env file so you have to make your own env file with adding the concern details to make it working
6. Code is full of comments which will show the purpose of the code


*CSS for Sign-up and Login Template*
1. Just add empty block in
<venv-directory>/Lib/site-packages/allauth/layouts/base.html

{% block css %} {% endblock css %} 

2. Add this below endblock headtitle

location - <venv-file>/Lib/site-packages/allauth/templates/account/login.html

content to add - 

{% block css %}
<style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        div {
            margin-bottom: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            display: inline;
            margin-right: 10px;
        }
        ul li a {
            text-decoration: none;
            color: #000;
            font-weight: bold;
        }
        h1 {
            margin-top: 20px;
        }
        p {
            margin-bottom: 20px;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            width: 50%;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"],
        input[type="password"],
        input[type="checkbox"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="text"],
        input[type="password"]{
            width: calc(100% - 20px); 
        }
        input[type="checkbox"] {
            margin-right: 5px; 
        }
        button {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        label[for="id_remember"] {
            display: inline;
        }
        #id_remember {
            width: 2%;
        }
</style>
{% endblock css %}


3. Add this below endblock headtitle

location - <venv-file>/Lib/site-packages/allauth/templates/account/signup.html

content to add - 

{% block css %}
<style>
    body {
        font-family: Arial, sans-serif;
    }
    form {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    h1 {
        text-align: center;
    }
    p {
        text-align: center;
        margin-bottom: 20px;
    }
    label {
        display: block;
        margin-bottom: 10px;
    }
    input[type="text"],
    input[type="email"],
    input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }
    button[type="submit"] {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    button[type="submit"]:hover {
        background-color: #0056b3;
    }
</style>
{% endblock css %}


