
# PalmCare

![GitHub repo size](https://img.shields.io/github/repo-size/hsndev18/PalmCare)
![GitHub contributors](https://img.shields.io/github/contributors/hsndev18/PalmCare)
![GitHub stars](https://img.shields.io/github/stars/hsndev18/PalmCare?style=social)
![GitHub forks](https://img.shields.io/github/forks/hsndev18/PalmCare?style=social)
![GitHub issues](https://img.shields.io/github/issues/hsndev18/PalmCare)


Welcome to the GitHub repository of **PalmCare**, crafted by the **Falcons** team for the **MADINAH DATES** hackathon.

## Installation

PalmCare consists of two main components: the app (built with Laravel) and the API Of Model AI (powered by Python Flask). Below are the steps to set up the API.

### Prerequisites

Ensure you have Python installed on your machine. The project uses various Python packages, which can be installed via pip:

```bash
conda create -n palmcare python=3.8 
conda activate palmcare
pip install openai  
conda install pandas numpy scikit-learn
cd Plant-Disease-Detection-main
pip install -r requirements.txt
cd ..
pip install python-dotenv
pip install tensorflow-macos==2.13.0 tensorflow==2.13.0
```

### Setting Up

1. Clone the repository:
    ```bash
    git clone https://github.com/hsndev18/PalmCare.git
    ```
2. Navigate to the API directory:
    ```bash
    cd PalmCare
    ```
3. Set up the API environment(Add openai api key in .env file):
    ```bash
    OPENAI_API_KEY=############
    ```
4. Set up the WepAPP Laravel environment:
    ```bash
    cd WebAPP
    composer install
    ```
5. copy .env.example > .env
6. change database connection to your own connection
7. run migration
    ```php
    php artisan migrate
    ```
8. Run web app
   ```php
   php artisan serve
   php artisan horizon
   ```
9. Go back to main directory and run api.py
    ```bash
    cd ..
    python API.py
    ```
10. Open web app and upload image 
    
## Usage

Once the server is running, you can access the API endpoints from your Laravel application to interact with the data processed by the Flask backend.

## Team

- **Abdulaziz Thabit** - Industrial Engineer, Team Leader
- **Abdullah Abumuall** - Product Designer
- **Hasan Alshikh** - AI & Senior Software Engineer
- **SAEED DRAA** - UI UX

## Acknowledgements

Thanks to all contributors and MADINAH DATES organizers for the opportunity to develop this innovative solution.
