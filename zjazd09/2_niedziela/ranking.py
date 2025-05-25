"""
1. Załaduj data/ranking.json
2. Wyłoń zwycięzcę
3. Kto ma najdłuższe imię i nazwisko?
4. Wyłoń podium
"""
import json


"""1. Załaduj data/ranking.json"""
# from pathlib import Path
# json.load(open("data/ranking.json"))
# json.loads(open("data/ranking.json").read())
#
# with open("data/ranking.json") as ranking_file:
#     json.load(ranking_file)
#
# with open("data/ranking.json") as ranking_file:
#     ranking = ranking_file.read()
#     json.loads(ranking)
#
# json.loads(Path("data/ranking.json").read_text())

def load_ranking() -> dict:
    return json.load(open("data/ranking.json"))

"""2. Wyłoń zwycięzcę"""

# def find_winner(ranking: dict):
#     winner_so_far = ""
#     max_points_so_far = 0
#     for name, points in ranking.items():
#         if points > max_points_so_far:
#             max_points_so_far = points
#             winner_so_far = name
#     print(winner_so_far)

# print(max(ranking.items(), key=lambda name_and_points: name_and_points[1])[0])

def find_winner(ranking: dict):
    print(max(ranking, key=lambda name: ranking[name]))


"""3. Kto ma najdłuższe imię i nazwisko?"""
def longest_name(ranking: dict):
    print(max(ranking, key=len))


"""4. Wyłoń podium"""
# def podium(ranking: dict):
#     winner = max(ranking, key=lambda name: ranking[name])
#     winner_item = ranking.pop(winner)
#     second = max(ranking, key=lambda name: ranking[name])
#     second_item = ranking.pop(second)
#     third = max(ranking, key=lambda name: ranking[name])
#     print(winner)
#     print(second)
#     print(third)
#     ranking[winner_item[0]] = winner_item[1]
#     ranking[second_item[0]] = second_item[1]



def podium(ranking: dict):
    sorted_ranking = sorted(ranking, key=lambda name: ranking[name], reverse=True)
    print(sorted_ranking[:3])



def main():
    ranking = load_ranking()
    find_winner(ranking)
    longest_name(ranking)
    podium(ranking)


if __name__ == "__main__":
    main()
