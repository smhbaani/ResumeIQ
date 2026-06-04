# analyzer/skill_analyzer.py

from collections import Counter

# ==========================================================
# SKILL DATABASE
# ==========================================================

SKILL_CATEGORIES = {

    "Programming": [
        "python",
        "java",
        "c++",
        "c",
        "javascript",
        "typescript",
        "go",
        "rust"
    ],

    "AI/ML": [
        "tensorflow",
        "pytorch",
        "keras",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "nlp",
        "computer vision",
        "pandas",
        "numpy"
    ],

    "Web Development": [
        "html",
        "css",
        "react",
        "nextjs",
        "node.js",
        "express",
        "flask",
        "django"
    ],

    "Database": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "sqlite"
    ],

    "Cloud & DevOps": [
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "jenkins",
        "terraform"
    ],

    "Tools": [
        "git",
        "github",
        "linux",
        "jira",
        "postman",
        "vscode"
    ]
}

# ==========================================================
# EXTRACT SKILLS
# ==========================================================

def extract_skills(text):
    """
    Extract skills from resume text.
    """

    text = text.lower()

    found_skills = []

    for category, skills in SKILL_CATEGORIES.items():

        for skill in skills:

            if skill.lower() in text:
                found_skills.append(skill)

    return sorted(list(set(found_skills)))

# ==========================================================
# CATEGORIZE SKILLS
# ==========================================================

def categorize_skills(skills):
    """
    Group skills into categories.
    """

    categorized = {}

    for category, skill_list in SKILL_CATEGORIES.items():

        matches = []

        for skill in skills:

            if skill in skill_list:
                matches.append(skill)

        categorized[category] = matches

    return categorized

# ==========================================================
# SKILL DISTRIBUTION
# ==========================================================

def skill_distribution(categorized_skills):
    """
    Count skills per category.
    Useful for Pie Charts.
    """

    distribution = {}

    for category, skills in categorized_skills.items():

        distribution[category] = len(skills)

    return distribution

# ==========================================================
# FREQUENT SKILLS
# ==========================================================

def frequent_skills(text):
    """
    Find most frequently occurring skills.
    Useful for keyword heatmaps.
    """

    text = text.lower()

    counter = Counter()

    for category_skills in SKILL_CATEGORIES.values():

        for skill in category_skills:

            occurrences = text.count(skill)

            if occurrences > 0:
                counter[skill] = occurrences

    return counter.most_common(15)

# ==========================================================
# SKILL MATURITY SCORE
# ==========================================================

def skill_maturity_score(skills):
    """
    Generate a skill profile score.
    """

    total_skills = len(skills)

    if total_skills >= 20:
        return 100

    elif total_skills >= 15:
        return 85

    elif total_skills >= 10:
        return 70

    elif total_skills >= 5:
        return 50

    return 25

# ==========================================================
# SKILL RECOMMENDATIONS
# ==========================================================

def recommend_skills(skills):
    """
    Suggest missing industry-relevant skills.
    """

    recommended = []

    target_skills = [
        "docker",
        "aws",
        "kubernetes",
        "tensorflow",
        "pytorch",
        "sql",
        "git"
    ]

    for skill in target_skills:

        if skill not in skills:
            recommended.append(skill)

    return recommended

# ==========================================================
# COMPLETE ANALYSIS PIPELINE
# ==========================================================

def analyze_skills(text):
    """
    Main function called from app.py
    Returns complete skill intelligence data.
    """

    skills = extract_skills(text)

    categorized = categorize_skills(skills)

    distribution = skill_distribution(categorized)

    frequent = frequent_skills(text)

    maturity_score = skill_maturity_score(skills)

    recommendations = recommend_skills(skills)

    return {
        "skills": skills,
        "categorized": categorized,
        "distribution": distribution,
        "frequent": frequent,
        "maturity_score": maturity_score,
        "recommendations": recommendations
    }


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    sample_text = """
    Experienced AI Engineer skilled in Python,
    TensorFlow, PyTorch, SQL, Git, Docker,
    AWS, React and Machine Learning.
    """

    result = analyze_skills(sample_text)

    from pprint import pprint
    pprint(result)