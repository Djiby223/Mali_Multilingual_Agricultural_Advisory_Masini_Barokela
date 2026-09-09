"""
Masini Barokɛla
N’Ko Challenge — NKO-V5

N’Ko → V5 Adapter

Purpose:
    Provide a stable interface between the experimental N’Ko
    semantic layer and a future Masini V5 mapping layer.

This module is experimental.
It does NOT modify the V5.3/V5.4 production search engine.
"""

from utils.nko_sense_resolver import resolve_senses


def adapt_nko_query(query):
    """
    Adapt an N’Ko query into a stable V5-facing structure.

    The adapter delegates script detection and contextual sense
    resolution to the existing N’Ko experimental modules.

    It does not perform knowledge-base retrieval.

    Returns:
        dict with:
            status
            script
            recognized_forms
            resolved_senses
            concept_ids
    """

    result = resolve_senses(query)

    status = result["status"]
    script = result["script"]

    concept_ids = []

    for sense in result.get("resolved_senses", []):
        concept_id = sense.get("Concept_ID")

        if (
            concept_id
            and concept_id != "NOT_MAPPED"
            and concept_id not in concept_ids
        ):
            concept_ids.append(concept_id)

    if status == "RESOLVED" and not concept_ids:
        status = "NON_AGRICULTURE"

    return {
        "status": status,
        "script": script,
        "recognized_forms": result.get("recognized_forms", []),
        "resolved_senses": result.get("resolved_senses", []),
        "concept_ids": concept_ids,
    }


if __name__ == "__main__":
    examples = [
        "\u07d6\u07cc",
        "\u07d8\u07ce\u07f0\u07de\u07df\u07cf",
        "\u07db\u07cc",
        "\u07db\u07cc seed",
        "\u07db\u07cc hair",
        "\u07ca\u07cb\u07cc",
        "Hello",
    ]

    for query in examples:
        print("=" * 60)
        print(f"Query: {query}")
        print(adapt_nko_query(query))
