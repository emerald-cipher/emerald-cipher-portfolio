# Emerald Cipher LLC - Professional Invoice Validator & Discount Tool
# Validates inputs, applies smart discounts, generates clean invoices
# Perfect for e-commerce, freelance, or small business clients

def validate_invoice(price, quantity):
    """Validates price and quantity – returns True/False with error messages"""
    if not isinstance(price, (int, float)) or price <= 0:
        print("❌ Error: Price must be a positive number greater than $0")
        return False
    if not isinstance(quantity, int) or quantity <= 0:
        print("❌ Error: Quantity must be a positive whole number")
        return False
    return True

def apply_discount(subtotal, customer_type, promo_code=""):
    """Calculates discount based on customer status or promo code"""
    discount_rate = 0
    discount_reason = "None"
    
    if customer_type.lower() == "returning":
        discount_rate = 0.10
        discount_reason = "Returning Customer (10%)"
    elif promo_code.upper() == "WELCOME2026":
        discount_rate = 0.15
        discount_reason = "Promo Code WELCOME2026 (15%)"
    
    discount_amount = subtotal * discount_rate
    return discount_amount, discount_reason

def generate_invoice():
    """Main function – runs the full invoice process"""
    print("=== Emerald Cipher LLC Invoice Generator ===\n")
    
    try:
        price = float(input("Enter item price ($): "))
        quantity = int(input("Enter quantity: "))
        customer_type = input("Customer type (new/returning): ").strip()
        promo_code = input("Promo code (optional, press Enter for none): ").strip()
        
        if not validate_invoice(price, quantity):
            return  # Stop if invalid
        
        subtotal = price * quantity
        discount_amount, discount_reason = apply_discount(subtotal, customer_type, promo_code)
        total = subtotal - discount_amount
        
        # Clean receipt-style output
        print("\n" + "="*40)
        print("           INVOICE")
        print("="*40)
        print(f"Item Price:      ${price:.2f}")
        print(f"Quantity:        {quantity}")
        print(f"Subtotal:        ${subtotal:.2f}")
        print(f"Discount ({discount_reason}): -${discount_amount:.2f}")
        print("-"*40)
        print(f"TOTAL DUE:       ${total:.2f}")
        print("="*40)
        print("Thank you for your business! – Emerald Cipher LLC")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers for price and quantity.")

# Run the tool
if __name__ == "__main__":
    generate_invoice()