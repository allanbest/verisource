# Citation Styles

How to write citations in the style the user wants. Read this whenever the user asks for citations, a bibliography, works cited, references, or names a style.

## Contents
1. Picking the style
2. Getting the details right (the most important part)
3. Templates: APA 7, MLA 9, Chicago 18, Harvard, IEEE
4. Formatting the list

## 1. Picking the style

Use the first of these that applies:

1. **The user named a style** in this conversation ("use MLA", "Chicago footnotes", "IEEE"). Keep using it for the rest of the conversation.
2. **A saved setting.** Look for a line such as `citation_style: mla` in a `.verisource` file in the project, or in the project's `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`, or in the chat's custom instructions.
3. **Context clues.** For a school essay with no style given, ask once: "Which citation style does your teacher want (MLA, APA, Chicago...)?" If the user doesn't know or doesn't care, use **APA 7**. Engineering or computer-science work usually means IEEE; humanities usually means MLA or Chicago.
4. **Casual question, no bibliography needed.** Use plain linked source names (`[NASA](url)`). Don't force a formal style on someone who only asked "is this true?".

Supported style keys: `apa` (APA 7th), `mla` (MLA 9th), `chicago` (Chicago 18th, notes-bibliography by default; `chicago-author-date` on request), `harvard` (Cite Them Right), `ieee`, `links` (informal). If the user asks for another style (Vancouver, AMA, ASA, Turabian...), follow that style's own rules as best you know them, and say that it isn't one of the built-in templates.

## 2. Getting the details right

A citation is a factual claim about a source, so the fact-check rules apply to it too.

- **Use only details you actually saw.** Take author, title, date, publisher, volume, issue, pages and DOI from the page you opened or from a metadata record. Never fill in a missing field from memory. A made-up page range or DOI turns a real source into a fake citation.
- **For anything with a DOI, use the formatter.** It builds the citation from the publisher's registered metadata:
  - With a shell: `python3 <skill-dir>/scripts/cite_doi.py <doi> --style apa|mla|chicago|harvard|ieee`
  - Without a shell, web-fetch `https://citation.doi.org/format?doi=<doi>&style=<csl-style>&lang=en-US`, where `<csl-style>` is `apa`, `modern-language-association`, `chicago-author-date`, `harvard-cite-them-right` or `ieee`.
  - A 404 or "not found" means the DOI doesn't exist. Treat it as a red flag that the paper may not be real.
  - The output is plain text, so add italics yourself. Also fix capitalization: APA and Harvard want article titles in sentence case, while MLA and Chicago want title case. For Chicago notes-bibliography, the formatter only gives author-date, so rearrange it using the template below.
