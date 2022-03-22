from math import ceil
movie_name = str(input())
episode_length = int(input())
break_time = int(input())

time_to_eat = break_time * 1/8
time_to_rest = break_time * 1/4

time_left = break_time - (time_to_eat + time_to_rest)
after_movie = time_left - episode_length
if time_left >= episode_length:
    print(f"You have enough time to watch {movie_name} and left with {ceil(after_movie)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(abs(after_movie))} more minutes.")
