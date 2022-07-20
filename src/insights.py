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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
    return []
