import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python",
    "java",
    "c++",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "docker",
    "git",
    "react",
    "node.js",
    "aws",
    "sql"
]


def extract_email(text):
    match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )
    return match.group() if match else "Not Found"


def extract_phone(text):
    match = re.search(
        r'(\+?\d[\d\-\s]{8,15})',
        text
    )
    return match.group() if match else "Not Found"


def extract_skills(text):
    text_lower = text.lower()

    found = []

    for skill in SKILLS_DB:
        if skill.lower() in text_lower:
            found.append(skill)

    return list(set(found))


def extract_education(text):
    education_keywords = [
        "bachelor",
        "master",
        "b.tech",
        "bachelor of engineering",
        "university",
        "college"
    ]

    found = []

    text_lower = text.lower()

    for keyword in education_keywords:
        if keyword in text_lower:
            found.append(keyword)

    return found


def extract_experience(text):
    experience_keywords = [
        "intern",
        "internship",
        "experience",
        "developer",
        "engineer",
        "worked"
    ]

    found = []

    text_lower = text.lower()

    for keyword in experience_keywords:
        if keyword in text_lower:
            found.append(keyword)

    return found


def extract_resume_data(text):

    data = {}

    data["email"] = extract_email(text)
    data["phone"] = extract_phone(text)

    data["skills"] = extract_skills(text)
    data["education"] = extract_education(text)
    data["experience"] = extract_experience(text)

    data["projects"] = []
    data["certifications"] = []

    return data