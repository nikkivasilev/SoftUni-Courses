def water_overflow(flows):
    space_left = 255
    for _ in range(flows):
        current_flow = int(input())
        if current_flow <= space_left:
            space_left -= current_flow
        else:
            print("Insufficient capacity!")
    print(255 - space_left)


flows = int(input())
water_overflow(flows)
