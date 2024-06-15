def grade(score):
    if score < 50:
        return "F"
    elif score < 60:
        return "D"
    elif score < 70:
        return "C"
    elif score < 80:
        return "B"
    return 'A'

scores = [55, 85, 75, 45, 65]
for i in range(len(scores)):
    g = grade(scores[i])
    print(i+1, scores[i], g)