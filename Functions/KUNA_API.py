import requests

api_key = "0"  # put here your Api key

def parcing():
    
    url = "https://api.kuna.io"
    path = "/v4/markets/public/tickers?pairs=USDT_UAH"
    headers = {
        "accept": "application/json"
    }

    response = requests.get(url + path, headers=headers)

    data = response.json()
    price = data['data'][0]['price']
    return price

class order_manipulation:

    def create_order():
        url = "https://api.kuna.io"
        path = "/v4/order/prvate/create"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": api_key,
        }
        body = {
            "type": "Limit",
            "orderSide": "Bid",
            "pair": "UAH_USDT",
            "quantity": "0.06",
            "price": {},
        }

        request = requests.post(url + path, headers=headers, json=body)
        return request
