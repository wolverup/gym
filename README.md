# 🏋️ Dumbbell PPL — 3-Day Training Tracker

A clean, browser-based workout tracker for a 3-day dumbbell Push / Pull+Core / Legs+Core split.
100% client-side — no backend, no sign-up, no data leaves your browser.

![Split](https://img.shields.io/badge/split-Push%2FPull%2FLegs-64ffda)
![Storage](https://img.shields.io/badge/storage-localStorage-blue)
![Offline](https://img.shields.io/badge/works-offline-success)

## Features

- **3-day tabs** — Day 1 Push · Day 2 Pull+Core · Day 3 Legs+Core
- **18 exercises**, each with a form-reference illustration, sets, reps, and coaching notes
- **Tap-to-complete sets** — check off each set as you finish it; the card turns green when all sets are done
- **Auto rest timer** (90s) pops up after each set, with −15s / +15s / Skip
- **Progress saved in `localStorage`** — survives reloads; remembers your last workout date
- **Fully responsive** — works on phone, tablet, desktop
- **Offline** — single HTML file, runs without internet

## The workout

| Day  | Focus        | Exercises                                                              |
|------|--------------|------------------------------------------------------------------------|
| 1    | **PUSH**     | Bench press, incline press, shoulder press, lateral raise, triceps ext, kickbacks |
| 2    | **PULL + CORE** | Pull-ups, rows, single-arm rows, reverse flyes, bicep curls, hammer curls, russian twists |
| 3    | **LEGS + CORE** | Goblet squat, Bulgarian split squat, RDL, lunges, weighted crunches |

## Run it

Just open `index.html` in any browser. No build step, no dependencies, no external files — everything (HTML, CSS, JS, and all 18 illustrations) is inlined into one ~870 KB file.

```bash
# optionally serve it
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Project structure

```
workout/
├── index.html   # the entire app — single self-contained file (HTML + CSS + JS + images as data URIs)
├── README.md
└── LICENSE
```

## Credits

- Exercise illustrations: [Wikimedia Commons](https://commons.wikimedia.org/) contributors (CC-BY-SA / public domain), plus custom line drawings for exercises with no Commons source.

## License

MIT — see [LICENSE](LICENSE).
