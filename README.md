# 🔥 1-MONTH MUSCLE PROTOCOL — Dumbbell + Bodyweight

A browser-based 4-week progressive muscle program — dumbbells + bodyweight only, upper-body focus, no legs.
100% client-side — no backend, no sign-up, no data leaves your browser.

![Split](https://img.shields.io/badge/split-Push%2FPull%2FLegs-64ffda)
![Storage](https://img.shields.io/badge/storage-localStorage-blue)
![Offline](https://img.shields.io/badge/works-offline-success)

## Features

- **4-week progression** — W1 Adapt · W2 Volume · W3 Overload (+1 set auto-applied) · W4 Peak (AMRAP finishers)
- **4-day tabs** — Push A · Pull A · Push B · Pull B (upper hit 2×/week)
- **24 exercises** — dumbbell + bodyweight only, with illustrations or icons, coaching notes per exercise
- **Tap-to-complete sets** — check off each set as you finish it; the card turns green when all sets are done
- **Auto rest timer** (90s) pops up after each set, with −15s / +15s / Skip
- **Progress saved in `localStorage`** — survives reloads; remembers your last workout date
- **Fully responsive** — works on phone, tablet, desktop
- **Offline** — single HTML file, runs without internet

## The workout

| Day  | Focus        | Exercises                                                              |
|------|--------------|------------------------------------------------------------------------|
| 1    | **PUSH A**   | Bench press, incline press, shoulder press, lateral raise, overhead ext, push-ups (AMRAP) |
| 2    | **PULL A**   | Pull-ups, bent-over rows, single-arm rows, curls, hammer curls, russian twists |
| 3    | **PUSH B**   | Incline press, shoulder press, lateral raise burnout, pike push-ups, chair dips, kickbacks |
| 4    | **PULL B**   | Heavy single-arm rows, bent-over rows, reverse flyes, table rows, slow curls, plank |

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
