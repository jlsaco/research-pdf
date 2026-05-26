# Deep-Research

Turn a source document (PDF, markdown, plain text, …) into a web-researched
markdown bundle, tailored to a **role**, a **language**, and a **depth**.

## How to run it

1. Drop your file into `input/`, e.g. `input/my-deck.pdf`.
2. Launch your runtime of choice and ask for the research in natural
   language, referencing the file:

   **Claude Code**
   ```
   claude
   > do a deep research on input/my-deck.pdf
   ```

   **OpenCode**
   ```
   opencode
   > do a deep research on input/my-deck.pdf
   ```

   The slash command `/deep-research` works in both.

3. The orchestrator **always asks interactively** for the three parameters
   before starting. Confirm with one click or change anything you want.

## Parameters

| Param      | Values                           |
| ---------- | -------------------------------- |
| `role`     | free text (any audience)         |
| `language` | `es` \| `en`                     |
| `depth`    | `quick` \| `standard` \| `deep`  |

You can pre-fill them in the prompt — they'll show up as the recommended
option so confirming is one click:

```
deep research on input/my-deck.pdf for a Project Manager, in English, standard depth
```

**What changes with `depth`:**

- **quick** — fixed sections only; 1 general + 1 specific source per topic.
- **standard** — adds "Why it matters for &lt;role&gt;" and "Common
  pitfalls"; 1 general + 2–3 specific sources.
- **deep** — all optional sections; 1 general + 3–5 specific sources.

## Where the output lands

```
output/<slug>/                  # slug = your filename, lowercased + hyphenated
  README.md                     # index of topics and sections
  topics/<NN>-<slug>.md         # one researched topic per file
  sections/<NN>.md              # one file per source section
  .research/                    # intermediate artifacts
```

Example: `input/My Deck.pdf` → `output/my-deck/`.


## Done criterion

- Every source section is covered.
- Each topic has ≥1 general source plus the specifics required by the
  chosen depth.
- 0 broken links.
- Cited sources actually support the claims.

If the reviewer can't get there within **3 iterations**, the run stops and
documents the remaining gaps in the bundle's `README.md`.
