facts = [
    "HighAttendance",
    "ScoresAbove70",
    "CompletedProjects",
    "PassedAllSubjects",
    "GoodCommunication",
]

rules = [
    ("R1", ["HighAttendance", "ScoresAbove70"], "GoodAcademicPerformance"),
    ("R2", ["CompletedProjects", "PassedAllSubjects"], "TechnicallyStrong"),
    ("R3", ["GoodAcademicPerformance", "TechnicallyStrong", "GoodCommunication"], "EligibleForPlacement"),
    ("R4", ["LowTestScores"], "NeedsExtraPractice"),
]


def backward_chain(goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Goal: {goal}")

    if goal in facts:
        print(f"{indent}  -> '{goal}' is a known fact. PROVED")
        return True

    for name, conditions, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}  Trying {name}: IF {' AND '.join(conditions)} THEN {conclusion}")
            if all(backward_chain(c, depth + 2) for c in conditions):
                print(f"{indent}  -> {name} satisfied. '{goal}' PROVED")
                return True
            print(f"{indent}  -> {name} failed")

    print(f"{indent}  -> '{goal}' cannot be proved. FAILED")
    return False


if __name__ == "__main__":
    goal = "EligibleForPlacement"

    print("Known Facts")
    print("-" * 40)
    for f in facts:
        print(f"  {f}")

    print("\nRules")
    print("-" * 40)
    for name, conditions, conclusion in rules:
        print(f"  {name}: IF {' AND '.join(conditions)} THEN {conclusion}")

    print("\nBackward Chaining Reasoning Steps")
    print("-" * 40)
    result = backward_chain(goal)

    print("\nFinal Conclusion")
    print("-" * 40)
    if result:
        print(f"{goal} is TRUE: the student is eligible for placement.")
    else:
        print(f"{goal} is FALSE: the goal could not be proved.")