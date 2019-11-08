import requests
from team import OwlTeam


def get_teams(url):

    url = url.format("/v2/teams")
    teams = requests.get(url).json()
    owl_teams = []

    for idx, val in enumerate(teams['data']):
        owl_teams.append(OwlTeam(val['id'], val['name'], val['location'], val['players']))

    return owl_teams
