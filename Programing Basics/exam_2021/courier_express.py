weight_of_pack_kilos = float(input())
type_fo_order = input()
distance_kilometers = int(input())
price = 0
if type_fo_order == "standard":
    if weight_of_pack_kilos < 1:
        price += distance_kilometers * 0.03
    elif weight_of_pack_kilos < 10:
        price += distance_kilometers * 0.05
    elif weight_of_pack_kilos < 40:
        price += distance_kilometers * 0.1
    elif weight_of_pack_kilos < 90:
        price += distance_kilometers * 0.15
    elif weight_of_pack_kilos < 150:
        price += distance_kilometers * 0.2
elif type_fo_order == "express":
    if weight_of_pack_kilos < 1:
        price += distance_kilometers * 0.03
        price = ((price * 0.8) * weight_of_pack_kilos) + price
    elif weight_of_pack_kilos < 10:
        price += distance_kilometers * 0.05
        price = ((price * 0.4) * weight_of_pack_kilos) + price
    elif weight_of_pack_kilos < 40:
        price += distance_kilometers * 0.1
        price = ((price * 0.05) * weight_of_pack_kilos) + price
    elif weight_of_pack_kilos < 90:
        price += distance_kilometers * 0.15
        price = ((price * 0.02) * weight_of_pack_kilos) + price
    elif weight_of_pack_kilos < 150:
        price += distance_kilometers * 0.2
        price = ((price * 0.01) * weight_of_pack_kilos) + price
print(f"The delivery of your shipment with weight of {weight_of_pack_kilos:.3f} kg. would cost {price:.2f} lv.")
