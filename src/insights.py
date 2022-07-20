from src.jobs import read


def get_unique_job_types(path):
    reader = read(path)
    list_types = [type["job_type"] for type in reader]
    set_list = set(list_types)
    return set_list


def filter_by_job_type(jobs, job_type):
    list_dict = [li for li in jobs if li["job_type"] == job_type]
    return list_dict


def get_unique_industries(path):
    reader = read(path)
    list_ind = [ind["industry"] for ind in reader if ind["industry"] != ""]
    set_industries = set(list_ind)
    return set_industries


def filter_by_industry(jobs, industry):
    list_dict = [li for li in jobs if li["industry"] == industry]
    return list_dict


def get_max_salary(path):
    r = read(path)
    list_sal = [s["max_salary"].isnumeric() and int(s["max_salary"])for s in r]
    return max(list_sal)


def get_min_salary(path):
    r = read(path)
    list_sal = [int(s["min_salary"]) for s in r if s["min_salary"].isnumeric()]
    return min(list_sal)


def matches_salary_range(job, salary):
    try:
        int(salary)
        if job["min_salary"] <= salary <= job["max_salary"]:
            return True
        if job["min_salary"] > job["max_salary"]:
            raise ValueError
        return False
    except (TypeError, KeyError):
        raise ValueError()


def filter_by_salary_range(jobs, salary):
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
    list_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salary.append(job)
        except ValueError:
            pass
    return list_salary
