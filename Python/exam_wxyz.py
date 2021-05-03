def compound(principal, rate, period):
    future=principal*(1+rate)**period
    return(future)

print("final amount = {:.2f}".format(compound(1000, 3.6/100,10)))

x = 'hello world'
x[-1] = '.'