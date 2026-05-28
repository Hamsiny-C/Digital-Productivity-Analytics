def calculate_score(screen_hours, internet_usage):

    score = 100

    if screen_hours > 5:
        score -= 20

    if internet_usage > 500:
        score -= 10

    if score < 0:
        score = 0

    return score