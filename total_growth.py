def sum(a):
    s = 0
    for val in a:
        s += float(val)
    return s
def total_growth(stock_amount, stock_growth, bond_amounts, bond_interests, saving_amount, saving_interest):
    growth = 0;
    growth += stock_amount * stock_growth
    for i in range(0, len(bond_amounts)):
        growth += float(bond_amounts[i]) * (float(bond_interests[i])/100)
    growth += (saving_interest/100) * saving_amount;
    return growth/(stock_amount + sum(bond_amounts) + saving_amount) * 100
# print(total_growth(100, .05, [1, 2], [1, 2], 100, 100))
    