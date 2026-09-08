from utils.nko_detector import detect_script, is_nko_character


# --------------------------------------------------
# Basic N’Ko detection
# --------------------------------------------------

def test_nko():
    assert detect_script("ߊߓߊ") == "NKO"


def test_nko_letter():
    assert is_nko_character("ߊ") is True


def test_nko_letter_ba():
    assert is_nko_character("ߓ") is True


# --------------------------------------------------
# Unicode Script=Nko range coverage
# --------------------------------------------------

def test_nko_digit():
    assert is_nko_character("߀") is True


def test_nko_tone_mark():
    assert is_nko_character("߫") is True


def test_nko_punctuation():
    assert is_nko_character("߸") is True


def test_nko_currency_symbol():
    assert is_nko_character("߾") is True


# --------------------------------------------------
# Latin detection
# --------------------------------------------------

def test_latin():
    assert detect_script("Bambara") == "LATIN"


def test_french():
    assert detect_script("Quelle est la meilleure période ?") == "LATIN"


# --------------------------------------------------
# Mixed text
# --------------------------------------------------

def test_mixed():
    assert detect_script("Bambara ߊߓߊ") == "MIXED"


# --------------------------------------------------
# Empty / whitespace
# --------------------------------------------------

def test_empty():
    assert detect_script("") == "UNKNOWN"


def test_whitespace():
    assert detect_script("   ") == "UNKNOWN"


# --------------------------------------------------
# Important distinction:
# Arabic comma has Script_Extensions=Nko,
# but Script=Arabic.
#
# Therefore it must NOT be classified as NKO.
# --------------------------------------------------

def test_arabic_comma_not_nko():
    assert is_nko_character("،") is False


# --------------------------------------------------
# Invalid / non-N’Ko characters
# --------------------------------------------------

def test_latin_character_not_nko():
    assert is_nko_character("A") is False


def test_accented_latin_not_nko():
    assert is_nko_character("é") is False


if __name__ == "__main__":
    test_nko()
    test_nko_letter()
    test_nko_letter_ba()
    test_nko_digit()
    test_nko_tone_mark()
    test_nko_punctuation()
    test_nko_currency_symbol()
    test_latin()
    test_french()
    test_mixed()
    test_empty()
    test_whitespace()
    test_arabic_comma_not_nko()
    test_latin_character_not_nko()
    test_accented_latin_not_nko()

    print("NKO-02 ALL TESTS PASSED")