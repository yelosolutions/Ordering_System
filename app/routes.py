from flask import Flask, render_template
from app import app


@app.route('/')
def order_info():
    return render_template('order2.html')

#@app.route('/preview_order', methods=['GET', 'POST'])
#def preview_order():
#    return render_template('preview_order.html')

#@app.route('/add_files_and_paypal', methods=['GET', 'POST'])
#def add_files_and_paypal():
#    return render_template('add_files_and_paypal.html')