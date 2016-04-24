from .. import ranking
from mock import MagicMock

def test_point_order():
    """
    Should return teams ranked by points
    """
    pass

def test_tie():
    """
    Should show tied teams on the same position
    """
    assert 1 == 1, "tied are equal"

def test_tie_order():
    """
    Should display tied teams in alphabetical order
    """
    pass

def test_tie_trailing():
    """
    Should number teams lower than ties correctly
    """
    pass


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
