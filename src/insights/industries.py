from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries = []
    for row in jobs:
        industry = row["industry"]
        if industry not in industries and industry:
            industries.append(industry)
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry = []
    for row in jobs:
        if row["industry"] == industry:
            filter_industry.append(row)
    return filter_industry
