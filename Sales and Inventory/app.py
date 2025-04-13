from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Static credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# In-memory data
inventory = {}
sales_history = []

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
            session['user'] = ADMIN_USERNAME
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    if name in inventory:
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
    return redirect(url_for('inventory_view'))

@app.route('/inventory')
def inventory_view():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('inventory.html', inventory=inventory)

@app.route('/make_sale', methods=['POST'])
def make_sale():
    name = request.form['name']
    quantity = int(request.form['quantity'])

    if name in inventory and inventory[name]['quantity'] >= quantity:
        total = quantity * inventory[name]['price']
        inventory[name]['quantity'] -= quantity
        sales_history.append({'item': name, 'quantity': quantity, 'total': total})
    return redirect(url_for('sales_view'))

@app.route('/sales')
def sales_view():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('sales.html', inventory=inventory)

@app.route('/history')
def history_view():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('history.html', sales=sales_history)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
