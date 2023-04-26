actor = input()
starting_points = float(input())
count_judges = int(input())

total_points = starting_points

for _ in range(1, count_judges + 1):
    judge_name = input()
    judge_points = float(input())

    current_points = (len(judge_name) * judge_points) / 2
    total_points += current_points

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {abs(total_points - 1250.5):.1f} more!")