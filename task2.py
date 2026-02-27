def get_valid_score():
    while True:
        user_input = input("Enter a score (0-100) or 'q' to quit: ")

        if user_input.lower() == "q":
            return None

        try:
            score = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue

        return score


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return round(sum(scores) / len(scores), 2)


def classify_performance(avg_score):
    if avg_score >= 90:
        return "Excellent"
    elif avg_score >= 75:
        return "Good"
    else:
        return "Needs Improvement"


scores = []

while True:
    score = get_valid_score()

    if score is None:
        break

    scores.append(score)

if len(scores) == 0:
    print("No scores were entered.")
else:
    average = calculate_average(scores)
    performance = classify_performance(average)

    print("Average score:", average)
    print("Performance:", performance)
    