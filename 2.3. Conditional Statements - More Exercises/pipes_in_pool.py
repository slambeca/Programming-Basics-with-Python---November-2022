volume = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours = float(input())

pipe_one_filled_lts = pipe_one * hours
pipe_two_filled_lts = pipe_two * hours
all_volume = pipe_one_filled_lts + pipe_two_filled_lts
percent_pipe_one = pipe_one_filled_lts / all_volume * 100
percent_pipe_two = pipe_two_filled_lts / all_volume * 100
percent_of_pool_filled = all_volume / volume * 100

if all_volume <= volume:
    print(f"The pool is {percent_of_pool_filled:.2f}% full. Pipe 1: {percent_pipe_one:.2f}%. "
          f"Pipe 2: {percent_pipe_two:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {all_volume - volume:.2f} "
          f"liters.")