from src.sorting import sort_by


def jobs_criteria():
    return [
        {"max_salary": 2000, "min_salary": 1000, "date_posted": "2022-01-01"},
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2022-02-02"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2022-03-03"},
    ]


def test_sort_by_criteria():
    jobs = jobs_criteria()
    for criteria in ["min_salary", "max_salary", "date_posted"]:
        sort_by(jobs, criteria)
        if criteria == "min_salary":
            assert jobs[0][criteria] <= jobs[1][criteria]
        else:
            assert jobs[0][criteria] >= jobs[1][criteria]
