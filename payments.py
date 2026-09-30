"""UPI payment request links, not payment processing."""
from urllib.parse import urlencode
from amounts import money

def make_link(upi, amount, number):
    return "upi://pay?" + urlencode({
        "pa": upi,
        "pn": "Bill receiver",
        "am": money(amount),
        "cu": "INR",
        "tn": "Bill split - person " + str(number),
    })


