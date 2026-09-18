import os
import json
import sys
from utils.duplicate_detector import detect_duplicates

# Force stdout UTF-8 encoding on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

EXPECTED_ROLES = [
    "Python Developer",
    "Java Developer",
    "Full Stack Developer",
    "Data Analyst",
    "Data Scientist",
    "Software Engineer",
    "ML Engineer",
    "Frontend Developer",
    "Backend Developer"
]

ROLE_FILE_MAP = {
    "Python Developer": "python_developer.json",
    "Java Developer": "java_developer.json",
    "Full Stack Developer": "full_stack_developer.json",
    "Data Analyst": "data_analyst.json",
    "Data Scientist": "data_scientist.json",
    "Software Engineer": "software_engineer.json",
    "ML Engineer": "ml_engineer.json",
    "Frontend Developer": "frontend_developer.json",
    "Backend Developer": "backend_developer.json"
}

REQUIRED_FIELDS = [
    "question_id", "role", "round", "category", "difficulty",
    "question", "interviewer_intent", "expected_answer_points",
    "follow_up_question", "evaluation_criteria", "tags"
]

def validate():
    print("Question Bank Validation\n")
    questions_dir = os.path.join("data", "questions")

    if not os.path.exists(questions_dir):
        print(f"FAILED: Directory '{questions_dir}' does not exist.")
        sys.exit(1)

    all_questions = []
    role_counts = {}
    seen_ids = set()
    missing_fields_count = 0

    for role in EXPECTED_ROLES:
        file_name = ROLE_FILE_MAP[role]
        file_path = os.path.join(questions_dir, file_name)

        if not os.path.exists(file_path):
            print(f"{role:<22} [FAIL] Missing file {file_name}")
            role_counts[role] = 0
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            count = len(data)
            role_counts[role] = count
            status_symbol = "[OK]" if count == 90 else "[FAIL]"
            print(f"{role:<22} {status_symbol} {count}")

            for q in data:
                all_questions.append(q)
                q_id = q.get("question_id")
                if q_id:
                    seen_ids.add(q_id)

                for field in REQUIRED_FIELDS:
                    if field not in q or not q[field]:
                        missing_fields_count += 1

        except Exception as e:
            print(f"{role:<22} [FAIL] Error reading file: {e}")
            role_counts[role] = 0

    total_questions = len(all_questions)

    # Detect duplicates using TF-IDF cosine similarity
    duplicates = detect_duplicates(all_questions, threshold=0.92)

    print(f"\nTotal Questions: {total_questions}")
    print(f"Duplicates: {len(duplicates)}")
    print(f"Missing Questions: {810 - total_questions}")

    if total_questions == 810 and len(duplicates) == 0 and missing_fields_count == 0:
        print("\nVALIDATION PASSED [OK]")
    else:
        print("\nVALIDATION FAILED [FAIL]")
        if len(duplicates) > 0:
            print("\nDuplicate items detected:")
            for dup in duplicates[:5]:
                print(f" - [{dup['sim_score']}] {dup['q1_id']} vs {dup['q2_id']}")

if __name__ == "__main__":
    validate()
