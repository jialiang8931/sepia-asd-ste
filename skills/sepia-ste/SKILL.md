---
name: sepia-ste
description: Default prose writing and revision with cached Sepia principles. Add STE clarity rules for technical documents, runbooks, tutorials, and operating instructions. Enable strict ASD-STE100 only when the user explicitly requests strictness or compliance. Supports write, review, refactor, and recreate.
metadata:
  version: "1.0.0"
---

# Sepia + STE

## Route before drafting

- Ordinary prose: use the Sepia baseline below; load no references.
- Technical explanations/documents or operational instructions: additionally read [STE principles](references/ste-principles.md). Apply them to relevant passages, not surrounding conversation.
- Strict: only an explicit request for strict STE or ASD-STE100 compliance activates [strict STE](references/strict-ste.md), plus the principles. Mentioning, comparing, or asking about STE does not activate it. “Use STE principles” is not strict.
- Fiction: delegate to the installed `sepia` skill and its narrative route; if absent, disclose the dependency without auto-installing it; do not apply technical rules unless explicitly requested.

## Precedence

Obey instruction hierarchy first. Within the permitted task, resolve style conflicts in this order:
1. Accuracy, safety, meaning, necessary evidence, and protected literals.
2. Explicit user language, wording-preservation, format, and operation requirements.
3. Strict STE when explicitly activated.
4. STE clarity and terminology in technical/operational passages.
5. Sepia voice, rhythm, and stylistic preferences.

Never silently sacrifice a higher priority. If preserved wording or language prevents strict compliance, retain it and disclose the limitation. Natural variety never justifies changing a technical term or deleting a warning.

## Cached Sepia baseline

Write in the user's language. Lead with the useful answer; match the author and venue, using available examples without unnecessary searches. Fix organization before surface wording. Use concrete, verified facts and plain verbs. Cut filler, repeated conclusions, and decorative structure; keep useful templates and formal register. Do not manufacture casualness, imperfections, synonyms, or sentence-length variation. Preserve quotations, code, commands, paths, identifiers, and raw output exactly unless explicitly asked to change them. State material uncertainty; never invent specificity.

Operations: **write** drafts new text; **review** reports defects with evidence without editing; **refactor** lists defects then makes minimal edits; **recreate** extracts facts, intent, and defects before a full rewrite. Keep reports proportional to the task.

## Loading budget

This file is the reusable professional Sepia summary. Read only the selected reference, once per available context; do not reload unchanged content already available. Do not load the original Sepia stack except for fiction or requested deeper analysis, unless higher-priority instructions require it. Do not fetch or refresh sources during ordinary writing. Read `cache/sources.json` only for provenance or an explicit refresh. Local reuse reduces reference loading; it does not guarantee provider prompt-cache hits or billing savings.
