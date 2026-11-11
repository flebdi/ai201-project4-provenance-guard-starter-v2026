"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

import csv
from pathlib import Path

_ATTACKS = Path(__file__).parent / "attack_set" / "attacks.csv"


def _staff_human(*ids):
    """Genuine human texts from the staff attack set, read verbatim by id."""
    with _ATTACKS.open(encoding="utf-8") as f:
        rows = {r["id"]: r["text"] for r in csv.DictReader(f)}
    return [rows[i] for i in ids]


# ── Criterion 2's material: unedited AI text ─────────────────────────────────
# Written by Claude (Opus 5.5) for this test, each as a plain answer to
# "Write a paragraph about <topic>", with no editing and no tuning toward or
# away from this detector. Criterion 2 says "from ChatGPT or Claude, with a
# plain prompt like 'write a paragraph about X'".
AI_PARAGRAPHS = [
    # Write a paragraph about the benefits of regular exercise.
    "Regular exercise offers a wide range of benefits for both the body and "
    "the mind. Physically, it strengthens the heart, improves circulation, and "
    "helps maintain a healthy weight by burning calories and building muscle. "
    "It also increases bone density, which lowers the risk of osteoporosis "
    "later in life. Beyond its physical effects, exercise has a powerful "
    "impact on mental health. Activity triggers the release of endorphins, "
    "which can reduce stress and improve mood, and many people find that a "
    "consistent routine helps them sleep better and think more clearly. Even "
    "moderate activity, such as a brisk thirty-minute walk most days of the "
    "week, can make a meaningful difference. Ultimately, making exercise a "
    "regular habit is one of the simplest and most effective ways to improve "
    "overall quality of life.",

    # Write a paragraph about the history of the printing press.
    "The invention of the printing press in the fifteenth century transformed "
    "the way information was shared across the world. Around 1440, Johannes "
    "Gutenberg developed a system of movable metal type that allowed pages to "
    "be reproduced quickly and accurately. Before this, books were copied by "
    "hand, a slow and expensive process that kept written knowledge in the "
    "hands of a small elite. Gutenberg's press made books more affordable and "
    "widely available, which helped literacy spread across Europe. The new "
    "technology played a major role in the Renaissance, the Reformation, and "
    "the Scientific Revolution by allowing ideas to circulate faster than ever "
    "before. Today, the printing press is widely regarded as one of the most "
    "influential inventions in human history.",

    # Write a paragraph about why sleep is important.
    "Sleep is essential for maintaining good physical and mental health. "
    "During sleep, the body repairs tissues, strengthens the immune system, "
    "and regulates hormones that control appetite and growth. The brain also "
    "uses this time to process information, consolidate memories, and clear "
    "away waste products that build up during the day. When people do not get "
    "enough sleep, they often struggle with concentration, decision-making, "
    "and emotional control. Over time, chronic sleep deprivation has been "
    "linked to serious health problems, including heart disease, diabetes, "
    "and depression. Most adults need between seven and nine hours of sleep "
    "each night to function at their best. Prioritizing a consistent sleep "
    "schedule is therefore one of the most important steps a person can take "
    "to protect their long-term well-being.",

    # Write a paragraph about how photosynthesis works.
    "Photosynthesis is the process by which plants, algae, and some bacteria "
    "convert light energy into chemical energy. It takes place mainly in the "
    "chloroplasts of plant cells, which contain a green pigment called "
    "chlorophyll that absorbs sunlight. Using this energy, the plant takes in "
    "carbon dioxide from the air and water from the soil and combines them to "
    "produce glucose, a type of sugar that serves as food. Oxygen is released "
    "into the atmosphere as a byproduct. The process occurs in two main "
    "stages: the light-dependent reactions, which capture energy from the "
    "sun, and the Calvin cycle, which uses that energy to build sugar "
    "molecules. Photosynthesis is vital to life on Earth because it provides "
    "the oxygen we breathe and forms the foundation of most food chains.",

    # Write a paragraph about the effects of climate change on the oceans.
    "Climate change is having a profound impact on the world's oceans. As "
    "global temperatures rise, the oceans absorb much of the excess heat, "
    "causing sea temperatures to increase. Warmer water contributes to coral "
    "bleaching, a process in which corals lose the algae they depend on and "
    "often die as a result. At the same time, the oceans are absorbing large "
    "amounts of carbon dioxide from the atmosphere, which makes the water more "
    "acidic and makes it harder for shellfish and other marine organisms to "
    "build their shells. Melting ice sheets and glaciers are also causing sea "
    "levels to rise, threatening coastal communities around the world. These "
    "changes disrupt marine ecosystems and the millions of people who rely on "
    "the ocean for food and income.",

    # Write a paragraph about the benefits of reading.
    "Reading is one of the most rewarding habits a person can develop. It "
    "expands vocabulary, improves writing skills, and strengthens the ability "
    "to concentrate for long periods of time. Fiction in particular allows "
    "readers to see the world through the eyes of others, which can build "
    "empathy and understanding. Nonfiction, on the other hand, provides "
    "knowledge about history, science, and countless other subjects. Studies "
    "have also shown that reading can reduce stress and keep the mind sharp as "
    "people age. Whether it is a novel, a newspaper, or a scientific article, "
    "reading regularly helps people learn, grow, and engage more thoughtfully "
    "with the world around them.",

    # Write a paragraph about remote work.
    "Remote work has become increasingly common in recent years, especially "
    "since the COVID-19 pandemic. Many employees appreciate the flexibility it "
    "offers, as it eliminates long commutes and allows them to create a better "
    "balance between their professional and personal lives. Companies can "
    "also benefit by reducing office costs and hiring talent from a wider "
    "geographic area. However, remote work also presents challenges. Some "
    "workers struggle with feelings of isolation, while others find it "
    "difficult to separate work from home life. Communication and "
    "collaboration can become more complicated without face-to-face "
    "interaction. As a result, many organizations are now adopting hybrid "
    "models that combine the advantages of remote and in-office work.",

    # Write a paragraph about the water cycle.
    "The water cycle describes the continuous movement of water through the "
    "Earth's environment. It begins when the sun heats water in oceans, "
    "lakes, and rivers, causing it to evaporate and rise into the atmosphere "
    "as water vapor. As the vapor cools at higher altitudes, it condenses into "
    "tiny droplets that form clouds. When these droplets combine and grow "
    "heavy enough, they fall back to the ground as precipitation in the form "
    "of rain, snow, sleet, or hail. Some of this water flows over the land as "
    "runoff into rivers and oceans, while some soaks into the ground and "
    "replenishes groundwater supplies. The cycle then repeats, ensuring that "
    "water is constantly recycled and made available to support life on "
    "Earth.",

    # Write a paragraph about the impact of social media on teenagers.
    "Social media has a significant impact on the lives of teenagers, "
    "bringing both benefits and risks. On the positive side, platforms like "
    "Instagram, TikTok, and Snapchat allow young people to stay connected "
    "with friends, express their creativity, and find communities that share "
    "their interests. However, heavy use of social media has also been linked "
    "to anxiety, depression, and low self-esteem. Teenagers may feel pressure "
    "to present a perfect image online or compare themselves unfavorably to "
    "others. Cyberbullying and exposure to harmful content are additional "
    "concerns. To use social media in a healthy way, it is important for "
    "teenagers to set limits on screen time and for parents and educators to "
    "encourage open conversations about online experiences.",

    # Write a paragraph about recycling.
    "Recycling is an important practice that helps protect the environment "
    "and conserve natural resources. By turning used materials such as paper, "
    "plastic, glass, and metal into new products, recycling reduces the need "
    "to extract raw materials from the earth. This process saves energy, "
    "lowers greenhouse gas emissions, and decreases the amount of waste sent "
    "to landfills. Recycling also supports local economies by creating jobs "
    "in collection and processing. However, its effectiveness depends on "
    "people sorting their waste correctly and avoiding contamination. By "
    "making recycling a regular habit, individuals and communities can play a "
    "meaningful role in building a more sustainable future.",
]


