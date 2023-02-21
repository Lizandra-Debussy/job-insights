from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected = {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }

    path = "tests/mocks/brazilians_jobs.csv"

    file_reader = read_brazilian_file(path)[0]
    assert file_reader == expected
