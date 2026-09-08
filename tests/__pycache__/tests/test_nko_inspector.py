from utils.nko_inspector import inspect_text


def test_basic_inspection():

    results = inspect_text("ߊߓߊ")

    assert len(results) == 3

    assert results[0]["codepoint"] == "U+07CA"
    assert results[1]["codepoint"] == "U+07D3"

    assert results[0]["name"] == "NKO LETTER A"
    assert results[1]["name"] == "NKO LETTER BA"

    assert results[0]["is_nko"] is True
    assert results[1]["is_nko"] is True


def test_combining_mark():

    results = inspect_text("ߊ߫")

    assert len(results) == 2

    assert results[0]["codepoint"] == "U+07CA"
    assert results[1]["codepoint"] == "U+07EB"

    assert results[1]["name"] == (
        "NKO COMBINING SHORT HIGH TONE"
    )

    assert results[1]["combining"] != 0


def test_bidirectional_classes():

    results = inspect_text("ߊ߫")

    assert results[0]["bidirectional"] == "R"

    # Combining marks use the Unicode NSM class.
    assert results[1]["bidirectional"] == "NSM"


def test_nko_detection():

    results = inspect_text("ߊߓߊ߫")

    assert all(
        item["is_nko"] is True
        for item in results
    )


def test_latin_text():

    results = inspect_text("Bambara")

    assert all(
        item["is_nko"] is False
        for item in results
    )


if __name__ == "__main__":

    test_basic_inspection()
    test_combining_mark()
    test_bidirectional_classes()
    test_nko_detection()
    test_latin_text()

    print("NKO-04 ALL TESTS PASSED")