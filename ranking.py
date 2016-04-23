#!/bin/env python

import sys

from pprint import pprint

points = {}


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


def process_line(line):
    """
    Process a line of results
    :param line:
    :return: dict representing point distribution. key is team name, value is the number of points
    """
    if not line:  # cater for files that end with newlines (effectively blank)
        return {}
    partial_results = line.split(", ")
    scores = [get_score(x) for x in partial_results]
    teams = [get_team_name(x) for x in partial_results]
    if (scores[0] > scores[1]):
        return {teams[0]: 3, teams[1]: 0}
    elif (scores[0] < scores[1]):
        return {teams[0]: 0, teams[1]: 3}
    else:
        return {teams[0]: 1, teams[1]: 1}


def rank(input_file=sys.stdin, output_file=sys.stdout):
    """
    Process rankings
    :param input_file: Optional file pointer to input file from; defaults to STDIN
    :param output_file: Optional file pointer to output file; defaults to STDOUT
    :return:
    """
    points = {}
    for line in input_file:
        results = process_line(line.rstrip()) #trim newline character(s)
        for key in results:
                points[key] = points.get(key, 0) + results[key]

    pprint(points)

if __name__ == "__main__":
    rank()