- **Missing pieces.** With no author, start with the title (or the organization if it's the author). With no date, use `n.d.` (APA/Harvard) or leave the date out and add an access date (MLA). Tell the user which fields were missing so they can check.
- **Access dates.** Use today's date for "Accessed" or "Retrieved" when a style asks for one. MLA recommends one for undated web pages. APA uses one only for pages designed to change (e.g. a live dashboard).
- **Cite where you read it.** If you only saw a fact quoted in a news article, cite the news article, or open the original and cite that. Don't cite a study you never opened as if you had read it.

## 3. Templates

`*asterisks*` mark italics. Examples use real sources.

### APA 7th edition

In-text: `(Jambeck et al., 2015)`, `(NASA, 2005)`, or narrative `Jambeck et al. (2015) found...`. Use "et al." for 3+ authors. For two authors: `(Smith & Lee, 2020)`.

| Source | Reference list format |
|---|---|
| Journal article | Author, A. A., Author, B. B., & Author, C. C. (Year). Title of article in sentence case. *Journal Name, Volume*(Issue), pages. https://doi.org/xxxx |
| Web page | Author, A. A., or Organization. (Year, Month Day). *Title of page*. Site Name. URL *(omit the site name if it's the same as the author)* |
| News article | Author, A. A. (Year, Month Day). Title of article. *Newspaper Name*. URL |
| Book | Author, A. A. (Year). *Title of book* (2nd ed.). Publisher. https://doi.org/xxxx *(if any)* |
| Report (organization) | Organization. (Year). *Title of report*. Publisher if different. https://doi.org/xxxx or URL |
| YouTube video | Channel or Person Name. (Year, Month Day). *Title of video* [Video]. YouTube. URL |

Example: Jambeck, J. R., Geyer, R., Wilcox, C., Siegler, T. R., Perryman, M., Andrady, A., Narayan, R., & Law, K. L. (2015). Plastic waste inputs from land into the ocean. *Science, 347*(6223), 768–771. https://doi.org/10.1126/science.1260352

List up to 20 authors. The heading is **References**.

### MLA 9th edition

In-text: `(Jambeck et al. 770)`, author plus page with no comma; leave out the page if there isn't one: `(NASA)`. Use "et al." for 3+ authors.

| Source | Works Cited format |
|---|---|
| Journal article | Last, First, et al. "Title of Article." *Journal Name*, vol. 347, no. 6223, 2015, pp. 768–71, https://doi.org/xxxx. |
| Web page | Last, First. "Title of Page." *Website Name*, Publisher (if different), Day Mon. Year, URL. Accessed Day Mon. Year. |
| News article | Last, First. "Title of Article." *Newspaper Name*, Day Mon. Year, URL. |
| Book | Last, First. *Title of Book*. Publisher, Year. |
| Report (organization) | Organization. *Title of Report*. Publisher, Year, URL. *(If the organization is both author and publisher, start with the title and list it only as publisher.)* |
| YouTube video | "Title of Video." *YouTube*, uploaded by Channel Name, Day Mon. Year, URL. *(Start with the creator's name if it differs from the uploader.)* |

Example: Jambeck, Jenna R., et al. "Plastic Waste Inputs from Land into the Ocean." *Science*, vol. 347, no. 6223, Feb. 2015, pp. 768–71, https://doi.org/10.1126/science.1260352.

Abbreviate months longer than four letters (Jan., Feb., Aug., Sept., Oct., Nov., Dec.). Use title case for titles. The heading is **Works Cited**.

### Chicago 18th edition (notes-bibliography)

Footnote (first citation): `1. Jenna R. Jambeck et al., "Plastic Waste Inputs from Land into the Ocean," *Science* 347, no. 6223 (2015): 770, https://doi.org/10.1126/science.1260352.`
Later short note: `2. Jambeck et al., "Plastic Waste Inputs," 771.`

| Source | Bibliography format |
|---|---|
| Journal article | Last, First, and First Last. "Title of Article." *Journal Name* 347, no. 6223 (2015): 768–71. https://doi.org/xxxx. |
| Web page | Last, First, or Organization. "Title of Page." Site Name. Month Day, Year. URL. |
| News article | Last, First. "Title of Article." *Newspaper Name*, Month Day, Year. URL. |
| Book | Last, First. *Title of Book*. Publisher, Year. |
| YouTube video | Channel Name. "Title of Video." YouTube video, length. Month Day, Year. URL. |

In footnotes, use "et al." for 4+ authors. In the bibliography, list up to six authors; for seven or more, list the first three and then "et al." (18th ed.). The 18th edition no longer requires the place of publication for books. The heading is **Bibliography**.

**Chicago author-date** (on request): bibliography entries put the year right after the author (`Jambeck, Jenna R., Roland Geyer, Chris Wilcox, et al. 2015. "Title." *Science* 347 (6223): 768–71.`), and in-text citations look like `(Jambeck et al. 2015, 770)`.

### Harvard (Cite Them Right)

In-text: `(Jambeck et al., 2015)` or `(Jambeck et al., 2015, p. 770)`.

| Source | Reference list format |
|---|---|
| Journal article | Last, I. et al. (Year) 'Title of article', *Journal Name*, 347(6223), pp. 768–771. Available at: https://doi.org/xxxx. |
| Web page | Last, I. or Organization (Year) *Title of page*. Available at: URL (Accessed: Day Month Year). |
| News article | Last, I. (Year) 'Title of article', *Newspaper Name*, Day Month. Available at: URL (Accessed: Day Month Year). |
| Book | Last, I. (Year) *Title of book*. Edition. Place: Publisher. |
| YouTube video | Channel Name (Year) *Title of video*. Available at: URL (Accessed: Day Month Year). |

Universities use many slightly different Harvard variants. If the user's school has its own guide, follow that. The heading is **Reference list**.

### IEEE

In-text: numbers in square brackets in order of first appearance: `[1]`, `[2], [3]`, `[1]–[4]`. Reuse a source's number each time it's cited.

| Source | Reference list format |
|---|---|
| Journal article | [1] A. B. Last, C. Last, and D. Last, "Title of article," *Abbrev. Journal*, vol. 347, no. 6223, pp. 768–771, Mon. Year, doi: xxxx. |
| Web page | [2] Author or Organization, "Title of page," Site Name. Accessed: Mon. Day, Year. [Online]. Available: URL |
| Book | [3] A. B. Last, *Title of Book*, xth ed. City, Country: Publisher, Year. |
| YouTube video | [4] Channel Name, "Title of video," YouTube. Accessed: Mon. Day, Year. [Online]. Available: URL |

Use "et al." after the first author for 7+ authors. The heading is **References**, listed in number order, not alphabetical.

## 4. Formatting the list

- Sort alphabetically by first author's last name (APA, MLA, Chicago, Harvard); IEEE goes in number order.
- Remind the user to apply a **hanging indent** (and double spacing for MLA/APA papers) in their word processor, because chat can't show it.
- Put the in-text citation right in any sentence you suggest they use, so the in-text citation and the list entry match.
- After the list, briefly mention any entry with a missing or unconfirmed detail.
