def generate_swot(data):

    strengths = []
    weaknesses = []
    opportunities = []
    threats = []

    if len(data["skills"]) > 8:
        strengths.append(
            "Strong technical profile"
        )

    if data["experience"]:
        strengths.append(
            "Experience available"
        )

    if len(data["skills"]) < 5:
        weaknesses.append(
            "Limited technical stack"
        )

    opportunities.append(
        "Add certifications"
    )

    opportunities.append(
        "Improve ATS optimization"
    )

    threats.append(
        "Competitive AI hiring market"
    )

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "opportunities": opportunities,
        "threats": threats
    }