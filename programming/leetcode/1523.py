SELECT STOCK_NAME, sum(IF( OPERATION = 'Buy', -price, price)) as capital_gain_loss from Stocks group by stock_name
