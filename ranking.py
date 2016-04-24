#!/bin/env python

import sys


def get_score(team_str):
    """
    Get score from partial result string
    :param team_str:
    :return: dict representing team name and score
    """
    last_space = team_str.rfind(" ")
    score = int(team_str[(last_space+1):])
    return score


def get_team_name(team_str):
    """
    Get team name from partial result string
    :param team_str:
    :return: dict representing team name and score
    """
    last_space = team_str.rfind(" ")
    team_name = team_str[:last_space]
    return team_name


def process_result(result):
    """
    Process a line of results
    :param result:
    :return: dict representing point distribution. key is team name, value is the number of points
    """
    if not result:  # cater for files that end with newlines (effectively blank)
        return {}
    partial_results = result.split(", ")
    scores = [get_score(x) for x in partial_results]
    teams = [get_team_name(x) for x in partial_results]
    if scores[0] > scores[1]:
        return {teams[0]: 3, teams[1]: 0}
    elif scores[0] < scores[1]:
        return {teams[0]: 0, teams[1]: 3}
    else:
        return {teams[0]: 1, teams[1]: 1}

def _pluralize(num):
    """
    Optionally pluralize pt/pts
    :param num: number of points
    :return: 'pt' if num is 1, else 'pts'
    """
    if num == 1:
        return "pt"
    else:
        return "pts"


def print_sorted(output_file, results):
    """
    print sorted results to given output file stream
    :param output_file: file pointer to output filestream
    :param results: points dict in {team_name: points} format
    :return: None
    """
    s = sorted(results.items(), key=lambda x: x[0])
    s = sorted(s, key=lambda x: x[1], reverse=True)
    last_points = None
    displayed_position = 0
    logical_position = 0

    for team_name, team_points in s:
        logical_position += 1
        if last_points != team_points:
            displayed_position = logical_position
            last_points = team_points
        output_file.write("{}. {}, {} {}\n".format(displayed_position, team_name, team_points, _pluralize(team_points)))


def rank(input_file=sys.stdin, output_file=sys.stdout):
    """
    Process rankings
    :param input_file: Optional file pointer to input file from; defaults to STDIN
    :param output_file: Optional file pointer to output file; defaults to STDOUT
    :return:
    """
    points = {}
    for line in input_file:
        results = process_result(line.rstrip())  # trim newline character(s)
        for key in results:
                points[key] = points.get(key, 0) + results[key]
    print_sorted(output_file, points)

if __name__ == "__main__":
    rank()
