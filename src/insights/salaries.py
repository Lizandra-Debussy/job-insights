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
    if "min_salary" or "max_salary" not in job:
        raise ValueError
    if type(job["min_salary"]) or type(job["max_salary"]) != int:
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if type(salary) != int:
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
