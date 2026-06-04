import json

with open("data/job_roles.json", "r") as f:
    JOB_ROLES = json.load(f)


def role_match(resume_skills, role):

    required = JOB_ROLES.get(role, [])

    if not required:
        return 0, ["Role definition not found"]

    matched = []
    missing = []

    for skill in required:

        if skill.lower() in [s.lower() for s in resume_skills]:
            matched.append(skill)

        else:
            missing.append(skill)

    percentage = int(
        len(matched) /
        len(required) * 100
    )

    return percentage, missing