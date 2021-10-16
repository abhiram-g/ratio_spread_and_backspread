import plot_graph

# Get input
data = {}
def get_input():
    print('Choose an option from below. Press')
    print('1. Call ratio spread')
    print('2. Put ratio spread')
    print('3. Call ratio backspread')
    print('4. Put ratio backspread')
    data = {}
    while True:
        data['type'] = input('Enter your choice: ')
        if data['type'] in '1234':
            break
        else:
            print('Invalid option, please select between 1 and 4.')


    data['cmp'] = float(input('Enter the CMP of the stock/index: '))
    data['lot_size'] = int(input('Enter the lot size: '))

    data['itm_price'] = float(input('Enter the ITM option price: '))
    data['itm_strike'] = float(input('Enter the ITM option strike price: '))

    data['otm1_price'] = float(input('Enter the first OTM option price: '))
    data['otm1_strike'] = float(input('Enter the first OTM option strike price: '))
    data['otm2_price'] = float(input('Enter the second OTM option price: '))
    data['otm2_strike'] = float(input('Enter the second OTM option strike price: '))
    return data

data = get_input()
# print(data)

# Validate data
while True:
    if data['type'] in '12':
        if data['otm1_price'] + data['otm2_price'] <= data['itm_price']:
            print('Make sure you sell OTM calls at higher price than you buy an ITM call! Retry again')
            data = get_input()
        else:
            break
    else:
        if data['otm1_price'] + data['otm2_price'] >= data['itm_price']:
            print('Make sure you sell ITM call at higher price than you buy OTM calls! Retry again')
            data = get_input()
        else:
            break
            

