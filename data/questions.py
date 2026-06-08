QUESTIONS = [

# 가중치 기준

# 1.0 : 보조 문항

# 1.1~1.3 : 핵심 성향 측정 문항

# 1.4~1.5 : 대표 지표 또는 역문항

    {

        # 사회성 핵심

        "id": 1,
        "category": "social",
        "text": "새로운 사람과 대화하는 것이 즐겁다.",
        "reverse": False,
        "weight": 1.2

    },

    {

        # 보조
        
        "id": 2,
        "category": "social",
        "text": "모임에서 먼저 대화를 시작하는 편이다.",
        "reverse": False,
        "weight": 1.0
    },

    {

        # 사회성 대표 지표
        
        "id": 3,
        "category": "social",
        "text": "여럿이 함께 있을 때 에너지를 얻는다.",
        "reverse": False,
        "weight": 1.3

    },
    {

        # 상황 의존적

        "id": 4,
        "category": "social",
        "text": "발표나 토론에 적극적으로 참여한다.",
        "reverse": False,
        "weight": 1.0

    },
    {
        
        # 역문항, 내향성 핵심

        "id": 5,
        "category": "social",
        "text": "혼자 있는 시간이 사람들과 함께 있는 시간보다 더 편하다.",
        "reverse": True,
        "weight": 1.5

    },
    {
        
        # 개방성 핵심

        "id": 6,
        "category": "openness",
        "text": "새로운 경험을 하는 것을 좋아한다.",
        "reverse": False,
        "weight": 1.2

    },
    {
        
        # 보조

        "id": 7,
        "category": "openness",
        "text": "익숙한 방법보다 새로운 방법을 시도하는 편이다.",
        "reverse": False,
        "weight": 1.0

    },
    {
        
        # 학습 개방성

        "id": 8,
        "category": "openness",
        "text": "다양한 분야의 지식을 배우는 것이 즐겁다.",
        "reverse": False,
        "weight": 1.1

    },
    {
        
        # 창의성 측정

        "id": 9,
        "category": "openness",
        "text": "창의적인 아이디어를 떠올리는 것을 좋아한다.",
        "reverse": False,
        "weight": 1.3

    },
    {
        
        # 역문항

        "id": 10,
        "category": "openness",
        "text": "변화를 싫어하고 익숙한 환경을 선호한다.",
        "reverse": True,
        "weight": 1.5

    },
    {
        
        # 사고성 핵심

        "id": 11,
        "category": "thinking",
        "text": "문제를 해결할 때 감정보다 논리를 우선한다.",
        "reverse": False,
        "weight": 1.3

    },
    {
        
        # 객관성 측정

        "id": 12,
        "category": "thinking",
        "text": "결정을 내릴 때 객관적인 근거를 중요하게 생각한다.",
        "reverse": False,
        "weight": 1.4

    },

    {
        
        # 데이터 기반 판단

        "id": 13,
        "category": "thinking",
        "text": "토론에서 사실과 데이터를 중시한다.",
        "reverse": False,
        "weight": 1.1

    },
        {
        
        # 원칙 성향

        "id": 14,
        "category": "thinking",
        "text": "규칙과 원칙을 지키는 것이 중요하다고 생각한다.",
        "reverse": False,
        "weight": 1.0

    },

    {
        
        # 역문항

        "id": 15,
        "category": "thinking",
        "text": "사람들의 감정을 고려하여 결정을 바꾸는 경우가 많다.",
        "reverse": True,
        "weight": 1.5

    },

    {
        
        # 계획성 핵심

        "id": 16,
        "category": "planning",
        "text": "일정을 미리 계획하는 것을 좋아한다.",
        "reverse": False,
        "weight": 1.3

    },

    {
        
        # 실행력

        "id": 17,
        "category": "planning",
        "text": "마감일보다 훨씬 전에 일을 끝내려고 한다.",
        "reverse": False,
        "weight": 1.2

    },

    {
        
        # 습관

        "id": 18,
        "category": "planning",
        "text": "할 일을 목록으로 정리하는 편이다.",
        "reverse": False,
        "weight": 1.0

    },

    {
        
        # 계획 의존성

        "id": 19,
        "category": "planning",
        "text": "계획이 바뀌면 불편함을 느낀다.",
        "reverse": False,
        "weight": 1.1

    },

    {
        
        # 역문항

        "id": 20,
        "category": "planning",
        "text": "즉흥적으로 행동하는 것을 즐긴다.",
        "reverse": True,
        "weight": 1.5

    },

    {
        
        # 안정성 핵심

        "id": 21,
        "category": "stability",
        "text": "예상치 못한 문제가 발생해도 침착하게 대응한다.",
        "reverse": False,
        "weight": 1.4

    },

    {
        
        # 회복력

        "id": 22,
        "category": "stability",
        "text": "실수하더라도 오래 신경 쓰지 않는다.",
        "reverse": False,
        "weight": 1.1

    },

    {
        
        # 감정 조절

        "id": 23,
        "category": "stability",
        "text": "스트레스를 받아도 감정 조절이 잘 되는 편이다.",
        "reverse": False,
        "weight": 1.3

    },

    {
        
        # 비판 수용

        "id": 24,
        "category": "stability",
        "text": "비판을 받아도 크게 흔들리지 않는다.",
        "reverse": False,
        "weight": 1.2

    },

    {
        
        # 역문항

        "id": 25,
        "category": "stability",
        "text": "작은 일에도 걱정이 많은 편이다.",
        "reverse": True,
        "weight": 1.5

    },
]
