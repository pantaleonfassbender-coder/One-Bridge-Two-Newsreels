# Eine Brücke, zwei Wochenschauen. Remagen 1945 – One Bridge, Two Newsreels

Ein zweisprachiger Quellenapparat zur Brücke von Remagen, 7. bis 17. März 1945: Texte und Filme ihrer Zeit, im Original neben einer Übersetzung, die Filme kommentiert an Zeitmarken. Die amerikanischen und britischen Wochenschauen brachten die Brücke ins Kino; die Deutsche Wochenschau schwieg. Der Apparat endet nicht mit dem Einsturz, sondern mit den Lagern am Rhein.

*A bilingual documentary apparatus on the bridge at Remagen, 7–17 March 1945: texts and films of the time, the original beside a translation, the films with commentary at time marks. The American and British newsreels brought the bridge to the cinema; the German newsreel was silent. The apparatus does not end with the collapse but with the camps on the Rhine.*

**Stand:** im Aufbau. Abgedruckt:

- **Der 7. März** — Charles B. MacDonald, *The Last Offensive* (1973), S. 211–219, am Seitenbild gelesen, mit deutscher Übersetzung; dazu die Stimmen von Engeman, Drabik und den Pionieren aus *Combat Bulletin No. 51* (1945) nach der Tonspur. Sechs Abschnitte, 28 Einheiten, fünf Tafeln (zwei Photographien und eine Karte aus MacDonald, zwei Standbilder des Signal Corps) und eine Zeitachse der Stunden des 7. März.
- **Warum sie stand** — MacDonald, S. 209–216 und 230, die deutsche Seite nach Hechlers Studie: Befehlswege, Schellers Fahrt, der Sprengplan und der Befehl des OKW, Bratge am Vormittag, der Tunnel, die Erklärungen. Sechs Abschnitte, 22 Einheiten, zwei Tafeln und ein Schema der Befehlswege.
- **Der Brückenkopf** — MacDonald, S. 219–235 in Auswahl, und die Wehrmachtberichte vom 12., 17. und 21. März 1945 (am Zeitungsbild gelesen): die erste Nacht, Eisenhowers Auflagen, die Deutschen ohne Plan, Fähren und Pontonbrücken, die Ausweitung bis zur Sieg und MacDonalds Bilanz. Sechs Abschnitte, 19 Einheiten, drei Tafeln und ein Schema „Wege über den Rhein“.
- **Das fliegende Standgericht** — Wehrmachtberichte vom 8., 9., 11. und 18. März 1945 und eine DNB-Meldung vom 11. März nach Zeitungen im Deutschen Zeitungsportal (am Seitenbild gelesen; die Scans sind verlinkt, nicht gezeigt), MacDonald S. 222 und 230, Kesselrings Erlass (Bundesarchiv RH 19-IV/226, Bl. 42, als Zitat). Vier Abschnitte, acht Einheiten, eine Doppelzeitleiste „Was geschah, was gemeldet wurde“; gemeinfreie Bilder gibt es für dieses Modul nicht.

Fünf weitere Module sind geplant (die Brücke, die Angriffe, der Einsturz, zwei Wochenschauen, die Lager am Rhein). Die Seite „Filme“ zeigt elf Filme mit Zeitmarken und, wo es Ton gibt, einer Abschrift mit Übersetzung; die Seite „Vergleich“ stellt Stimmen aus den Modulen nebeneinander.

**Nur Gemeinfreies, und was eingebettet werden darf.** Hauptquelle ist Charles B. MacDonald, *The Last Offensive* (Center of Military History 1973), als Werk der US-Regierung gemeinfrei. Die Filme sind nicht im Repository: Aufnahmen der US-Regierung werden aus dem Internet Archive eingebettet, britische Wochenschauen nur über den offiziellen YouTube-Kanal ihrer Rechteinhaber, beide erst auf Klick. Die Deutsche Wochenschau wird weder gezeigt noch eingebettet. Geschützte Darstellungen (Hechler 1957, der Spielfilm von 1969, die neuere Forschung) werden nur referiert.

**Begleitspiel:** *Zehn Tage am Rhein – Ten Days on the Rhine* (in Vorbereitung): zwei Rollen, Hauptmann Willi Bratge und der amerikanische Brückenkopf, vom 7. bis zum 17. März 1945.

## Aufbau

Statische Site ohne Build-Schritt: `index.html`, `app.js` (Hash-Routen, Sprachumschalter, Filmeinbettung auf Klick), `style.css`, `legal.html`; Bauskripte in `tools/` (`build-siebter.py`, `viz-siebter.py`, `make-plates.py`); Daten in `data/` (`modules.json`, `films.json`, `timeline.json`, `compare.json`, `plates.json`, später je Modul eine Datei). Felder mit dem Suffix `_en` tragen die englische Fassung; fehlt sie, zeigt die Site die deutsche.

Lokal: `python -m http.server` im Repository, dann `http://localhost:8000/`.

## Lizenzen

Code MIT; redaktionelle Texte CC BY 4.0; Editionen und Übersetzungen CC0 1.0; Filme nur eingebettet. Siehe [LICENSES.md](LICENSES.md).

## Impressum und Datenschutz

Siehe `legal.html` auf der Site.
