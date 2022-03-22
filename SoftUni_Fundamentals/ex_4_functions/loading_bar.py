def loading_bar(num):
    loading_status = f""
    if num == 100:
        print(f"100% Complete!")
        print(f"[%%%%%%%%%%]")
    else:
        percent = (num//10) * "%"
        dots = (10 - (num//10)) * "."
        print(f"{num}% [{percent}{dots}]")
        print('Still loading...')


number = int(input())
loading_bar(number)
