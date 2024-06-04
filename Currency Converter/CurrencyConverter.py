def currency_converter():
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "INR": 74.0,
        "JPY": 110.0
    }
    
    print("Welcome to the Currency Converter!")
    
    source_currency = input("Enter the source currency (USD, EUR, GBP, INR, JPY): ").upper()
    if source_currency not in exchange_rates:
        print("Invalid source currency code.")
        return

    target_currency = input("Enter the target currency (USD, EUR, GBP, INR, JPY): ").upper()
    if target_currency not in exchange_rates:
        print("Invalid target currency code.")
        return

    try:
        amount = float(input(f"Enter the amount in {source_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a numerical value.")
        return

    
    amount_in_usd = amount / exchange_rates[source_currency]

    converted_amount = amount_in_usd * exchange_rates[target_currency]

    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")

currency_converter()
