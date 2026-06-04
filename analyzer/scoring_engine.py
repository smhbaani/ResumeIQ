def calculate_resume_score(data):

    scores = {}

    scores["Contact"] = 15

    scores["Skills"] = min(
        len(data["skills"]) * 3,
        20
    )

    scores["Education"] = 15

    scores["Projects"] = 15

    scores["Experience"] = 20

    scores["ATS"] = 15

    overall = sum(scores.values())

    return overall, scores