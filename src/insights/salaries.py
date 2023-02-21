from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = []

    for row in jobs:
        salary = row["max_salary"]
        if salary.isnumeric():
            max_salary.append(int(salary))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = []

    for row in jobs:
        salary = row["min_salary"]
        if salary.isnumeric():
            min_salary.append(int(salary))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("value doesn't exists")

    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError("min_salary, max_salary or salary is invalid")

    if min_salary > max_salary:
        raise ValueError("min_salary cannot be greater than max_salary")

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salaries.append(job)
        except ValueError as error:
            print(error)

    return filtered_salaries
