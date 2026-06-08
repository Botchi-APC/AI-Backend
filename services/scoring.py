from data.questions import QUESTIONS

def calculate_score(answers):
    scores = {
        "social": 0,
        "openness": 0,
        "thinking": 0,
        "planning": 0,
        "stability": 0
    }

    counts = {
        "social": 0,
        "openness": 0,
        "thinking": 0,
        "planning": 0,
        "stability": 0
    }

    for i, question in enumerate(QUESTIONS):

        if i >= len(answers):
            continue

        answer = answers[i]

        # reverse 처리
        if question["reverse"]:
            answer = 5 - answer

        # weight 적용
        weighted = answer * question["weight"]

        category = question["category"]

        scores[category] += weighted
        counts[category] += question["weight"]

    # 0~100 정규화
    for key in scores:
        scores[key] = round((scores[key] / (counts[key] * 4)) * 100)

    return scores