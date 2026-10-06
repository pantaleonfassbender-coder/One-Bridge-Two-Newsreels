"""Zeichnet assets/viz/warum.svg und warum-en.svg: Wer an der Brücke von Remagen am 7. März 1945
wem unterstand, nach MacDonald (1973), S. 209–214. Durchgezogene Linien: Unterstellung; gestrichelt:
versuchte Verbindung, die nicht zustande kam. Jedes Feld verweist auf die Stelle im Modul.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-warum.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
T = "#/text/warum/"
W, H = 900, 560
BW, BH = 168, 50

# id: (x, y, de1, de2, en1, en2, Farbe, Verweis)
B = {
    "hgb": (60, 80, "Heeresgruppe B", "Model", "Army Group B", "Model", "deutsch", "befehle/3"),
    "a15": (60, 190, "15. Armee", "von Zangen", "Fifteenth Army", "von Zangen", "deutsch", "scheller/5"),
    "k67": (60, 300, "LXVII. Korps", "Hitzfeld", "LXVII Corps", "Hitzfeld", "deutsch", "scheller/6"),
    "botsch": (300, 190, "Botsch", "6.3., 17 Uhr fort", "Botsch", "left 6 Mar, 1700", "deutsch", "befehle/4"),
    "bonn": (300, 80, "Bonn", "von Bothmer", "Bonn", "von Bothmer", "deutsch", "befehle/3"),
    "luft": (540, 80, "Luftwaffe", "", "Luftwaffe", "", "deutsch", "befehle/2"),
    "partei": (730, 80, "NSDAP", "Funktionäre", "Nazi party", "officials", "deutsch", "befehle/1"),
    "okw": (730, 300, "OKW-Befehl", "schriftlich, spät", "OKW order", "in writing, late", "bruecke", "sprengplan/10"),
    "scheller": (60, 430, "Scheller", "ab 11.15 Uhr", "Scheller", "from 1115", "deutsch", "bratge/15"),
    "bratge": (250, 430, "Bratge", "Kampfkommandant", "Bratge", "combat commander", "deutsch", "bratge/11"),
    "fries": (440, 430, "Friesenhahn", "Brückenkommandant", "Friesenhahn", "bridge commander", "bruecke", "befehle/1"),
    "flak": (540, 300, "Flak", "keinem unterstellt", "Antiaircraft", "under neither", "deutsch", "bratge/12"),
    "vs": (730, 190, "Volkssturm", "Bratge nicht unterstellt", "Volkssturm", "not under Bratge", "menschen", "bratge/12"),
}
# (von, nach, Art)  Art: "s" Unterstellung, "d" versucht/gescheitert, "o" Befehl wirkt auf
E = [
    ("a15", "hgb", "s"), ("k67", "a15", "s"), ("scheller", "k67", "s"), ("botsch", "a15", "s"),
    ("flak", "luft", "s"), ("vs", "partei", "s"), ("okw", "fries", "o"), ("bratge", "scheller", "o"),
]
# Linien mit Knick: (Punkte, Art)
PATHS = [
    ([(280, 430), (280, 105), (228, 105)], "d"),   # Bratge -> Heeresgruppe B
    ([(384, 430), (384, 240)], "d"),               # Bratge -> Botsch
    ([(144, 480), (144, 492), (524, 492), (524, 480)], "o"),  # Scheller -> Friesenhahn
]


def poly(pts, kind):
    dash = ' stroke-dasharray="6 5"' if kind == "d" else ' stroke-dasharray="2 4"'
    col = "var(--film)" if kind == "d" else "var(--bruecke)"
    d = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2"{dash} marker-end="url(#ar-{kind})"/>'



def c(k, side):
    x, y = B[k][0], B[k][1]
    return {"t": (x + BW / 2, y), "b": (x + BW / 2, y + BH), "l": (x, y + BH / 2), "r": (x + BW, y + BH / 2)}[side]


def edge(a, b, kind):
    ax, ay = B[a][0], B[a][1]
    bx, by = B[b][0], B[b][1]
    if abs(ay - by) < 5:
        p, q = (c(a, "r"), c(b, "l")) if ax < bx else (c(a, "l"), c(b, "r"))
    elif ay > by:
        p, q = c(a, "t"), c(b, "b")
    else:
        p, q = c(a, "b"), c(b, "t")
    dash = ' stroke-dasharray="6 5"' if kind == "d" else (' stroke-dasharray="2 4"' if kind == "o" else "")
    col = "var(--film)" if kind == "d" else ("var(--bruecke)" if kind == "o" else "var(--ink2)")
    return f'<line x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}" stroke="{col}" stroke-width="2"{dash} marker-end="url(#ar-{kind})"/>'


def build(en):
    title = "Who commanded at the bridge?" if en else "Wer befahl an der Brücke?"
    sub = ("7 March 1945, after MacDonald. Solid: subordination; dashed: contact attempted and failed; dotted: order acting on."
           if en else "7. März 1945, nach MacDonald. Durchgezogen: Unterstellung; gestrichelt: versuchte Verbindung, gescheitert; gepunktet: Befehl wirkt auf.")
    desc = ("A chart of command at the Remagen bridge on 7 March 1945 after MacDonald. Army Group B under Model above the Fifteenth Army under von Zangen, "
            "above the LXVII Corps under Hitzfeld, which sent Major Scheller, in command from 1115. General Botsch, under the Fifteenth Army, left on 6 March at 1700; "
            "Bonn under von Bothmer. Captain Bratge, combat commander, tried and failed to reach Army Group B and Botsch, and handed command to Scheller. "
            "Captain Friesenhahn, bridge commander, was bound by the OKW order requiring written demolition orders. Antiaircraft troops answered to the Luftwaffe, "
            "the Volkssturm to Nazi party officials, neither to Bratge."
            if en else
            "Ein Schema der Befehlswege an der Brücke von Remagen am 7. März 1945 nach MacDonald. Über der 15. Armee unter von Zangen die Heeresgruppe B unter Model, "
            "darunter das LXVII. Korps unter Hitzfeld, das Major Scheller schickte, der ab 11.15 Uhr befahl. General Botsch, der 15. Armee unterstellt, ging am 6. März um 17 Uhr; "
            "Bonn unter von Bothmer. Hauptmann Bratge, Kampfkommandant, versuchte vergeblich, die Heeresgruppe B und Botsch zu erreichen, und gab den Befehl an Scheller ab. "
            "Hauptmann Friesenhahn, Brückenkommandant, war an den OKW-Befehl gebunden, der den Sprengbefehl schriftlich verlangte. Die Flak unterstand der Luftwaffe, "
            "der Volkssturm Funktionären der NSDAP, beide nicht Bratge.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="wa-t wa-d" font-family="var(--serif)">',
         f'<title id="wa-t">{escape(title)}</title><desc id="wa-d">{escape(desc)}</desc><defs>']
    for k, col in (("s", "var(--ink2)"), ("d", "var(--film)"), ("o", "var(--bruecke)")):
        o.append(f'<marker id="ar-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
    o.append("</defs>")
    o.append(f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>')
    o.append(f'<text x="16" y="50" font-size="13" fill="var(--ink2)">{escape(sub)}</text>')
    o.append(f'<rect x="40" y="410" width="590" height="90" rx="10" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>')
    o.append(f'<text x="50" y="520" font-size="12" fill="var(--ink2)">{"At the bridge" if en else "An der Brücke"}</text>')
    for a, b, k in E:
        o.append(edge(a, b, k))
    for pts, k in PATHS:
        o.append(poly(pts, k))
    for k, (x, y, d1, d2, e1, e2, col, href) in B.items():
        t1, t2 = (e1, e2) if en else (d1, d2)
        o.append(f'<a href="{T}{href}"><rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="8" fill="var(--panel)" stroke="var(--{col})" stroke-width="2"/>'
                 f'<text x="{x + BW / 2}" y="{y + 21}" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{escape(t1)}</text>'
                 f'<text x="{x + BW / 2}" y="{y + 39}" text-anchor="middle" font-size="12" fill="var(--ink2)">{escape(t2)}</text></a>')
    o.append("</svg>")
    name = "warum-en.svg" if en else "warum.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
