"""Zeichnet assets/viz/brueckenkopf.svg und brueckenkopf-en.svg: die Wege über den Rhein vom 7. bis
25. März 1945 nach MacDonald (1973), S. 219–233. Balken: in Betrieb; gestreift: gesperrt; Rauten:
Eröffnung. Unten die Wendepunkte des Brückenkopfes. Jede Zeile verweist auf ihre Stelle im Modul.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-brueckenkopf.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
T = "#/text/brueckenkopf/"
W, H = 900, 520
X0, X1, D0, D1 = 250, 880, 7, 25.6


def x(d):
    return X0 + (X1 - X0) * (d - D0) / (D1 - D0)


# (de, en, [(von, bis, Art)], Verweis, Farbe)  Art: "on" in Betrieb, "off" gesperrt, "x" Einsturz
ROWS = [
    ("Ludendorff-Brücke", "Ludendorff Bridge", [(7.67, 13, "on"), (13, 17.6, "off"), (17.6, 17.6, "x")], "uebergaenge/12", "bruecke"),
    ("Fähren aus Pontons", "Ponton ferries", [(9.3, 25.6, "on")], "uebergaenge/11", "us"),
    ("Schwimmlastwagen (DUKW)", "Amphibious trucks (DUKW)", [(14, 25.6, "on")], "uebergaenge/11", "us"),
    ("Pontonbrücke Remagen–Erpel", "Treadway Remagen–Erpel", [(10, 11.3, "build"), (11.3, 25.6, "on")], "uebergaenge/12", "us"),
    ("Schwere Pontonbrücke Linz", "Heavy ponton Linz", [(12, 25.6, "on")], "uebergaenge/12", "us"),
    ("Drei Brücken des VII. Korps", "Three VII Corps bridges", [(17.9, 25.6, "on"), (19, 25.6, "on"), (21, 25.6, "on")], "ausweitung/17", "us"),
    ("Bailey-Brücke", "Bailey bridge", [(18, 20, "build"), (20, 25.6, "on")], "uebergaenge/13", "us"),
]
EV = [  # (Tag, de, en, Verweis)
    (7.67, "Übergang", "crossing", "#/text/siebter/uebergang/17"),
    (9, "1 000 Yards/Tag", "1,000 yards/day", T + "auflagen/4"),
    (13, "Eisenhowers Weisung", "Eisenhower's directive", T + "auflagen/6"),
    (17.6, "Einsturz", "collapse", "#/timeline"),
    (21, "an der Sieg", "at the Sieg", T + "ausweitung/17"),
    (24, "dt. Gegenangriff", "German counterattack", T + "ausweitung/18"),
    (25, "Ausbruch", "breakout", "#/timeline"),
]


def build(en):
    title = "Ways across the Rhine" if en else "Wege über den Rhein"
    sub = ("7–25 March 1945, after MacDonald. Bars: in use; hatched: closed; light: under construction."
           if en else "7.–25. März 1945, nach MacDonald. Balken: in Betrieb; schraffiert: gesperrt; hell: im Bau.")
    desc = ("A chart of the crossings at Remagen from 7 to 25 March 1945 after MacDonald. The Ludendorff Bridge is in use from the evening of 7 March, closed for repairs from 13 March and collapses on 17 March. "
            "Ponton ferries run from 9 March, amphibious trucks from 14 March. The treadway bridge from Remagen to Erpel is built from 10 March and opened on 11 March; a heavy ponton bridge at Linz opens at midnight on 11 March. "
            "Three VII Corps bridges open on 17, 19 and 21 March, a Bailey bridge on 20 March. Below: the crossing on 7 March, the limit of a thousand yards a day on 9 March, Eisenhower's directive on 13 March, the collapse on 17 March, the Sieg on 21 March, the German counterattack on 24 March and the breakout on 25 March."
            if en else
            "Ein Schema der Übergänge bei Remagen vom 7. bis 25. März 1945 nach MacDonald. Die Ludendorff-Brücke ist ab dem Abend des 7. März in Betrieb, ab dem 13. März zur Ausbesserung gesperrt und stürzt am 17. März ein. "
            "Fähren aus Pontons fahren ab dem 9. März, Schwimmlastwagen ab dem 14. März. Die Pontonbrücke Remagen–Erpel wird ab dem 10. März gebaut und am 11. März eröffnet; eine schwere Pontonbrücke bei Linz um Mitternacht am 11. März. "
            "Drei Brücken des VII. Korps werden am 17., 19. und 21. März fertig, eine Bailey-Brücke am 20. März. Unten: der Übergang am 7. März, die Auflage von tausend Yards am Tag am 9. März, Eisenhowers Weisung am 13. März, der Einsturz am 17. März, die Sieg am 21. März, der deutsche Gegenangriff am 24. März und der Ausbruch am 25. März.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="bk-t bk-d" font-family="var(--serif)">',
         f'<title id="bk-t">{escape(title)}</title><desc id="bk-d">{escape(desc)}</desc>',
         '<defs><pattern id="bk-h" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="var(--panel)"/><line x1="0" y1="0" x2="0" y2="8" stroke="var(--bruecke)" stroke-width="3"/></pattern></defs>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    top, rh = 80, 40
    bottom = top + rh * len(ROWS)
    for d in range(7, 26):
        o.append(f'<line x1="{x(d):.1f}" y1="{top - 8}" x2="{x(d):.1f}" y2="{bottom + 70}" stroke="var(--line)"/>')
        if d % 2 == 1:
            o.append(f'<text x="{x(d):.1f}" y="{bottom + 92}" text-anchor="middle" font-size="11" fill="var(--ink2)">{d}{"" if en else "."}</text>')
    o.append(f'<text x="{X1}" y="{bottom + 108}" text-anchor="end" font-size="11" fill="var(--ink2)">{"March 1945" if en else "März 1945"}</text>')
    for i, (de, eng, spans, href, col) in enumerate(ROWS):
        y = top + i * rh
        o.append(f'<a href="{T}{href}"><text x="{X0 - 10}" y="{y + 20}" text-anchor="end" font-size="13" fill="var(--ink)" text-decoration="underline">{escape(eng if en else de)}</text></a>')
        for a, b, kind in spans:
            if kind == "x":
                o.append(f'<text x="{x(a):.1f}" y="{y + 25}" text-anchor="middle" font-size="22" font-weight="bold" fill="var(--film)">✕</text>')
                continue
            fill = {"on": f"var(--{col})", "off": "url(#bk-h)", "build": f"var(--{col})"}[kind]
            op = ' opacity="0.3"' if kind == "build" else ""
            o.append(f'<rect x="{x(a):.1f}" y="{y + 8}" width="{max(x(b) - x(a), 2):.1f}" height="18" rx="3" fill="{fill}"{op}/>')
            if kind == "on" and a > 7.7:
                o.append(f'<path d="M{x(a):.1f},{y + 3} l6,14 l-6,14 l-6,-14 z" fill="var(--panel)" stroke="var(--{col})" stroke-width="2"/>')
    ly = bottom + 30
    o.append(f'<line x1="{X0}" y1="{ly}" x2="{X1}" y2="{ly}" stroke="var(--ink2)" stroke-width="2"/>')
    for k, (d, de, eng, href) in enumerate(EV):
        o.append(f'<circle cx="{x(d):.1f}" cy="{ly}" r="5" fill="var(--ink2)"/>')
        yy = ly + (22 if k % 2 == 0 else -10)
        o.append(f'<a href="{href}"><text x="{x(d):.1f}" y="{yy}" text-anchor="middle" font-size="11.5" fill="var(--ink)" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(eng if en else de)}</text></a>')
    o.append(f'<text x="{X0 - 10}" y="{ly + 4}" text-anchor="end" font-size="13" font-weight="bold" fill="var(--ink2)">{"Turning points" if en else "Wendepunkte"}</text>')
    o.append("</svg>")
    name = "brueckenkopf-en.svg" if en else "brueckenkopf.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
