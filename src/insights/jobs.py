from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file)
        list_jobs = list(jobs_reader)
        return list_jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = []
    for row in jobs:
        job_type = row["job_type"]
        if job_type not in job_types:
            job_types.append(job_type)
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_job_type = []
    for row in jobs:
        if row["job_type"] == job_type:
            filter_job_type.append(row)
    return filter_job_type
