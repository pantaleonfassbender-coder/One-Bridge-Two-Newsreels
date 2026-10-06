"""Zeichnet assets/viz/lager.svg und lager-en.svg: links Soll- und Höchstbelegung der Lager Remagen und Sinzig
nach dem Bericht von 1969 und nach der Landeszentrale für politische Bildung Rheinland-Pfalz, rechts die
Krankheitstoten in allen Lagern der ADSEC in sechs Wochen bis zum 15. Juni 1945 (S. 394, 396), die Sterberaten
im Vergleich mit den US-Truppen und, gestrichelt, die Toten beider Lager nach der Forschung.
Jede Beschriftung verweist auf ihre Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-lager.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz"
W, H = 900, 420
T = "#/text/lager/"

CAMPS = [("Remagen (A2)", "Remagen (A2)", [(184000, "Bericht 1969, ohne Datum", "1969 report, undated", T + "rhein/4", False),
                                         (170000, "2. Mai, nach LpB RLP", "2 May, after state agency", T + "graeber/13", True)]),
         ("Sinzig (A5)", "Sinzig (A5)", [(116000, "12. Mai, Bericht 1969", "12 May, 1969 report", T + "rhein/3", False),
                                       (118000, "höchstens, nach LpB RLP", "at most, after state agency", T + "graeber/13", True)])]


def n(v, en):
    s = f"{v:,}"
    return s if en else s.replace(",", " ")


def build(en):
    title = "Too many, too little water, too many dead" if en else "Zu viele, zu wenig Wasser, zu viele Tote"
    sub = ("Dashed: recent literature, only summarized. The death figures on the right cover different areas and periods." if en
           else "Gestrichelt: neuere Literatur, nur referiert. Die Totenzahlen rechts gelten für verschiedene Räume und Zeiten.")
    desc = ("Left: the enclosures at Remagen and Sinzig were each built for 100,000 prisoners. Remagen held 184,000 according to the 1969 report (undated) and 170,000 on 2 May 1945 according to the state agency; "
            "Sinzig held 116,000 on 12 May 1945 according to the report and at most 118,000 according to the state agency. "
            "Right: in the six weeks to 15 June 1945, 2,754 prisoners died of disease in all ADSEC enclosures, 833 of them of diarrhea and dysentery; the annual death rate from disease was 34.2 per 1,000 prisoners against 0.6 for US troops. "
            "According to research some 1,200 people died at Remagen and Sinzig over the whole period."
            if en else
            "Links: Die Lager Remagen und Sinzig waren für je 100 000 Gefangene gebaut. In Remagen lagen nach dem Bericht von 1969 184 000 (ohne Datum), nach der Landeszentrale 170 000 am 2. Mai 1945; "
            "in Sinzig nach dem Bericht 116 000 am 12. Mai 1945, nach der Landeszentrale höchstens 118 000. "
            "Rechts: In den sechs Wochen bis zum 15. Juni 1945 starben in allen Lagern der ADSEC 2 754 Gefangene an Krankheiten, 833 davon an Durchfall und Ruhr; die Sterberate durch Krankheit lag bei 34,2 auf 1 000 Gefangene im Jahr gegen 0,6 bei den US-Truppen. "
            "Nach der Forschung starben in Remagen und Sinzig über die ganze Zeit etwa 1 200 Menschen.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="la-t la-d" font-family="var(--serif)">',
         f'<title id="la-t">{escape(title)}</title><desc id="la-d">{escape(desc)}</desc>',
         f'<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">{escape(title)}</text>',
         f'<text x="16" y="48" font-size="13" fill="var(--ink2)">{escape(sub)}</text>']
    # links: Belegung
    X0, SC = 20, 380 / 200000
    o.append(f'<a href="{T}rhein/1"><text x="{X0}" y="86" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"Prisoners held" if en else "Belegung"}</text></a>')
    xs = X0 + 100000 * SC
    o.append(f'<line x1="{xs:.0f}" y1="104" x2="{xs:.0f}" y2="304" stroke="var(--ink2)" stroke-dasharray="3 3"/>')
    o.append(f'<text x="{xs + 6:.0f}" y="100" font-size="11.5" fill="var(--ink2)">{"rated capacity 100,000" if en else "Sollbelegung 100 000"}</text>')
    y = 104
    for de, eng, rows in CAMPS:
        o.append(f'<text x="{X0}" y="{y + 10}" font-size="13" font-weight="bold" fill="var(--menschen)">{escape(eng if en else de)}</text>')
        y += 18
        for v, lde, len_, href, lit in rows:
            w = v * SC
            if lit:
                o.append(f'<rect x="{X0}" y="{y}" width="{w:.0f}" height="24" rx="3" fill="var(--panel)" stroke="var(--menschen)" stroke-width="2" stroke-dasharray="5 3"/>')
                o.append(f'<text x="{X0 + 6}" y="{y + 17}" font-size="12.5" font-weight="bold" fill="var(--menschen)">{n(v, en)}</text>')
            else:
                o.append(f'<rect x="{X0}" y="{y}" width="{w:.0f}" height="24" rx="3" fill="var(--menschen)"/>')
                o.append(f'<text x="{X0 + 6}" y="{y + 17}" font-size="12.5" font-weight="bold" fill="#fff">{n(v, en)}</text>')
            o.append(f'<a href="{href}"><text x="{X0 + 72}" y="{y + 17}" font-size="11.5" fill="{"var(--ink)" if lit else "#fff"}" text-decoration="underline">{escape(len_ if en else lde)}</text></a>')
            y += 32
        y += 18
    o.append(f'<a href="{T}rhein/1"><text x="{X0}" y="{y + 12}" font-size="11.5" fill="var(--ink)" text-decoration="underline">{"17 enclosures on the Rhine: 1,095,000 places for some 1.5 million expected" if en else "17 Lager am Rhein: 1 095 000 Plätze für rund 1,5 Millionen Erwartete"}</text></a>')
    # rechts: Tote
    RX, CS = 480, 360 / 2754
    o.append(f'<a href="{T}krankheit/10"><text x="{RX}" y="86" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"Deaths from disease" if en else "Tote durch Krankheit"}</text></a>')
    o.append(f'<text x="{RX}" y="104" font-size="11.5" fill="var(--ink2)">{"all ADSEC enclosures, six weeks to 15 June 1945" if en else "alle Lager der ADSEC, sechs Wochen bis 15. Juni 1945"}</text>')
    o.append(f'<rect x="{RX}" y="114" width="{2754 * CS:.0f}" height="26" rx="3" fill="var(--film)"/>')
    o.append(f'<rect x="{RX}" y="114" width="{833 * CS:.0f}" height="26" rx="3" fill="var(--bruecke)"/>')
    o.append(f'<a href="{T}krankheit/11"><text x="{RX + 6}" y="132" font-size="12" fill="#fff" text-decoration="underline">{"833 dysentery" if en else "833 Ruhr"}</text></a>')
    o.append(f'<a href="{T}krankheit/10"><text x="{RX + 833 * CS + 8:.0f}" y="132" font-size="12.5" font-weight="bold" fill="#fff" text-decoration="underline">{n(2754, en)} {"in all" if en else "insgesamt"}</text></a>')
    o.append(f'<a href="{T}graeber/13"><text x="{RX}" y="170" font-size="11.5" fill="var(--ink2)" text-decoration="underline">{"Remagen and Sinzig, whole period, after research" if en else "Remagen und Sinzig, ganze Zeit, nach der Forschung"}</text></a>')
    o.append(f'<rect x="{RX}" y="180" width="{1200 * CS:.0f}" height="26" rx="3" fill="none" stroke="var(--film)" stroke-width="2" stroke-dasharray="5 3"/>')
    o.append(f'<text x="{RX + 6}" y="198" font-size="12.5" font-weight="bold" fill="var(--film)">≈ {n(1200, en)}</text>')
    o.append(f'<a href="{T}krankheit/10"><text x="{RX}" y="250" font-size="14" font-weight="bold" fill="var(--ink)" text-decoration="underline">{"Death rate from disease" if en else "Sterberate durch Krankheit"}</text></a>')
    o.append(f'<text x="{RX}" y="268" font-size="11.5" fill="var(--ink2)">{"per 1,000 per year, same six weeks" if en else "auf 1 000 im Jahr, dieselben sechs Wochen"}</text>')
    RS = 360 / 34.2
    for i, (v, de, eng, col) in enumerate([(34.2, "deutsche Gefangene", "German prisoners", "var(--menschen)"), (0.6, "US-Truppen", "US troops", "var(--us)")]):
        yy = 280 + i * 36
        o.append(f'<rect x="{RX}" y="{yy}" width="{max(v * RS, 3):.0f}" height="26" rx="3" fill="{col}"/>')
        txt = f'{str(v) if en else str(v).replace(".", ",")}  {eng if en else de}'
        o.append(f'<text x="{RX + (6 if i == 0 else 12)}" y="{yy + 18}" font-size="12.5" font-weight="bold" fill="{"#fff" if i == 0 else "var(--ink)"}">{escape(txt)}</text>')
    for k, line in enumerate(["The report: its figures count hospital admissions", "and understate the sickness in the enclosures."] if en else ["Der Bericht: seine Zahlen zählen Lazarettaufnahmen", "und untertreiben die Krankheit in den Lagern."]):
        o.append(f'<a href="{T}krankheit/9"><text x="{RX}" y="{360 + k * 16}" font-size="11.5" fill="var(--ink)" text-decoration="underline">{escape(line)}</text></a>')
    o.append(f'<a href="{T}krankheit/12"><text x="{RX}" y="404" font-size="11.5" fill="var(--ink)" text-decoration="underline">{"First typhus among German prisoners: March 1945, at Remagen." if en else "Erstes Fleckfieber unter deutschen Gefangenen: März 1945, in Remagen."}</text></a>')
    o.append("</svg>")
    name = "lager-en.svg" if en else "lager.svg"
    (OUT / name).write_text("\n".join(o), encoding="utf-8")
    print(name)


build(False)
build(True)
