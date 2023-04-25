period = int(input())

doctors = 7

treated_patients = 0
untreated_patients = 0

for num in range(1, period + 1):
    current_patients = int(input())
    if num % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if current_patients <= doctors:
        treated_patients += current_patients
    elif current_patients > doctors:
        untreated_patients += current_patients - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")