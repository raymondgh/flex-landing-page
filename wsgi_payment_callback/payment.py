import os
from flask import Flask, render_template, request
import stripe
import logging, sys
import json
import config

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

stripe.api_key = config.StripeConfig.TEST_STRIPE_SECRET_KEY

app = Flask(__name__)

@app.route('/', methods=['POST'])
def charge():

    token = request.form['stripeToken']
    try:
        charge = stripe.Charge.create(
            amount=2900,
            currency="usd",
            source=token,
            description="Leasetogether Preorder"
        )
        return "success"
    except stripe.error.CardError, e:
        # The card has been declined
        pass

if __name__ == '__main__':
    app.run(debug=True)