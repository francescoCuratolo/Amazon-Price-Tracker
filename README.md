# Amazon Price Tracker
A simple Python script that monitors the price of a product on Amazon and sends an email alert when the price drops below a specified threshold.

## Features
- Fetches product page using requests
- Parses HTML using BeautifulSoup
- Extracts product title and price
- Sends email notification when price is below a target value
- Uses environment variables for sensitive data

## How It Works
1.	The script sends a GET request to a specific Amazon product URL.
2.	It parses the HTML response using BeautifulSoup.
3.	It extracts:
o	Product title
o	Product price (whole + fractional part)
4.	If the price is below $100, an email is sent to notify the user.

## Project Structure
~~~
.
├── main.py
├── .env
└── README.md

~~~
## Environment Variables

Create a .env file in the root directory and add the following:

SMTP_ADDRESS=smtp.yourprovider.com

EMAIL_ADDRESS=your_email@example.com

EMAIL_PASSWORD=your_password

URL=url

USER_AGENT=user_agent

## Usage

1.	Clone the repository:

~~~
git clone https://github.com/francescoCuratolo/Amazon-Price-Tracker.git
cd amazon-price-tracker

~~~
2.	Install dependencies:

~~~
pip install requests beautifulsoup dotenv

~~~
3.	Run the script:

~~~
python main.py

~~~

## Requirements

•	Python 3.x

•	requests

•	Beautifulsoup

•	dotenv

## Disclaimer

- Amazon frequently changes its HTML structure, which may break the parser.

- Scraping Amazon may violate their Terms of Service — use this script responsibly.

- This project is for educational purposes only.

- Consider adding delays or headers to avoid being blocked.

## Example Alert

Subject: Amazon Price Alert!

Product Name is now $89.99.

https://www.amazon.com/dp/PRODUCT_ID

##  Credits

This project was inspired by a 100 Days of CodeTM: the Complete Python Pro Bootcamp from Dr. Angela Yu on Udemy.
