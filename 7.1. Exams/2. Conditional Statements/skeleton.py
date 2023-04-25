control_minutes = int(input())
control_seconds = int(input())
length_of_slide = float(input())
seconds_for_100_mt = int(input())

time_in_seconds = control_minutes * 60 + control_seconds
delay_time = length_of_slide / 120
delay_time_in_seconds = delay_time * 2.5
final_time = (length_of_slide / 100) * seconds_for_100_mt - delay_time_in_seconds

if final_time <= time_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {final_time:.3f}.")
else:
    print(f"No, Marin failed! He was {final_time - time_in_seconds:.3f} second slower.")