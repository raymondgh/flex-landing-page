var handler = StripeCheckout.configure({
  key: 'pk_live_zOn9v7b2BQII3NYxpCENGl4W',
  image: '/images/logo_spaced.png',
  locale: 'auto',
  token: function(token) {
    $.post(
            'payment/',
            {stripeToken: token.id, purchasePref: $("#pdf-checkbox").prop('checked')},
            function(){ window.location.replace('/success.html') }
          )
  }
});

$('#customButton').on('click', function(e) {
  // Open Checkout with further options
  handler.open({
    name: 'Leasetogether.com',
    description: 'Leasetogether Preorder',
    amount: 2900
  });
  e.preventDefault();
});

// Close Checkout on page navigation
$(window).on('popstate', function() {
  handler.close();
});