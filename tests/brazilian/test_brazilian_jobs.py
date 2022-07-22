from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    header, *tail = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    keys = ["title", "salary", "type"]
    assert all((key in keys) for key in header)
