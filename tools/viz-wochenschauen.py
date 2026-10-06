"""Zeichnet assets/viz/wochenschauen.svg und -en.svg: März 1945 in drei Bahnen, oben die Ereignisse,
darunter die amerikanischen und britischen Wochenschauen, unten die Deutsche Wochenschau. Gefüllt: zeigt
Remagen; leer: zeigt Remagen nicht. Undatierte Filme stehen am Rand. Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-wochenschauen.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
W, H = 900, 400
X0, X1, D0, D1 = 200, 760, 6, 28


def x(d):
    return X0 + (X1 - X0) * (d - D0) / (D1 - D0)


LANES = [(120, "Ereignisse", "Events", "bruecke"), (220, "USA und Großbritannien", "US and Britain", "us"), (320, "Deutsche Wochenschau", "German newsreel", "deutsch")]
EV = [  # (Bahn, Tag, zeigt Remagen?, de, en, Verweis, Reihe)
    (0, 7, None, "Übergang", "crossing", "#/text/siebter/uebergang/17", -1),
    (0, 17, None, "Einsturz", "collapse", "#/text/einsturz/nachmittag/2", -1),
    (0, 18, None, "Todesurteile gemeldet", "death sentences announced", "#/text/standgericht/okw/7", 1),
    (0, 20, None, "Presse: Hitlerjungen und Remagen", "press: Hitler Youths and Remagen", "#/text/wochenschauen/deutsch/8", -2),
    (1, 26, True, "Universal, Movietone 825", "Universal, Movietone 825", "#/text/wochenschauen/universal/1", -1),
    (2, 16, False, "Nr. 754: der Rhein, nicht Remagen", "no. 754: the Rhine, not Remagen", "#/text/wochenschauen/deutsch/6", -1),
    (2, 22, False, "Nr. 755, die letzte", "no. 755, the last", "#/text/wochenschauen/deutsch/7", 1),
]


def build(en):
    title = "What the cinemas showed" if en else "Was die Kinos zeigten"
    sub = ("March 1945. Filled: shows Remagen; open: does not. Undated films on the right." if en
           else "März 1945. Gefüllt: zeigt Remagen; leer: zeigt Remagen nicht. Undatierte Filme rechts.")
    desc = ("A timeline of March 1945. Events: crossing on 7 March, collapse on 17 March, death sentences announced on 18 March, a newspaper of 20 March prints the Hitler Youth reception above the Remagen collapse. "
            "American and British newsreels: Universal and Movietone no. 825 on 26 March show Remagen; undated: United News, Combat Bulletins 48 and 51, Pathé, Gaumont-British in May. "
            "German newsreel: no. 754 on 16 March mentions the Rhine but not Remagen; no. 755 on 22 March, the last issue, nothing from the west."
            if en else
            "Eine Zeitleiste des März 1945. Ereignisse: Übergang am 7. März, Einsturz am 17. März, Todesurteile gemeldet am 18. März, eine Zeitung vom 20. März druckt den Empfang der Hitlerjungen über dem Einsturz von Remagen. "
            "Amerikanische und britische Wochenschauen: Universal und Movietone Nr. 825 am 26. März zeigen Remagen; undatiert: United News, Combat Bulletins 48 und 51, Pathé, Gaumont-British im Mai. "
            "Deutsche Wochenschau: Nr. 754 am 16. März nennt den Rhein, nicht Remagen; Nr. 755 am 22. März, die letzte, nichts aus dem Westen.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="wo-t wo-d" font-family="var(--serif)">',
         f'<title id="wo-t">{escape(title)}</title><desc id="wo-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    for d in range(6, 29, 2):
        o.append(f'<line x1="{x(d):.1f}" y1="80" x2="{x(d):.1f}" y2="{H - 30}" stroke="var(--line)"/>')
        o.append(f'<text x="{x(d):.1f}" y="{H - 12}" text-anchor="middle" font-size="11" fill="var(--ink2)">{d}{"" if en else "."}</text>')
    for y, de, eng, col in LANES:
        o.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="var(--{col})" stroke-width="3"/>')
        o.append(f'<text x="{X0 - 10}" y="{y + 4}" text-anchor="end" font-size="12.5" font-weight="bold" fill="var(--{col})">{escape(eng if en else de)}</text>')
    for lane, d, shows, de, eng, href, row in EV:
        y, col = LANES[lane][0], LANES[lane][3]
        xx = x(d)
        if shows is None:
            o.append(f'<circle cx="{xx:.1f}" cy="{y}" r="5" fill="var(--{col})"/>')
        elif shows:
            o.append(f'<rect x="{xx - 8:.1f}" y="{y - 8}" width="16" height="16" fill="var(--film)"/>')
        else:
            o.append(f'<rect x="{xx - 8:.1f}" y="{y - 8}" width="16" height="16" fill="var(--panel)" stroke="var(--deutsch)" stroke-width="2.5"/>')
        ly = {-2: y - 38, -1: y - 18, 1: y + 28}[row]
        t = eng if en else de
        lx = min(max(xx, X0 + 3.2 * len(t)), X1 - 3.2 * len(t))
        o.append(f'<a href="{href}"><text x="{lx:.1f}" y="{ly}" text-anchor="middle" font-size="12" fill="var(--ink)" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(t)}</text></a>')
    ux = X1 + 18
    o.append(f'<text x="{ux}" y="{LANES[1][0] - 40}" font-size="11.5" font-weight="bold" fill="var(--ink2)">{"undated" if en else "undatiert"}</text>')
    for k, (de, eng, href) in enumerate([("United News", "United News", "#/text/wochenschauen/united/3"), ("Combat Bulletin 48", "Combat Bulletin 48", "#/text/angriffe/film/8"),
                                          ("Combat Bulletin 51", "Combat Bulletin 51", "#/text/siebter/film/23"), ("Pathé", "Pathé", "#/films"), ("Gaumont, Mai", "Gaumont, May", "#/text/wochenschauen/britisch/5")]):
        yy = LANES[1][0] - 22 + k * 17
        o.append(f'<rect x="{ux}" y="{yy - 9}" width="10" height="10" fill="var(--film)"/>')
        o.append(f'<a href="{href}"><text x="{ux + 15}" y="{yy}" font-size="11.5" fill="var(--ink)" text-decoration="underline">{escape(eng if en else de)}</text></a>')
    o.append("</svg>")
    name = "wochenschauen-en.svg" if en else "wochenschauen.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
