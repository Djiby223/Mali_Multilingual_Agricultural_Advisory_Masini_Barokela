from pathlib import Path

p = next(
    x for x in Path("docs").glob("*.md")
    if "Challenge_Architecture_and_Current_Status" in x.name
    and not x.name.endswith(".backup.md")
)

t = p.read_text(encoding="utf-8")

assert "## 4. NKO-V5 Adapter Validation" not in t

t = t.replace(
    "**Current checkpoint:** `98f80f2`",
    "**Current checkpoint:** NKO-V5 adapter validation"
)

t = t.replace(
    "validated through NKO-07A",
    "validated through NKO-V5"
)

lines = [
    "",
    "",
    "---",
    "",
    "## 4. NKO-V5 Adapter Validation",
    "",
    "The experimental NKO-V5 adapter provides a controlled interface between the N’Ko semantic layer and a future Masini Barokɛla V5 integration layer.",
    "",
    "The adapter delegates N’Ko recognition and contextual sense resolution to the experimental N’Ko subsystem, extracts validated agricultural `Concept_ID` values, and returns a stable V5-facing structure containing `status`, `script`, `recognized_forms`, `resolved_senses`, and `concept_ids`.",
    "",
    "The adapter does **not** perform knowledge-base retrieval.",
    "",
    "The adapter does **not** modify the production V5.3/V5.4 search engine.",
    "",
    "### Validation result",
    "",
    "The dedicated NKO-V5 adapter test suite passed:",
    "",
    "**8/8 tests passed**",
    "",
    "The validated cases include:",
    "",
    "- N’Ko water → `RESOLVED` → `AGRI-WATER`",
    "- N’Ko soil → `RESOLVED` → `AGRI-SOIL-EARTH`",
    "- ambiguous seed query → `AMBIGUOUS`",
    "- seed with agricultural context → `RESOLVED` → `AGRI-SEED`",
    "- seed with non-agricultural context → `NON_AGRICULTURE`",
    "- unknown N’Ko input → `NO_LEXICAL_MATCH`",
    "- English input → `NOT_NKO`",
    "- empty input → `NOT_NKO`",
    "",
    "### Full regression validation",
    "",
    "Following NKO-V5 adapter validation, the complete Masini Barokɛla test suite was executed:",
    "",
    "**71/71 tests passed**",
    "",
    "This confirms that the experimental N’Ko adapter currently operates without regression against the existing project test suite.",
    "",
    "---",
    "",
    "## 5. Current Experimental Boundary",
    "",
    "The current architecture remains intentionally isolated:",
    "",
    "```text",
    "N’Ko Input",
    "    |",
    "    v",
    "NKO Detection / Recognition",
    "    |",
    "    v",
    "Sense Resolution",
    "    |",
    "    v",
    "NKO-V5 Adapter",
    "    |",
    "    v",
    "Validated Concept_ID",
    "    |",
    "    v",
    "Future controlled V5 integration",
    "```",
    "",
    "No direct connection to the production V5.3/V5.4 retrieval engine has yet been activated.",
    "",
    "Any future integration should be introduced as a separately tested and reversible stage.",
    "",
    "---",
    "",
    "## 6. Current Checkpoint",
    "",
    "At this stage, the N’Ko experimental subsystem has been validated through the NKO-V5 adapter boundary.",
    "",
    "Current validation status:",
    "",
    "- NKO-01 through NKO-07A: validated",
    "- NKO-V5 adapter: **8/8 tests passed**",
    "- Full project regression: **71/71 tests passed**",
    "- Production V5.3/V5.4: **preserved and isolated**",
    "- Working tree after validation: **clean**",
    "",
    "The next development stage should focus on controlled evaluation of how validated N’Ko agricultural concepts could be mapped to existing Masini Barokɛla knowledge-base concepts, without directly modifying the production search engine.",
]

p.write_text(
    t.rstrip() + "\n" + "\n".join(lines) + "\n",
    encoding="utf-8"
)

print("Target:", p)
print("UTF-8 write: OK")
print("Sections 4-6 restored successfully")