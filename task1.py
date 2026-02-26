scores = [72, 85, 90, 60, 88]

def calculate_average(scores):
    return sum(scores) / len(scores)

def classify_performance(avg_score):

    if avg_score >= 85:
        return "Excellent"
    elif avg_score >= 70:
        return "Good"
    elif avg_score >= 50:
        return "Average"
    else:
        return "Poor"

def generate_report(scores):

    average = calculate_average(scores)
    performance = classify_performance(average)

    print("Model Average Score:", average)
    print("Performance Level:", performance)

generate_report(scores)



