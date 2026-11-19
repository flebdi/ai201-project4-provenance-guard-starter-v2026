"""
The input gate — capstone extension.

Decides whether a string is writing at all, before either signal is asked to
judge it. Both signals will happily score anything: GPT-2 has a perplexity for
a row of emoji, and stylometry has a sentence-length spread for punctuation.
A number comes out either way, so the only place to say "this isn't something
I can judge" is in front of them.

    from gate import writing_problem
    problem = writing_problem(text)   # None if it's writing, else a reason dict
"""

import re

import config

# A run of letters in any script. [^\W\d_] is "word character that isn't a
# digit or underscore", which in Python's Unicode regex is a letter.
_LETTER_RUN = re.compile(r"[^\W\d_]+")


def measure(text: str) -> dict:
    """The numbers the gate decides on. Logged with every refusal."""
    non_space = [c for c in text if not c.isspace()]
    letters = sum(1 for c in non_space if c.isalpha())
    words = [w for w in _LETTER_RUN.findall(text) if len(w) >= 2]
    return {
        "words": len(words),
        "letter_share": round(letters / len(non_space), 3) if non_space else 0.0,
    }


def writing_problem(text: str) -> dict | None:
    """
    None if `text` looks like writing. Otherwise a dict saying why not, with
    the measurements, so the refusal in the log can be checked by hand.
    """
    m = measure(text)
    if m["words"] < config.GATE_MIN_WORDS:
        why = (f"found {m['words']} word(s); at least "
               f"{config.GATE_MIN_WORDS} are needed")
    elif m["letter_share"] < config.GATE_MIN_LETTER_SHARE:
        why = (f"only {m['letter_share']:.0%} of the characters are letters; "
               f"at least {config.GATE_MIN_LETTER_SHARE:.0%} are needed")
    else:
        return None
    return {"why": why, **m}


if __name__ == "__main__":
    samples = {
        "FP08": "Went for a run. Legs hurt. Worth it.",
        "MF03": "\x00\x01\x02 test \x1b[31mred\x1b[0m",
        "MF04": "!!! ??? ... ,,, ;;; --- ((( )))",
        "MF05": "a" * 160,
        "MF06": "\U0001F600" * 20,
        "MF07": "هذا نص عربي قصير",
    }
    for name, s in samples.items():
        p = writing_problem(s)
        print(f"{name}: {'pass' if p is None else 'REFUSE — ' + p['why']}  {measure(s)}")
