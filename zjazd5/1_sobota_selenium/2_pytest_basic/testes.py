from kod import dodawanie

def test_dodawanie_calkowite():
    assert dodawanie(1, 2) == 3

def test_dodawanie_ulamki():
    assert dodawanie(0.1, 0.2) == 0.3

def test_dodawanie_string():
    assert dodawanie('3', '5') == 8

def test_dodawanie_string2():
    assert dodawanie('3', 'A') == None

def test_dodawanie_string3():
    assert dodawanie('3', 'B') == None

