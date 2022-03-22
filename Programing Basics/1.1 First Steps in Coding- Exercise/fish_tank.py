length_in_centimeters = int(input())
width_in_centimeters =  int(input())
height_in_centimeters = int(input())
percent_of_taken_space = float(input())

aquarium_volume = length_in_centimeters * width_in_centimeters * height_in_centimeters
volume_in_leters = aquarium_volume * 0.001
taken_space = percent_of_taken_space * 0.01

requaried_liters = volume_in_leters * (1 - taken_space)
print(requaried_liters)