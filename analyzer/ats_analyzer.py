def analyze_ats(data):

    score = 100

    recommendations = []

    if not data["skills"]:
        score -= 15
        recommendations.append(
            "Add technical skills section."
        )

    if len(data["skills"]) < 5:
        score -= 10
        recommendations.append(
            "Include more role-specific keywords."
        )

    if not data["experience"]:
        score -= 20
        recommendations.append(
            "Add internship or project experience."
        )

    if not data["education"]:
        score -= 10
        recommendations.append(
            "Mention education details."
        )

    return {
        "score": score,
        "recommendations": recommendations
    }