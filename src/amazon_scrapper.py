from bs4 import BeautifulSoup
import requests


def extract_title(soup, truncate):
    title = soup.find(id='productTitle').getText().strip()
    if truncate:
        title = (title[:70] + '...') if len(title) > 70 else title
    return title


def scrap(url_to_scrape):
    headers = {"Content-Type": "application/json; charset=utf-8", "User-Agent": "PostmanRuntime/7.29.2",
               "Accept": "*/*",
               "Host": "www.amazon.in",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}
    page = requests.get(url_to_scrape, headers=headers)
    soup = BeautifulSoup(page.content, features="html.parser")
    price_as_number = extract_price(soup)
    product_title = extract_title(soup, True)
    return product_title, "Rs. " + str(price_as_number)


def extract_price(soup):
    price = ""
    core_price_desktop = soup.find(id='corePrice_desktop')
    if core_price_desktop is None:
        core_price_desktop = soup.find(id='corePriceDisplay_desktop_feature_div')
        price = core_price_desktop.find('span', attrs={'class': 'a-price-whole'})
        price = price.getText().replace('₹', '').replace(',', '')
    else:
        index_of_deal_of_the_day = core_price_desktop.getText().find('Deal of the Day')
        if index_of_deal_of_the_day > -1:
            price = core_price_desktop.find('span', attrs={'class': 'apexPriceToPay'})
            price = price.find('span').getText().replace('₹', '').replace(',', '')
        else:
            index_of_deal_of_the_day = core_price_desktop.getText().find('Deal Price')
            if index_of_deal_of_the_day > -1:
                price = core_price_desktop.find('span', attrs={'class': 'apexPriceToPay'})
                price = price.find('span').getText().replace('₹', '').replace(',', '')
            elif core_price_desktop.getText().find('a-price-range'):
                return -1
    price_as_number = int(price.split('.')[0])
    return price_as_number


urls = [
    'https://www.amazon.in/Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863TXGM3/ref=sr_1_1?crid=20SPXSFOD1TZF&keywords=xm4&qid=1662128244&sprefix=xm4%2Caps%2C253&sr=8-1',
    'https://www.amazon.in/Bose-Quiet-Comfort-Wireless-Headphone/dp/B0756CYWWD/ref=psdc_14146390031_t1_B0863TXGM3',
    'https://www.amazon.in/Sennheiser-HD-450SE-Headphones-Black/dp/B09325WTV5/ref=psdc_14146390031_t2_B0756CYWWD',
    'https://www.amazon.in/Logitech-Advanced-Illuminated-Bluetooth-Responsive/dp/B08196YFMK/?_encoding=UTF8&pd_rd_w=H7GBj&content-id=amzn1.sym.8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pf_rd_p=8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pf_rd_r=AP6K3J4ST1KP8VDS31AF&pd_rd_wg=XsiJL&pd_rd_r=d546b710-512a-405b-ac4a-b28eaa5ebdac&ref_=pd_gw_bmx_gp_1k8ql61o',
    'https://www.amazon.in/Kaku-Fancy-Dresses-Krishnaleela-Mythological/dp/B07VBKT3QY/?_encoding=UTF8&pf_rd_p=8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pd_rd_wg=FBgR7&pf_rd_r=36RS1DE82SZPPEPR7HMD&content-id=amzn1.sym.8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pd_rd_w=Njeiy&pd_rd_r=69f72aee-5ae0-4e39-81fc-212d0deb857f&ref_=pd_gw_bmx_gp_213ngqtn',
    'https://www.amazon.in/Sparx-Black-Brown-Flip-Flops-Slippers/dp/B00IZ94LHG/?_encoding=UTF8&pd_rd_w=N0YM9&content-id=amzn1.sym.8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pf_rd_p=8f64e8c0-5bc3-401c-a570-b800a4fa8c0e&pf_rd_r=36RS1DE82SZPPEPR7HMD&pd_rd_wg=FBgR7&pd_rd_r=69f72aee-5ae0-4e39-81fc-212d0deb857f&ref_=pd_gw_bmx_gp_213ngqtn&th=1&psc=1',
    'https://www.amazon.in/Sparx-Black-Brown-Flip-Flops-Slippers/dp/B00IZ94K54/?th=1&psc=1',
    'https://www.amazon.in/Sparx-Black-Brown-Flip-Flops-Slippers/dp/B00IZ94LHG/?th=1&psc=1',
    'https://www.amazon.in/Crocs-Bayaband-Black-Flip-Flops-8-205393-066/dp/B0819RYHC2?ref_=Oct_d_otopr_d_1983575031&pd_rd_w=M5dtJ&content-id=amzn1.sym.f5d0d3e7-fe8a-4766-96ee-1c39e69d20b3&pf_rd_p=f5d0d3e7-fe8a-4766-96ee-1c39e69d20b3&pf_rd_r=JNF1A8RSVHA07CCCWCSF&pd_rd_wg=heaWJ&pd_rd_r=5717ef5c-5dfd-4a44-ab9b-1e463b5936b2&pd_rd_i=B0819RYHC2'
]

for url in urls:
    print(scrap(url))

