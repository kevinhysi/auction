def buy_a_car(old_car, new_car, saving, percent_loss):
    month = 0
    total = 0


    while new_car_loss >= old_car_loss:
        old_car_loss = old_car + saving - (percent_loss * 100)
        new_car_loss = new_car - (percent_loss * 100)
        month += 1
        percent_loss += 0.5
        total = new_car_loss - old_car_loss
    return [month, total]


buy_car = buy_a_car(2000, 10000, 1000, 1.5)
print(buy_car)
