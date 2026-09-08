"""
Masini Barokɛla
N’Ko Challenge — NKO-03

Unicode Normalization & N’Ko Text

This experiment does NOT modify the V5.3/V5.4 core.
"""

import unicodedata


# --------------------------------------------------
# 1. Basic N’Ko characters
# --------------------------------------------------

def test_basic_nko_characters():

    text = "ߊߓߊ"

    assert len(text) == 3
    assert all(
        0x07C0 <= ord(char) <= 0x07FF
        for char in text
    )


# --------------------------------------------------
# 2. Unicode normalization
# --------------------------------------------------

def test_nfc_normalization():

    text = "ߊߓߊ"

    normalized = unicodedata.normalize("NFC", text)

    assert normalized == text


def test_nfd_normalization():

    text = "ߊߓߊ"

    normalized = unicodedata.normalize("NFD", text)

    assert normalized == text


# --------------------------------------------------
# 3. N’Ko combining mark
# --------------------------------------------------

def test_nko_combining_mark():

    base = "ߊ"
    tone = "߫"

    text = base + tone

    assert len(text) == 2

    assert "NKO" in unicodedata.name(base)
    assert "NKO" in unicodedata.name(tone)

    assert unicodedata.combining(tone) != 0


# --------------------------------------------------
# 4. Normalization must preserve N’Ko text
# --------------------------------------------------

def test_combining_mark_normalization():

    text = "ߊ߫"

    nfc = unicodedata.normalize("NFC", text)
    nfd = unicodedata.normalize("NFD", text)

    assert nfc == text
    assert nfd == text


# --------------------------------------------------
# 5. Unicode names
# --------------------------------------------------

def test_unicode_names():

    assert unicodedata.name("ߊ") == "NKO LETTER A"
    assert unicodedata.name("ߓ") == "NKO LETTER BA"


# --------------------------------------------------
# 6. Right-to-left property
# --------------------------------------------------

def test_nko_direction():

    text = "ߊߓߊ"

    for char in text:
        assert unicodedata.bidirectional(char) == "R"


# --------------------------------------------------
# 7. N’Ko remains N’Ko after normalization
# --------------------------------------------------

def test_normalized_text_is_still_nko():

    text = "ߊߓߊ߫"

    for form in ("NFC", "NFD", "NFKC", "NFKD"):

        normalized = unicodedata.normalize(form, text)

        for char in normalized:
            if not char.isspace():
                assert 0x07C0 <= ord(char) <= 0x07FF


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    test_basic_nko_characters()
    test_nfc_normalization()
    test_nfd_normalization()
    test_nko_combining_mark()
    test_combining_mark_normalization()
    test_unicode_names()
    test_nko_direction()
    test_normalized_text_is_still_nko()

    print("NKO-03 ALL TESTS PASSED")