# Define methods for each technique and select the method according to the user's input
def call_spread(data, closing_price):
    base_profit = (data['otm1_price'] + data['otm2_price'] - data['itm_price']) * data['lot_size']

    if data['otm1_strike'] == data['otm2_strike']:
        same_otm = True
    else:
        same_otm = False
        if data['otm1_strike'] > data['otm2_strike']:
            data['otm1_strike'], data['otm2_strike'] = data['otm2_strike'], data['otm1_strike']
            data['otm1_price'], data['otm2_price'] = data['otm2_price'], data['otm1_price']

    
    if closing_price <= data['itm_strike']:
        return base_profit
    elif same_otm and closing_price <= data['otm1_strike']:
        return base_profit + (closing_price - data['itm_strike']) * data['lot_size']
    elif not same_otm and closing_price <= data['otm1_strike']:
        return base_profit + (closing_price - data['itm_strike']) * data['lot_size']
    elif not same_otm and closing_price <= data['otm2_strike']:
        return base_profit + (data['otm1_strike'] - data['itm_strike']) * data['lot_size']
    else:
        return base_profit + (data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'] - closing_price) * data['lot_size']
    

def put_spread(data, closing_price):
    base_profit = (data['otm1_price'] + data['otm2_price'] - data['itm_price']) * data['lot_size']

    if data['otm1_strike'] == data['otm2_strike']:
        same_otm = True
    else:
        same_otm = False
        if data['otm1_strike'] < data['otm2_strike']:
            data['otm1_strike'], data['otm2_strike'] = data['otm2_strike'], data['otm1_strike']
            data['otm1_price'], data['otm2_price'] = data['otm2_price'], data['otm1_price']

    
    if closing_price >= data['itm_strike']:
        return base_profit
    elif same_otm and closing_price >= data['otm1_strike']:
        return base_profit + (data['itm_strike'] - closing_price) * data['lot_size']
    elif not same_otm and closing_price >= data['otm1_strike']:
        return base_profit + (data['itm_strike'] - closing_price) * data['lot_size']
    elif not same_otm and closing_price >= data['otm2_strike']:
        return base_profit + (data['itm_strike'] - data['otm1_strike']) * data['lot_size']
    else:
        return base_profit + (data['itm_strike'] + closing_price - data['otm1_strike'] - data['otm2_strike']) * data['lot_size']
    

def call_backspread(data, closing_price):
    base_profit = (data['itm_price'] - data['otm1_price'] - data['otm2_price']) * data['lot_size']

    if data['otm1_strike'] == data['otm2_strike']:
        same_otm = True
    else:
        same_otm = False
        if data['otm1_strike'] > data['otm2_strike']:
            data['otm1_strike'], data['otm2_strike'] = data['otm2_strike'], data['otm1_strike']
            data['otm1_price'], data['otm2_price'] = data['otm2_price'], data['otm1_price']

    
    if closing_price <= data['itm_strike']:
        return base_profit
    elif same_otm and closing_price <= data['otm1_strike']:
        return base_profit + (data['itm_strike'] - closing_price) * data['lot_size']
    elif not same_otm and closing_price <= data['otm1_strike']:
        return base_profit + (data['itm_strike'] - closing_price) * data['lot_size']
    elif not same_otm and closing_price <= data['otm2_strike']:
        return base_profit + (data['itm_strike'] - data['otm1_strike']) * data['lot_size']
    else:
        return base_profit + (data['itm_strike'] + closing_price - data['otm1_strike'] - data['otm2_strike']) * data['lot_size']
    

def put_backspread(data, closing_price):
    base_profit = (data['itm_price'] - data['otm1_price'] - data['otm2_price']) * data['lot_size']

    if data['otm1_strike'] == data['otm2_strike']:
        same_otm = True
    else:
        same_otm = False
        if data['otm1_strike'] < data['otm2_strike']:
            data['otm1_strike'], data['otm2_strike'] = data['otm2_strike'], data['otm1_strike']
            data['otm1_price'], data['otm2_price'] = data['otm2_price'], data['otm1_price']

    
    if closing_price >= data['itm_strike']:
        return base_profit
    elif same_otm and closing_price >= data['otm1_strike']:
        return base_profit + (closing_price - data['itm_strike']) * data['lot_size']
    elif not same_otm and closing_price >= data['otm1_strike']:
        return base_profit + (closing_price - data['itm_strike']) * data['lot_size']
    elif not same_otm and closing_price >= data['otm2_strike']:
        return base_profit + (data['otm1_strike'] - data['itm_strike']) * data['lot_size']
    else:
        return base_profit + (data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'] - closing_price) * data['lot_size']
    

if data['type'] == '1':
    base_profit = (data['otm1_price'] + data['otm2_price'] - data['itm_price']) * data['lot_size']
    breakeven = [round((base_profit/data['lot_size']) + data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'])]
    func = call_spread
elif data['type'] == '2':
    base_profit = (data['otm1_price'] + data['otm2_price'] - data['itm_price']) * data['lot_size']
    breakeven = [round(data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'] - (base_profit/data['lot_size']))]
    func = put_spread
elif data['type'] == '3':
    base_profit = (data['itm_price'] - data['otm1_price'] - data['otm2_price']) * data['lot_size']
    breakeven = [(base_profit/data['lot_size']) + data['itm_strike']]
    if (data['otm1_strike'] - data['itm_strike']) * data['lot_size'] > base_profit:
        breakeven.append(round(data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'] - (base_profit/data['lot_size'])))
    func = call_backspread
else:
    base_profit = (data['itm_price'] - data['otm1_price'] - data['otm2_price']) * data['lot_size']
    breakeven = [data['itm_strike'] - (base_profit/data['lot_size'])]
    if (data['itm_strike'] - data['otm1_strike']) * data['lot_size'] > base_profit:
        breakeven.append(round(data['otm1_strike'] + data['otm2_strike'] - data['itm_strike'] + (base_profit/data['lot_size'])))
    func = put_backspread

# Process data
x = list(range(int(0.4*data['cmp']), int(2*data['cmp'])))

y = [func(data, closing_price) for closing_price in x]

# Plot data
strike_price_xy = [[data['itm_strike'], data['otm1_strike'], data['otm2_strike']], [func(data, data['itm_strike']), func(data, data['otm1_strike']), func(data, data['otm2_strike'])]]
cmp_xy = [[data['cmp']], [func(data, data['cmp'])]]
breakeven_xy = [breakeven, [func(data, br) for br in breakeven]]

plot_graph.plot(x, y, strike_price_xy, cmp_xy, breakeven_xy, data['type'])
