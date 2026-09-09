"""
Masini Barokɛla
N’Ko Challenge — NKO-07A

Contextual Sense Resolver

Purpose:
    Resolve ambiguous N’Ko lexical forms using explicit context.

This module is experimental.
It does NOT modify the V5.3/V5.4 production search engine.
"""

from utils.nko_query import recognize_nko_query


# --------------------------------------------------
# Context rules
# --------------------------------------------------

AGRICULTURAL_CONTEXT = {
    "seed",
    "seeds",
    "grain",
    "grains",
    "semence",
    "semences",
    "graine",
    "graines",
    "plant",
    "planting",
    "crop",
    "crops",
    "agriculture",
    "agricultural",
    "farmer",
    "farm",
    "field",
    "cultivation",
    "culture",
}


NON_AGRICULTURAL_CONTEXT = {
    "hair",
    "cheveux",
    "fleece",
    "toison",
    "feather",
    "plume",
}


def normalize_context(text):
    """
    Convert context text into lowercase tokens.
    """

    if not text:
        return set()

    normalized = text.lower()

    # Simple punctuation normalization.
    for punctuation in ",.;:!?()[]{}":
        normalized = normalized.replace(punctuation, " ")

    return set(normalized.split())


def resolve_senses(query):
    """
    Resolve possible senses using explicit contextual rules.

    Returns:
        {
            "script": ...,
            "status": ...,
            "recognized_forms": [...],
            "candidate_senses": [...],
            "resolved_senses": [...]
        }

    Status values:
        NOT_NKO
        NO_LEXICAL_MATCH
        UNAMBIGUOUS
        RESOLVED
        AMBIGUOUS
    """

    result = recognize_nko_query(query)

    script = result["script"]

    if script not in {"NKO", "MIXED"}:
        return {
            "script": script,
            "status": "NOT_NKO",
            "recognized_forms": [],
            "candidate_senses": [],
            "resolved_senses": [],
        }

    if not result["recognized_forms"]:
        return {
            "script": script,
            "status": "NO_LEXICAL_MATCH",
            "recognized_forms": [],
            "candidate_senses": [],
            "resolved_senses": [],
        }

    candidates = result["possible_concepts"]

    context_tokens = normalize_context(query)

    resolved = []

    for candidate in candidates:

        domain = candidate["Domain"]
        meaning = candidate["Meaning"].lower()

        # Agricultural context.
        if domain == "AGRICULTURE":
            if context_tokens & AGRICULTURAL_CONTEXT:
                resolved.append(candidate)
                continue

        # Non-agricultural context.
        if domain == "NON_AGRICULTURE":
            if context_tokens & NON_AGRICULTURAL_CONTEXT:
                resolved.append(candidate)
                continue

    # No contextual evidence.
    if not resolved:
        if len(candidates) == 1:
            return {
                "script": script,
                "status": "UNAMBIGUOUS",
                "recognized_forms": result["recognized_forms"],
                "candidate_senses": candidates,
                "resolved_senses": candidates,
            }

        return {
            "script": script,
            "status": "AMBIGUOUS",
            "recognized_forms": result["recognized_forms"],
            "candidate_senses": candidates,
            "resolved_senses": [],
        }

    # Context resolved exactly one sense.
    if len(resolved) == 1:
        return {
            "script": script,
            "status": "RESOLVED",
            "recognized_forms": result["recognized_forms"],
            "candidate_senses": candidates,
            "resolved_senses": resolved,
        }

    # More than one candidate matched the context.
    return {
        "script": script,
        "status": "AMBIGUOUS",
        "recognized_forms": result["recognized_forms"],
        "candidate_senses": candidates,
        "resolved_senses": resolved,
    }


# --------------------------------------------------
# Demonstration
# --------------------------------------------------

if __name__ == "__main__":

    print("NKO-07A — Contextual Sense Resolver")
    print("=" * 60)

    examples = [
        "ߛߌ",
        "ߛߌ seed",
        "ߛߌ hair",
        "ߖߌ",
        "ߓߊ߲߬ߞߎ",
        "Hello",
    ]

    for query in examples:

        result = resolve_senses(query)

        print()
        print(f"Query: {query}")
        print(f"Script: {result['script']}")
        print(f"Status: {result['status']}")
        print(
            f"Recognized forms: "
            f"{len(result['recognized_forms'])}"
        )
        print(
            f"Candidate senses: "
            f"{len(result['candidate_senses'])}"
        )
        print(
            f"Resolved senses: "
            f"{len(result['resolved_senses'])}"
        )

        for sense in result["resolved_senses"]:
            print(
                f"  -> {sense['Meaning']} "
                f"= {sense['Concept_ID']}"
            )