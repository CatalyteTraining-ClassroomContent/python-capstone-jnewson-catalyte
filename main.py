all_students = [
    "Alice",
    "Bob",
    "Charlie",
]


list_of_submissions = [
    {
        "quizName": "Quiz 1",
        "quizModule": "Math",
        "quizScore": 85,
        "studentId": 101,
        "studentName": "Alice",
        "submissionDate": "2025-09-20",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "Math",
        "quizScore": 92,
        "studentId": 102,
        "studentName": "Bob",
        "submissionDate": "2025-09-20",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "Science",
        "quizScore": 78,
        "studentId": 103,
        "studentName": "Charlie",
        "submissionDate": "2025-09-21",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "Science",
        "quizScore": 88,
        "studentId": 101,
        "studentName": "Alice",
        "submissionDate": "2025-09-21",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "History",
        "quizScore": 90,
        "studentId": 104,
        "studentName": "David",
        "submissionDate": "2025-09-20",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "History",
        "quizScore": 84,
        "studentId": 102,
        "studentName": "Bob",
        "submissionDate": "2025-09-22",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "Math",
        "quizScore": 76,
        "studentId": 105,
        "studentName": "Eve",
        "submissionDate": "2025-09-21",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "Science",
        "quizScore": 95,
        "studentId": 104,
        "studentName": "David",
        "submissionDate": "2025-09-22",
    },
    # Submissions specifically for find_unsubmitted test
    {
        "quizName": "Quiz 1",
        "quizModule": "Math",
        "quizScore": 85,
        "studentId": 101,
        "studentName": "Alice",
        "submissionDate": "2025-09-23",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "Science",
        "quizScore": 78,
        "studentId": 103,
        "studentName": "Charlie",
        "submissionDate": "2025-09-23",
    },
]


def filter_by_date(submissionDate, list_of_submissions):
    """
    filters submission of students quizzes.
    params are date they submitted using list_of_submission dict
    if no results return empty list
    search submissions in dict, if true add to submission list and return that list
    """
    results = []
    for submission in list_of_submissions:
        if submission["submissionDate"] == submissionDate:
            results.append(submission)
    if len(results) > 0:
        return results
    else:
        return []


def filter_by_student_id(studentId, list_of_submissions):
    """
    filter results based on studentid we want to search individual students submissions
    if no results return empty list
    create and return submission list if studentid is correct and they have submitted quizzes
    """
    results = []
    for submission in list_of_submissions:
        if submission["studentId"] == studentid:
            results.append(submission)
    if len(results) > 0:
        return results
    else:
        return []


def find_unsubmitted(date, list_of_student_names, list_of_submission_objects):
    """
    find unsubmitted work using
    params: date, dict, and submission list
    return empty list if no results
    if there are create a list of the unsubmitted with their name and the due date
    """
    results = []

    for student in list_of_student_names:
        submitted = False
        for submission in list_of_submission_objects:
            if (
                submission["studentName"] == student
                and submission["submissionDate"] == date
            ):
                submitted = True
                break
        if not submitted:
            results.append(student)

    return results


def get_average_score(list_of_submission_objects):
    """
    get the average score of all the quizzes
    param: submission list
    start from 0
    add submissions quizscores until finished
    return a average with 1 decimal point
    """
    total = 0
    count = 0

    for submission in list_of_submission_objects:
        total += submission["quizScore"]
        count += 1

    average_score = total / count
    return round(average_score, 1)


def get_average_score_by_module(list_of_submission_objects):
    """
    returns a key for each subject using the subject name
    then gives the average of that course based on student quizscores
    """
    module_scores = {}

    for submission in list_of_submission_objects:
        module_name = submission["quizModule"]
        score = submission["quizScore"]

        if module_name not in module_scores:
            module_scores[module_name] = []
        module_scores[module_name].append(score)

    module_averages = {}
    for module_name, scores in module_scores.items():
        temp_submissions = [{"quizScore": s} for s in scores]
        module_averages[module_name] = get_average_score(temp_submissions)

    return module_averages
