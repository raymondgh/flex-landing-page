import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
    'secret_key': 'sk_test_BQokikJOvBiI2HlWgH4olfQ2',
    'publishable_key': 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)