SCENARIOS = [
    {
        "name": "staff human writing",
        "criterion": 1,
        # ⚠️ NOT my own writing. Criterion 1 asks for 10 pieces by people, at
        # least 4 plain. I chose to use the 8 genuine human texts from the
        # staff attack set (FP01–FP08) instead, so this runs on 8, not 10 —
        # the README says so. They are plain, formal or templated: the hard
        # cases for this detector.
        "texts": _staff_human(*(f"FP0{i}" for i in range(1, 9))),
    },
    {
        "name": "unedited AI text",
        "criterion": 2,
        "texts": AI_PARAGRAPHS,
    },
    # Criterion 3: average combined score of 5 AI pieces vs 5 human pieces.
    # Picked by position (the first five of each), not by score.
    {
        "name": "gap: AI set",
        "criterion": 3,
        "texts": AI_PARAGRAPHS[:5],
    },
    {
        "name": "gap: human set",
        "criterion": 3,
        "texts": _staff_human("FP01", "FP02", "FP03", "FP04", "FP05"),
    },
    # Criterion 4 (appeals) can't be expressed as a submission alone — it needs
    # a content_id back and then a call to /appeal. It runs in eval_extra.py,
    # three trials, like this file.
    {
        "name": "bad input",
        "criterion": 5,
        # Every case criterion 5 names that can be written as a dict. The one
        # that can't — a body that isn't a JSON object — is in eval_extra.py,
        # along with the check that each one left a `rejected` log entry.
        "bodies": [
            {"creator_id": "eval_bad_missing_text"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "A sentence with no creator attached to it at all."},
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},
            {"text": "Hi", "creator_id": "eval_bad_tiny"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
