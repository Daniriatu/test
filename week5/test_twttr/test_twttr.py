import week5.test_twttr.twttr as twttr

def test_shorten():
    assert twttr.shorten("Twitter") == "twttr"
    assert twttr.shorten("apple") == "ppl"
    assert twttr.shorten("greaT") == "grt"
