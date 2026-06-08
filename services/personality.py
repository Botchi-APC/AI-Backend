def determine_type(scores):
    social = scores["social"]
    openness = scores["openness"]
    thinking = scores["thinking"]
    planning = scores["planning"]
    stability = scores["stability"]

    avg = sum(scores.values()) / 5
    threshold = 8

    # 전략가형
    if thinking - avg >= threshold and planning - avg >= threshold:
        return "전략가형"

    # 탐험가형
    elif social - avg >= threshold and openness - avg >= threshold:
        return "탐험가형"

    # 분석가형
    elif thinking - avg >= threshold and social < avg:
        return "분석가형"

    # 협력가형
    elif social - avg >= threshold and stability - avg >= threshold:
        return "협력가형"

    # 균형형
    else:
        return "균형형"