"""Baut data/angriffe.json (Modul 6: Die Angriffe auf die Brücke, 8.–17. März 1945).
Quellen: MacDonald, The Last Offensive (1973), S. 227–229, am Seitenbild gelesen; Lagebericht zum
OKW-Bericht im Erzgebirgischen Volksfreund vom 17. März 1945, am Seitenbild gelesen; Combat Bulletin
No. 48 (Army Pictorial Service, 1945), Bild und Ton. Übersetzungen: eigene Arbeit (CC0).
Aufruf aus dem Wurzelverzeichnis: python tools/build-angriffe.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
DZP = "https://www.deutsche-digitale-bibliothek.de/newspaper/item/"
TON = json.loads((ROOT / "tools" / "cb48-ton.json").read_text(encoding="utf-8")) if (ROOT / "tools" / "cb48-ton.json").exists() else []


def u(n, pg, lang, orig, tr, titel=None, titel_en=None, note=None, note_en=None, pgl=None):
    x = {"n": n, "pg": pg, "lang": lang}
    if pgl: x["pgl"] = pgl
    if titel: x["titel"], x["titel_en"] = titel, titel_en
    x["orig"] = orig
    x["en" if lang == "de" else "de"] = tr
    if note: x["note"], x["note_en"] = note, note_en
    return x


S1 = [
    u(1, "S. 227–228", "en",
      "Unlike the artillery fire, German air attacks were more annoying than destructive. A strong cordon of defenses around the bridge manned by the 16th Antiaircraft Artillery Group, antiaircraft battalions borrowed from the divisions of the III Corps, and additional units transferred from the V Corps sharply interfered with German accuracy. On 12 March, at the height of air attacks against the bridge, sixteen 90-mm. gun batteries were emplaced on the west bank of the Rhine and twenty-five batteries of automatic antiaircraft weapons were almost equally divided between the two banks, probably the most intensive tactical grouping of antiaircraft weapons in the European theater during the course of the war.",
      "Anders als das Artilleriefeuer waren die deutschen Luftangriffe eher lästig als zerstörerisch. Ein starker Abwehrring um die Brücke, besetzt von der 16th Antiaircraft Artillery Group, von Flakbataillonen, die man sich von den Divisionen des III. Korps geliehen hatte, und von weiteren Einheiten aus dem V. Korps, störte die deutsche Treffsicherheit empfindlich. Am 12. März, auf dem Höhepunkt der Luftangriffe auf die Brücke, standen sechzehn Batterien 9-cm-Geschütze auf dem Westufer des Rheins und fünfundzwanzig Batterien automatischer Flakwaffen, fast gleich auf beide Ufer verteilt, wohl die dichteste taktische Ansammlung von Flakwaffen auf dem europäischen Kriegsschauplatz während des ganzen Krieges.",
      "Der Flakring", "The antiaircraft ring",
      "„Unlike the artillery fire“: Die gefährlichste Waffe gegen die Brücke war die deutsche Artillerie, am 8. und 9. März eine Granate alle zwei Minuten (Modul 4, Einheit 12).",
      "‘Unlike the artillery fire’: the most dangerous weapon against the bridge was German artillery, on 8 and 9 March one shell every two minutes (module 4, unit 12)."),
    u(2, "S. 228", "en",
      "The Luftwaffe first struck at the railroad bridge on the morning after Lieutenant Timmerman and his intrepid little band had crossed. Although low overcast interfered with flight, the Germans made ten sweeps with a total of ten planes, most of them Stuka dive bombers. None inflicted any damage on the bridge, and antiaircraft units claimed eight destroyed.\n\nExhortation to the Luftwaffe to strike and strike again was one of the few immediate steps Field Marshal Kesselring could take toward eliminating the Ludendorff Bridge after he assumed command in the west on 10 March. He conferred that day with senior Luftwaffe commanders, urging them to knock out the bridge and any auxiliary bridges the Americans might construct.",
      "Die Luftwaffe griff die Eisenbahnbrücke zum ersten Mal am Morgen nach dem Übergang von Leutnant Timmerman und seiner kühnen kleinen Schar an. Obwohl tiefe Wolken den Flug behinderten, flogen die Deutschen zehn Angriffe mit insgesamt zehn Flugzeugen, meist Sturzkampfbombern. Keiner beschädigte die Brücke, und die Flak meldete acht Abschüsse.\n\nDie Luftwaffe zu Angriff auf Angriff anzutreiben, war einer der wenigen Schritte, die Generalfeldmarschall Kesselring sofort unternehmen konnte, um die Ludendorff-Brücke zu beseitigen, nachdem er am 10. März den Befehl im Westen übernommen hatte. Er beriet sich an diesem Tag mit hohen Befehlshabern der Luftwaffe und drängte sie, die Brücke und alle Hilfsbrücken zu zerstören, die die Amerikaner bauen würden.",
      "8. und 10. März", "8 and 10 March"),
    u(3, "S. 228", "en",
      "From 8 through 16 March, the Luftwaffe tried. The German planes struck at the railroad bridge, at the ferries, and at the tactical bridges, but with no success. Whenever the weather allowed, American planes flying cover over the bridgehead interfered; even when the German pilots got through the fighter screen, they ran into a dense curtain of antiaircraft fire. When they tried a stratagem of sending slow bombers in the lead to draw the antiaircraft fire, then following with speedy jet fighters, the Americans countered by withholding part of their fire until the jets appeared. American antiaircraft units estimated that during the nine days they destroyed 109 planes and probably eliminated 36 others out of a total of 367 that attacked.",
      "Vom 8. bis zum 16. März versuchte es die Luftwaffe. Die deutschen Flugzeuge griffen die Eisenbahnbrücke an, die Fähren und die Pontonbrücken, aber ohne Erfolg. Wann immer das Wetter es erlaubte, griffen amerikanische Jäger über dem Brückenkopf ein; und auch wenn die deutschen Piloten durch den Jagdschutz kamen, gerieten sie in einen dichten Vorhang aus Flakfeuer. Als sie es mit der List versuchten, langsame Bomber vorauszuschicken, die das Flakfeuer auf sich ziehen sollten, und dann schnelle Düsenjäger folgen zu lassen, hielten die Amerikaner einen Teil ihres Feuers zurück, bis die Düsenflugzeuge kamen. Die amerikanische Flak schätzte, dass sie in den neun Tagen 109 Flugzeuge zerstört und 36 weitere wahrscheinlich ausgeschaltet hatte, von insgesamt 367 Angreifern.",
      "367 Flugzeuge", "367 aircraft",
      "Schätzungen der Flak selbst, nach MacDonalds Anm. 32 aus dem Bericht der 16th AAA Group vom 17. März 1945. Abschussmeldungen lagen im Krieg auf allen Seiten oft zu hoch. Wie viele deutsche Flieger starben, sagt die Quelle nicht.",
      "Estimates by the antiaircraft units themselves, according to MacDonald's n. 32 from the 16th AAA Group report of 17 March 1945. Claims of aircraft destroyed were often too high on all sides in the war. How many German airmen died, the source does not say."),
]

S2 = [
    u(4, "Erzgebirgischer Volksfreund, 17.3.1945, S. 2", "de",
      "Bei aufhellendem Frühlingswetter standen unsere Truppen, wie ergänzend zum OKW.-Bericht gemeldet wird, am Donnerstag an der West- und Ostfront in neuen schweren Abwehrkämpfen. […]\n\nIm Westen verstärkte sich der Ansturm der Nordamerikaner aus ihrem Brückenkopf Remagen und an unserem Frontbogen zwischen Koblenz und Hagenau. Am Mittelrhein brachten unsere Truppen den zwischen Remagen und der Autobahn Köln—Frankfurt örtlich eingebrochenen Gegner zum Stehen […]. Der sonnenklare Himmel erlaubte den Angloamerikanern in den letzten 48 Stunden, ihre Luftstreitkräfte über den Kampfgebieten am Rhein und in Westdeutschland zum vollen Einsatz zu bringen. Auch unsere Luftwaffe war mit starken Kräften eingesetzt, um den Aufmarsch des Gegners zu stören. Bei Tag und Nacht entwickelten sich über dem Brückenkopf ostwärts Remagen erbitterte Luftkämpfe. Obwohl feindliche Jäger und Flak alles daran setzten, die Brückenstege zu schützen, gelang es unseren Schlachtfliegern, einige Treffer auf den Brücken und Zufahrtsrampen anzubringen. Fortgesetzt griffen auch von beiden Seiten Tiefflieger in die vor allem nordöstlich Honnef tobenden Kämpfe ein.",
      "With the spring weather brightening, our troops, as is reported in addition to the OKW report, were engaged on Thursday in new heavy defensive fighting on the western and eastern fronts. […]\n\nIn the west the onslaught of the North Americans from their Remagen bridgehead and against our salient between Koblenz and Hagenau grew stronger. On the middle Rhine our troops brought to a halt the enemy who had broken in locally between Remagen and the Cologne–Frankfurt autobahn […]. The cloudless sky allowed the Anglo-Americans over the last 48 hours to commit their air forces in full over the battle areas on the Rhine and in western Germany. Our Luftwaffe too was committed in strength to disrupt the enemy's deployment. By day and night bitter air battles developed over the bridgehead east of Remagen. Although enemy fighters and antiaircraft did everything to protect the bridge crossings, our ground-attack aircraft succeeded in scoring several hits on the bridges and approach ramps. Low-flying aircraft of both sides also intervened continually in the fighting raging above all north-east of Honnef.",
      "„einige Treffer“", "‘several hits’",
      "Kein Wehrmachtbericht, sondern eine ergänzende Lagedarstellung zum OKW-Bericht; der Donnerstag ist der 15. März 1945. Im Druck steht „Brückensteige“. Dass Treffer die Brücken unbrauchbar gemacht hätten, behauptet der Text nicht; nach MacDonald blieben die Angriffe ohne Erfolg (Einheit 3). Fraktursatz, am Seitenbild der SLUB Dresden gelesen. Zeitungsseite: " + DZP + "OUAZFPAWVOZQ3QWYYVASLESKWAGFU4GH",
      "Not a Wehrmacht report but a supplementary situation summary to the OKW report; the Thursday is 15 March 1945. The print has ‘Brückensteige’. The text does not claim that any hit put the bridges out of use; according to MacDonald the attacks had no success (unit 3). Set in Fraktur, read against the page image of the SLUB Dresden. Newspaper page: " + DZP + "OUAZFPAWVOZQ3QWYYVASLESKWAGFU4GH"),
]

S3 = [
    u(5, "S. 228", "en",
      "By three other means the Germans tried to destroy the railroad bridge. Soon after losing the bridge, they brought up a tank-mounted 540-mm. piece called the Karl Howitzer. The weapon itself weighed 132 tons and fired a projectile of 4,400 pounds, but after only a few rounds that did no damage except to random houses, the weapon had to be evacuated for repairs.",
      "Auf drei weitere Arten versuchten die Deutschen, die Eisenbahnbrücke zu zerstören. Bald nach ihrem Verlust brachten sie ein auf Kettenfahrgestell gesetztes 54-cm-Geschütz heran, den „Karl“-Mörser. Die Waffe selbst wog 132 Tonnen und verschoss eine Granate von 4 400 Pfund, musste aber nach nur wenigen Schüssen, die außer an beliebigen Häusern keinen Schaden anrichteten, zur Instandsetzung abgezogen werden.",
      "Der „Karl“", "The ‘Karl’",
      "„did no damage except to random houses“: Wem die Häuser gehörten und ob Menschen darin waren, sagt MacDonald nicht. 4 400 Pfund sind rund zwei Tonnen.",
      "‘Did no damage except to random houses’: whose houses they were and whether people were inside, MacDonald does not say."),
    u(6, "S. 228", "en",
      "From 12 through 17 March a rocket unit with weapons emplaced in the Netherlands fired eleven supersonic V–2's in the direction of the bridge, the first and only tactical use of either of the so-called German V-weapons (Vergeltungswaffen, for vengeance) during World War II. One rocket hit a house 300 yards east of the bridge, killing three American soldiers and wounding fifteen. That was the only damage. Three landed in the river not far from the bridge, five others west of the bridge, and one near Cologne; one was never located.",
      "Vom 12. bis zum 17. März feuerte eine Raketeneinheit aus Stellungen in den Niederlanden elf überschallschnelle V-2 in Richtung der Brücke, der erste und einzige taktische Einsatz einer der sogenannten deutschen V-Waffen („Vergeltungswaffen“) im Zweiten Weltkrieg. Eine Rakete traf ein Haus 300 Yards östlich der Brücke, tötete drei amerikanische Soldaten und verwundete fünfzehn. Das war der einzige Schaden. Drei schlugen nicht weit von der Brücke in den Fluss, fünf westlich der Brücke und eine bei Köln; eine wurde nie gefunden.",
      "Elf V-2", "Eleven V-2s",
      "Die Zahlen nach MacDonalds Anm. 34 aus einem Bericht der Luftverteidigung von SHAEF für die Woche bis zum 19. März 1945. „300 yards“ sind rund 275 Meter; das Haus stand also in Erpel. Ob Bewohner darin waren, sagt die Quelle nicht. „Fünf westlich der Brücke“: in oder bei Remagen.",
      "The figures after MacDonald's n. 34 from a SHAEF air defence report for the week to 19 March 1945. 300 yards are about 275 metres; the house therefore stood in Erpel. Whether residents were inside, the source does not say. ‘Five west of the bridge’: in or near Remagen."),
]

S4 = [
    u(7, "S. 228–229", "en",
      "The night of 16 March, the Germans tried a third method—seven underwater swimmers in special rubber suits and carrying packages of plastic explosive compound—but from the first the Americans had anticipated such a gambit. During the first few days of the bridgehead, before nets could be strung across the river, they dropped demolition charges to discourage enemy swimmers and stationed riflemen at intervals along the railroad bridge to fire at suspicious objects. Later, with nets in place, they stationed tanks equipped with searchlights along the river.\n\nWhen the German swimmers first tried to reach the bridge, American artillery fire discouraged them from entering the water. On the next night, the 17th, they moved not against the railroad bridge but against tactical ponton bridges, only to be spotted by the American searchlights. Blinded by the lights, the seven Germans, one by one, surrendered.",
      "In der Nacht des 16. März versuchten es die Deutschen auf eine dritte Art, mit sieben Kampfschwimmern in besonderen Gummianzügen und mit Paketen plastischen Sprengstoffs; doch die Amerikaner hatten mit einem solchen Schachzug von Anfang an gerechnet. In den ersten Tagen des Brückenkopfes, bevor Netze über den Fluss gespannt werden konnten, warfen sie Sprengladungen ins Wasser, um feindliche Schwimmer abzuschrecken, und stellten in Abständen Schützen auf die Eisenbahnbrücke, die auf verdächtige Gegenstände schießen sollten. Später, als die Netze hingen, stellten sie Panzer mit Scheinwerfern am Fluss auf.\n\nAls die deutschen Schwimmer zum ersten Mal versuchten, die Brücke zu erreichen, hielt amerikanisches Artilleriefeuer sie davon ab, ins Wasser zu gehen. In der nächsten Nacht, der des 17., schwammen sie nicht gegen die Eisenbahnbrücke, sondern gegen die Pontonbrücken, wurden aber von den amerikanischen Scheinwerfern entdeckt. Von den Lichtern geblendet, ergaben sich die sieben Deutschen einer nach dem anderen.",
      "Sieben Schwimmer", "Seven swimmers",
      "MacDonald gibt nicht an, ob er eine Nacht nach ihrem Beginn oder Ende datiert. Am Nachmittag des 17. März war die Ludendorff-Brücke schon eingestürzt (Modul 7).",
      "MacDonald does not say whether he dates a night by its beginning or its end. On the afternoon of 17 March the Ludendorff Bridge had already collapsed (module 7)."),
]

S5 = [u(8 + i, z["t"], "en", z["en"], z["de"], pgl="Film", **({"titel": z["titel"], "titel_en": z["titel_en"]} if z.get("titel") else {}),
        **({"note": z["note"], "note_en": z["note_en"]} if z.get("note") else {})) for i, z in enumerate(TON)]

secs = [
    {"id": "luftwaffe", "titel": "Die Luftwaffe gegen die Brücke", "titel_en": "The Luftwaffe against the bridge", "zk": "Angriffe · Luftwaffe", "zk_en": "Attacks · Luftwaffe",
     "blurb": "Sturzkampfbomber am Morgen des 8. März, Kesselrings Drängen ab dem 10., Düsenflugzeuge hinter langsamen Bombern, und um die Brücke die dichteste Flak des Krieges in Europa: 367 Angreifer in neun Tagen, nach amerikanischer Schätzung.",
     "blurb_en": "Dive bombers on the morning of 8 March, Kesselring's urging from the 10th, jets behind slow bombers, and around the bridge the densest antiaircraft defence of the war in Europe: 367 attackers in nine days, by American estimate.",
     "plates": ["adc3612c_flak"], "viz": "angriffe", "units": S1},
    {"id": "meldung", "titel": "„Einige Treffer“", "titel_en": "‘Several hits’", "zk": "Angriffe · Meldung", "zk_en": "Attacks · Report",
     "blurb": "Wie die deutsche Presse die Luftschlacht über dem Brückenkopf darstellte: erbitterte Kämpfe, Schlachtflieger, Treffer auf Brücken und Rampen.",
     "blurb_en": "How the German press presented the air battle over the bridgehead: bitter fighting, ground-attack aircraft, hits on bridges and ramps.",
     "units": S2},
    {"id": "fernwaffen", "titel": "Das Geschütz „Karl“ und die V-2", "titel_en": "The ‘Karl’ gun and the V-2", "zk": "Angriffe · Fernwaffen", "zk_en": "Attacks · Long-range weapons",
     "blurb": "Ein 54-cm-Mörser, der nach wenigen Schüssen in die Werkstatt muss, und elf Raketen aus den Niederlanden, der einzige taktische Einsatz der V-Waffen: Eine traf ein Haus in Erpel.",
     "blurb_en": "A 54-cm mortar that has to go for repairs after a few rounds, and eleven rockets from the Netherlands, the only tactical use of the V-weapons: one hit a house in Erpel.",
     "plates": ["sc1945_ley"], "units": S3},
    {"id": "schwimmer", "titel": "Kampfschwimmer", "titel_en": "Frogmen", "zk": "Angriffe · Schwimmer", "zk_en": "Attacks · Swimmers",
     "blurb": "Sprengladungen im Wasser, Schützen auf der Brücke, Netze, Panzer mit Scheinwerfern: sieben Schwimmer mit Sprengstoff, die sich einer nach dem anderen ergeben.",
     "blurb_en": "Charges in the water, riflemen on the bridge, nets, tanks with searchlights: seven swimmers with explosives who surrender one by one.",
     "units": S4},
]
if S5:
    secs.append({"id": "film", "titel": "Combat Bulletin No. 48", "titel_en": "Combat Bulletin No. 48", "zk": "Angriffe · Film", "zk_en": "Attacks · Film",
                 "blurb": "Ein Filmbericht der Army: Boote der Navy, Schwimmlastwagen, die Brücke zehn Tage unter Feuer, Pontonbrücken, die Instandsetzung. Den Einsturz im selben Film zeigt Modul 7.",
                 "blurb_en": "An Army film report: Navy craft, amphibious trucks, the bridge ten days under fire, treadway bridges, the repair. The collapse in the same film is in module 7.",
                 "plates": ["cb48_schweisser"], "films": [{"film": "cb48", "start": "12:20", "end": "15:08"}], "units": S5})

T = {
    "id": "angriffe",
    "titel": "Die Angriffe auf die Brücke", "titel_en": "The attacks on the bridge",
    "autor": "Charles B. MacDonald, The Last Offensive (1973); Lagebericht zum OKW-Bericht (März 1945); Combat Bulletin No. 48 (1945)",
    "autor_en": "Charles B. MacDonald, The Last Offensive (1973); supplement to the OKW report (March 1945); Combat Bulletin No. 48 (1945)",
    "jahr": "8.–17. März 1945", "jahr_en": "8–17 March 1945",
    "sprache": "de", "orig_sprache": "en", "pg_label": "", "pg_label_en": "",
    "quelle": "Charles B. MacDonald, The Last Offensive (1973), S. 227–229, am Seitenbild des Internet Archive gelesen, gemeinfrei. Lagebericht „ergänzend zum OKW.-Bericht“ im Erzgebirgischen Volksfreund vom 17. März 1945, am Seitenbild im Deutschen Zeitungsportal gelesen (amtliche Meldung; der Scan ist verlinkt). Combat Bulletin No. 48 (War Department, Army Pictorial Service, 1945), Internet Archive CB-48 (Public Domain Mark), Ton maschinell abgeschrieben und durchgesehen.",
    "quelle_en": "Charles B. MacDonald, The Last Offensive (1973), pp. 227–229, read against the page images of the Internet Archive, public domain. Situation report ‘supplementary to the OKW report’ in the Erzgebirgischer Volksfreund of 17 March 1945, read against the page image in the Deutsches Zeitungsportal (official report; the scan is linked). Combat Bulletin No. 48 (War Department, Army Pictorial Service, 1945), Internet Archive CB-48 (Public Domain Mark), soundtrack transcribed by machine and reviewed.",
    "hinweis": "Zehn Tage lang versuchten die Deutschen, die Brücke zu zerstören, die sie am 7. März nicht hatten sprengen können: aus der Luft, mit dem schwersten Geschütz, mit Raketen, mit Schwimmern. Keiner der Angriffe brachte sie zum Einsturz. Die Zahlen sind Schätzungen der Verteidiger; Opfer unter den Bewohnern von Remagen und Erpel nennt keine der Quellen, und deutsche Verluste nur in Flugzeugen. Texte nach dem Druck, Auslassungen […]; Übersetzungen eigene Arbeit (CC0).",
    "hinweis_en": "For ten days the Germans tried to destroy the bridge they had failed to blow on 7 March: from the air, with the heaviest gun, with rockets, with swimmers. None of the attacks brought it down. The figures are the defenders' estimates; casualties among the inhabitants of Remagen and Erpel are not given by any of the sources, and German losses only in aircraft. Texts after the print, omissions […]; translations my own (CC0).",
    "sections": secs,
}
(D / "angriffe.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")

P = json.loads((D / "plates.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "sc1945_ley", "side": "us", "titel": "Die Brücke von der Erpeler Ley, 9. März 1945", "titel_en": "The bridge from the Erpeler Ley, 9 March 1945",
     "caption": "Ein amerikanischer Soldat auf der Höhe der Ley über der Brücke; unten der Rhein und Remagen. Photographie des Signal Corps mit der Beschriftung des Archivs am unteren Rand.",
     "caption_en": "An American soldier on top of the Ley above the bridge; below, the Rhine and Remagen. Signal Corps photograph with the archive caption at the bottom.",
     "source": "U.S. Army Signal Corps (National Archives), über Wikimedia Commons; gemeinfrei."},
    {"id": "adc3612c_flak", "side": "film", "titel": "Flak am Rhein", "titel_en": "Antiaircraft on the Rhine",
     "caption": "Ein Fahrzeug mit Flakgeschütz am Rheinufer bei Remagen, im Hintergrund der Fluss. Standbild aus der stummen Signal-Corps-Rolle, März 1945.",
     "caption_en": "A vehicle with an antiaircraft gun on the Rhine bank near Remagen, the river behind. Still from the silent Signal Corps reel, March 1945.",
     "source": "U.S. Army, Antiaircraft & Troops Moving Up, Remagen, Germany (National Archives, NAID 17415), 1:30; Internet Archive ADC-3612c."},
    {"id": "cb48_schweisser", "side": "film", "titel": "Ein Schweißer an der Brücke", "titel_en": "A welder on the bridge",
     "caption": "Ein Pionier schweißt an einem Träger der Ludendorff-Brücke. Standbild aus Combat Bulletin No. 48, März 1945.",
     "caption_en": "An engineer welding a girder of the Ludendorff Bridge. Still from Combat Bulletin No. 48, March 1945.",
     "source": "War Department, Combat Bulletin No. 48 (1945), 15:10; Internet Archive CB-48 (Public Domain Mark)."},
]
ids = {p["id"] for p in NEW}
P["plates"] = [p for p in P["plates"] if p["id"] not in ids] + NEW
(D / "plates.json").write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")

M = json.loads((D / "modules.json").read_text(encoding="utf-8"))
m = next((x for x in M["planned"] if x["id"] == "angriffe"), None) or next(x for x in M["shipped"] if x["id"] == "angriffe")
M["planned"] = [x for x in M["planned"] if x["id"] != "angriffe"]
m.update({"datei": "angriffe", "zk": "Luftwaffe · Meldung · Fernwaffen · Schwimmer" + (" · Film" if S5 else ""), "zk_en": "Luftwaffe · Report · Long-range weapons · Swimmers" + (" · Film" if S5 else ""),
          "kurz": "6 · Die Angriffe auf die Brücke", "kurz_en": "6 · The attacks on the bridge",
          "warum": "Zehn Tage lang versuchten die Deutschen, die Brücke doch noch zu zerstören: 367 Flugzeuge nach amerikanischer Schätzung, das Geschütz „Karl“, elf V-2, sieben Kampfschwimmer. Keiner der Angriffe brachte sie zum Einsturz.",
          "warum_en": "For ten days the Germans tried to destroy the bridge after all: 367 aircraft by American estimate, the ‘Karl’ gun, eleven V-2s, seven frogmen. None of the attacks brought it down.",
          "quelle": "MacDonald (1973), S. 227–229; Lagebericht zum OKW-Bericht, 17. März 1945; Combat Bulletin No. 48 (1945).",
          "quelle_en": "MacDonald (1973), pp. 227–229; supplement to the OKW report, 17 March 1945; Combat Bulletin No. 48 (1945)."})
order = ["bruecke", "siebter", "warum", "brueckenkopf", "standgericht", "angriffe"]
M["shipped"] = sorted([x for x in M["shipped"] if x["id"] != "angriffe"] + [m], key=lambda x: order.index(x["id"]) if x["id"] in order else 99)
(D / "modules.json").write_text(json.dumps(M, ensure_ascii=False, indent=1), encoding="utf-8")

C = json.loads((D / "compare.json").read_text(encoding="utf-8"))
PAIRS = [{"id": "treffer", "titel": "Treffer?", "titel_en": "Hits?",
          "frage": "Trafen die deutschen Flieger die Brücken?", "frage_en": "Did the German airmen hit the bridges?",
          "note": "Die deutsche Lagedarstellung meldet „einige Treffer auf den Brücken und Zufahrtsrampen“, MacDonald nach den amerikanischen Berichten „with no success“. Beides kann stimmen: Ein Treffer auf eine Rampe ist noch keine zerstörte Brücke. Die Flugzeugzahlen sind Schätzungen der Flak.",
          "note_en": "The German situation report claims ‘several hits on the bridges and approach ramps’, MacDonald after the American reports ‘with no success’. Both may be true: a hit on a ramp is not yet a destroyed bridge. The aircraft figures are the antiaircraft units' estimates.",
          "voices": [{"text": "angriffe", "sec": "meldung", "n": [4], "wer": "Lagebericht zum OKW-Bericht, 17. März 1945", "wer_en": "Supplement to the OKW report, 17 March 1945"},
                     {"text": "angriffe", "sec": "luftwaffe", "n": [3], "wer": "MacDonald 1973", "wer_en": "MacDonald 1973"}]}]
pid = {p["id"] for p in PAIRS}
C["pairs"] = [p for p in C["pairs"] if p["id"] not in pid] + PAIRS
(D / "compare.json").write_text(json.dumps(C, ensure_ascii=False, indent=1), encoding="utf-8")

TL = json.loads((D / "timeline.json").read_text(encoding="utf-8"))
for s in TL["stations"]:
    if s["titel"] == "Elf V-2":
        s.update({"text": "Von den Niederlanden aus werden elf V-2-Raketen auf die Brücke abgefeuert, der einzige taktische Einsatz der V-Waffen im Krieg. Eine trifft ein Haus 300 Yards östlich der Brücke, also in Erpel: drei amerikanische Soldaten tot, fünfzehn verwundet (MacDonald, S. 228).",
                  "text_en": "Eleven V-2 rockets are fired at the bridge from the Netherlands, the only tactical use of the V-weapons in the war. One hits a house 300 yards east of the bridge, that is in Erpel: three American soldiers killed, fifteen wounded (MacDonald, p. 228).",
                  "cite": "#/text/angriffe/fernwaffen/6", "citeLabel": "Die Angriffe [6]", "citeLabel_en": "The attacks [6]"})
    if s["titel"] == "Kampfschwimmer":
        s.update({"d": "16.–18. März", "d_en": "16–18 March",
                  "text": "Sieben Schwimmer in Gummianzügen mit Sprengstoff sollen die Brücke erreichen. Artilleriefeuer hält sie in der ersten Nacht ab; in der zweiten schwimmen sie gegen die Pontonbrücken, werden von Scheinwerfern geblendet und ergeben sich (MacDonald, S. 228–229).",
                  "text_en": "Seven swimmers in rubber suits carrying explosives are to reach the bridge. Artillery fire keeps them back on the first night; on the second they swim against the treadway bridges, are blinded by searchlights and surrender (MacDonald, pp. 228–229).",
                  "cite": "#/text/angriffe/schwimmer/7", "citeLabel": "Die Angriffe [7]", "citeLabel_en": "The attacks [7]"})
(D / "timeline.json").write_text(json.dumps(TL, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", sum(len(s["units"]) for s in T["sections"]), "units", "film" if S5 else "ohne Film")
