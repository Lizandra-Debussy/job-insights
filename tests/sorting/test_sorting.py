from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    # lista de dicionários com detalhes de empregos
    jobs = [
        {
            "title": "Data Analyst",
            "min_salary": 47060,
            "max_salary": 87407,
            "date_posted": "2020-05-06",
        },
        {
            "title": "Data Research Scientists",
            "min_salary": 112235,
            "max_salary": 168045,
            "date_posted": "2020-04-30",
        },
        {
            "title": "Data Engineer",
            "min_salary": 72676,
            "max_salary": 102840,
            "date_posted": "2020-05-01",
        },
    ]

    # testa ordenação por min_salary (crescente)
    sort_by(jobs, "min_salary")
    assert jobs == [
        {
            "title": "Data Analyst",
            "min_salary": 47060,
            "max_salary": 87407,
            "date_posted": "2020-05-06",
        },
        {
            "title": "Data Engineer",
            "min_salary": 72676,
            "max_salary": 102840,
            "date_posted": "2020-05-01",
        },
        {
            "title": "Data Research Scientists",
            "min_salary": 112235,
            "max_salary": 168045,
            "date_posted": "2020-04-30",
        },
    ]

    # testa ordenação por max_salary (decrescente)
    sort_by(jobs, "max_salary")
    assert jobs == [
        {
            "title": "Data Research Scientists",
            "min_salary": 112235,
            "max_salary": 168045,
            "date_posted": "2020-04-30",
        },
        {
            "title": "Data Engineer",
            "min_salary": 72676,
            "max_salary": 102840,
            "date_posted": "2020-05-01",
        },
        {
            "title": "Data Analyst",
            "min_salary": 47060,
            "max_salary": 87407,
            "date_posted": "2020-05-06",
        },
    ]

    # testa ordenação por date_posted (decrescente)
    sort_by(jobs, "date_posted")
    assert jobs == [
        {
            "title": "Data Analyst",
            "min_salary": 47060,
            "max_salary": 87407,
            "date_posted": "2020-05-06",
        },
        {
            "title": "Data Engineer",
            "min_salary": 72676,
            "max_salary": 102840,
            "date_posted": "2020-05-01",
        },
        {
            "title": "Data Research Scientists",
            "min_salary": 112235,
            "max_salary": 168045,
            "date_posted": "2020-04-30",
        },
    ]
