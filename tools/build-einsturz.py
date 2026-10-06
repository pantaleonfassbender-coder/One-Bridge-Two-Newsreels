"""Baut data/einsturz.json (Modul 7: Der Einsturz, 17. März 1945).
Quellen: MacDonald, The Last Offensive (1973), S. 229–230 und 230–231, am Seitenbild gelesen;
Combat Bulletin No. 48 (1945), Tonspur; Erzgebirgischer Volksfreund und Müglitztal- und Geising-Bote vom
20. März 1945, am Seitenbild gelesen. Übersetzungen: eigene Arbeit (CC0).
Aufruf aus dem Wurzelverzeichnis: python tools/build-einsturz.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
DZP = "https://www.deutsche-digitale-bibliothek.de/newspaper/item/"


def u(n, pg, lang, orig, tr, titel=None, titel_en=None, note=None, note_en=None, pgl=None):
    x = {"n": n, "pg": pg, "lang": lang}
    if pgl: x["pgl"] = pgl
    if titel: x["titel"], x["titel_en"] = titel, titel_en
    x["orig"] = orig
    x["en" if lang == "de" else "de"] = tr
    if note: x["note"], x["note_en"] = note, note_en
    return x


S1 = [
    u(1, "S. 229", "en",
      "Two days later General Van Fleet, former commander of the 90th Division, arrived at Hodges' headquarters to take Millikin's place. Shortly before 1500, Hodges telephoned Millikin.\n\n“I have some bad news for you,” Hodges said, then went on to inform him of his relief.\n\nThe III Corps commander waited until Hodges had finished.\n\n“Sir,” he said finally, “I have some bad news for you too. The railroad bridge has just collapsed.”",
      "Zwei Tage später traf General Van Fleet, der frühere Kommandeur der 90th Division, in Hodges' Hauptquartier ein, um Millikins Platz einzunehmen. Kurz vor 15 Uhr rief Hodges Millikin an.\n\n„Ich habe eine schlechte Nachricht für Sie“, sagte Hodges und teilte ihm dann seine Ablösung mit.\n\nDer Kommandeur des III. Korps wartete, bis Hodges geendet hatte.\n\n„Sir“, sagte er schließlich, „ich habe auch eine schlechte Nachricht für Sie. Die Eisenbahnbrücke ist gerade eingestürzt.“",
      "Zwei schlechte Nachrichten", "Two pieces of bad news",
      "Nach MacDonalds Anm. 36 aus dem Kriegstagebuch von Hodges' Adjutanten (Sylvan Diary) vom 17. März. Millikins Ablösung hatte nichts mit dem Einsturz zu tun; sie war schon am 15. März beschlossen (S. 229).",
      "According to MacDonald's n. 36 from the war diary of Hodges' aide (Sylvan Diary) of 17 March. Millikin's relief had nothing to do with the collapse; it had been decided on 15 March (p. 229)."),
    u(2, "S. 229–230", "en",
      "It happened during a period of relative quiet. No German planes were around, and German artillery was silent. About 200 American engineers with their equipment were working on the bridge.\n\nThe first indication that anything was wrong was a sharp report like the crack of a rifle. Then another. The deck of the bridge began to tremble. The entire deck vibrated and swayed. Dust rose from the planking. It was every man for himself.\n\nWith a grinding roar of tearing steel, the Ludendorff railroad bridge slipped, sagged, and with a convulsive twist plunged into the Rhine. Of those working on the bridge at the time, 93 were injured, 28 killed.",
      "Es geschah in einer Zeit verhältnismäßiger Ruhe. Keine deutschen Flugzeuge waren in der Nähe, und die deutsche Artillerie schwieg. Etwa 200 amerikanische Pioniere arbeiteten mit ihrem Gerät auf der Brücke.\n\nDas erste Anzeichen, dass etwas nicht stimmte, war ein scharfer Knall wie ein Gewehrschuss. Dann noch einer. Die Fahrbahn begann zu zittern. Die ganze Fahrbahn bebte und schwankte. Staub stieg von den Bohlen auf. Jeder rettete sich, so gut er konnte.\n\nMit dem knirschenden Dröhnen reißenden Stahls rutschte die Ludendorff-Eisenbahnbrücke, sackte ein und stürzte mit einer krampfhaften Drehung in den Rhein. Von denen, die damals auf der Brücke arbeiteten, wurden 93 verletzt und 28 getötet.",
      "Der Einsturz", "The collapse",
      "28 Tote, am Seitenbild gelesen; die maschinelle Textfassung des Internet Archive liest 38. Das Bundesarchiv nennt 32 tote Pioniere (Online-Präsentation zum Erlass Kesselrings), Combat Bulletin 48 spricht von „about 300“ Pionieren auf der Brücke, die deutsche Presse nach Reuter von 290 (Einheiten 4–5). Der Bericht der Army Service Forces über den Einsturz (Report No. 126) ließ sich nicht einsehen.",
      "28 killed, read against the page image; the Internet Archive's machine text reads 38. The Bundesarchiv gives 32 dead engineers (online presentation of Kesselring's decree), Combat Bulletin 48 speaks of ‘about 300’ engineers on the bridge, the German press after Reuters of 290 (units 4–5). The Army Service Forces report on the collapse (Report No. 126) could not be consulted."),
]

S2 = [
    u(3, "S. 230", "en",
      "The collapse of the bridge could be attributed to no one specific factor but rather to a combination of things, some even antedating the emergency demolition. As far back as 1940 Allied planes had launched sporadic attacks against the bridge, and in late 1944 had damaged it to such an extent that it was unserviceable for fifteen days. Then came the heavy planking to convert the bridge for vehicles; the assault by the 27th Armored Infantry Battalion's Company A and the fire of the big Pershing tanks that accompanied it; Friesenhahn's emergency demolition; the drumbeat of hundreds of infantry feet; the heavy tread of tanks and other vehicles; the pounding of German artillery; the vibrations from German bombs, from American antiaircraft pieces and big 8-inch howitzers emplaced nearby, from the near misses of the V–2's; and then the weight of heavy engineer equipment as the Americans tried to repair the bridge. All had to be borne by the downstream truss alone after Friesenhahn's demolition so damaged the upstream truss that it was useless. In the end, it was too much for one weakened truss.",
      "Der Einsturz der Brücke ließ sich keiner einzelnen Ursache zuschreiben, sondern einem Zusammenwirken vieler Dinge, von denen manche sogar vor der Notsprengung lagen. Schon seit 1940 hatten alliierte Flugzeuge die Brücke gelegentlich angegriffen und sie Ende 1944 so schwer beschädigt, dass sie fünfzehn Tage lang unbenutzbar war. Dann kamen die schweren Bohlen, die die Brücke für Fahrzeuge befahrbar machten; der Sturm der Kompanie A des 27th Armored Infantry Battalion und das Feuer der großen Pershing-Panzer, die sie begleiteten; Friesenhahns Notsprengung; der Trommelschlag Hunderter Infanteristenstiefel; das schwere Rollen von Panzern und anderen Fahrzeugen; das Hämmern der deutschen Artillerie; die Erschütterungen durch deutsche Bomben, durch amerikanische Flak und große 20-cm-Haubitzen in der Nähe, durch die Nahtreffer der V-2; und schließlich das Gewicht des schweren Pioniergeräts, als die Amerikaner die Brücke auszubessern versuchten. All das musste nach Friesenhahns Sprengung der stromabwärtige Fachwerkträger allein tragen, denn der stromaufwärtige war so beschädigt, dass er nutzlos war. Am Ende war es zu viel für einen geschwächten Träger.",
      "Warum sie fiel", "Why it fell",
      "Nach MacDonalds Anm. 37 aus einem Gefechtsinterview mit Oberstleutnant Clayton A. Rust, Kommandeur des 276th Engineer Combat Battalion. Die Last der Instandsetzung steht am Ende der Reihe: Die Brücke stürzte ein, während man sie rettete.",
      "According to MacDonald's n. 37 from a combat interview with Lt. Col. Clayton A. Rust, commander of the 276th Engineer Combat Battalion. The weight of the repair stands at the end of the list: the bridge collapsed while it was being saved."),
]

S3 = [
    u(4, "Erzgebirgischer Volksfreund, 20.3.1945, S. 1", "de",
      "Rheinbrücke bei Remagen durch deutschen Beschuß vernichtet.\n\nWie Reuter meldet, ist die Ludendorff-Brücke über den Rhein bei Remagen am Sonnabend nachmittag „zusammengebrochen und in den Fluß gestürzt“. Das englische Nachrichtenbüro fügt hinzu: Die Brücke stellte die Hauptverbindung zwischen der 1. USA.-Armee auf dem Westufer des Rheins und dem Brückenkopf auf dem Ostufer dar. Wie feindliche Frontberichte der letzten Tage andeuteten, besteht außerdem eine Pontonbrücke, die vorläufig noch die Verbindung der beiden Kräftegruppen herstellt. Ein amerikanischer Offizier berichtet, der Einsturz der Ludendorff-Brücke sei auf eine „allgemeine Schwächung der Konstruktion“ infolge der Beschießung mit Granaten und der Bombardierung aus der Luft zurückzuführen. Während des Einsturzes arbeiteten 290 amerikanische Pioniere am mittleren Bogen der Brücke, von denen nur einige aus dem Wasser geborgen werden konnten. Die Mehrzahl wird vermißt.",
      "Rhine bridge at Remagen destroyed by German fire.\n\nAs Reuters reports, the Ludendorff Bridge over the Rhine at Remagen ‘collapsed and fell into the river’ on Saturday afternoon. The English news agency adds: the bridge was the main link between the US 1st Army on the west bank of the Rhine and the bridgehead on the east bank. As enemy front reports of the last few days have indicated, there is also a pontoon bridge which for the time being still connects the two groups of forces. An American officer reports that the collapse of the Ludendorff Bridge was due to a ‘general weakening of the structure’ as a result of shelling and bombing from the air. At the time of the collapse 290 American engineers were working on the centre arch of the bridge, of whom only a few could be recovered from the water. The majority are missing.",
      "„Durch deutschen Beschuß vernichtet“", "‘Destroyed by German fire’",
      "Die Überschrift macht aus einer Reuter-Meldung einen deutschen Erfolg; im Text selbst steht nur, ein amerikanischer Offizier habe von Schwächung durch Beschuss und Bomben gesprochen. Dass „nur einige“ geborgen wurden und „die Mehrzahl“ vermisst sei, widerspricht MacDonalds 28 Toten und 93 Verletzten von rund 200. „Pontonbrücke“: es waren am 17. März schon mehrere (Modul 4). Fraktursatz, am Seitenbild der SLUB Dresden gelesen. Zeitungsseite: " + DZP + "R6HE5YI22772YFTH4HR5FYDYPI6ZTSSG",
      "The headline turns a Reuters report into a German success; the text itself only says that an American officer spoke of weakening by shelling and bombs. That ‘only a few’ were recovered and ‘the majority’ were missing contradicts MacDonald's 28 killed and 93 injured out of some 200. ‘A pontoon bridge’: there were already several on 17 March (module 4). Set in Fraktur, read against the page image of the SLUB Dresden. Newspaper page: " + DZP + "R6HE5YI22772YFTH4HR5FYDYPI6ZTSSG"),
    u(5, "Müglitztal- und Geising-Bote, 20.3.1945, S. 1", "de",
      "Brückenkopf Remagen schwer umkämpft\n\nDer militärische Mitarbeiter der „Daily Mail“ ist der Ansicht, daß Eisenhower vor der Notwendigkeit stehe, seine Offensivpläne weitgehend umzuarbeiten. […] Aber ein zweiter Offensivschwerpunkt ist im Rheinbrückenkopf östlich Remagen entstanden, der wie eine riesige Saugpumpe wirkt. Im Hauptquartier Eisenhowers scheint darüber keine reine Freude zu herrschen.\n\nDie Entstehung des Brückenkopfes Remagen ist auf den für den Feind günstigen Umstand zurückzuführen, daß die Ludendorff-Eisenbahnbrücke, die dort über den Rhein führt, nicht rechtzeitig gesprengt und nicht entschlossen verteidigt wurde. Wie der Wehrmachtsbericht vom Sonntag meldete, haben die dafür verantwortlichen pflichtvergessenen Offiziere durch das Standgericht ihre verdiente Strafe erhalten. Inzwischen ist die Eisenbahnbrücke nun durch deutsche Bomben und Granaten eingestürzt.\n\nDie Nachschubschwierigkeiten des Feindes, der gezwungen ist, immer neue Kräfte in den wie ein Magnet wirkenden Brückenkopf hineinzuwerfen, wachsen also. […] An keiner Stelle konnte der Feind den Brückenkopf weiter als bis zu 9 km Tiefe und 20 km Breite ausweiten.",
      "Remagen bridgehead hard fought over\n\nThe military correspondent of the ‘Daily Mail’ is of the opinion that Eisenhower faces the need to rework his offensive plans extensively. […] But a second focus of the offensive has arisen in the Rhine bridgehead east of Remagen, which acts like a huge suction pump. At Eisenhower's headquarters there seems to be no unmixed joy about this.\n\nThe origin of the Remagen bridgehead is due to the circumstance, favourable to the enemy, that the Ludendorff railway bridge which crosses the Rhine there was not blown in time and not resolutely defended. As the Wehrmacht report of Sunday announced, the negligent officers responsible have received their deserved punishment from the court-martial. Meanwhile the railway bridge has now collapsed under German bombs and shells.\n\nThe enemy's supply difficulties, as he is forced to throw ever new forces into the bridgehead, which acts like a magnet, are therefore growing. […] Nowhere could the enemy extend the bridgehead beyond a depth of 9 km and a width of 20 km.",
      "„ihre verdiente Strafe“", "‘their deserved punishment’",
      "In drei Sätzen: die Brücke nicht gesprengt, die Offiziere erschossen „zu Recht“, die Brücke nun „durch deutsche Bomben und Granaten eingestürzt“. Das Schweigen über die Brücke endete, als beides zu melden war, Strafe und Einsturz (Modul 5). Fraktursatz, am Seitenbild der SLUB Dresden gelesen; im Druck „erhaltrn“. Zeitungsseite: " + DZP + "ZSWBPHNX62NQG3JSANA2HKMV5534UBO4",
      "In three sentences: the bridge not blown, the officers shot ‘deservedly’, the bridge now ‘collapsed under German bombs and shells’. The silence about the bridge ended when both could be announced, the punishment and the collapse (module 5). Set in Fraktur, read against the page image of the SLUB Dresden. Newspaper page: " + DZP + "ZSWBPHNX62NQG3JSANA2HKMV5534UBO4"),
]

S4 = [
    u(6, "15:08–16:45", "en",
      "But weakened by the cumulative damage, the Ludendorff collapses on 17th March while about 300 engineer troops are working on it. Many of them are hurled into the swift icy water or crushed by the falling structure. Rescue crews save those who manage to cling to sections of the span as it gave way. Rescuers swim out into the Rhine to reach injured men kept afloat by driftwood, bringing out a line to pull in the surviving engineers. Quick action of this type saves many lives.\n\nWhen the 512-foot center span of the Ludendorff gave way, there was no vehicular traffic crossing the bridge. Crews extricate bodies pinned beneath the heavy beams. Three days later on 20th March, Supreme Headquarters announces that the collapsed Ludendorff bridge has been abandoned. The dispatch says that the span is no longer necessary because of the existence of other facilities across the Rhine into the Remagen bridgehead.",
      "Doch geschwächt von den angehäuften Schäden stürzt die Ludendorff-Brücke am 17. März ein, während etwa 300 Pioniere auf ihr arbeiten. Viele von ihnen werden in das reißende, eiskalte Wasser geschleudert oder von der stürzenden Konstruktion zerquetscht. Rettungsmannschaften bergen die, die sich an Teilen der Brücke festhalten konnten, als sie nachgab. Retter schwimmen in den Rhein hinaus zu Verletzten, die sich an Treibholz über Wasser halten, und bringen eine Leine, um die überlebenden Pioniere hereinzuziehen. Schnelles Handeln dieser Art rettet viele Leben.\n\nAls das 512 Fuß lange Mittelstück der Ludendorff-Brücke nachgab, fuhren keine Fahrzeuge über die Brücke. Mannschaften bergen Leichen, die unter den schweren Trägern eingeklemmt sind. Drei Tage später, am 20. März, gibt das Oberste Hauptquartier bekannt, die eingestürzte Ludendorff-Brücke werde aufgegeben. Die Meldung sagt, die Brücke sei nicht mehr nötig, weil es andere Übergänge über den Rhein in den Brückenkopf Remagen gebe.",
      "Combat Bulletin No. 48", "Combat Bulletin No. 48",
      "Ton maschinell abgeschrieben und durchgesehen. 512 Fuß sind rund 156 Meter. Die Bilder der Rettung stammen aus derselben Rolle des Signal Corps wie die stumme Aufnahme 111-ADC-3597; anders als die Wochenschau United News zeigt der Combat Bulletin auch die Bergung von Toten (Modul 8).",
      "Soundtrack transcribed by machine and reviewed. The rescue pictures come from the same Signal Corps reel as the silent footage 111-ADC-3597; unlike the United News newsreel, the Combat Bulletin also shows the recovery of the dead (module 8).",
      pgl="Film"),
]

T = {
    "id": "einsturz",
    "titel": "Der Einsturz", "titel_en": "The collapse",
    "autor": "Charles B. MacDonald, The Last Offensive (1973); deutsche Presse (20. März 1945); Combat Bulletin No. 48 (1945)",
    "autor_en": "Charles B. MacDonald, The Last Offensive (1973); German press (20 March 1945); Combat Bulletin No. 48 (1945)",
    "jahr": "17.–20. März 1945", "jahr_en": "17–20 March 1945",
    "sprache": "de", "orig_sprache": "en", "pg_label": "", "pg_label_en": "",
    "quelle": "Charles B. MacDonald, The Last Offensive (1973), S. 229–230, am Seitenbild des Internet Archive gelesen, gemeinfrei. Erzgebirgischer Volksfreund und Müglitztal- und Geising-Bote vom 20. März 1945, am Seitenbild im Deutschen Zeitungsportal gelesen (Meldungen ohne Verfasser nach Agenturen; die Scans sind verlinkt). Combat Bulletin No. 48 (Army Pictorial Service, 1945), Internet Archive CB-48, Tonspur. Stumme Aufnahmen des Signal Corps vom 17. März 1945 (National Archives, NAID 17400), Internet Archive 111-adc-3597.",
    "quelle_en": "Charles B. MacDonald, The Last Offensive (1973), pp. 229–230, read against the page images of the Internet Archive, public domain. Erzgebirgischer Volksfreund and Müglitztal- und Geising-Bote of 20 March 1945, read against the page images in the Deutsches Zeitungsportal (unsigned agency reports; the scans are linked). Combat Bulletin No. 48 (Army Pictorial Service, 1945), Internet Archive CB-48, soundtrack. Silent Signal Corps footage of 17 March 1945 (National Archives, NAID 17400), Internet Archive 111-adc-3597.",
    "hinweis": "Am Nachmittag des 17. März 1945, in einer ruhigen Stunde, stürzte die Brücke in den Rhein, während amerikanische Pioniere sie instand setzten. Wie viele auf ihr waren und wie viele starben, sagen die Quellen verschieden; die Zahlen stehen nebeneinander. Die deutsche Presse machte aus dem Einsturz einen Erfolg der eigenen Waffen. Der Film zeigt Verletzte und Tote. Texte nach dem Druck, Fraktur in Antiqua, Auslassungen […]; Übersetzungen eigene Arbeit (CC0).",
    "hinweis_en": "On the afternoon of 17 March 1945, in a quiet hour, the bridge fell into the Rhine while American engineers were repairing it. How many were on it and how many died, the sources say differently; the figures stand side by side. The German press turned the collapse into a success of German arms. The film shows injured and dead men. Texts after the print, Fraktur set in roman type, omissions […]; translations my own (CC0).",
    "sections": [
        {"id": "nachmittag", "titel": "Der Nachmittag des 17. März", "titel_en": "The afternoon of 17 March", "zk": "Einsturz · Nachmittag", "zk_en": "Collapse · Afternoon",
         "blurb": "Kurz vor 15 Uhr: Hodges löst Millikin ab, und Millikin meldet den Einsturz. Kein Flugzeug, keine Granate; ein Knall wie ein Gewehrschuss, dann noch einer, dann fällt die Brücke mit den Pionieren in den Rhein.",
         "blurb_en": "Shortly before 1500: Hodges relieves Millikin, and Millikin reports the collapse. No aircraft, no shell; a crack like a rifle shot, then another, then the bridge falls into the Rhine with the engineers.",
         "plates": ["nara195343", "adc3597_truemmer"], "viz": "einsturz", "units": S1},
        {"id": "ursachen", "titel": "Warum sie fiel", "titel_en": "Why it fell", "zk": "Einsturz · Ursachen", "zk_en": "Collapse · Causes",
         "blurb": "Bomben seit 1940, Bohlen, Panzer, Friesenhahns Sprengung, Stiefel, Artillerie, Flak, V-2, und zuletzt das Gerät der Pioniere: alles auf einem einzigen Träger.",
         "blurb_en": "Bombs since 1940, planks, tanks, Friesenhahn's demolition, boots, artillery, antiaircraft, V-2s, and last the engineers' equipment: all on a single truss.",
         "units": S2},
        {"id": "presse", "titel": "„Durch deutschen Beschuß vernichtet“", "titel_en": "‘Destroyed by German fire’", "zk": "Einsturz · Presse", "zk_en": "Collapse · Press",
         "blurb": "Drei Tage später meldet die deutsche Presse den Einsturz nach Reuter, mit eigener Überschrift, und verbindet ihn mit den Erschossenen: Strafe und Erfolg in einem Absatz.",
         "blurb_en": "Three days later the German press reports the collapse after Reuters, under its own headline, and links it with the officers who were shot: punishment and success in one paragraph.",
         "units": S3},
        {"id": "film", "titel": "Bergung", "titel_en": "Rescue", "zk": "Einsturz · Film", "zk_en": "Collapse · Film",
         "blurb": "Retter schwimmen mit einer Leine in den Strom, Verletzte werden ans Ufer gezogen, Leichen aus den Trägern geborgen. Drei Tage später gibt das Oberste Hauptquartier die Brücke auf.",
         "blurb_en": "Rescuers swim into the current with a line, injured men are pulled ashore, bodies recovered from the girders. Three days later Supreme Headquarters abandons the bridge.",
         "plates": ["adc3597_rettung"], "films": [{"film": "collapse"}, {"film": "cb48", "start": "15:08", "end": "16:45"}], "units": S4},
    ],
}
(D / "einsturz.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")

P = json.loads((D / "plates.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "nara195343", "side": "bruecke", "titel": "Die eingestürzte Brücke", "titel_en": "The collapsed bridge",
     "caption": "Soldaten am Remagener Ufer vor den Trümmern der Ludendorff-Brücke, um den 17. März 1945.",
     "caption_en": "Soldiers on the Remagen bank in front of the wreckage of the Ludendorff Bridge, about 17 March 1945.",
     "source": "U.S. Army, „U.S. First Army at Remagen Bridge“ (National Archives, NAID 195343), über Wikimedia Commons; gemeinfrei."},
    {"id": "adc3597_truemmer", "side": "film", "titel": "Die Brücke im Rhein", "titel_en": "The bridge in the Rhine",
     "caption": "Die Trümmer im Strom, dahinter die Türme auf dem Remagener Ufer. Standbild aus den stummen Aufnahmen des Signal Corps vom 17. März 1945.",
     "caption_en": "The wreckage in the river, behind it the towers on the Remagen bank. Still from the silent Signal Corps footage of 17 March 1945.",
     "source": "Collapse of Remagen (Ludendorff) Bridge, Germany (National Archives, NAID 17400), 0:16; Internet Archive 111-adc-3597."},
    {"id": "adc3597_rettung", "side": "film", "titel": "Rettung aus dem Rhein", "titel_en": "Rescue from the Rhine",
     "caption": "Soldaten ziehen einen Pionier aus dem Wasser. Standbild aus den stummen Aufnahmen des Signal Corps vom 17. März 1945.",
     "caption_en": "Soldiers pull an engineer out of the water. Still from the silent Signal Corps footage of 17 March 1945.",
     "source": "Collapse of Remagen (Ludendorff) Bridge, Germany (National Archives, NAID 17400), 2:13; Internet Archive 111-adc-3597."},
]
ids = {p["id"] for p in NEW}
P["plates"] = [p for p in P["plates"] if p["id"] not in ids] + NEW
(D / "plates.json").write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")

M = json.loads((D / "modules.json").read_text(encoding="utf-8"))
m = next((x for x in M["planned"] if x["id"] == "einsturz"), None) or next(x for x in M["shipped"] if x["id"] == "einsturz")
M["planned"] = [x for x in M["planned"] if x["id"] != "einsturz"]
m.update({"datei": "einsturz", "zk": "Nachmittag · Ursachen · Presse · Film", "zk_en": "Afternoon · Causes · Press · Film",
          "kurz": "7 · Der Einsturz", "kurz_en": "7 · The collapse",
          "warum": "In einer ruhigen Stunde am 17. März stürzte die Brücke mit den Pionieren, die sie instand setzten, in den Rhein: nach MacDonald 28 Tote und 93 Verletzte. Die deutsche Presse meldete: „durch deutschen Beschuß vernichtet“.",
          "warum_en": "In a quiet hour on 17 March the bridge fell into the Rhine with the engineers repairing it: according to MacDonald 28 killed and 93 injured. The German press reported: ‘destroyed by German fire’.",
          "quelle": "MacDonald (1973), S. 229–230; deutsche Presse vom 20. März 1945; Combat Bulletin No. 48; Signal Corps, 17. März 1945.",
          "quelle_en": "MacDonald (1973), pp. 229–230; German press of 20 March 1945; Combat Bulletin No. 48; Signal Corps, 17 March 1945."})
order = ["bruecke", "siebter", "warum", "brueckenkopf", "standgericht", "angriffe", "einsturz"]
M["shipped"] = sorted([x for x in M["shipped"] if x["id"] != "einsturz"] + [m], key=lambda x: order.index(x["id"]) if x["id"] in order else 99)
(D / "modules.json").write_text(json.dumps(M, ensure_ascii=False, indent=1), encoding="utf-8")

C = json.loads((D / "compare.json").read_text(encoding="utf-8"))
PAIRS = [
    {"id": "zahlen", "titel": "Wie viele?", "titel_en": "How many?",
     "frage": "Wie viele Pioniere waren auf der Brücke, und wie viele starben?", "frage_en": "How many engineers were on the bridge, and how many died?",
     "note": "Auf der Brücke: etwa 200 (MacDonald), 290 (Reuter in der deutschen Presse), etwa 300 (Combat Bulletin 48). Tote: 28 und 93 Verletzte (MacDonald), 32 (Bundesarchiv, nach neuerer Darstellung), „die Mehrzahl wird vermißt“ (deutsche Presse am 20. März, drei Tage danach). Die Zahlen stammen aus verschiedenen Zeitpunkten; die frühe Meldung kannte das Ergebnis der Bergung noch nicht.",
     "note_en": "On the bridge: about 200 (MacDonald), 290 (Reuters in the German press), about 300 (Combat Bulletin 48). Dead: 28 and 93 injured (MacDonald), 32 (Bundesarchiv, after a recent account), ‘the majority are missing’ (German press on 20 March, three days later). The figures come from different moments; the early report did not yet know the outcome of the rescue.",
     "voices": [{"text": "einsturz", "sec": "nachmittag", "n": [2], "wer": "MacDonald 1973", "wer_en": "MacDonald 1973"},
                {"text": "einsturz", "sec": "presse", "n": [4], "wer": "Deutsche Presse nach Reuter, 20. März 1945", "wer_en": "German press after Reuters, 20 March 1945"},
                {"text": "einsturz", "sec": "film", "n": [6], "wer": "Combat Bulletin 48, 1945", "wer_en": "Combat Bulletin 48, 1945"}]},
    {"id": "ursache", "titel": "Wer brachte sie zum Einsturz?", "titel_en": "Who brought it down?",
     "frage": "Bomben, Granaten oder das eigene Gewicht?", "frage_en": "Bombs, shells or its own weight?",
     "note": "Die deutsche Presse: „durch deutsche Bomben und Granaten“. MacDonald: das Zusammenwirken vieler Lasten auf einem einzigen geschwächten Träger, zuletzt das Gerät der amerikanischen Pioniere, „in einer Zeit verhältnismäßiger Ruhe“. Die Wochenschau Universal sprach von „heavy traffic and bomb hits“ (Seite „Filme“).",
     "note_en": "The German press: ‘German bombs and shells’. MacDonald: the combined loads on a single weakened truss, last of all the American engineers' equipment, ‘during a period of relative quiet’. The Universal newsreel spoke of ‘heavy traffic and bomb hits’ (Films page).",
     "voices": [{"text": "einsturz", "sec": "presse", "n": [5], "wer": "Müglitztal-Bote, 20. März 1945", "wer_en": "Müglitztal-Bote, 20 March 1945"},
                {"text": "einsturz", "sec": "ursachen", "n": [3], "wer": "MacDonald 1973", "wer_en": "MacDonald 1973"}]},
]
pid = {p["id"] for p in PAIRS}
C["pairs"] = [p for p in C["pairs"] if p["id"] not in pid] + PAIRS
(D / "compare.json").write_text(json.dumps(C, ensure_ascii=False, indent=1), encoding="utf-8")

TL = json.loads((D / "timeline.json").read_text(encoding="utf-8"))
for s in TL["stations"]:
    if s["titel"] == "Der Einsturz":
        s.update({"d": "17. März, kurz vor 15 Uhr", "d_en": "17 March, shortly before 1500",
                  "text": "In einer ruhigen Stunde, während rund 200 amerikanische Pioniere auf ihr arbeiten, stürzt die Brücke in den Rhein; nach MacDonald 28 Tote und 93 Verletzte (S. 230), nach dem Bundesarchiv 32 Tote. Am 20. März meldet die deutsche Presse sie „durch deutschen Beschuß vernichtet“, und das Oberste Hauptquartier gibt sie auf.",
                  "text_en": "In a quiet hour, while some 200 American engineers are working on it, the bridge falls into the Rhine; according to MacDonald 28 killed and 93 injured (p. 230), according to the Bundesarchiv 32 dead. On 20 March the German press reports it ‘destroyed by German fire’, and Supreme Headquarters abandons it.",
                  "cite": "#/text/einsturz/nachmittag/2", "citeLabel": "Der Einsturz [2]", "citeLabel_en": "The collapse [2]", "plate": "nara195343"})
(D / "timeline.json").write_text(json.dumps(TL, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", sum(len(s["units"]) for s in T["sections"]), "units")
