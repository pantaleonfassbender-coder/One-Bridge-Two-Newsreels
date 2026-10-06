"""Zeichnet assets/viz/siebter.svg und siebter-en.svg: die Stunden des 7. März 1945 in drei Bahnen,
die amerikanische und die deutsche Seite nach MacDonald (1973) und Engemans Erinnerung im Film
(Combat Bulletin No. 51). Zeiten, die die Quelle nennt, stehen als Punkt; erschlossene als Ring.
Jede Beschriftung verweist auf die Stelle im Modul.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-siebter.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
T = "#/text/siebter/"
W, H = 900, 470
X0, X1 = 190, 875
SEG = [(8.0, 15.0, 190, 470), (15.0, 17.0, 470, 730), (17.0, 21.0, 730, 875)]  # 15–17 Uhr gedehnt


def x(h):
    for a, b, xa, xb in SEG:
        if a <= h <= b:
            return xa + (xb - xa) * (h - a) / (b - a)
    raise ValueError(h)


LANES = [  # (y, de, en, Farbe)
    (150, "Amerikaner (MacDonald)", "Americans (MacDonald)", "us"),
    (270, "Deutsche (MacDonald)", "Germans (MacDonald)", "deutsch"),
    (380, "Engeman im Film", "Engeman in the film", "film"),
]
# (Bahn, Stunde, genannt?, de, en, Verweis, Höhenversatz)
EV = [
    (0, 8 + 20 / 60, True, "8.20 Aufbruch Meckenheim", "0820 leave Meckenheim", "vormarsch/7", -1),
    (0, 11.9, False, "vor Mittag: Wald", "before noon: woods", "vormarsch/7", 1),
    (0, 12 + 55 / 60, True, "kurz vor 13: Burrows sieht die Brücke", "before 1300: Burrows sees the bridge", "vormarsch/8", -1),
    (0, 15.25, True, "15.15 Meldung aus Sinzig", "1515 message from Sinzig", "hoehe/12", -2),
    (0, 16.0, False, "gegen 16: an der Brücke", "around 1600: at the bridge", "uebergang/13", -1),
    (0, 16.2, False, "Drabik drüben", "Drabik across", "uebergang/17", 1),
    (0, 16.5, True, "16.30 Anruf beim Korps", "1630 call to corps", "meldung/20", 2),
    (0, 18.75, True, "18.45 Genehmigung", "1845 approval", "meldung/22", -1),
    (0, 20.25, True, "≈ 20.15 Ahr-Auftrag entfällt", "≈ 2015 Ahr task lifted", "meldung/22", 1),
    (1, 11.25, True, "11.15 Scheller übernimmt", "1115 Scheller takes over", None, -1),
    (1, 15.95, False, "Sperrladung", "ditch charge", "uebergang/13", 1),
    (1, 16.15, False, "Sprengung: die Brücke hebt sich", "demolition: the bridge lifts", "uebergang/14", -1),
    (1, 16.45, False, "Übergabe im Tunnel", "surrender in the tunnel", "uebergang/18", 2),
    (2, 12.0, True, "„about noon“: auf dem Hügel", "‘about noon’: on the hill", "film/23", -1),
    (2, 15.5, True, "„about 3.30“: Infanterie geht hinüber", "‘about 3.30’: infantry crosses", "film/23", 1),
    (2, 15.6, True, "Meldung „blown at 4 o'clock“", "message ‘blown at 4 o'clock’", "film/23", -1),
]


def label(xx, y, text, href, colour):
    t = (f'<text x="{xx:.1f}" y="{y}" text-anchor="middle" font-size="12" fill="var(--ink)" stroke="var(--panel)" '
         f'stroke-width="4" paint-order="stroke"{" text-decoration=" + chr(34) + "underline" + chr(34) if href else ""}>{escape(text)}</text>')
    return f'<a href="{T}{href}">{t}</a>' if href else t


def build(lang):
    en = lang == "en"
    title = "The hours of 7 March 1945" if en else "Die Stunden des 7. März 1945"
    sub = ("Dots: times given in the source; rings: inferred. The Engeman lane is memory, recorded after the event."
           if en else "Punkte: Zeiten, die die Quelle nennt; Ringe: erschlossen. Die Bahn Engeman ist Erinnerung, nach dem Ereignis aufgenommen.")
    desc = ("A timeline from 8 a.m. to 9 p.m. on 7 March 1945 in three lanes. Americans after MacDonald: departure from Meckenheim at 0820, "
            "the woods before noon, Burrows sees the bridge shortly before 1300, a message from Sinzig at 1515, at the bridge around 1600, "
            "Drabik across, a call to corps at 1630, approval at 1845, the Ahr task lifted about 2015. Germans after MacDonald: Scheller takes "
            "command at 1115, the ditch charge, the demolition lifts the bridge, the surrender in the tunnel, all around 1600. Engeman in the film: "
            "about noon on the hill, about 3.30 the infantry crosses, a message that the bridge would be blown at 4 o'clock."
            if en else
            "Eine Zeitleiste von 8 bis 21 Uhr am 7. März 1945 in drei Bahnen. Amerikaner nach MacDonald: Aufbruch in Meckenheim um 8.20 Uhr, "
            "vor Mittag der Wald, kurz vor 13 Uhr sieht Burrows die Brücke, um 15.15 Uhr die Meldung aus Sinzig, gegen 16 Uhr an der Brücke, "
            "Drabik drüben, um 16.30 Uhr der Anruf beim Korps, um 18.45 Uhr die Genehmigung, gegen 20.15 Uhr wird der Ahr-Auftrag aufgehoben. "
            "Deutsche nach MacDonald: um 11.15 Uhr übernimmt Scheller, gegen 16 Uhr die Sperrladung, die Sprengung hebt die Brücke, die Übergabe im Tunnel. "
            "Engeman im Film: gegen Mittag auf dem Hügel, gegen halb vier geht die Infanterie hinüber, Meldung, um vier Uhr werde gesprengt.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sb-t sb-d" font-family="var(--serif)">',
         f'<title id="sb-t">{escape(title)}</title><desc id="sb-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    # Stundenraster
    o.append(f'<text x="{(x(15) + x(17)) / 2:.1f}" y="92" text-anchor="middle" font-size="11" fill="var(--ink2)">{"1500–1700 stretched" if en else "15–17 Uhr gedehnt"}</text>')
    for h in [8, 9, 10, 11, 12, 13, 14, 15, 15.5, 16, 16.5, 17, 18, 19, 20, 21]:
        xx = x(h)
        o.append(f'<line x1="{xx:.1f}" y1="80" x2="{xx:.1f}" y2="{H - 30}" stroke="var(--line)" stroke-width="1"/>')
        o.append(f'<text x="{xx:.1f}" y="{H - 12}" text-anchor="middle" font-size="11" fill="var(--ink2)">{int(h)}:{"30" if h % 1 else "00"}</text>')
    # Brennpunkt 15.30–16.45
    o.append(f'<rect x="{x(15.5):.1f}" y="80" width="{x(16.75) - x(15.5):.1f}" height="{H - 110}" fill="var(--bruecke)" opacity="0.08"/>')
    for i, (y, de, enl, col) in enumerate(LANES):
        o.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="var(--{col})" stroke-width="3"/>')
        o.append(f'<text x="16" y="{y + 4}" font-size="13" font-weight="bold" fill="var(--{col})">{escape(enl if en else de)}</text>')
    for lane, h, given, de, enl, href, dy in EV:
        y = LANES[lane][0]
        col = LANES[lane][3]
        xx = x(h)
        if given:
            o.append(f'<circle cx="{xx:.1f}" cy="{y}" r="6" fill="var(--{col})"/>')
        else:
            o.append(f'<circle cx="{xx:.1f}" cy="{y}" r="6" fill="var(--panel)" stroke="var(--{col})" stroke-width="2.5"/>')
        ly = {-2: y - 40, -1: y - 18, 1: y + 28, 2: y + 50}[dy]
        o.append(f'<line x1="{xx:.1f}" y1="{y}" x2="{xx:.1f}" y2="{ly + 4 if dy < 0 else ly - 12}" stroke="var(--{col})" stroke-width="1"/>')
        o.append(label(min(xx, W - 8 - 3.2 * len(enl if en else de)), ly, enl if en else de, href, col))
    o.append("</svg>")
    name = "siebter-en.svg" if en else "siebter.svg"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build("de")
build("en")
