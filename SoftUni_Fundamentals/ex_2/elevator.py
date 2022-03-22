num_of_ppl = int(input())
space_in_elv = int(input())
trips = 1
aditional_trips = num_of_ppl // space_in_elv
if num_of_ppl % space_in_elv == 0:
    trips -= 1

total = trips + aditional_trips
print(total)