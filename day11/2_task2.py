total_hours = int(input("Enter total hours "))
rate = float(input("Enter rate per hour "))
if total_hours <= 40:
    pay = total_hours * rate
else:
    overtime = total_hours - 40
    normal_pay = 40 * rate
    extra_pay = overtime * rate * 1.5
    pay = normal_pay + extra_pay
print("Total pay is", pay)
