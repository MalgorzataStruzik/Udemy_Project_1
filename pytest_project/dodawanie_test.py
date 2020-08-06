import pytest

@pytest.mark.parametrize("składnik, suma",[(5,7),(2,4)])
def test_dodawanie(składnik,suma):
    assert składnik + składnik == suma, "suma dwóch takich samych składników powiinna byc równa " + str(suma)