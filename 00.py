# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
import requests


def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    res = requests.get(url=url).json()
    data = res["data"]
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())
