from city_functionss import get_city_country


def test_city_country():
    """Apakah 'Santiago, Chile' dihasilkan dengan benar?"""
    result = get_city_country("santiago", "chile")
    assert result == "Santiago, Chile"