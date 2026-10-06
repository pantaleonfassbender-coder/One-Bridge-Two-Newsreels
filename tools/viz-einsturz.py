"""Zeichnet assets/viz/einsturz.svg und einsturz-en.svg: links die Zahlen zum Einsturz nach Quelle
(Pioniere auf der Brücke, Tote), rechts MacDonalds Reihe der Lasten, die zuletzt ein einziger Träger
tragen musste (S. 230). Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-einsturz.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
W, H = 900, 500

ON = [(200, "MacDonald 1973", "MacDonald 1973", "#/text/einsturz/nachmittag/2"),
      (290, "Presse nach Reuter, 20.3.", "press after Reuters, 20 Mar", "#/text/einsturz/presse/4"),
      (300, "Combat Bulletin 48", "Combat Bulletin 48", "#/text/einsturz/film/6")]
DEAD = [(28, "MacDonald 1973 (dazu 93 Verletzte)", "MacDonald 1973 (and 93 injured)", "#/text/einsturz/nachmittag/2"),
        (32, "Bundesarchiv (neuere Darstellung)", "Bundesarchiv (recent account)", "#/text/standgericht/hitler/6"),
        (None, "Presse 20.3.: „die Mehrzahl wird vermißt“", "press 20 Mar: ‘the majority are missing’", "#/text/einsturz/presse/4")]
LOADS = [("1940–1944: Luftangriffe, 15 Tage gesperrt", "1940–1944: air raids, 15 days closed"),
         ("Bohlen für Fahrzeuge", "planking for vehicles"),
         ("7. März: Sturm, Pershing-Feuer", "7 March: assault, Pershing fire"),
         ("Friesenhahns Notsprengung", "Friesenhahn's emergency demolition"),
         ("Hunderte Infanteristen", "hundreds of infantrymen"),
         ("Panzer und Fahrzeuge", "tanks and vehicles"),
         ("deutsche Artillerie", "German artillery"),
         ("Bomben, Flak, 20-cm-Haubitzen", "bombs, antiaircraft, 8-inch howitzers"),
         ("Nahtreffer der V-2", "near misses of V-2s"),
         ("Gerät der Pioniere bei der Instandsetzung", "engineers' equipment during the repair")]


def build(en):
    title = "The collapse in figures and causes" if en else "Der Einsturz in Zahlen und Ursachen"
    sub = ("Figures differ by source and moment; the causes after MacDonald, p. 230." if en
           else "Die Zahlen unterscheiden sich nach Quelle und Zeitpunkt; die Ursachen nach MacDonald, S. 230.")
    desc = ("Left: engineers on the bridge: about 200 (MacDonald), 290 (German press after Reuters, 20 March), about 300 (Combat Bulletin 48). Dead: 28 and 93 injured (MacDonald), 32 (Bundesarchiv), "
            "‘the majority are missing’ (German press, 20 March). Right: the loads MacDonald lists, from air raids since 1940 to the engineers' equipment during the repair, all borne in the end by the downstream truss alone."
            if en else
            "Links: Pioniere auf der Brücke: etwa 200 (MacDonald), 290 (deutsche Presse nach Reuter, 20. März), etwa 300 (Combat Bulletin 48). Tote: 28 und 93 Verletzte (MacDonald), 32 (Bundesarchiv), "
            "„die Mehrzahl wird vermißt“ (deutsche Presse, 20. März). Rechts: die Lasten nach MacDonald, von den Luftangriffen seit 1940 bis zum Gerät der Pioniere bei der Instandsetzung, die am Ende der stromabwärtige Träger allein tragen musste.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ei-t ei-d" font-family="var(--serif)">',
         f'<title id="ei-t">{escape(title)}</title><desc id="ei-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    sc = 1.05
    o.append(f'<text x="20" y="86" font-size="14" font-weight="bold" fill="var(--ink)">{"Engineers on the bridge" if en else "Pioniere auf der Brücke"}</text>')
    for i, (v, de, eng, href) in enumerate(ON):
        y = 100 + i * 34
        o.append(f'<rect x="20" y="{y}" width="{v * sc:.0f}" height="22" rx="3" fill="var(--us)"/>')
        o.append(f'<text x="{26}" y="{y + 16}" font-size="12.5" font-weight="bold" fill="#fff">{v if i == 1 else "≈ " + str(v)}</text>')
        o.append(f'<a href="{href}"><text x="{24 + v * sc:.0f}" y="{y + 16}" font-size="12" fill="var(--ink)" text-decoration="underline"> {escape(eng if en else de)}</text></a>')
    o.append(f'<text x="20" y="246" font-size="14" font-weight="bold" fill="var(--ink)">{"Killed" if en else "Tote"}</text>')
    for i, (v, de, eng, href) in enumerate(DEAD):
        y = 260 + i * 34
        if v:
            o.append(f'<rect x="20" y="{y}" width="{v * sc * 3:.0f}" height="22" rx="3" fill="var(--film)"/>')
            o.append(f'<text x="26" y="{y + 16}" font-size="12.5" font-weight="bold" fill="#fff">{v}</text>')
            lx = 24 + v * sc * 3
        else:
            o.append(f'<rect x="20" y="{y}" width="60" height="22" rx="3" fill="none" stroke="var(--film)" stroke-dasharray="4 3"/>')
            o.append(f'<text x="50" y="{y + 16}" text-anchor="middle" font-size="12.5" fill="var(--film)">?</text>')
            lx = 84
        o.append(f'<a href="{href}"><text x="{lx:.0f}" y="{y + 16}" font-size="12" fill="var(--ink)" text-decoration="underline"> {escape(eng if en else de)}</text></a>')
    o.append(f'<text x="20" y="384" font-size="11" fill="var(--ink2)">{"Bars for the dead drawn at three times the scale." if en else "Balken der Toten im dreifachen Maßstab."}</text>')
    # rechts: Lasten
    rx = 560
    o.append(f'<a href="#/text/einsturz/ursachen/3"><text x="{rx}" y="86" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"Loads on the bridge" if en else "Lasten auf der Brücke"}</text></a>')
    for i, (de, eng) in enumerate(LOADS):
        y = 98 + i * 30
        o.append(f'<rect x="{rx}" y="{y}" width="320" height="25" rx="3" fill="var(--bruecke)" opacity="{0.25 + 0.06 * i:.2f}"/>')
        o.append(f'<text x="{rx + 8}" y="{y + 17}" font-size="12" fill="var(--ink)">{escape(eng if en else de)}</text>')
    ty = 98 + len(LOADS) * 30 + 6
    o.append(f'<path d="M{rx},{ty} l320,0 l-20,26 l-280,0 z" fill="var(--ink2)"/>')
    o.append(f'<text x="{rx + 160}" y="{ty + 18}" text-anchor="middle" font-size="12" fill="#fff">{"one weakened truss" if en else "ein geschwächter Träger"}</text>')
    o.append("</svg>")
    name = "einsturz-en.svg" if en else "einsturz.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
