people_in_the_group = int(input())
number_of_nights = int(input())
number_of_transport_passes = int(input())
number_of_museum_passes = int(input())

price_for_night = 20
transport_pass = 1.60
museum_pass = 6

sum_for_single_person = number_of_nights * price_for_night + number_of_transport_passes * transport_pass + \
                        number_of_museum_passes * museum_pass

sum_for_all_people = sum_for_single_person * people_in_the_group

final_sum = sum_for_all_people * 1.25

print(f"{final_sum:.2f}")