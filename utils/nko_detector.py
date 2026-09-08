"""
Masini Barokɛla
N’Ko Challenge — NKO-01
N’Ko Script Detector

Purpose:
    Detect whether a text contains N’Ko script characters.

This module is experimental.
It does NOT modify the V5.3/V5.4 search engine.
"""

import unicodedata


def is_nko_character(char):
    """
    Return True if a character belongs to the N’Ko script.

    N’Ko is encoded primarily in Unicode U+07C0–U+07FF.
    """
    codepoint = ord(char)

    return 0x07C0 <= codepoint <= 0x07FF


def detect_script(text):
    """
    Detect the script composition of a text.

    Returns:
        "NKO"
        "LATIN"
        "MIXED"
        "UNKNOWN"
    """

    if not text or not text.strip():
        return "UNKNOWN"

    has_nko = False
    has_latin = False

    for char in text:

        if char.isspace():
            continue

        if is_nko_character(char):
            has_nko = True

        elif "LATIN" in unicodedata.name(char, ""):
            has_latin = True

    if has_nko and has_latin:
        return "MIXED"

    if has_nko:
        return "NKO"

    if has_latin:
        return "LATIN"

    return "UNKNOWN"