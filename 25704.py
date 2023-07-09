coupon = int(input())
price = int(input())

result = [price]
if coupon >= 5:
    result.append(price-500)
if coupon >= 10:
    result.append(round(price*9/10))
if coupon >= 15:
    result.append(price-2000)
if coupon >= 20:
    result.append(round(price*3/4))

print(max(min(result),0))
