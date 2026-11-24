#!/usr/bin/env python3
"""Format a citation for a DOI using the official DOI citation formatter.

The formatter (citation.doi.org, run by DataCite/Crossref) builds the citation
from the publisher's registered metadata, so authors, volume, issue and pages
come from the record rather than from memory.

Usage:
    python3 cite_doi.py 10.1126/science.1260352 --style mla
    python3 cite_doi.py https://doi.org/10.1126/science.1260352 --style apa

Styles: apa, mla, chicago (author-date), harvard, ieee
Output is plain text: add italics (journal / book titles) yourself.
"""
import argparse
import re
import sys
import urllib.parse
import urllib.request

STYLES = {
    "apa": "apa",
    "mla": "modern-language-association",
    "chicago": "chicago-author-date",
    "harvard": "harvard-cite-them-right",
    "ieee": "ieee",
}


def clean(text: str) -> str:
    # Artifacts the formatter sometimes adds when metadata fields are empty.
    text = re.sub(r",?\s*[Ee]dited by\s*,", ",", text)
    # MLA output lists "Crossref" as a second container; drop it and keep the
    # comma that MLA puts before the DOI.
    text = text.replace(". Crossref, ", ", ").replace(" Crossref, ", " ")
    text = re.sub(r"^\[\d+\]\s*", "", text)  # IEEE number; renumber in your list
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("doi")
    p.add_argument("--style", default="apa", choices=sorted(STYLES))
    a = p.parse_args()

    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", a.doi.strip())
    url = "https://citation.doi.org/format?" + urllib.parse.urlencode(
        {"doi": doi, "style": STYLES[a.style], "lang": "en-US"}
    )
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "verisource-cite/1.0"}), timeout=20) as r:
            out = r.read().decode("utf-8", "replace")
    except Exception as e:  # network blocked, DOI not found, etc.
        print(f"ERROR: could not format DOI {doi}: {e}", file=sys.stderr)
        print(f"Fallback: open {url} in a browser or web-fetch tool.", file=sys.stderr)
        return 1
    if not out.strip() or out.lstrip().startswith(("{", "<", "Unknown")):
        print(f"ERROR: formatter returned no citation for {doi}: {out[:200]}", file=sys.stderr)
        return 1
    print(clean(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
