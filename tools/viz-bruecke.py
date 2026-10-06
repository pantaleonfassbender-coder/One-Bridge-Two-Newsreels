"""Zeichnet assets/viz/bruecke.svg und bruecke-en.svg: das Leben der Brücke 1916–1945 als Zeitachse
nach den Quellen von Modul 1 und MacDonald. Oben die Brücke, unten die Zeit um sie herum (Kriege,
Besatzung). Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-bruecke.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
T = "#/text/"
W, H = 900, 400
X0, X1, Y0, Y1 = 40, 870, 1916, 1945.4


SEG = [(1916, 1920, X0, 360), (1920, Y1, 360, X1)]  # 1916–1920 gedehnt


def x(y):
    for a, b, xa, xb in SEG:
        if a <= y <= b:
            return xa + (xb - xa) * (y - a) / (b - a)
    raise ValueError(y)


BANDS = [  # (von, bis, de, en, Farbe)
    (1916, 1918.86, "Erster Weltkrieg", "First World War", "deutsch"),
    (1918.9, 1925.93, "Besatzung, Wache auf der Brücke", "occupation, guard on the bridge", "us"),
    (1939.67, 1945.4, "Zweiter Weltkrieg", "Second World War", "deutsch"),
]
EV = [  # (Jahr, de, en, Verweis, Reihe)
    (1916.3, "Bau (nach MacDonald 1916)", "built (MacDonald: 1916)", "bruecke/bau/1", -2),
    (1918.33, "Mai 1918: Name Ludendorff", "May 1918: named Ludendorff", "bruecke/bau/2", -1),
    (1918.62, "Aug. 1918: Einweihung", "Aug 1918: dedication", "bruecke/bau/3", 1),
    (1918.86, "10.11.1918: Fußgänger", "10 Nov 1918: pedestrians", "bruecke/kriegsende/4", 2),
    (1918.9, "Nov. 1918: 7. Armee zurück", "Nov 1918: 7th Army returns", "bruecke/kriegsende/5", -3),
    (1925.93, "Dez. 1925: Wache zieht ab", "Dec 1925: guard leaves", "bruecke/kriegsende/6", -1),
    (1928.22, "März 1928: Brand", "Mar 1928: fire", "bruecke/alltag/7", 1),
    (1928.88, "Nov. 1928: Eisenplatten", "Nov 1928: iron plates", "bruecke/alltag/8", 2),
    (1935.3, "1935: wenige Züge", "1935: few trains", "bruecke/alltag/9", -1),
    (1938, "1938: Sprengplan", "1938: demolition scheme", "warum/sprengplan/9", 1),
    (1940, "ab 1940: Luftangriffe", "from 1940: air raids", "bruecke/krieg/10", -2),
    (1944.85, "Ende 1944: 15 Tage gesperrt", "late 1944: closed 15 days", "bruecke/krieg/10", 2),
    (1945.18, "7.3.1945", "7 Mar 1945", "siebter/uebergang/14", -1),
]


def build(en):
    title = "The life of the bridge" if en else "Das Leben der Brücke"
    sub = "1916–1945, after the newspapers of the time and MacDonald; 1916–1920 stretched." if en else "1916–1945, nach den Zeitungen der Zeit und MacDonald; 1916–1920 gedehnt."
    desc = ("A timeline from 1916 to 1945. Built during the First World War; named after Ludendorff in May 1918; dedicated in August 1918; opened to pedestrians on 10 November 1918; "
            "the 7th Army returns across it at the end of November 1918; a guard stands on it under occupation until December 1925; the decking burns in March 1928 and is replaced by iron plates by November 1928; "
            "in 1935 only a few trains use it; in 1938 a demolition scheme is prepared; from 1940 Allied air raids; at the end of 1944 it is closed for fifteen days; on 7 March 1945 it is captured."
            if en else
            "Eine Zeitleiste von 1916 bis 1945. Im Ersten Weltkrieg gebaut; im Mai 1918 nach Ludendorff benannt; im August 1918 eingeweiht; am 10. November 1918 für Fußgänger freigegeben; "
            "Ende November 1918 marschiert die 7. Armee über sie zurück; unter Besatzung steht bis Dezember 1925 eine Wache auf ihr; im März 1928 brennt der Belag und wird bis November 1928 durch Eisenplatten ersetzt; "
            "1935 fahren nur wenige Züge; 1938 wird ein Sprengplan vorbereitet; ab 1940 alliierte Luftangriffe; Ende 1944 fünfzehn Tage gesperrt; am 7. März 1945 genommen.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="br-t br-d" font-family="var(--serif)">',
         f'<title id="br-t">{escape(title)}</title><desc id="br-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    ly = 200
    for a, b, de, eng, col in BANDS:
        o.append(f'<rect x="{x(a):.1f}" y="{ly + 70}" width="{x(b) - x(a):.1f}" height="26" rx="4" fill="var(--{col})" opacity="0.25"/>')
        o.append(f'<text x="{(x(a) + x(b)) / 2:.1f}" y="{ly + 88}" text-anchor="middle" font-size="12" fill="var(--ink)">{escape(eng if en else de)}</text>')
    for yr in [1916, 1917, 1918, 1919, 1920] + list(range(1922, 1946, 2)):
        o.append(f'<line x1="{x(yr):.1f}" y1="{ly - 6}" x2="{x(yr):.1f}" y2="{ly + 6}" stroke="var(--ink2)"/>')
        o.append(f'<text x="{x(yr):.1f}" y="{ly + 120}" text-anchor="middle" font-size="11" fill="var(--ink2)">{yr}</text>')
    o.append(f'<line x1="{X0}" y1="{ly}" x2="{X1}" y2="{ly}" stroke="var(--bruecke)" stroke-width="4"/>')
    for yr, de, eng, href, row in EV:
        xx = x(yr)
        o.append(f'<circle cx="{xx:.1f}" cy="{ly}" r="5.5" fill="var(--bruecke)"/>')
        yy = {-3: ly - 98, -2: ly - 62, -1: ly - 26, 1: ly + 30, 2: ly + 56}[row]
        o.append(f'<line x1="{xx:.1f}" y1="{ly}" x2="{xx:.1f}" y2="{yy + 4 if row < 0 else yy - 12}" stroke="var(--bruecke)"/>')
        t = eng if en else de
        lx = min(max(xx, X0 + 3.2 * len(t)), W - 8 - 3.2 * len(t))
        o.append(f'<a href="{T}{href}"><text x="{lx:.1f}" y="{yy}" text-anchor="middle" font-size="12" fill="var(--ink)" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(t)}</text></a>')
    o.append("</svg>")
    name = "bruecke-en.svg" if en else "bruecke.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
