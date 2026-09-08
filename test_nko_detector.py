from utils.nko_detector import detect_script


def test_nko():
    assert detect_script("ߊߓߊ") == "NKO"


def test_latin():
    assert detect_script("Bambara") == "LATIN"


def test_french():
    assert detect_script("Quelle est la meilleure période ?") == "LATIN"


def test_mixed():
    assert detect_script("Bambara ߊߓߊ") == "MIXED"


def test_empty():
    assert detect_script("") == "UNKNOWN"


def test_whitespace():
    assert detect_script("   ") == "UNKNOWN"


if __name__ == "__main__":
    test_nko()
    test_latin()
    test_french()
    test_mixed()
    test_empty()
    test_whitespace()

    print("NKO-01 ALL TESTS PASSED")