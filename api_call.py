import requests
from classes.team import OwlTeam
from classes.matches import OwlMatch
from classes.player import OwlPlayer


def request(url):
    return requests.get(url).json()


def get_teams(root_url):

    url = root_url.format("/v2/teams")
    teams = request(url)
    owl_teams = []

    for idx, val in enumerate(teams['data']):

        player_handles = []
        for index, value in enumerate(val['players']):
            if 'name' in value:
                player_handles.append(value['name'])

        owl_teams.append(OwlTeam(id=val['id'], name=val['name'], location=val['location'], players=player_handles))

    return owl_teams


def get_players(root_url):

    url = root_url.format("/stats/players")
    players = request(url)
    owl_players = []

    for idx, val in enumerate(players['data']):
        owl_players.append(OwlPlayer(id=val['playerId'], team_id=val['teamId'], role=val['role'], name=val['name'],
                                     team=val['team'], avg_elim_per10m=val['eliminations_avg_per_10m'], avg_death_per10m
                                     =val['deaths_avg_per_10m'], avg_herodmg_per10m=val['hero_damage_avg_per_10m'],
                                     avg_heals_per10m=val['healing_avg_per_10m'], avg_ult_per10m=
                                     val['ultimates_earned_avg_per_10m'], avg_final_blow_per10m=
                                     val['final_blows_avg_per_10m']))

    return owl_players


def get_matches(root_url):

    url = root_url.format("/matches")
    matches = request(url)
    owl_matches = []

    for idx, val in enumerate(matches['content']):
        owl_matches.append(OwlMatch(val['id'], val['competitors'], val['scores'], val['games']))

    return owl_matches
