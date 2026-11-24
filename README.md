<p align="center"><img src="assets/icon.svg" width="72" alt=""></p>

# Verisource

**Fact-checking and proper citations for AI assistants.** Verisource is an agent skill that makes Claude, ChatGPT/Codex, Gemini and Antigravity check claims against credible sources before stating them, and cite those sources in the style you need.

- 🔎 **Source credibility.** Sources are rated in tiers: government data and peer-reviewed research first, content farms and anonymous pages never. YouTube is judged by who uploaded the video, not by the platform.
- ✅ **Fact validation.** Each claim is labelled ✅ verified, ⚠️ disputed, ❌ contradicted, or ❓ couldn't verify, with links. Important claims need two independent sources, and five sites copying one press release count as one.
- 📚 **Real citations.** APA 7, MLA 9, Chicago 18, Harvard and IEEE. Citations for papers with a DOI are built from the official DOI record, so authors, volume and pages aren't made up. A fake DOI gets caught.
- 🚫 **No invented sources.** If something can't be verified, it says so.

> Verisource **reduces** hallucinations and makes unverified claims visible. It doesn't eliminate them, so check anything important yourself.

## Install

### Coding agents (full version, including the DOI citation script)

| App | Install |
|---|---|
| **Claude Code** | `/plugin marketplace add allanbest/verisource` then `/plugin install verisource@verisource` |
| **Claude Cowork** | Customize → Plugins → Add marketplace → `allanbest/verisource` |
| **Codex** (CLI / IDE / app) | `codex plugin marketplace add allanbest/verisource` then `codex plugin add verisource@verisource` |
| **Antigravity** | `agy plugin install https://github.com/allanbest/verisource` |
| **Gemini CLI** | `gemini extensions install https://github.com/allanbest/verisource` |

Any other tool that reads `.agents/skills/` or `~/.agents/skills/` can use it too: copy `skills/fact-check/` there.

### Chat apps

Download the zips from the [latest release](https://github.com/allanbest/verisource/releases/latest), or build them yourself with `./scripts/build-zips.sh`.

| App | How |
|---|---|
| **Claude.ai** | Customize → Skills → upload `verisource-claude.zip` (needs code execution turned on) |
| **Gemini app** | Customize → Skills → Create → upload `verisource-gemini.zip` |
| **ChatGPT** (plans with Skills) | Plugins → Skills → Create → upload `verisource-claude.zip` |
| **ChatGPT custom GPT / any chatbot** | Paste [`chat/instructions.md`](chat/instructions.md) into the instructions box (it's under 8,000 characters). Optionally attach [`citation-styles.md`](skills/fact-check/references/citation-styles.md) and [`source-credibility.md`](skills/fact-check/references/source-credibility.md) as knowledge files. Also works in Claude Projects and as custom instructions. |

## Choosing a citation style

Just say it: *"use MLA"*, *"Chicago footnotes"*, *"IEEE please"*. To make a style the default, add this line to a `.verisource` file in your project, or to your `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` or chat custom instructions:

```
citation_style: mla
```

Options: `apa`, `mla`, `chicago`, `chicago-author-date`, `harvard`, `ieee`, `links`. If no style is set, it asks you once for school work, then uses APA 7.

## Example

> **You:** i saw a youtube video saying humans only use 10% of their brain. is this true??
>
> **Claude:** No, it's a well-known myth… *(followed by a fact-check table citing MIT McGovern Institute, Scientific American and the British Psychological Society, plus tips for judging that kind of video next time)*

## How it was tested

The [evals](evals/fact-check) folder has 5 test cases: a homework paragraph with planted myths, a citable statistic for an essay, a YouTube claim, an MLA works cited request, and a fabricated citation. Each was run with and without the skill:

| | With Verisource | Without |
|---|---|---|
| Checks passed | **25 / 25** | 21 / 25 |
| Answers that searched and linked sources | 5 / 5 | 3 / 5 |
| Average time | ~3.3 min | ~40 s |

The skill's main gain is that it always checks and always shows its sources. Without it, the model often answers from memory with no links. The cost is time.

## Repo layout

```
skills/fact-check/            the skill (same folder for every platform)
  SKILL.md                    instructions
  references/                 source-credibility + citation-style guides
  scripts/cite_doi.py         DOI → formatted citation (APA/MLA/Chicago/Harvard/IEEE)
chat/instructions.md          paste-in version for chatbots without skill support
.claude-plugin/               Claude Code + Cowork plugin and marketplace
.codex-plugin/, .agents/      Codex plugin and marketplace
plugin.json                   portable Agent Plugins manifest (Antigravity, Codex)
gemini-extension.json         Gemini CLI extension
evals/                        test cases
scripts/build-zips.sh         builds the chat-app zips into dist/
```

## License

[MIT](LICENSE)
