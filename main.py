import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv  import load_dotenv

load_dotenv()

url = os.environ["URL"]
headers = {
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": os.environ["USER_AGENT"],
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.find(name="span", id="productTitle")
if title_tag:
    product_title = title_tag.getText().strip()
else:
    product_title = "Titolo non trovato"
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_whole) + float(price_fraction)/100

if price < 100:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"],
                            to_addrs=os.environ["EMAIL_ADDRESS"],
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${price}.\n{url}".encode("utf-8"))