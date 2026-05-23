# Contributing to MIR Guide

## What this guide covers

MIR Guide maps the people, labs, communities, and events shaping Music Information Retrieval and
the industry that intersects with it. In scope: academic MIR research, industry research that
engages with MIR (audio ML at Spotify, Meta, Sony CSL, etc.), communities where MIR people gather,
and media produced by or for the MIR community.

Out of scope: pure music business content with no research angle, pure music criticism, generic AI
content that happens to mention audio, and one-person projects without an established audience.

## Inclusion criteria

A resource must satisfy all three:

1. **Active** — newsletter published in the last 6 months, meetup held in the last 6 months, lab
   published a paper or released code in the last 2 years.
2. **Working link** — the URL resolves to the resource.
3. **Not already listed** — check the existing `data/*.yaml` files before submitting.

## Two ways to contribute

**Suggest via issue (easiest)**
Open an issue using the "Suggest a resource" template. Fill in all required fields. A maintainer
will review and add the entry to the right YAML file.

**Open a PR**
1. Edit the correct `data/*.yaml` file — one entry per resource, following the existing format.
2. Run `python scripts/build_readme.py --check` locally to validate your entry against the schema.
3. Open a PR using the pull request template checklist.

## Editorial style

- **Length**: 1–2 complete sentences, 400 characters maximum.
- **Tone**: neutral. Lead with what the resource *is*, not why it's great.
- **No marketing copy**: do not use "leading", "best", "world-class", "cutting-edge",
  "pioneering", or similar superlatives.
- **People names**: "Firstname Lastname" — no honorifics or titles.
- **Descriptions** should answer: what is this, and who is it for?

Bad: *"The world's leading MIR research lab, producing groundbreaking work."*
Good: *"Academic research lab at Queen Mary University of London focused on music analysis,
synthesis, and retrieval."*

## Review cadence

Reviews happen weekly to biweekly. There is no SLA — this is a side project. If your PR or issue
sits for more than two weeks without response, feel free to leave a comment.
