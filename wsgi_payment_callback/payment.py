import os
from flask import Flask, render_template, request
import stripe
import logging, sys
import json

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

stripe_keys = {
    'secret_key': '',
    'publishable_key': ''
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/', methods=['POST'])
def charge():

    token = request.form['stripeToken']
    try:
        charge = stripe.Charge.create(
            amount=2500,
            currency="usd",
            source=token,
            description="Leasetogether preorder"
        )
        return "success"
    except stripe.error.CardError, e:
        # The card has been declined
        pass

if __name__ == '__main__':
    app.run(debug=True)