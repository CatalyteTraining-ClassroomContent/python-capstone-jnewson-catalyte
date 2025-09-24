from main import (
    
    all_students,
    list_of_submissions,
    filter_by_date,
    filter_by_student_id, 
    find_unsubmitted, 
    get_average_score,
    get_average_score_by_module

)

def test_filter_by_date():  
    results = filter_by_date("2025-09-20", list_of_submissions)
    assert len(results) == 3 

def test_filter_by_student_id():
    results = filter_by_student_id(104, list_of_submissions)
    assert results[0]["studentName"] == "David"

def test_find_unsubmitted():
    all_students = ["Alice", "Bob", "Charlie"]
    test_submissions = [
        {"studentName": "Bob", "quizScore": 90, "submissionDate": "2025-09-23" },
    ]
    results = find_unsubmitted("2025-09-23", all_students, test_submissions)
   
    expected = ["Alice" "Charlie"]
    
    assert results == expected

def test_get_average_score(): 
    test_submissions = [ 
        {"quizName": "Quiz 1", "quizScore": 85, "studentId": 101, "studentName": "Alice"}, 
        {"quizName": "Quiz 2", "quizScore": 84, "studentId":102, "studentName": "Bob" },
        {"quizName": "Quiz 2", "quizScore": 95, "studentId": 104, "studentName": "David"}
         
         
         ]
    results = get_average_score(test_submissions) 
    assert results == 88

def test_get_average_score_by_module(): 
    

