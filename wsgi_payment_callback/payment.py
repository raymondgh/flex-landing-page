import os
from flask import Flask, render_template, request
import stripe
import logging, sys
import json
import config

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

trans_log = logging.getLogger('trans_logger')

trans_handler = logging.FileHandler('trans.log')
trans_handler.setLevel(logging.INFO)
trans_log.addHandler(trans_handler)

stripe.api_key = config.StripeConfig.TEST_STRIPE_SECRET_KEY

app = Flask(__name__)

@app.route('/', methods=['POST'])
def charge():

    token = request.form['stripeToken']
    purchase_pref = request.form['purchasePref']

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

    trans_log.info(str(token) + ", " + str(purchase_pref))


if __name__ == '__main__':
    app.run(debug=True)