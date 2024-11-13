
# Boad Project

![GitHub repo size](https://img.shields.io/github/repo-size/hsndev18/boad-api)
![GitHub contributors](https://img.shields.io/github/contributors/hsndev18/boad-api)
![GitHub stars](https://img.shields.io/github/stars/hsndev18/boad-api?style=social)
![GitHub forks](https://img.shields.io/github/forks/hsndev18/boad-api?style=social)
![GitHub issues](https://img.shields.io/github/issues/hsndev18/boad-api)


Welcome to the GitHub repository of **BOAD TEAM**, crafted for the **ROSHEN** hackathon.

## Installation

SANA is built with two primary components:

1. Flask (Python) - A RESTful API that processes data with OpenAI and interacts with the front-end. (Back-end)
2. Web Application (Laravel) - A web application that interacts with the API. (Front-end)

Follow these steps to set up the API:
### Prerequisites

Ensure you have Python installed on your machine. The project uses various Python packages, which can be installed via pip:


```bash
git clone https://github.com/hsndev18/boad-api.git
```
    
```bash
conda create -n boad python=3.8
```

```bash
conda activate boad
```

```bash
pip install -r requirements.txt
```

### Setting Up

1. Clone the repository https://github.com/hsndev18/boad-web :
    ```bash
    git clone https://github.com/hsndev18/boad-api.git
    ```
2. Set up the API environment(Add openai api key in .env file):
    ```bash
    OPENAI_API_KEY=############
    ```
3. Run the server:
    ```bash
    python API.py
    ```
4.  You should install the Laravel project to interact with the API.
5.  Clone the repository:
    ```bash
    git clone https://github.com/hsndev18/boad-web
    ```
4. Set up the WepAPP Laravel environment:
    ```bash
    cd boad-web
    composer install
    ```
5. copy .env.example > .env
6. change database connection to your own connection with mysql
   ```php
    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=YOUR_DATABASE_NAME
    DB_USERNAME=YOUR_DATABASE_USERNAME
    DB_PASSWORD=YOUR_DATABASE_PASSWORD
    ```
7. run migration
    ```php
    php artisan migrate --seed
    ```
8. Run web app
   ```php
   php artisan serve
   php artisan horizon
   ```
9. Now you can access the web app from your browser.
10. Enjoy!
## Usage

Once the server is running, you can access the API endpoints from your Laravel application to interact with the allam and preprocess the data before sending it to the openai.

## Team

- **Abulrahman Alhasan** - Team Leader
- **Hasan Alshikh** - Senior Software Engineer, AI Engineer
- **Ibrahim Alnabhan** - Data Analyst & Project Specialist
- **Abdallah Abumuala** - Business Developor
- **Majid Dasuqi** - UX/UI designer


## Acknowledgements

Thanks to all contributors and Roshen organizers for the opportunity to develop this innovative solution.
