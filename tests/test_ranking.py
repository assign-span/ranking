from .. import ranking
from mock import call, MagicMock


def test_get_score():
    """
    get_score(): Test extraction of score from partial result b
    """
    res = ranking.get_score("Tigers 5")
    assert res == 5, "Expected score of 5, got {} instead".format(res)

    res = ranking.get_score("Royal 11 0")
    assert res == 0, "Expected score of 0, got {} instead ".format(res)


def test_get_team_name():
    """
    get_team_name():
    """
    res = ranking.get_team_name("Tigers 5")
    assert res == "Tigers", "Expected team name to be 'Tigers', got {} instead".format(res)

    res = ranking.get_team_name("Royal 11 0")
    assert res == "Royal 11", "Expected team name to be 'Royal 11', got {} instead ".format(res)


def test_process_result():
    """
    Test process_result()
    """
    res = ranking.process_result("TeamA 1, TeamB 0")
    assert res == {"TeamA": 3, "TeamB": 0}

    res = ranking.process_result("TeamA 0, TeamB 4")
    assert res == {"TeamA": 0, "TeamB": 3}

    res = ranking.process_result("TeamA 1, TeamB 1")
    assert res == {"TeamA": 1, "TeamB": 1}


def test__pluralize():
    """
    Test _pluralize()
    """
    res = ranking._pluralize(0)
    assert res == "pts", "Expected 0 to be pluralized as 'pts', got {} instead".format(res)

    res = ranking._pluralize(1)
    assert res == "pt", "Expected 1 to be pluralized as 'pt', got {} instead".format(res)

    res = ranking._pluralize(2)
    assert res == "pts", "Expected 2 to be pluralized as 'pt', got {} instead".format(res)


def test_print_sorted():
    # sort by points
    output_file = MagicMock()
    results = {"A": 0, "B": 3}
    ranking.print_sorted(output_file, results)
    expected = [call("1. B, 3 pts\n"), call("2. A, 0 pts\n")]
    assert expected == output_file.write.call_args_list,\
        "Expected {} teams to be equal {} ".format(expected, output_file.write.call_args_list)

    # test tie sorted alphabetically
    output_file.reset_mock()
    results = {"A": 0, "Z": 1, "D": 4, "F": 1}
    ranking.print_sorted(output_file, results)
    expected = [call("1. D, 4 pts\n"), call("2. F, 1 pt\n"), call("2. Z, 1 pt\n"),
                call("4. A, 0 pts\n")]
    assert expected == output_file.write.call_args_list, "Expected {} teams to be equal {} ".format(expected, output_file.write.call_args_list)
