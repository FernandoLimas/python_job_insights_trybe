from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        reader = csv.DictReader(file)
        list_dict = [row for row in reader]
        print(list_dict[0])
        return list_dict
    return []
