def filter_players(players, attribute, value):
    """
    Filters the list of players based on the given attribute value.
    The comparison is case-insensitive.
    """
    return [player for player in players if player[attribute].lower() == value.lower()]

def main():

    players = [
        {"name": "Lionel Messi", "league": "MLS", "team": "Inter Miami", "position": "Forward", "age": "37", "nationality": "Argentina"},
        {"name": "Cristiano Ronaldo", "league": "Saudi Pro League", "team": "Al Nassr", "position": "Forward", "age": "40", "nationality": "Portugal"},
        {"name": "Neymar Jr", "league": "Brasilian Serie A", "team": "Santos Futebol", "position": "Forward", "age": "33", "nationality": "Brazil"},
        {"name": "Kevin De Bruyne", "league": "Premier League", "team": "Manchester City", "position": "Midfielder", "age": "33", "nationality": "Belgium"},
        {"name": "Luka Modrić", "league": "La Liga", "team": "Real Madrid", "position": "Midfielder", "age": "39", "nationality": "Croatia"},
        {"name": "Kylian Mbappe", "league": "La Liga", "team": "Real Madrid", "position": "Forward", "age": "26", "nationality": "France"},
        {"name": "Mohamed Salah", "league": "Premier League", "team": "Liverpool", "position": "Forward", "age": "32", "nationality": "Egypt"},
        {"name": "Robert Lewandowski", "league": "La Liga", "team": "Barcelona", "position": "Forward", "age": "36", "nationality": "Poland"},
        {"name": "Virgil van Dijk", "league": "Premier League", "team": "Liverpool", "position": "Defender", "age": "33", "nationality": "Netherlands"},
        {"name": "Sergio Ramos", "league": "La Liga", "team": "Sevilla", "position": "Defender", "age": "38", "nationality": "Spain"},
        {"name": "Sadio Mané", "league": "Bundesliga", "team": "Bayern Munich", "position": "Forward", "age": "32", "nationality": "Senegal"},
        {"name": "Karim Benzema	", "league": "Saudi Pro League", "team": "Al-Ittihad", "position": "Forward", "age": "37", "nationality": "France"},
        {"name": "Erling Haaland", "league": "Premier League", "team": "Manchester City", "position": "Forward", "age": "24", "nationality": "Norway"},
        {"name": "Harry Kane", "league": "Bundesliga", "team": "Bayern Munich", "position": "Forward", "age": "31", "nationality": "England"},
        {"name": "Paulo Dybala", "league": "Serie A", "team": "AS Roma", "position": "Forward", "age": "31", "nationality": "Argentina"},
        {"name": "Antoine Griezmann", "league": "La Liga", "team": "Atlético Madrid", "position": "Forward", "age": "33", "nationality": "France"},
        {"name": "N’Golo Kanté", "league": "Premier League", "team": "Chelsea", "position": "Midfielder", "age": "33", "nationality": "France"},
        {"name": "Jan Oblak", "league": "La Liga", "team": "Atlético Madrid", "position": "Goalkeeper", "age": "32", "nationality": "Slovenia"},
        {"name": "Manuel Neuer", "league": "Bundesliga", "team": "Bayern Munich", "position": "Goalkeeper", "age": "38", "nationality": "Germany"},
        {"name": "Marc-André ter Stegen", "league": "La Liga", "team": "Barcelona", "position": "Goalkeeper", "age": "32", "nationality": "Germany"},
        {"name": "Son Heung-min", "league": "Premier League", "team": "Tottenham", "position": "Forward", "age": "32", "nationality": "South Korea"},
        {"name": "Raheem Sterling", "league": "Premier League", "team": "Chelsea", "position": "Forward", "age": "30", "nationality": "England"},
        {"name": "Bernardo Silva", "league": "Premier League", "team": "Manchester City", "position": "Midfielder", "age": "30", "nationality": "Portugal"},
        {"name": "Joshua Kimmich", "league": "Bundesliga", "team": "Bayern Munich", "position": "Midfielder", "age": "30", "nationality": "Germany"},
        {"name": "Alisson Becker", "league": "Premier League", "team": "Liverpool", "position": "Goalkeeper", "age": "32", "nationality": "Brazil"},
        {"name": "Thibaut Courtois", "league": "La Liga", "team": "Real Madrid", "position": "Goalkeeper", "age": "32", "nationality": "Belgium"},
        {"name": "Casemiro", "league": "Premier League", "team": "Manchester United", "position": "Midfielder", "age": "33", "nationality": "Brazil"},
        {"name": "Frenkie de Jong", "league": "Premier League", "team": "Manchester United", "position": "Midfielder", "age": "27", "nationality": "Netherlands"},
        {"name": "Jadon Sancho", "league": "Premier League", "team": "Manchester United", "position": "Winger", "age": "24", "nationality": "England"},
        {"name": "Bruno Fernandes", "league": "Premier League", "team": "Manchester United", "position": "Midfielder", "age": "30", "nationality": "Portugal"},
        {"name": "Romelu Lukaku", "league": "Serie A", "team": "Roma", "position": "Forward", "age": "31", "nationality": "Belgium"},
        {"name": "Luis Suárez", "league": "Brasileiro Série A", "team": "Grêmio", "position": "Forward", "age": "38", "nationality": "Uruguay"},
        {"name": "Thomas Müller", "league": "Bundesliga", "team": "Bayern Munich", "position": "Midfielder", "age": "35", "nationality": "Germany"},
        {"name": "Vinicius Junior", "league": "La Liga", "team": "Real Madrid", "position": "Forward", "age": "24", "nationality": "Brazil"},
        # You can add more players here
    ]

    print("Think of a football player, and I'll try to guess who it is by asking a few questions.")


    candidates = players.copy()


    questions = [
        ("league", "Which league does he play in?"),
        ("position", "What is his position?"),
        ("nationality", "What is his nationality?"),
        ("team", "Which team does he play for?"),
        ("age", "What is his age?")

    ]

    for attribute, question in questions:

        if len(candidates) == 1:
            break

        answer = input(question + " ").strip()
        candidates = filter_players(candidates, attribute, answer)

        if not candidates:
            print("No player matches that description.")
            return

    if len(candidates) == 1:
        print("The player you are thinking of is:", candidates[0]["name"])
    else:
        print("I couldn't guess with certainty. The players that match are:")
        for player in candidates:
            print("- " + player["name"])

if __name__ == "__main__":
    main()