#Flask Web App on AWS EC2 - Registration and SQLite3 Integration

#Project Overview

This project demonstrates deploying a **Flask web application** on an **AWS EC2 instance** using **Apache2 with mod_wsgi**, and integrating a **SQLite3 database** for user registration and information retrieval.

#EC2 Instance Setup

- Launched a free-tier eligible **Ubuntu Server 24.04 LTS** EC2 instance.
- Created and used a secure **key pair** for SSH access.
- Configured **security groups** to allow HTTP (port 80) and SSH (port 22).

#Web Server & Database Configuration 

- Installed and configured:
  - **Apache2**
  - **mod_wsgi for Python 3**
  - **Flask** using `python3-pip`
  - **SQLite3** for persistent data storage

- Flask app setup with:
  - A registration route
  - A SQLite3 table creation and insertion
  - Apache virtual host setup to serve the app via mod_wsgi

#Interactive Web Page Features 

#a.Registration Page 
- Collects:
  - Username
  - Password

#b.User Details 
- Collects:
  - First Name
  - Last Name
  - Email

#c. Submission Redirect 
- Redirects to profile page upon registration
- Displays user information

#d. Login for Retrieval 
- Allows user to enter **username & password**
- Displays saved information from the database
