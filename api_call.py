import requests
from team import OwlTeam
from matches import OwlMatch


def request(url):
    return requests.get(url).json()


def get_teams(root_url):

    url = root_url.format("/v2/teams")
    teams = request(url)
    owl_teams = []

    for idx, val in enumerate(teams['data']):
        owl_teams.append(OwlTeam(val['id'], val['name'], val['location'], val['players']))

    return owl_teams


def get_matches(root_url):

    url = root_url.format("/matches")
    matches = request(url)
    owl_matches = []

    for idx, val in enumerate(matches['content']):
        owl_matches.append(OwlMatch(val['id'], val['competitors'], val['scores'], val['games']))

    return owl_matches
