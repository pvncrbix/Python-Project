def currency_converter(amount, from_currency, to_currency):
    rates = {
        "USD": 1.0,
        "EUR": 1.10,
        "INR": 97.0,
        "GBP": 0.89,
        "JPY": 160.0
    }
    if from_currency not in rates or to_currency not in rates:
        print("Currency not supported.")
        return
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
currency_converter(amount, from_currency, to_currency)
new_amount = float(input("Enter new amount: "))
currency_converter(new_amount, from_currency, to_currency)