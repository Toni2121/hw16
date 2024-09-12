import sqlite_lib

sqlite_lib.connect('hw16.db')

answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT *
	        FROM eurovision_winners
	        WHERE year > 2013
    ''')
print(f"last ten winners: {answer}")


def did_it_win_that_year(input_country: str, input_year: int) -> str:
    song_name: list[tuple] = sqlite_lib.run_query_select(f'''
        SELECT song_name
        FROM song_details s
        JOIN eurovision_winners e ON s.year = e.year
        WHERE LOWER(e.country) = '{input_country.lower()}' AND e.year = {input_year}
    ''')
    if song_name:
        return song_name[0][0]
    else:
        return "wrong"


country = input("Enter country: ")
year = int(input("Enter year: "))
result = did_it_win_that_year(country, year)
print(f"Winning song: {result}")


def did_it_win_that_year(input_country: str, input_year: int) -> str:
    all_songs: list[tuple] = sqlite_lib.run_query_select('''
        SELECT e.country, e.year, e.song_name
        FROM song_details s
        JOIN eurovision_winners e
            ON s.year = e.year
    ''')
    result1 = list(filter(lambda row: row[0].lower() == input_country.lower() and row[1] == input_year, all_songs))
    if result1:
        return result1[0][2]
    else:
        return "wrong"


country = input("Enter country: ")
year = int(input("Enter year: "))
result = did_it_win_that_year(country, year)
print(f"Winning song: {result}")


def genre_change(input_country: str, input_year: int, input_genre: str) -> str:
    result1 = did_it_win_that_year(input_country, input_year)
    if result1 == "wrong":
        return "wrong"
    genre1: list[tuple] = sqlite_lib.run_query_select(f'''
        SELECT s.genre
        FROM song_details s
        JOIN eurovision_winners e ON s.year = e.year
        WHERE LOWER(e.country) = '{input_country.lower()}' AND e.year = {input_year}
    ''')
    if genre1:
        current_genre = genre1[0][0]
        if current_genre.lower() == input_genre.lower():
            return "enter different genre"
        sqlite_lib.run_query_update(f'''
            UPDATE song_details
            SET genre = '{input_genre}'
            WHERE year = {input_year} AND EXISTS (
                SELECT 1 FROM eurovision_winners e
                WHERE LOWER(e.country) = '{input_country.lower()}' AND e.year = song_details.year
            )
        ''')
        return "done"


country = input("Enter country: ")
year = int(input("Enter year: "))
genre = input("Change genre to: ")
result = genre_change(country, year, genre)
print(result)
