---
name: fact-check
description: Anti-hallucination workflow that checks factual claims against credible sources and writes properly formatted citations (APA, MLA, Chicago, Harvard, IEEE). Use this skill whenever an answer depends on facts that could be wrong, such as statistics, dates, names, quotes, laws, scientific or medical claims, historical events, product specs, or "who said/did what". Also use it when the user asks "is this true?", "can you fact-check this?", "find sources for…", "cite your sources", needs a bibliography, works cited or reference list, wants research for a school paper or essay, or pastes text they want verified. Use it even when the user doesn't say "fact-check" but would clearly be hurt by a confident wrong answer.
---

# Fact-Check (verisource)

Language models can produce fluent, confident statements that are simply false: made-up numbers, misattributed quotes, citations to papers that don't exist. This skill slows the answer down long enough to check it. It does three things:

1. **Source credibility:** only rely on sources that hold up to scrutiny, judged the way a librarian or a citation tool would judge them.
2. **Fact validation:** check each important claim against those sources and say plainly how well supported it is.
3. **Proper citations:** cite sources in the user's chosen style (APA, MLA, Chicago, Harvard, IEEE), using only details taken from the source itself.

The goal isn't to look certain. It's to be honest about what is known, what is disputed, and what couldn't be checked.

## Workflow

### 1. Pull out the checkable claims

Before answering (or when reviewing text the user gave you), list the specific claims that could be true or false:

- numbers, statistics, percentages, money amounts
- dates and timelines
- names, titles, roles, who-said-what (quotes are a common hallucination)
- cause-and-effect claims ("X causes Y")
- citations: paper titles, authors, journals, URLs
- superlatives: "first", "largest", "only"

Skip opinions, definitions everyone agrees on, and trivially obvious facts. Spend your effort on claims that matter to the user's question and that you could plausibly get wrong.

### 2. Find sources and judge them

Search for each claim. Open the actual page rather than trusting the search snippet, because snippets get cut off, are out of date, or come from a different page than you think.

Rate every source before you rely on it, using the criteria in `references/source-credibility.md`. Read that file the first time you use this skill in a conversation. In short:

- **Tier 1 (strong):** primary sources and peer-reviewed or official material: government and intergovernmental agencies, peer-reviewed journals, court records, official statistics, the organization's own statement about itself.
- **Tier 2 (good):** established news outlets with editorial standards and corrections policies, university pages, reputable reference works, recognized expert organizations.
- **Tier 3 (use with care):** Wikipedia, trade publications, expert blogs, video from identifiable experts or institutions. Useful for leads and context; follow them back to a stronger source when you can.
- **Don't rely on:** anonymous content, content farms, sites selling the thing they're "reviewing", forums, social media posts, AI-generated pages, sites with no author, date or sourcing.

**About YouTube and other video:** judge the *uploader*, not the platform. A lecture posted by a university, a talk by a named researcher, an official channel of a government agency or company, or a news organization's own channel can be a Tier 2–3 source. A random explainer channel, a reaction video, or a reupload is not. Video should never be the *only* support for an important claim; pair it with a written source where possible.

**When the user names their own source** ("I saw on YouTube…", "my friend sent me this article", "TikTok says…"), check the claim *and* give a sentence or two on how they could judge that source next time. Tie it to what you know: who made it, whether they cite evidence, whether they're selling something. People rarely get taught this, and it's what helps them spot the next false claim without you.

### 3. Validate each claim

For each claim, decide how well it holds up:

- **Corroborate independently.** For anything important, look for at least two sources that are actually independent. Five outlets repeating the same press release or wire story count as one source. Tier 1 primary sources (the official statistic, the paper itself) can stand alone.
- **Match the details, not just the topic.** Check that the source supports the *exact* claim: same number, same year, same units, same population, same wording of the quote. "Roughly 30%" in the source doesn't support "exactly 31.4%".
- **Check the date.** Make sure the information is current enough for the question. Statistics, prices, office-holders and records change.
- **Look for disagreement.** If credible sources conflict, say so and explain which is more authoritative and why, rather than quietly picking one.
- **Check citations exist.** If you cite a paper, book or article, confirm it exists, with the right title, authors and year. Never write a citation or URL you haven't seen. For anything with a DOI, the formatter in step 4 doubles as an existence check: an unknown DOI returns "not found".

### 4. Cite properly

If the user wants citations, a bibliography, or anything for a school or work paper, read `references/citation-styles.md` and follow it. The main points:

- **Pick the style:** the one the user names; otherwise a saved setting (`citation_style: mla` in a `.verisource` file, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` or custom instructions); otherwise ask once for school work, defaulting to APA 7. For casual questions, linked source names are enough.
- **For DOIs, use the formatter** rather than typing the citation from memory: `python3 scripts/cite_doi.py <doi> --style <style>` (path relative to this skill's folder), or web-fetch `https://citation.doi.org/format?doi=<doi>&style=<csl-style>&lang=en-US`.
- **Use only details you saw.** Leave a field out, and tell the user, rather than guessing a page number, date or DOI.

### 5. Label and report

Give the user the answer, with each key claim marked:

- ✅ **Verified:** supported by Tier 1, or by two independent Tier 2 sources.
- ⚠️ **Partly supported / disputed:** weaker sources only, sources disagree, or the details only partly match.
- ❌ **Contradicted:** credible sources say otherwise. Give the corrected fact.
- ❓ **Couldn't verify:** no credible source found. Say this outright; don't fill the gap with a guess dressed up as fact.

Use this format unless the user asked for something else:

```
[Direct answer to the question, written normally]

**Fact check**
| Claim | Status | Source(s) |
|---|---|---|
| ... | ✅ Verified | [Name of source](url) (Tier 1, 2024) |
| ... | ⚠️ Disputed | [Source A](url) says X; [Source B](url) says Y |
| ... | ❓ Couldn't verify | No credible source found |

**Notes:** [anything the user should know: outdated data, conflicts, limits of the search]

**References** *(only when the user needs citations, in their chosen style)*
```

For a short answer with one or two facts, inline citations are enough; you don't need the table. Fit the size of the report to the question. Lead with the answer itself, and keep the explanation tight: the table and notes carry the evidence, so the prose above them doesn't need to repeat it.

## Rules that matter most

- **Never invent sources.** A fake citation is worse than no citation, because it makes a false claim look checked. If you can't find a source, say "I couldn't verify this."
- **Correct yourself.** If checking shows that something you or the user said earlier is wrong, say so clearly.
- **Don't overstate.** "Studies suggest" is not "it is proven". Keep the confidence level of the source.
- **Separate fact from inference.** If you're reasoning beyond what sources say, label it ("my inference:", "likely, but not confirmed").

## When you can't search the web

If no web search or fetch tool is available, don't pretend you checked anything. Answer from your own knowledge, mark every claim **❓ Not checked (from memory)**, point out the claims most likely to be wrong or out of date, and tell the user which sources they could check themselves.
