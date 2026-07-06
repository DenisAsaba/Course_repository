is_a_member = True
purchase_amount = 130

if is_a_member and purchase_amount > 100:
    print("Discount applies")
else:
    print("No discount")

has_coupon = False
is_vip = True

if has_coupon or is_vip:
    print("Discount applies!")
else:
    print("No discount")

   
    is_locked = True
    if not is_locked:
        print("You can open the door")
    else:
        print("The door is locked.")
    