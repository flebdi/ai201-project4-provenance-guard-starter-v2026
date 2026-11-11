# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 20:42
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `2d698402a05a` | human | 0.307 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9892fbc69d8a` | unsure | 0.511 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `7a94705a6cfc` | unsure | 0.598 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `954f7ef45ea2` | unsure | 0.651 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `98779b61afb1` | human | 0.305 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c75ea3dd4c2c` | unsure | 0.538 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bd605cc13289` | unsure | 0.529 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c46c7ba2649e` | unsure | 0.360 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b12474168d4a` | unsure | 0.645 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `81f3368ac7f4` | ai | 0.925 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `8e340f43e694` | unsure | 0.623 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d5c1c310d742` | unsure | 0.763 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `053e3f6055b0` | unsure | 0.798 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `41248e1d8c47` | unsure | 0.813 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `52b260887968` | unsure | 0.805 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b99ca3f27e6f` | unsure | 0.821 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `be0f0615198f` | unsure | 0.785 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `476a733c24b2` | unsure | 0.391 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `a6fbaecb527e` | unsure | 0.458 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `46aa35234468` | human | 0.231 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `87930821b12c` | unsure | 0.572 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `42108fae68a8` | unsure | 0.462 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c7060536b2d5` | unsure | 0.558 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c6cd30a24eb0` | unsure | 0.578 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `c539065af390` | human | 0.140 |  |
| MF04 | malformed | text is only punctuation | 200 | `5814708b981a` | human | 0.209 |  |
| MF05 | malformed | text is a very long single word | 200 | `c6d52a1feaef` | ai | 0.938 |  |
| MF06 | malformed | text is emoji only | 200 | `63a65375514c` | ai | 0.938 |  |
| MF07 | malformed | text is right-to-left script | 200 | `cd76ae6c68f0` | unsure | 0.865 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbfde20c54df` | human | 0.163 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9f20e202facf` | human | 0.163 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b28bc73f9c96` | human | 0.163 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8550e218b71c` | human | 0.163 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0a495cacc235` | human | 0.163 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "2d698402a05a",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3069,
  "model_score": 0.1635,
  "style_score": 0.8803,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9892fbc69d8a",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5114,
  "model_score": 0.5943,
  "style_score": 0.18,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "7a94705a6cfc",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5983,
  "model_score": 0.6662,
  "style_score": 0.3266,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "954f7ef45ea2",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.651,
  "model_score": 0.6114,
  "style_score": 0.8095,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "98779b61afb1",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3053,
  "model_score": 0.3212,
  "style_score": 0.2417,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c75ea3dd4c2c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5382,
  "model_score": 0.5727,
  "style_score": 0.4,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bd605cc13289",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.529,
  "model_score": 0.5862,
  "style_score": 0.3,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c46c7ba2649e",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3596,
  "model_score": 0.2452,
  "style_score": 0.8172,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b12474168d4a",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6449,
  "model_score": 0.7042,
  "style_score": 0.4075,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "81f3368ac7f4",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9246,
  "model_score": 0.9792,
  "style_score": 0.7061,
  "label": "Our automated check thinks this was probably generated by AI. Automated checks can be wrong, including about real writers. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "8e340f43e694",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6225,
  "model_score": 0.6175,
  "style_score": 0.6425,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "d5c1c310d742",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7629,
  "model_score": 0.7387,
  "style_score": 0.8597,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "053e3f6055b0",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7984,
  "model_score": 0.8051,
  "style_score": 0.7718,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "41248e1d8c47",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.813,
  "model_score": 0.8329,
  "style_score": 0.7333,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "52b260887968",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.805,
  "model_score": 0.8005,
  "style_score": 0.8231,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "b99ca3f27e6f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.8213,
  "model_score": 0.8814,
  "style_score": 0.5808,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "be0f0615198f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7853,
  "model_score": 0.8816,
  "style_score": 0.4,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "476a733c24b2",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3912,
  "model_score": 0.3223,
  "style_score": 0.667,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "a6fbaecb527e",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4575,
  "model_score": 0.4625,
  "style_score": 0.4373,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "46aa35234468",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.231,
  "model_score": 0.2044,
  "style_score": 0.3372,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "87930821b12c",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5723,
  "model_score": 0.5943,
  "style_score": 0.4844,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "42108fae68a8",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4621,
  "model_score": 0.4998,
  "style_score": 0.3113,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c7060536b2d5",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5578,
  "model_score": 0.6401,
  "style_score": 0.2286,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c6cd30a24eb0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5776,
  "model_score": 0.5583,
  "style_score": 0.6546,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c539065af390",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.14,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "5814708b981a",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.209,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c6d52a1feaef",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9381,
  "model_score": 0.9976,
  "style_score": 0.7,
  "label": "Our automated check thinks this was probably generated by AI. Automated checks can be wrong, including about real writers. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "63a65375514c",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9375,
  "model_score": 0.9969,
  "style_score": 0.7,
  "label": "Our automated check thinks this was probably generated by AI. Automated checks can be wrong, including about real writers. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "cd76ae6c68f0",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.8651,
  "model_score": 0.9064,
  "style_score": 0.7,
  "label": "Our automated check couldn't tell whether this was written by a person or generated by AI. That happens with a lot of genuine writing, so this is not an accusation, and nothing about the piece changes because of it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "dbfde20c54df",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "9f20e202facf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "b28bc73f9c96",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "8550e218b71c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "0a495cacc235",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was written by a person. Nothing in it looked machine-generated to our automated check.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
