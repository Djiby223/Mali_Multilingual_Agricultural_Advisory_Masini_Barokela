"""
Masini Barokɛla
N’Ko Challenge — NKO-02
Unicode Script=Nko Detector

Purpose:
    Detect whether a character belongs to the Unicode N’Ko script
    using the official Script=Nko ranges stored in:

        data/unicode_nko_ranges.txt

This module is experimental.
It does NOT modify the V5.3/V5.4 search engine.
"""

from pathlib import Path
import unicodedata


# --------------------------------------------------
# Load official Unicode Script=Nko ranges
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NKO_RANGES_FILE = PROJECT_ROOT / "data" / "unicode_nko_ranges.txt"


def _load_nko_ranges():
    """
    Load Unicode Script=Nko ranges from the local data file.

    Supports:
        07C0..07C9
        07F6
    """

    ranges = []

    with open(NKO_RANGES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if ".." in line:
                start, end = line.split("..")
                ranges.append(
                    (int(start, 16), int(end, 16))
                )
            else:
                codepoint = int(line, 16)
                ranges.append(
                    (codepoint, codepoint)
                )

    return ranges


NKO_RANGES = _load_nko_ranges()


# --------------------------------------------------
# Character detection
# --------------------------------------------------

def is_nko_character(char):
    """
    Return True if a character belongs to Unicode Script=Nko.
    """

    if not char or len(char) != 1:
        return False

    codepoint = ord(char)

    for start, end in NKO_RANGES:
        if start <= codepoint <= end:
            return True

    return False


# --------------------------------------------------
# Script detection
# --------------------------------------------------

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