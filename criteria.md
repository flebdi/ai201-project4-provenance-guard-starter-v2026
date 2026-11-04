# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

<!-- DRAFT written by Claude at my request (see README → How I Used AI).
     Revise each criterion and its reason into your own words and numbers
     before relying on it — you'll have to defend these in unit 8. -->

## 1. Plain human writing is not accused

Of 10 pieces written by people — at least 4 of them plainly written (short
sentences, common words, little punctuation beyond full stops and commas) — **at
most 1 is labelled high-confidence AI**, in **each** of the three trials.

**Why this target:** On a writing site a wrong accusation costs the writer far
more than a missed detection costs the site. Plain writing is named because both
of my signals score it as machine-like — it's where false positives will come
from, so a test made only of colourful human prose would pass without proving
anything.

---

## 2. Obvious AI text still gets caught

Of 10 unedited AI-generated pieces (from ChatGPT or Claude, with a plain prompt
like "write a paragraph about X"), **at least 5 are labelled high-confidence
AI**, in each of the three trials.

**Why this target:** A system that never says "AI" would pass criterion 1 and be
useless. This target stops me from fixing false positives by raising the AI
threshold forever. With the threshold at 0.87 it's a real challenge, and that's
the trade: fewer wrong accusations means more AI text gets through.

---

## 3. Clearly-AI and clearly-human text score far apart

Across 5 clearly AI-generated pieces and 5 clearly human pieces, the **average
combined score of the AI set is at least 0.40 higher** than the average of the
human set, in each of the three trials.

**Why this target:** If the two groups score close together, every label is
driven by noise and the thresholds mean nothing. My two thresholds (0.35 and
0.87) are 0.52 apart; a gap of 0.40 between the averages is the least that
gives the obvious cases a real chance of landing on opposite sides of them.

---

## 4. An appeal is always recorded

**10 of 10** appeals sent with a real `content_id` return HTTP 200 and add a log
entry with `status: under_review` after the original decision. **5 of 5**
appeals with a made-up `content_id` return 404 and add no appeal entry.

**Why this target:** The appeal is the only thing between a wrong accusation and
nothing at all, so anything less than every time is a failure — a writer whose
appeal vanished has no reason to believe the next one will land. The 404 half
stops an appeal on a typo from looking like it worked.

---

## 5. Bad input never crashes the service

Of these requests to `/submit` — missing `text`, empty `text`, whitespace-only
`text`, `text` that isn't a string, a body that isn't a JSON object, missing
`creator_id`, `text` over 20,000 characters, and `text` under 3 tokens —
**0 return a 5xx**. Each returns a 4xx with an `error` field and writes a
`rejected` entry to the audit log.

**Why this target:** A crash on malformed input is one of the most common real
failures, and an attacker's first probe. A refusal that leaves no log entry
would make that probe invisible, which is why the log write is part of the
target.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
