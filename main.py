import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# url_product_data = product_url.split("dp/")[1]
# product_sku = url_product_data.split("?", maxsplit=1)[0]
#
# camel_product_url = f"https://camelcamelcamel.com/product/{product_sku}"
# # print(product_sku)
#
# response = requests.get(url=camel_product_url)
# print(response)
#
# # print(content)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=product_url, headers=headers)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
total_price = float(soup.find(name="span", class_="aok-offscreen").getText().split("$")[1].strip())

print(total_price)