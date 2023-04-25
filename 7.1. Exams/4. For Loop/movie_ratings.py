count_movies = int(input())

movie_highest_rating = None
maximum_rating = -10

movie_lowest_rating = None
minimum_rating = 10

average_rating = 0

for _ in range(1, count_movies + 1):
    current_movie = input()
    rating = float(input())
    if rating > maximum_rating:
        maximum_rating = rating
        movie_highest_rating = current_movie
    elif rating < minimum_rating:
        minimum_rating = rating
        movie_lowest_rating = current_movie

    average_rating += rating

average_rating = average_rating / count_movies

print(f"{movie_highest_rating} is with highest rating: {maximum_rating}")
print(f"{movie_lowest_rating} is with lowest rating: {minimum_rating}")
print(f"Average rating: {average_rating:.1f}")