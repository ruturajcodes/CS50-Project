from project import trd_name, nat_of_wok, date

def main():
    test_trd_name()
    test_nat_of_wok()
    test_date()

def test_trd_name():
    assert trd_name('JIVANJYOT ELECTRICALS') == 'JIVANJYOT ELECTRICALS'
    assert trd_name('124577') == 'NA'

# def test_trd_name2():
#     with pytest.raises(AssertionError):
#         assert trd_name("124577")


def test_nat_of_wok():
    assert nat_of_wok("Works Contract") == "Works Contract"
    assert nat_of_wok("457777") == "NA"

# def test_nat_of_wok2():
#     with pytest.raises(AssertionError):
#         assert nat_of_wok("457777")


def test_date():
    assert date('2017-07-01') == "Jul 01, 2017"
    assert date("Jul 01") == "NA"
