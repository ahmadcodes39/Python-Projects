import requests

API_KEY = '82e2b37b9e-792f48ab23-sil0a2'
response = requests.get(f'https://api.fastforex.io/fetch-all?api_key={API_KEY}')

data = response.json()

def convertCurrency():
    curr_from = input("\nEnter the currency you want to convert from (e.g., USD, INR): ").upper()
    curr_to = input("Enter the currency you want to convert to (e.g., PKR, AOA): ").upper()
    if curr_from not in data['results'] or curr_to not in data['results']:
        print("Invalid currency code. Please try again.")
        return
    
    amount = float(input("Enter the amount: "))

    if curr_from == "USD":
        rate_from = 1 
    else:
        rate_from = data['results'][curr_from]
    
    rate_to = data['results'][curr_to]

    # converted_amount = (amount / rate_from) * rate_to
    converted_amount = (rate_to/rate_from)*amount

    print(f"{amount} {curr_from} = {converted_amount:.2f} {curr_to}")

convertCurrency()

    #100 pkr to inr
    # 278 83
    # 100/278*83
    #  pkr 278 = inr 83
    # 1 usd = 278 pkr
    # 1 usd = 83 inr
    # 1 pkr = 1 inr
    # 278 pkr = 83 inr
    # 100 pkr = (83/278)*100
    # 1 inr to pkr
    # 83 inr  = 278 pkr 
    # 1 inr  = 
    # (278/83)*100
    # 