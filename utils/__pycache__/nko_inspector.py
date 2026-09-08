"""
Masini Barokɛla
N’Ko Challenge — NKO-04

N’Ko Unicode Text Inspector

Purpose:
    Inspect the Unicode structure of N’Ko text.

This module is experimental.
It does NOT modify the V5.3/V5.4 search engine.
"""

import unicodedata

from utils.nko_detector import is_nko_character


def inspect_text(text):
    """
    Return detailed Unicode information for each character.

    Returns:
        list of dictionaries
    """

    results = []

    for char in text:

        if char.isspace():
            continue

        codepoint = ord(char)

        results.append(
            {
                "character": char,
                "codepoint": f"U+{codepoint:04X}",
                "name": unicodedata.name(char, "UNKNOWN"),
                "category": unicodedata.category(char),
                "combining": unicodedata.combining(char),
                "bidirectional": unicodedata.bidirectional(char),
                "is_nko": is_nko_character(char),
            }
        )

    return results


def print_inspection(text):
    """
    Print a human-readable Unicode analysis.
    """

    print()
    print("NKO-04 — N’Ko Unicode Text Inspector")
    print("=" * 60)

    print(f"Text: {text}")
    print(f"Length: {len(text)}")

    print()
    print(
        f"{'Char':^6} "
        f"{'Code':^10} "
        f"{'Category':^10} "
        f"{'Combining':^10} "
        f"{'Bidi':^8} "
        f"{'NKO':^6} "
        f"Unicode Name"
    )

    print("-" * 100)

    for item in inspect_text(text):

        print(
            f"{item['character']:^6} "
            f"{item['codepoint']:^10} "
            f"{item['category']:^10} "
            f"{item['combining']:^10} "
            f"{item['bidirectional']:^8} "
            f"{str(item['is_nko']):^6} "
            f"{item['name']}"
        )


if __name__ == "__main__":

    sample = "ߊߓߊ߫"

    print_inspection(sample)