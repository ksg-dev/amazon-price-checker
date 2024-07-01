import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()


def check_price(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    product_name = soup.find(name="span", id="productTitle").getText()
    total_price = float(soup.find(name="span", class_="aok-offscreen").getText().split("$")[1].strip())
    return product_name, total_price


def send_email(product_name, product_price, product_url):
    my_email = os.environ["MY_EMAIL"]
    app_password = os.environ["EMAIL_PASS"]
    to_email = os.environ["TO_EMAIL"]

    body = f"{product_name} is now ${product_price}\n{product_url}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: PRICE DROP ALERT\n\n{body}"
        )



def main():
    product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url=product_url, headers=headers)
    response.raise_for_status()
    webpage = response.text
    prod_name, prod_price = check_price(webpage)
    print(prod_name, prod_price)

if __name__ == "__main__":
    main()
