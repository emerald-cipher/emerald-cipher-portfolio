# Invoice Validator & Discount Tool  
**Emerald Cipher LLC – Professional Python Automation**

<img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python"> <img src="https://img.shields.io/badge/Status-Ready%20for%20Clients-green" alt="Status"> <img src="https://img.shields.io/badge/Freelance-Available-orange" alt="Freelance">

A clean, reusable Python script that validates invoice data and automatically applies smart discounts — perfect for e-commerce stores, freelancers, consultants, and small businesses.

### ✨ Key Features
- **Input validation** with clear, user-friendly error messages
- **10% discount** for returning customers
- **15% discount** with promo code `WELCOME2026`
- Professional receipt-style output
- Fully commented and structured with reusable functions
- Easy to customize (add tax, multiple items, save to file, etc.)

### 🛠️ Built With
- Python 3
- Functions, conditionals (if/elif/else), try/except error handling
- Professional code style and refactoring (from Google IT Automation cert)

### 🚀 How to Run
1. Save the file as `invoice_validator.py`
2. Run in terminal, VS Code, or any Python environment:
   ```bash
   python invoice_validator.py

   === Emerald Cipher LLC Invoice Generator ===

Enter item price ($): 149.99
Enter quantity: 2
Customer type (new/returning): returning
Promo code (optional, press Enter for none): 

========================================
           INVOICE
========================================
Item Price:      $149.99
Quantity:        2
Subtotal:        $299.98
Discount (Returning Customer (10%)): -$30.00
----------------------------------------
TOTAL DUE:       $269.98
========================================
Thank you for your business! – Emerald Cipher LLC
