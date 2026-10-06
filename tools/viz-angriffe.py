"""Zeichnet assets/viz/angriffe.svg und angriffe-en.svg nach MacDonald (1973), S. 228: links die
367 angreifenden Flugzeuge nach der Schätzung der amerikanischen Flak, rechts die elf V-2 nach ihrem
Einschlagort, als Schema (nicht maßstäblich). Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-angriffe.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
T = "#/text/angriffe/"
W, H = 900, 440


def build(en):
    title = "Aircraft and rockets against the bridge" if en else "Flugzeuge und Raketen gegen die Brücke"
    sub = ("8–17 March 1945, after MacDonald. Aircraft: American antiaircraft estimates; rockets: schematic, not to scale."
           if en else "8.–17. März 1945, nach MacDonald. Flugzeuge: Schätzung der amerikanischen Flak; Raketen: Schema, nicht maßstäblich.")
    desc = ("Left: 367 German aircraft attacked from 8 to 16 March; American antiaircraft units estimated 109 destroyed and 36 probably destroyed, leaving 222. "
            "Right: eleven V-2 rockets fired from 12 to 17 March: one hit a house 300 yards east of the bridge, killing three American soldiers and wounding fifteen; three fell in the river near the bridge; five west of the bridge; one near Cologne; one never located."
            if en else
            "Links: 367 deutsche Flugzeuge griffen vom 8. bis 16. März an; die amerikanische Flak schätzte 109 zerstört und 36 wahrscheinlich zerstört, 222 übrige. "
            "Rechts: elf V-2 vom 12. bis 17. März: eine traf ein Haus 300 Yards östlich der Brücke, drei amerikanische Soldaten tot, fünfzehn verwundet; drei fielen nahe der Brücke in den Fluss; fünf westlich der Brücke; eine bei Köln; eine wurde nie gefunden.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="an-t an-d" font-family="var(--serif)">',
         f'<title id="an-t">{escape(title)}</title><desc id="an-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    # links: Flugzeuge als Punktraster, 367 Punkte
    o.append(f'<a href="{T}luftwaffe/3"><text x="30" y="84" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"367 attacking aircraft" if en else "367 angreifende Flugzeuge"}</text></a>')
    cols, r, gap, x0, y0 = 23, 4.2, 11.5, 36, 104
    for i in range(367):
        cx, cy = x0 + (i % cols) * gap, y0 + (i // cols) * gap
        if i < 109:
            o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="var(--deutsch)"/>')
        elif i < 145:
            o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="var(--panel)" stroke="var(--deutsch)" stroke-width="1.5"/>')
        else:
            o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r - 1.6}" fill="var(--line)"/>')
    ly = y0 + 16 * gap + 18
    for k, (lab, de, en_) in enumerate([("fill", "109 zerstört", "109 destroyed"), ("ring", "36 wahrscheinlich", "36 probably"), ("dot", "222 übrige", "222 others")]):
        xx = 40 + k * 140
        if lab == "fill":
            o.append(f'<circle cx="{xx}" cy="{ly}" r="5" fill="var(--deutsch)"/>')
        elif lab == "ring":
            o.append(f'<circle cx="{xx}" cy="{ly}" r="5" fill="var(--panel)" stroke="var(--deutsch)" stroke-width="1.5"/>')
        else:
            o.append(f'<circle cx="{xx}" cy="{ly}" r="3" fill="var(--line)"/>')
        o.append(f'<text x="{xx + 9}" y="{ly + 4}" font-size="12" fill="var(--ink)">{escape(en_ if en else de)}</text>')
    # rechts: Schema Rhein, Brücke, Einschläge
    rx = 470
    o.append(f'<a href="{T}fernwaffen/6"><text x="{rx}" y="84" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"Eleven V-2s, 12–17 March" if en else "Elf V-2, 12.–17. März"}</text></a>')
    o.append(f'<path d="M{rx + 150},100 C{rx + 170},200 {rx + 140},300 {rx + 170},400 L{rx + 230},400 C{rx + 200},300 {rx + 230},200 {rx + 210},100 Z" fill="var(--us)" opacity="0.18"/>')
    o.append(f'<text x="{rx + 175}" y="150" text-anchor="middle" font-size="12" font-style="italic" fill="var(--ink2)">{"Rhine" if en else "Rhein"}</text>')
    by = 250
    o.append(f'<line x1="{rx + 120}" y1="{by}" x2="{rx + 250}" y2="{by}" stroke="var(--bruecke)" stroke-width="6"/>')
    o.append(f'<text x="{rx + 185}" y="{by - 12}" text-anchor="middle" font-size="12" fill="var(--bruecke)">{"bridge" if en else "Brücke"}</text>')
    o.append(f'<text x="{rx + 20}" y="{by + 4}" font-size="12" fill="var(--ink2)">{"west: Remagen" if en else "West: Remagen"}</text>')
    o.append(f'<text x="{rx + 290}" y="{by + 4}" font-size="12" fill="var(--ink2)">{"east: Erpel" if en else "Ost: Erpel"}</text>')
    X = lambda x, y: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="18" font-weight="bold" fill="var(--film)">✕</text>'
    o.append(X(rx + 300, by + 50))
    o.append(f'<text x="{W - 10}" y="{by + 72}" text-anchor="end" font-size="11.5" fill="var(--ink)">{"house, 300 yd east:" if en else "Haus, 300 Yards östlich:"}</text>')
    o.append(f'<text x="{W - 10}" y="{by + 87}" text-anchor="end" font-size="11.5" fill="var(--ink)">{"3 killed, 15 wounded" if en else "3 Tote, 15 Verwundete"}</text>')
    for (x, y) in [(rx + 170, by - 60), (rx + 196, by + 50), (rx + 186, by + 105)]:
        o.append(X(x, y))
    o.append(f'<text x="{rx + 215}" y="{by + 165}" text-anchor="middle" font-size="11.5" fill="var(--ink)">{"3 in the river" if en else "3 in den Fluss"}</text>')
    for (x, y) in [(rx + 40, by - 70), (rx + 70, by - 30), (rx + 30, by + 40), (rx + 85, by + 70), (rx + 55, by + 110)]:
        o.append(X(x, y))
    o.append(f'<text x="{rx + 55}" y="{by + 165}" text-anchor="middle" font-size="11.5" fill="var(--ink)">{"5 west of the bridge" if en else "5 westlich der Brücke"}</text>')
    o.append(f'<text x="{rx + 30}" y="118" font-size="11.5" fill="var(--ink)">↑ {"1 near Cologne" if en else "1 bei Köln"}</text>')
    o.append(f'<text x="{rx + 270}" y="118" font-size="11.5" fill="var(--ink)">? {"1 never located" if en else "1 nie gefunden"}</text>')
    o.append("</svg>")
    name = "angriffe-en.svg" if en else "angriffe.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
