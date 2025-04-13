✅ Key Features:
🔐 Admin Login System
Secure access with static login credentials (admin / admin123).

📦 Inventory Management

Add new items to inventory

View current stock levels

Real-time inventory updates after each sale

💰 Sales Management

Select products from inventory

Specify quantity and make a sale

Auto-calculation of total sale value

📈 Sales History Tracking

See a detailed list of past sales

View item names, quantities sold, and total amounts

🎨 Responsive Design (Bootstrap)

Clean, mobile-friendly UI

Uses Bootstrap 5 for consistent styling and layout

🛠️ Tech Stack:
Frontend: HTML, CSS, Bootstrap 5

Backend: Python, Flask

📂 Project Structure:
Salas and Inventory_app/
├── app.py                  # Main Flask app
├── templates/              # HTML templates (Jinja2)
│   ├── base.html           # Shared layout
│   ├── login.html          # Login screen
│   ├── dashboard.html      # Admin dashboard
│   ├── inventory.html      # Inventory listing
│   ├── sales.html          # Make a sale
│   └── history.html        # Sales history

🚀 How to Run:
Install Flask:

bash
pip install flask
Run the app:

bash
python app.py
Open in browser: Navigate to: http://127.0.0.1:5000
Login with: admin / admin123

💡 Future Improvements:
Integrate SQLite or MySQL for persistent data storage


Add edit/delete items.

