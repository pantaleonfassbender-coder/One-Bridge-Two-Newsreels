# Eine Brücke, zwei Wochenschauen. Remagen 1945 – One Bridge, Two Newsreels

Ein zweisprachiger Quellenapparat zur Brücke von Remagen, 7. bis 17. März 1945: Texte und Filme ihrer Zeit, im Original neben einer Übersetzung, die Filme kommentiert an Zeitmarken. Die amerikanischen und britischen Wochenschauen brachten die Brücke ins Kino; die Deutsche Wochenschau schwieg. Der Apparat endet nicht mit dem Einsturz, sondern mit den Lagern am Rhein.

*A bilingual documentary apparatus on the bridge at Remagen, 7–17 March 1945: texts and films of the time, the original beside a translation, the films with commentary at time marks. The American and British newsreels brought the bridge to the cinema; the German newsreel was silent. The apparatus does not end with the collapse but with the camps on the Rhine.*

**Stand:** im Aufbau. Neun Module sind geplant (die Brücke, der 7. März, warum sie stand, der Brückenkopf, das fliegende Standgericht, die Angriffe, der Einsturz, zwei Wochenschauen, die Lager am Rhein); die Seite „Texte“ nennt sie mit ihren Quellen, die Seite „Filme“ die Aufnahmen, die Zeitleiste die bisher geprüften Stationen.

**Nur Gemeinfreies, und was eingebettet werden darf.** Hauptquelle ist Charles B. MacDonald, *The Last Offensive* (Center of Military History 1973), als Werk der US-Regierung gemeinfrei. Die Filme sind nicht im Repository: Aufnahmen der US-Regierung werden aus dem Internet Archive eingebettet, britische Wochenschauen nur über den offiziellen YouTube-Kanal ihrer Rechteinhaber, beide erst auf Klick. Die Deutsche Wochenschau wird weder gezeigt noch eingebettet. Geschützte Darstellungen (Hechler 1957, der Spielfilm von 1969, die neuere Forschung) werden nur referiert.

**Begleitspiel:** *Zehn Tage am Rhein – Ten Days on the Rhine* (in Vorbereitung): zwei Rollen, Hauptmann Willi Bratge und der amerikanische Brückenkopf, vom 7. bis zum 17. März 1945.

## Aufbau

Statische Site ohne Build-Schritt: `index.html`, `app.js` (Hash-Routen, Sprachumschalter, Filmeinbettung auf Klick), `style.css`, `legal.html`; Daten in `data/` (`modules.json`, `films.json`, `timeline.json`, `compare.json`, `plates.json`, später je Modul eine Datei). Felder mit dem Suffix `_en` tragen die englische Fassung; fehlt sie, zeigt die Site die deutsche.

Lokal: `python -m http.server` im Repository, dann `http://localhost:8000/`.

## Lizenzen

Code MIT; redaktionelle Texte CC BY 4.0; Editionen und Übersetzungen CC0 1.0; Filme nur eingebettet. Siehe [LICENSES.md](LICENSES.md).

## Impressum und Datenschutz

Siehe `legal.html` auf der Site.
