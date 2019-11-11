from api_call import *
from data_importer import import_data


def main(url):

    teams = get_teams(url)
    import_data(teams)
    #matches = get_matches(url)



if __name__ == "__main__":
    api_url = "https://api.overwatchleague.com{}"
    main(api_url)
