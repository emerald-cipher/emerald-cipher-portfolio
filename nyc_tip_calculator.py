# Emerald Cipher LLC - Professional NYC Tip & Tax Calculator
# Built with clean functions, conditionals, validation, and comments
# Perfect for restaurants, delivery apps, or freelance customization

def calculate_tip(bill_amount, service_quality):
    """Returns tip based on service quality (great=20%, good=15%, poor=10%)"""
    quality = service_quality.lower()
    if quality == "great":
        return bill_amount * 0.20
    elif quality == "good":
        return bill_amount * 0.15
    elif quality == "poor":
        return bill_amount * 0.10
    else:
        print("Warning: Invalid service quality. No tip added.")
        return 0

def add_nyc_tax(subtotal):
    """Adds standard NYC sales tax of 8.875%"""
    return subtotal * 0.08875

def validate_bill(amount):
    """Ensures bill amount is positive"""
    if amount <= 0:
        print("Error: Bill amount must be greater than $0.00")
        return False
    return True

# Main program - clean and user-friendly
print("=== Emerald Cipher LLC - Smart NYC Tip Calculator ===\n")

try:
    bill = float(input("Enter the bill amount ($): "))
    if validate_bill(bill):
        service = input("How was the service? (great/good/poor): ").strip()
        tip = calculate_tip(bill, service)
        tax = add_nyc_tax(bill)
        total = bill + tip + tax

        print("\n" + "="*40)
        print("           RECEIPT")
        print("="*40)
        print(f"Subtotal:      ${bill:.2f}")
        print(f"Tip ({service.capitalize()}):       ${tip:.2f}")
        print(f"NYC Tax (8.875%): ${tax:.2f}")
        print("-"*40)
        print(f"TOTAL:         ${total:.2f}")
        print("="*40)
        print("Thank you! – Emerald Cipher LLC\n")
except ValueError:
    print("Error: Please enter a valid number for the bill amount.")