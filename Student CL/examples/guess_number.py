import random

inclusive_range = (1, 100)

print("Guess my target number that is between %i and %i (inclusive).\n" % inclusive_range)
@@ begin question get_random_number
@@ points: 10
@@ time: 1 minute

@@ end question

answer, i = None, 0

while answer != target:
    i += 1
    answer = input("Your guess(%i): " % i)
    try:
@@ begin question convert_to_int
@@ points: 10
@@ time: 1 minute

@@ end question
    except ValueError:
        print("  I don't understand your input of '%s' ?" % answer)
        continue
@@ begin question detect_number_out_of_range
@@ points: 10
@@ time: 1 minute

@@ end question
        print("  Out of range!")
        continue
@@ begin question detect_correct_guess
@@ points: 10
@@ time: 1 minute

@@ end question
        print("  Ye-Haw!!")
        break
    if answer < target: print("  Too low.")
    if answer > target: print("  Too high.")

print("\nThanks for playing.")
