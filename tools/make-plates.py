"""Lädt und skaliert die Tafeln nach assets/plates/<id>.jpg (1400 px) und <id>_t.jpg (Vorschau).

    python tools/make-plates.py              # alle Tafeln
    python tools/make-plates.py mac1973_map3 # einzelne

Seitenbilder des Internet Archive werden direkt geladen und zugeschnitten (Ausschnitt in Promille).
Standbilder aus Filmen ("film") werden mit PyAV aus der MP4 des Internet Archive gelesen, ohne den
Film zu speichern; dafür braucht es `pip install av pillow`.
"""
import io
import sys
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "assets" / "plates"
UA = {"User-Agent": "Mozilla/5.0 (research; One Bridge, Two Newsreels; pantaleonfassbender@gmail.com)"}
MAC = "https://archive.org/download/CMHPub791TheLastOffensive/page/n{}.jpg"  # Blatt = Seite + 20

PLATES = {
    # Modul 2 (MacDonald, The Last Offensive, 1973; Signal Corps)
    "mac1973_timmerman": ("ia", MAC.format(215 + 20), (55, 108, 465, 500)),
    "mac1973_drabik": ("ia", MAC.format(217 + 20), (72, 98, 482, 512)),
    "mac1973_map3": ("ia", MAC.format(218 + 20), (85, 95, 925, 870)),
    "adc3612c_schild": ("film", "https://archive.org/download/ADC-3612c/ADC-3612c.mp4", 222.0),
    "adc3612c_tuerme": ("film", "https://archive.org/download/ADC-3612c/ADC-3612c.mp4", 209.0),
    # Modul 3
    "mac1973_bruecke": ("ia", MAC.format(224 + 20), (75, 105, 908, 605)),
    "adc3612c_ferne": ("film", "https://archive.org/download/ADC-3612c/ADC-3612c.mp4", 121.0),
    # Modul 4 (Commons: USACE, NARA; gemeinfrei als Werke der US-Regierung)
    "usace_ponton": ("commons", "File:212 Cameron bridgehead at Remagen - USACE-p15141coll5-15246.jpeg", None),
    "united_panzer": ("film", "https://archive.org/download/gov.archives.arc.39162/gov.archives.arc.39162_512kb.mp4", 289.0),
    "mac1973_luft1948": ("ia", MAC.format(231 + 20), (72, 108, 898, 555)),
    # Modul 1
    "tr1918_telegramm": ("local", "../quellen/anno/_ts_ludendorff.png", None),
    "nara1944_erpel": ("commons", "File:Erpel Germany 50.5824603486033, 7.2413274834195 1944-10-28 NARA ID531347349 deatil.webp", None),
    "nara1945_erpel": ("commons", "File:Erpel Germany 50.58099226, 7.24065513 1945-02-15 NARA ID291982353 detail.webp", None),
    "mtb1938_linz": ("commons", "File:Remagener Brücke R RW Karten-08601 gesamt 1938.jpg", None),
    # Modul 7
    "nara195343": ("commons", "File:WWII, Europe, Germany, \"U.S. First Army at Remagen Bridge\" - NARA - 195343.jpg", None),
}


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read()


def commons(title):
    import json, urllib.parse
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url", "iiurlwidth": 1400, "format": "json"})
    ii = next(iter(json.loads(fetch(u))["query"]["pages"].values()))["imageinfo"][0]
    return Image.open(io.BytesIO(fetch(ii.get("thumburl") or ii["url"])))


def frame(url, t):
    import av
    c = av.open(url, options={"timeout": "60000000"})
    s = c.streams.video[0]
    c.seek(int(max(t - 3, 0) / s.time_base), stream=s, backward=True)
    for fr in c.decode(s):
        if float(fr.pts * s.time_base) >= t:
            im = fr.to_image()
            c.close()
            return im
    raise RuntimeError("frame not found")


def save(pid, im):
    im = im.convert("RGB")
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    DEST.mkdir(parents=True, exist_ok=True)
    im.save(DEST / f"{pid}.jpg", quality=86)
    t = im.copy()
    t.thumbnail((420, 420))
    t.save(DEST / f"{pid}_t.jpg", quality=82)
    print(pid, im.size)


def main(ids):
    for pid in ids or PLATES:
        kind, src, arg = PLATES[pid]
        if kind == "film":
            save(pid, frame(src, arg))
            continue
        if kind == "local":
            im = Image.open(ROOT / src)
        else:
            im = commons(src) if kind == "commons" else Image.open(io.BytesIO(fetch(src)))
        if arg:
            w, h = im.size
            x0, y0, x1, y1 = arg
            im = im.crop((w * x0 // 1000, h * y0 // 1000, w * x1 // 1000, h * y1 // 1000))
        save(pid, im)


if __name__ == "__main__":
    main(sys.argv[1:])
