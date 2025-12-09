# 9. Цена с налогом и скидкой
# Функция final_price(price, tax_rate=0.2, with_tax=True, discount=0, apply_discount=False)
# Если with_tax=True → добавляет к price налог tax_rate.
# Если apply_discount=True → уменьшает цену на discount процентов.
# Продумай порядок: что сначала применять — налог или скидку (запиши в условии комментарий).

def final_price(price, tax_rate=0.2, with_tax=True, discount=0, apply_discount=False):
    if apply_discount:
        price = price - price * discount / 100
    if with_tax:
        price = price + price * tax_rate

    return price

print(final_price(150, 0.4, True, 25, True))
