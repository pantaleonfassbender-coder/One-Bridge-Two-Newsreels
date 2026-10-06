"""Zeichnet assets/viz/standgericht.svg und standgericht-en.svg: 7.–21. März 1945 in zwei Bahnen,
oben was geschah, unten was der Wehrmachtbericht und das DNB meldeten. Dazwischen die Spanne, in der
die Brücke in den gefundenen Wehrmachtberichten nicht vorkommt. Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-standgericht.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
W, H = 900, 430
X0, X1, D0, D1 = 100, 870, 7, 21
YA, YB = 150, 300


def x(d):
    return X0 + (X1 - X0) * (d - D0) / (D1 - D0)


# (Bahn, Tag, de, en, Verweis, Reihe, Farbe)
EV = [
    (0, 7, "Brücke genommen", "bridge taken", "#/text/siebter/uebergang/17", -1, "us"),
    (0, 9, "Hitler: fliegende Standgerichte", "Hitler: flying courts-martial", "#/text/standgericht/hitler/6", 1, "deutsch"),
    (0, 10, "Kesselring OB West", "Kesselring C-in-C West", "#/text/standgericht/hitler/5", -2, "deutsch"),
    (0, 13.5, "vier erschossen bei Rimbach", "four shot near Rimbach", "#/text/standgericht/hitler/6", -1, "deutsch"),
    (0, 17, "Einsturz", "collapse", "#/timeline", 1, "bruecke"),
    (0, 21, "Erlass beim Stab bekannt", "decree made known", "#/text/standgericht/erlass/8", -1, "deutsch"),
    (1, 8, "„bis Remagen“", "‘as far as Remagen’", "#/text/standgericht/bericht/1", 1, "film"),
    (1, 9, "Remagen fehlt", "Remagen missing", "#/text/standgericht/bericht/2", 2, "film"),
    (1, 11, "„über den Strom gesetzt“ (DNB)", "‘crossed the river’ (DNB)", "#/text/standgericht/bericht/3", -1, "film"),
    (1, 11.15, "„ihr Brückenkopf“", "‘their bridgehead’", "#/text/standgericht/bericht/4", 1, "film"),
    (1, 18, "„Rheinbrücke bei Remagen“: Todesurteile", "‘Rhine bridge at Remagen’: death sentences", "#/text/standgericht/okw/7", 1, "film"),
]


def build(en):
    title = "What happened, what was reported" if en else "Was geschah, was gemeldet wurde"
    sub = ("7–21 March 1945. Above: events after MacDonald and the Bundesarchiv; below: Wehrmacht report and DNB in the newspapers."
           if en else "7.–21. März 1945. Oben: Ereignisse nach MacDonald und dem Bundesarchiv; unten: Wehrmachtbericht und DNB in den Zeitungen.")
    gap = "the bridge is not named in the Wehrmacht reports found" if en else "die Brücke wird in den gefundenen Wehrmachtberichten nicht genannt"
    desc = ("Two timelines from 7 to 21 March 1945. Above: the bridge is taken on 7 March; on 9 March Hitler sets up flying courts-martial; on 10 March Kesselring takes command in the west; "
            "on 13 and 14 March four officers are shot near Rimbach; on 17 March the bridge collapses; on 21 March Kesselring's decree is made known to a staff. Below: on 8 March the Wehrmacht report has "
            "American spearheads ‘as far as Remagen’; on 9 March Remagen is missing; on 11 March the DNB speaks of forces that ‘crossed the river’ and the Wehrmacht report of ‘their bridgehead’; "
            "on 18 March the Wehrmacht report announces the death sentences and names the Rhine bridge at Remagen. Between 7 and 18 March the bridge is not named in the reports found."
            if en else
            "Zwei Zeitleisten vom 7. bis 21. März 1945. Oben: Am 7. März wird die Brücke genommen; am 9. März setzt Hitler fliegende Standgerichte ein; am 10. März übernimmt Kesselring den Befehl im Westen; "
            "am 13. und 14. März werden vier Offiziere bei Rimbach erschossen; am 17. März stürzt die Brücke ein; am 21. März wird Kesselrings Erlass einem Stab bekanntgegeben. Unten: Am 8. März meldet der Wehrmachtbericht "
            "amerikanische Panzerspitzen „bis Remagen“; am 9. März fehlt Remagen; am 11. März spricht das DNB von Kräften, die „über den Strom gesetzt“ sind, und der Wehrmachtbericht von „ihrem Brückenkopf“; "
            "am 18. März meldet der Wehrmachtbericht die Todesurteile und nennt dabei die Rheinbrücke bei Remagen. Zwischen dem 7. und dem 18. März wird die Brücke in den gefundenen Berichten nicht genannt.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sg-t sg-d" font-family="var(--serif)">',
         f'<title id="sg-t">{escape(title)}</title><desc id="sg-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    o.append(f'<rect x="{x(7):.0f}" y="{YA + 40}" width="{x(18) - x(7):.0f}" height="{YB - YA - 80}" fill="var(--film)" opacity="0.08"/>')
    o.append(f'<text x="{(x(7) + x(18)) / 2:.0f}" y="{(YA + YB) / 2 + 4:.0f}" text-anchor="middle" font-size="13" font-style="italic" fill="var(--film)">{escape(gap)}</text>')
    for d in range(7, 22):
        o.append(f'<line x1="{x(d):.1f}" y1="80" x2="{x(d):.1f}" y2="{H - 40}" stroke="var(--line)"/>')
        o.append(f'<text x="{x(d):.1f}" y="{H - 22}" text-anchor="middle" font-size="11" fill="var(--ink2)">{d}{"" if en else "."}</text>')
    o.append(f'<text x="{X1:.0f}" y="{H - 6}" text-anchor="end" font-size="11" fill="var(--ink2)">{"March 1945" if en else "März 1945"}</text>')
    for y, lab in ((YA, "happened" if en else "geschah"), (YB, "reported" if en else "gemeldet")):
        o.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="var(--ink2)" stroke-width="3"/>')
        o.append(f'<text x="{X0 - 6}" y="{y + 4}" text-anchor="end" font-size="12" font-weight="bold" fill="var(--ink2)">{escape(lab)}</text>')
    for lane, d, de, eng, href, row, col in EV:
        y = YA if lane == 0 else YB
        xx = x(d)
        o.append(f'<circle cx="{xx:.1f}" cy="{y}" r="6" fill="var(--{col})"/>')
        ly = {-2: y - 42, -1: y - 18, 1: y + 28, 2: y + 50}[row]
        o.append(f'<line x1="{xx:.1f}" y1="{y}" x2="{xx:.1f}" y2="{ly + 4 if row < 0 else ly - 12}" stroke="var(--{col})"/>')
        t = eng if en else de
        lx = min(max(xx, X0 + 3.3 * len(t)), W - 8 - 3.3 * len(t))
        o.append(f'<a href="{href}"><text x="{lx:.1f}" y="{ly}" text-anchor="middle" font-size="12" fill="var(--ink)" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(t)}</text></a>')
    o.append("</svg>")
    name = "standgericht-en.svg" if en else "standgericht.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
