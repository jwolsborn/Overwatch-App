from api_call import *


def main():

    url = "https://api.overwatchleague.com{}"
    teams = get_teams(url)
    matches = get_matches(url)

if __name__ == "__main__":
    main()
