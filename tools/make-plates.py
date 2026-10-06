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
}


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read()


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
        im = Image.open(io.BytesIO(fetch(src)))
        if arg:
            w, h = im.size
            x0, y0, x1, y1 = arg
            im = im.crop((w * x0 // 1000, h * y0 // 1000, w * x1 // 1000, h * y1 // 1000))
        save(pid, im)


if __name__ == "__main__":
    main(sys.argv[1:])
