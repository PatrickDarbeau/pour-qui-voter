# Pour qui voter ? — French presidential election 2027

**Pour qui voter ?** ("Who should I vote for?") is a free, neutral and **offline** voting advice tool for the 2027 French presidential election. It compares your opinions on concrete policy measures with the programmes of the candidates, and explains the result with sources.

> The application itself is in French, since it is meant for French voters. This page is for developers and contributors.
> A French version of this page is available in [LISEZMOI.md](LISEZMOI.md).

![Home page of the application](docs/captures/accueil.png)

| Questionnaire | Candidates |
|---|---|
| ![Questionnaire: give your opinion on each measure](docs/captures/questionnaire.png) | ![List of candidates with portraits](docs/captures/candidats.png) |

*Screenshots of the test pack (13 November 2026).*

## How it works

1. **Choose your priority themes** (optional): measures in these themes count twice.
2. **Give your opinion on each measure** (for / against / indifferent) and mark the ones that are essential to you with a ★ (they count three times).
3. **See the ranking** of candidates, with the details of agreements and disagreements, each backed by a link to the source (the candidate's campaign site first, then the party site, then reputable press, flagged as such).

The scoring method is fully documented in the app (*Méthode* page) and implemented in [`assets/js/score.js`](assets/js/score.js).

## Key principles

- **Privacy by design**: no account, no server, no analytics. Your answers never leave your device (they are stored only in your browser's `localStorage`).
- **Offline**: a static single-page application opened directly from `index.html` (`file://`). A strict Content Security Policy (`connect-src 'none'`) blocks every network request; an automated test checks it.
- **Neutrality**: measures are worded neutrally, every candidate position is quoted and sourced, and positions that are inferred or come from the press are marked "to be confirmed". Candidates whose positions have not been collected yet are listed but not ranked.
- **Transparency**: data and code are open; each data update is recorded in a changelog, and a dated "lessons learned" note follows every data collection ([`docs/enseignements/`](docs/enseignements/)).
- **Reusable**: an *Édition* (edit) mode lets anyone replace themes, measures and candidates, for example for a school election.

## Status

| Item | State |
|---|---|
| Application | Feature-complete (questionnaire, results, candidate pages, print/PDF, share link, edit mode, second-round mode) |
| Measure catalogue | 158 measures in 17 themes |
| Candidates | 10 likely candidates, with profiles (birth, education, profession from Wikipedia; free-licence portraits from Wikimedia Commons) |
| Positions | 380 **draft** positions for 9 candidates, under human review |
| First public data pack | Planned for 15 January 2027 |

The current data (`data/donnees.json`, version `2026.11.13-test`) is a **test pack**: do not use it to make a voting decision.

## Quick start

**Users**: download the ZIP archive from the [Releases](https://github.com/PatrickDarbeau/pour-qui-voter/releases/latest) page, unzip it and double-click `index.html`. Nothing to install.

**Developers**: clone the repository and open `index.html` in a browser, or serve it locally:

```bash
python -m http.server 8765
```

Requirements for the tools and tests: Python 3.10+ (with Pillow for portraits), Node.js 18+, and Google Chrome for the headless tests.

## Repository layout

| Path | Content |
|---|---|
| `index.html`, `assets/` | The application (vanilla JavaScript, CSS, candidate portraits) |
| `data/donnees.json`, `data/donnees.js` | Installed data pack (JSON, and the same data as a script for `file://` use) |
| `data/demo/` | Demonstration pack with fictional candidates |
| `outils/` | Python tools to build, validate and package the data |
| `tests/` | Unit tests (scoring, tools) and headless browser checks (offline, print) |
| `docs/` | Developer notice, catalogue, candidate profiles, positions, lessons-learned notes |

## Development commands

| Command | Purpose |
|---|---|
| `python outils/catalogue.py` | Generates the measure catalogue (draft) |
| `python outils/candidats.py` | Generates the candidate profiles (draft) |
| `python outils/portraits.py` | Downloads and crops the candidate portraits (3:4) from Wikimedia Commons |
| `python outils/positions.py` | Builds the candidate positions (draft) from `outils/positions_<id>.py` |
| `python outils/assembler.py --installer` | Assembles the test pack and installs it in `data/` |
| `python outils/valider.py --publier` | Validates `data/donnees.json` and generates `data/donnees.js` |
| `python outils/comparer.py` | Writes a comparative analysis (coverage, proximity, divisive and consensus measures) |
| `python outils/maj.py candidats` · `collecter` · `diff A B` · `publier --version YYYY.MM.DD` | Data update workflow (see the developer notice) |
| `python outils/demo.py` | Regenerates the demonstration pack |
| `python outils/paquet.py` | Builds the user ZIP archive in `dist/` |
| `node tests/score.test.js` | Scoring tests |
| `python -m unittest tests/test_outils.py` | Tool tests (validator, catalogue, profiles, positions) |
| `node tests/hors_ligne.mjs` | Opens the packaged app via `file://` in headless Chrome and checks that no network request is made |
| `node tests/pdf.mjs` | Renders the results page to PDF to check printing |

## Online demo

A demo can be published on GitHub Pages with the manual **"Démo en ligne"** workflow (*Actions* tab) once the repository is public. In the online demo, a banner invites visitors to download the app; the edit mode works as a sandbox (changes stay in the visitor's browser), candidates are locked and pack import is disabled. To try this mode locally, add `?demo` to the URL (e.g. `http://localhost:8765/?demo`). Download links are set in [`assets/js/config.js`](assets/js/config.js).

## Documentation

- [Specifications](CAHIER_DES_CHARGES.md) (in French; work packages in §10)
- [Developer notice](docs/NOTICE_DEVELOPPEUR.md): work packages, data release schedule, update procedure and changelog (§5)
- [Lessons-learned notes](docs/enseignements/README.md) after each data collection
- [Candidate profiles and sources](docs/fiches_candidats.md)

## Contributing

Found a wrong position, a missing source or a bug? Please open an [issue](https://github.com/PatrickDarbeau/pour-qui-voter/issues) with the measure, the candidate and a link to an official source. Contributions must respect the neutrality rules: official sources first, exact quotes, no aggregator or comparison sites as sources.

## Licences

- **Code**: European Union Public Licence **EUPL 1.2**, see [LICENCE](LICENCE).
- **Data** (themes, measures, candidate profiles, positions): **Creative Commons BY-SA 4.0**, see [LICENCE-DONNEES](LICENCE-DONNEES).
- **Portraits**: Wikimedia Commons, under free licences (CC0, CC BY, CC BY-SA) or reusable with attribution (European Parliament); author and licence are shown under each photo.
- Short quotes from candidates' programmes remain the property of their authors and are reproduced under the right of quotation, with their source.
- Legal notice, disclaimer and privacy: [MENTIONS-LEGALES.md](MENTIONS-LEGALES.md) (in French).
