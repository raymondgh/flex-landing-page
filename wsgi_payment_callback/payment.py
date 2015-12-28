from flask import Flask, render_template, request, redirect
import stripe
import logging
import config

app = Flask(__name__)
logging.basicConfig(filename='payment.log', level=logging.DEBUG)

@app.route('/', methods=['POST'])
def charge():

    stripe.api_key = config.StripeConfig.STRIPE_SECRET_KEY
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
        return "success"
    except stripe.error.CardError, e:
        # The card has been declined
        pass

if __name__ == '__main__':

    app.run(debug=True)
