from flask import Flask, render_template, request, redirect
import os
import stripe
import logging
import sys
import json
import config

app = Flask(__name__)
logging.basicConfig(filename='payment.log', level=logging.DEBUG)

@app.route('/', methods=['POST'])
def charge():

    stripe.api_key = config.StripeConfig.TEST_STRIPE_SECRET_KEY
    token = request.form['stripeToken']

    try:
        charge = stripe.Charge.create(
            amount=2900,
            currency="usd",
            source=token,
            description="Leasetogether Preorder"
        )

        purchase_pref = request.form['purchasePref']
        logging.info("Purchase Pref: %s, %s", token, purchase_pref)
        return redirect('https://leasetogether.com/success.html')
    except stripe.error.CardError, e:
        # The card has been declined
        pass

if __name__ == '__main__':

    app.run(debug=True)
