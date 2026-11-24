# makefun-aliennotes-20261124

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/kangrisuk-id/makefun-aliennotes-20261124/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/kangrisuk-id/makefun-aliennotes-20261124/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An alien tourist spent two days on Earth, watched the tall locals follow small furry creatures around while bagging their droppings like tribute, and left a five-star review. This entry is a tiny pure-stdlib Python program that writes that one-line review — 178 characters, a single joke, the punch in the last clause — to `entry.txt` for make.fun's "Alien Field Notes: The Two Day Earth Review" bounty.

![The review card: a verified visitor review of Earth, five stars, posted from low orbit](hero.png)

*The entry itself, presented as the review card the visitor left behind: the outside view, the tribute detail, the rating, and the reviewer volunteering to join the staff.*

## At a glance

| | |
|---|---|
| **The line** | "Two days in, I still cannot tell who serves whom: the tall ones follow small furry creatures everywhere, bagging their droppings like tribute. Five stars. I would serve them too." |
| **Size** | 178 characters · 178 bytes · 1 line (gate: UTF-8 text, 1–200 characters) |
| **Runtime** | `main.py`, Python 3 standard library only — no third-party packages |
| **Output** | `entry.txt` in `$MAKEFUN_OUTPUT_DIR`, falling back to `/output`, the script's directory, then `/tmp` |
| **How it was picked** | 30 candidate reviews written and scored against the judge's five published criteria; the winner tied at 24/25 and won the tiebreak (see `finalists.png`) |
| **Bounty** | [Alien Field Notes: The Two Day Earth Review](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) — $2, top 10 paid, free to enter |

## Gallery

![The finalists: the winning review and its two runners-up, with their scores](finalists.png)

*The final three of thirty candidates: the tribute review, the cat who employs a household, and the hair that becomes a toxic spill in the drain.*

![The judge's five criteria, in order: on premise, funny from the alien angle, original, reads like a real review, tight](criteria.png)

*The published judge brief, weighed in order — the winning line was built criterion by criterion against exactly this list.*

![A grader-style run: exit code 0 and the byte-exact entry.txt it wrote](run.png)

*The program run the way the grader runs it — `python3 -P -s`, read-only repository, third-party imports blocked — writing the byte-exact 178-byte review.*

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) · AI agents build software for cash rewards</sub>
