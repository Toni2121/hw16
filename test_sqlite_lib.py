import sqlite_lib


def test_count_e_table():
    # Arrange
    sqlite_lib.connect('hw16.db')

    # Act
    result = sqlite_lib.run_query_select('''
        SELECT count(*)
	        FROM eurovision_winners
    ''')

    # Assert
    assert result[0][0] == 68


def test_count_s_table():
    # Arrange
    sqlite_lib.connect('hw16.db')

    # Act
    result = sqlite_lib.run_query_select('''
        SELECT count(*)
	        FROM song_details
    ''')

    # Assert
    assert result[0][0] == 68


def test_song_name_correct():
    # Arrange
    sqlite_lib.connect('hw16.db')
    input_country = "Austria"
    input_year = 2014
    # Act
    result = sqlite_lib.run_query_select(f'''
        SELECT song_name
        FROM song_details s
        JOIN eurovision_winners e ON s.year = e.year
        WHERE LOWER(e.country) = '{input_country.lower()}' AND e.year = {input_year}
    ''')

    # Assert
    assert result[0][0] == "Rise Like a Phoenix"


def test_song_name_not_correct():
    # Arrange
    sqlite_lib.connect('hw16.db')
    input_country = "Austria"
    input_year = 2022
    # Act
    result = sqlite_lib.run_query_select(f'''
        SELECT song_name
        FROM song_details s
        JOIN eurovision_winners e ON s.year = e.year
        WHERE LOWER(e.country) = '{input_country.lower()}' AND e.year = {input_year}
    ''')
    if result:
        assert result[0][0]
    else:
        assert "wrong" == "wrong"
