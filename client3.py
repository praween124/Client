def getDataPoint(quote):
    """ Produce all of the needed values to get=nerate a datapoint """
    """ _________________Update this Function _____"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get ratio of price_a and price_b"""
    """_____________Update this fuction __________"""
    """Also create some unit tests for this function in client_test.py"""
    if(price_b == 0):
        return
    return price_a/price_b


if __name__ == "__main__":
    for _ in range(N):
        quotes = json.loads(urllib2.urlopen(QUERY.function())).read()
        """___________Update to get the ratio________"""
        prices = []
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask%s, price%s)"% (stock, bid_price, ask_price,price))

        print("Ratio %s" % getRatio(prices['ABC'], prices['DEF']))


