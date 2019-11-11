from api_call import *


def main(url):

    teams = get_teams(url)
    #matches = get_matches(url)



if __name__ == "__main__":
    api_url = "https://api.overwatchleague.com{}"
    main(api_url)
