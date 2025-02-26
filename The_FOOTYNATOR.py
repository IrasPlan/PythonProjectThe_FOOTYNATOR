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
        {"name": "Karim Benzema", "league": "Saudi Pro League", "team": "Al-Ittihad", "position": "Forward", "age": "37", "nationality": "France"},
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
        {"name": "Nico Williams", "league": "La Liga", "team": "Athletico Bilbao", "position": "Forward", "age": "22", "nationality": "Spain"},
        {"name": "Lamine Yamal", "league": "La Liga", "team": "Barcelona", "position": "Forward", "age": "17", "nationality": "Spain"},
        {"name": "Pau Cubarsi", "league": "La Liga", "team": "Barcelona", "position": "Defender", "age": "18", "nationality": "Spain"},
        {"name": "Ferran Torres", "league": "La Liga", "team": "Barcelona", "position": "Midfielder", "age": "24", "nationality": "Spain"},
        {"name": "Sergio Ramos", "league": "La Liga", "team": "Sevilla", "position": "Defender", "age": "38", "nationality": "Spain"},
        {"name": "Antony", "league": "Premier League", "team": "Manchester United", "position": "Forward", "age": "25", "nationality": "Brazil"},
        {"name": "Jude Bellingham", "league": "La Liga", "team": "Real Madrid", "position": "Midfielder", "age": "21", "nationality": "England"},
        {"name": "Antonio Rüdiger", "league": "La Liga", "team": "Real Madrid", "position": "Defencer", "age": "31", "nationality": "Germany"},
        {"name": "Dani Olmo", "league": "La Liga", "team": "Barcelona", "position": "Midfielder", "age": "26", "nationality": "Spain"},
        {"name": "Dani Carvajal", "league": "La Liga", "team": "Real Madrid", "position": "Defender", "age": "33", "nationality": "Spain"},
        {"name": "Gonzalo Garcia", "league": "La Liga", "team": "Real Madrid", "position": "Forward", "age": "20", "nationality": "Spain"},
    ]

    print("Think of a football player, and I'll try to guess who it is by asking a few questions.")
    print("At any point, type 'exit' to quit the game.")

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
        if answer.lower() == "exit":
            print("Exiting the game.")
            return

        candidates = filter_players(candidates, attribute, answer)

        if not candidates:
            print("No player matches that description. Please try again.")
            return

    if len(candidates) == 1:
        guessed_player = candidates[0]["name"]
        print("The player you are thinking of is:", guessed_player)
        correct = input("Was I correct? (yes/no) ").strip().lower()
        if correct in ("yes", "y"):
            print("Great! Thanks for playing!")
        else:
            correct_name = input("Oh no, what player were you thinking of? ").strip()
            correct_league = input("Which league does he play in? ").strip()
            correct_position = input("What position does he play in? ").strip()
            correct_nationality = input("What is his nationality? ").strip()
            correct_team = input("Which team does he play for? ").strip()
            correct_age = input("How old is he? ").strip()
            print(f"Thanks for letting me know! I'll add {correct_name} to my records")
            print("Thanks for playing!")
            return
    else:
        print("I couldn't guess with certainty. The players that match are:")
        for player in candidates:
            print("- " + player["name"])

if __name__ == "__main__":
    main()