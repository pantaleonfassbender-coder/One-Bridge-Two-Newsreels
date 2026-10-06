"""Baut data/wochenschauen.json (Modul 8: Zwei Wochenschauen).
Quellen: Tonspuren der Universal-Wochenschau vom 26. März 1945 und der United News (1945), maschinell
abgeschrieben und durchgesehen; Katalogtexte des Imperial War Museum zu britischen Wochenschauen (kurz
zitiert); eigene Inhaltsangaben der Deutschen Wochenschau Nr. 754 und 755 nach Sichtung und einer nicht
veröffentlichten Prüfabschrift; Erzgebirgischer Volksfreund vom 20. März 1945, am Seitenbild gelesen.
Übersetzungen: eigene Arbeit (CC0).
Aufruf aus dem Wurzelverzeichnis: python tools/build-wochenschauen.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
DZP = "https://www.deutsche-digitale-bibliothek.de/newspaper/item/"
F = {f["id"]: f for f in json.loads((D / "films.json").read_text(encoding="utf-8"))["films"]}


def ton(fid, *ts):
    z = [x for x in F[fid]["ton"] if x["t"] in ts]
    return "\n\n".join(x["en"] for x in z), "\n\n".join(x["de"] for x in z)


def u(n, pg, lang, orig, tr, titel=None, titel_en=None, note=None, note_en=None, pgl=None):
    x = {"n": n, "pg": pg, "lang": lang}
    if pgl: x["pgl"] = pgl
    if titel: x["titel"], x["titel_en"] = titel, titel_en
    x["orig"] = orig
    x["en" if lang == "de" else "de"] = tr
    if note: x["note"], x["note_en"] = note, note_en
    return x


uen, ude = ton("universal", "2:41", "2:54", "3:17", "3:37")
S1 = [u(1, "2:41–3:56", "en", uen, ude, "Universal Newsreel, 26. März 1945", "Universal Newsreel, 26 March 1945",
        "Die Bilder zeigen die Brücke, Fahrzeuge, Flak, Infanterie und lange Kolonnen von Gefangenen; vieles stammt aus der stummen Signal-Corps-Rolle ADC-3612c (Seite „Filme“). Der Sprecher macht aus dem Schild an der Brücke einen Satz: „dry feet were by courtesy of the 9th Armoured Division“. Von Toten spricht er nicht; der Einsturz ist ein Nebensatz. „minutes before the Germans […]“: ein Wort unverständlich.",
        "The pictures show the bridge, vehicles, antiaircraft guns, infantry and long columns of prisoners; much of it comes from the silent Signal Corps reel ADC-3612c (Films page). The narrator turns the sign at the bridge into a sentence: ‘dry feet were by courtesy of the 9th Armoured Division’. He does not speak of the dead; the collapse is a subordinate clause.",
        pgl="Film")]

a_en, a_de = ton("united", "4:32", "4:56", "5:07")
b_en, b_de = ton("united", "5:44", "5:59", "6:40", "6:59", "7:30")
S2 = [
    u(2, "4:32–5:40", "en", a_en, a_de, "United News: die Brücke", "United News: the bridge",
      "„the only bridge captured intact“ und „the Wehrmacht blunder“: Die amerikanische Wochenschau spricht wie der deutsche Wehrmachtbericht vom Versagen der Deutschen an der Brücke (Modul 5).",
      "‘The only bridge captured intact’ and ‘the Wehrmacht blunder’: the American newsreel speaks, like the German Wehrmacht report, of German failure at the bridge (module 5).",
      pgl="Film"),
    u(3, "5:44–7:40", "en", b_en, b_de, "United News: die Pioniere", "United News: the engineers",
      "Die Worte nennen die Toten: ertrunken, an Verletzungen gestorben, „more dead than alive“ geborgen. Die Bilder zeigen die Rettung aus dem Fluss und Tragen, aber nicht die Toten und Eingeklemmten zwischen den Trägern, die die stumme Rolle des Signal Corps vom selben Tag festhält (111-ADC-3597, 4:22–4:42). Das Wort sagt hier mehr als das Bild.",
      "The words name the dead: drowned, died of injuries, pulled out ‘more dead than alive’. The pictures show the rescue from the river and stretchers, but not the dead and trapped men between the girders recorded by the silent Signal Corps reel of the same day (111-ADC-3597, 4:22–4:42). Here the word says more than the picture.",
      pgl="Film"),
]

S3 = [
    u(4, "IWM 32000", "en",
      "Engineers repair the Remagen Bridge over the Rhine shortly before its collapse. Film taken immediately after the collapse shows rescue operations under way, including a stretcher casualty being lifted from the buckled girders and men coming ashore from the swift-flowing river.",
      "Pioniere setzen die Brücke von Remagen kurz vor ihrem Einsturz instand. Aufnahmen unmittelbar nach dem Einsturz zeigen die Rettung: Ein Verwundeter wird auf einer Trage aus den verbogenen Trägern gehoben, Männer kommen aus dem reißenden Fluss an Land.",
      "British Movietone News Nr. 825, 26. März 1945", "British Movietone News no. 825, 26 March 1945",
      "Kein Text der Wochenschau, sondern die Beschreibung im Katalog des Imperial War Museum (film.iwmcollections.org.uk, Datensatz 32000), hier kurz zitiert; den Film selbst habe ich nicht gesehen. Erschienen am selben Tag wie die Universal-Wochenschau, mit den Bildern der Bergung.",
      "Not a text of the newsreel but the description in the Imperial War Museum catalogue (film.iwmcollections.org.uk, record 32000), quoted briefly here; I have not seen the film itself. Released on the same day as the Universal newsreel, with the pictures of the rescue.",
      ),
    u(5, "IWM 28364", "en",
      "Softening up attacks using rocket-tanks lead to the taking of the bridge at Remagen by the American 9th Armoured Division. […] Americans have to be rescued from the wreckage, when the bridge collapses without warning.",
      "Zermürbende Angriffe mit Raketenpanzern führen zur Einnahme der Brücke von Remagen durch die amerikanische 9. Panzerdivision. […] Amerikaner müssen aus den Trümmern gerettet werden, als die Brücke ohne Vorwarnung einstürzt.",
      "Gaumont-British News, Mai 1945", "Gaumont-British News, May 1945",
      "Beschreibung im Katalog des Imperial War Museum (Datensatz 28364), kurz zitiert. Raketenpanzer kommen in keiner der hier abgedruckten Darstellungen des 7. März vor (Modul 2); der Katalog beschreibt, was der Film zeigt, nicht was geschah. Die britischen Wochenschauen sind nur über den YouTube-Kanal ihrer Rechteinhaber eingebettet.",
      "Description in the Imperial War Museum catalogue (record 28364), quoted briefly. Rocket tanks appear in none of the accounts of 7 March printed here (module 2); the catalogue describes what the film shows, not what happened. The British newsreels are embedded only through their rights holders' YouTube channel.",
      ),
]

S4 = [
    u(6, "DW 754, 16.3.1945", "de",
      "Die Deutsche Wochenschau Nr. 754 vom 16. März 1945, neun Tage nach dem Übergang, beginnt mit Streiks in England und den USA. Dann der Westen: Der Sprecher behauptet sinngemäß, auch am Rhein sei dem amerikanischen General die Umklammerung der deutschen Truppen nicht gelungen; das Gros sei mit allen schweren Waffen über den Strom gegangen, an der Rur sei die geplante Einkesselung gescheitert. Es folgen Volksgrenadiere mit Panzerfäusten, Fallschirmjäger, General Wlassow, Kurland, Flüchtlingstrecks, die Marienburg, Lauban und Görlitz mit Goebbels und einem sechzehnjährigen Hitlerjungen mit dem Eisernen Kreuz, zuletzt Hitler bei einem Divisionsstab im Osten. Remagen kommt nicht vor, weder Brücke noch Brückenkopf.",
      "Die Deutsche Wochenschau no. 754 of 16 March 1945, nine days after the crossing, opens with strikes in Britain and the United States. Then the west: the narrator claims, in substance, that on the Rhine too the American general failed to encircle the German troops; the bulk had crossed the river with all its heavy weapons, and on the Roer the planned encirclement had failed. There follow Volksgrenadiers with Panzerfausts, paratroopers, General Vlasov, Courland, refugee treks, the Marienburg, Lauban and Görlitz with Goebbels and a sixteen-year-old Hitler Youth with the Iron Cross, and finally Hitler at a divisional headquarters in the east. Remagen does not appear, neither bridge nor bridgehead.",
      "Nr. 754: der Rhein, aber nicht Remagen", "No. 754: the Rhine, but not Remagen",
      "Eigene Inhaltsangabe (CC BY 4.0) nach Sichtung und einer maschinellen Prüfabschrift des Tons, die nicht veröffentlicht wird; die Wochenschau selbst wird weder gezeigt noch eingebettet noch zitiert. Grundlage: Kopie im Internet Archive (1945-03-16-Die-Deutsche-Wochenschau-754, privater Upload) und deren Inhaltsangabe. Die Wochenschau kennt den Rhein als Strom, über den die eigenen Truppen geordnet zurückgingen, nicht als Strom, über den der Gegner gekommen war.",
      "My own summary (CC BY 4.0) after viewing and an unpublished machine check-transcript of the soundtrack; the newsreel itself is neither shown, embedded nor quoted. Basis: copy in the Internet Archive (1945-03-16-Die-Deutsche-Wochenschau-754, private upload) and its summary. The newsreel knows the Rhine as the river across which German troops withdrew in good order, not as the river the enemy had crossed.",
      ),
    u(7, "DW 755, 22.3.1945", "de",
      "Die Deutsche Wochenschau Nr. 755 vom 22. März 1945, die letzte: ein Feuerwerker, der über tausend Bomben entschärft hat; Volkssturm und Zivilisten an der Panzerfaust; Hitler empfängt in seinem Hauptquartier Reichsjugendführer Axmann mit zwanzig Hitlerjungen, die das Eiserne Kreuz erhalten haben, und lässt sich ihre Erlebnisse schildern; ein Volkssturmführer mit dem Ritterkreuz; Breslau, Königsberg, die Kriegsmarine vor Ost- und Westpreußen, der Brückenkopf Stettin. Aus dem Westen nichts.",
      "Die Deutsche Wochenschau no. 755 of 22 March 1945, the last: a bomb disposal officer who has defused over a thousand bombs; Volkssturm and civilians with the Panzerfaust; Hitler receives Reich Youth Leader Axmann with twenty Hitler Youths who have received the Iron Cross and has them describe their experiences; a Volkssturm commander with the Knight's Cross; Breslau, Königsberg, the navy off East and West Prussia, the Stettin bridgehead. Nothing from the west.",
      "Nr. 755: die letzte Ausgabe", "No. 755: the last issue",
      "Eigene Inhaltsangabe (CC BY 4.0) nach Sichtung und Prüfabschrift; Kopie im Internet Archive (1945-03-22-Die-Deutsche-Wochenschau-755, privater Upload). Nach dem Bundesarchiv ist die Ausgabe online „aus rechtlichen Gründen“ gesperrt; die Verwertungsrechte liegen bei der Transit Film GmbH.",
      "My own summary (CC BY 4.0) after viewing and a check-transcript; copy in the Internet Archive (1945-03-22-Die-Deutsche-Wochenschau-755, private upload). According to the Bundesarchiv the issue is blocked online ‘for legal reasons’; the rights are held by Transit Film GmbH.",
      ),
    u(8, "Erzgebirgischer Volksfreund, 20.3.1945, S. 1", "de",
      "Tapfere Hitlerjungen beim Führer.\nDer Führer empfing in seinem Hauptquartier Reichsjugendführer Axmann mit einer Abordnung von 20 Hitlerjungen, die sich bei der Verteidigung ihrer Heimat in Pommern, Nieder- und Oberschlesien als Einzelkämpfer besonders bewährt haben.\n\n[unmittelbar darunter:]\nRheinbrücke bei Remagen durch deutschen Beschuß vernichtet.\nWie Reuter meldet, ist die Ludendorff-Brücke über den Rhein bei Remagen am Sonnabend nachmittag „zusammengebrochen und in den Fluß gestürzt“. […]",
      "Brave Hitler Youths with the Führer.\nThe Führer received at his headquarters Reich Youth Leader Axmann with a delegation of 20 Hitler Youths who have proved themselves particularly as lone fighters in the defence of their homeland in Pomerania, Lower and Upper Silesia.\n\n[immediately below:]\nRhine bridge at Remagen destroyed by German fire.\nAs Reuters reports, the Ludendorff Bridge over the Rhine at Remagen ‘collapsed and fell into the river’ on Saturday afternoon. […]",
      "Zwei Meldungen, eine Spalte", "Two reports, one column",
      "Dieselbe Zeitungsspalte vom 20. März enthält beide Meldungen, eine über der anderen. Die Wochenschau zwei Tage später nahm die erste, fast mit denselben Worten, und ließ die zweite weg. Den vollständigen Remagen-Text gibt Modul 7, Einheit 4. Fraktursatz, am Seitenbild der SLUB Dresden gelesen. Zeitungsseite: " + DZP + "R6HE5YI22772YFTH4HR5FYDYPI6ZTSSG",
      "The same newspaper column of 20 March contains both reports, one above the other. The newsreel two days later took the first, in almost the same words, and left out the second. The full Remagen text is in module 7, unit 4. Set in Fraktur, read against the page image of the SLUB Dresden. Newspaper page: " + DZP + "R6HE5YI22772YFTH4HR5FYDYPI6ZTSSG"),
]

T = {
    "id": "wochenschauen",
    "titel": "Zwei Wochenschauen", "titel_en": "Two newsreels",
    "autor": "Universal Newsreel, United News, britische Wochenschauen, Deutsche Wochenschau (März 1945)",
    "autor_en": "Universal Newsreel, United News, British newsreels, Die Deutsche Wochenschau (March 1945)",
    "jahr": "März 1945", "jahr_en": "March 1945",
    "sprache": "de", "orig_sprache": "en", "pg_label": "", "pg_label_en": "",
    "quelle": "Universal Newsreel vom 26. März 1945 (Internet Archive, als gemeinfrei gekennzeichnet) und United News, „Bridgehead Extended“ (National Archives, ARC 39162, CC0), Tonspuren maschinell abgeschrieben und durchgesehen. Katalogtexte des Imperial War Museum zu British Movietone News Nr. 825 und Gaumont-British News, kurz zitiert. Eigene Inhaltsangaben der Deutschen Wochenschau Nr. 754 und 755. Erzgebirgischer Volksfreund vom 20. März 1945, am Seitenbild im Deutschen Zeitungsportal gelesen.",
    "quelle_en": "Universal Newsreel of 26 March 1945 (Internet Archive, marked public domain) and United News, ‘Bridgehead Extended’ (National Archives, ARC 39162, CC0), soundtracks transcribed by machine and reviewed. Imperial War Museum catalogue texts on British Movietone News no. 825 and Gaumont-British News, quoted briefly. My own summaries of Die Deutsche Wochenschau nos. 754 and 755. Erzgebirgischer Volksfreund of 20 March 1945, read against the page image in the Deutsches Zeitungsportal.",
    "hinweis": "Was die Kinos im März 1945 von Remagen zeigten. Die amerikanischen und britischen Wochenschauen brachten die Brücke, die Gefangenen, den Einsturz und die Rettung, und sie zeigten weniger, als ihre Kameraleute gefilmt hatten. Die Deutsche Wochenschau zeigte Remagen nicht: In Nr. 754 kommt der Rhein vor, als Strom des geordneten Rückzugs; in Nr. 755, der letzten, nichts aus dem Westen. Ihre Ausgaben werden hier nur nach ihrem Inhalt beschrieben. Wer in Deutschland im März 1945 mehr über Remagen erfahren wollte, war auf die Meldungen der Gegenseite angewiesen, die die Zeitungen nach Reuter druckten, oder auf verbotene Sender; darunter war auch ein amerikanischer Tarnsender („1212“), der sich als deutscher ausgab (neuere Literatur; ob er über Remagen sendete, ist hier nicht belegt).",
    "hinweis_en": "What the cinemas showed of Remagen in March 1945. The American and British newsreels brought the bridge, the prisoners, the collapse and the rescue, and they showed less than their cameramen had filmed. The German newsreel did not show Remagen: in no. 754 the Rhine appears, as the river of an orderly withdrawal; in no. 755, the last, nothing from the west. Its issues are described here only by their contents. Anyone in Germany in March 1945 who wanted to know more about Remagen depended on the enemy's reports, which the newspapers printed after Reuters, or on forbidden stations; among them was an American black station (‘1212’) posing as German (recent literature; whether it broadcast about Remagen is not documented here).",
    "sections": [
        {"id": "universal", "titel": "Universal: „Allies Drive Across Rhine to Victory“", "titel_en": "Universal: ‘Allies Drive Across Rhine to Victory’", "zk": "Wochenschauen · Universal", "zk_en": "Newsreels · Universal",
         "blurb": "Die amerikanische Kinowochenschau vom 26. März 1945: ein „spektakulärer Handstreich“, Gefangene, trockene Füße „mit freundlicher Empfehlung“, ein Einsturz im Nebensatz.",
         "blurb_en": "The American cinema newsreel of 26 March 1945: a ‘spectacular coup’, prisoners, dry feet ‘by courtesy’, a collapse in a subordinate clause.",
         "plates": ["universal_gefangene"], "viz": "wochenschauen", "films": [{"film": "universal", "start": "2:40", "end": "3:56"}], "units": S1},
        {"id": "united", "titel": "United News: das Wort und das Bild", "titel_en": "United News: word and picture", "zk": "Wochenschauen · United", "zk_en": "Newsreels · United",
         "blurb": "Die Wochenschau der US-Regierung ehrt die toten Pioniere mit Worten, „no battle stars for death on the Remagen Bridge“, und lässt ihre Bilder weg.",
         "blurb_en": "The US government newsreel honours the dead engineers in words, ‘no battle stars for death on the Remagen Bridge’, and leaves out their pictures.",
         "plates": ["united_bruecke"], "films": [{"film": "united", "start": "4:38", "end": "7:58"}], "units": S2},
        {"id": "britisch", "titel": "Die britischen Wochenschauen", "titel_en": "The British newsreels", "zk": "Wochenschauen · Britisch", "zk_en": "Newsreels · British",
         "blurb": "Pathé zeigt das Schild in Großaufnahme, Movietone am 26. März die Bergung, Gaumont-British im Mai den Einsturz „ohne Vorwarnung“. Nach Katalog und eigener Stichprobe.",
         "blurb_en": "Pathé shows the sign in close-up, Movietone the rescue on 26 March, Gaumont-British in May the collapse ‘without warning’. After the catalogue and my own spot checks.",
         "films": ["pathe", "movietone"], "units": S3},
        {"id": "deutsch", "titel": "Die Deutsche Wochenschau schweigt", "titel_en": "The German newsreel is silent", "zk": "Wochenschauen · Deutsch", "zk_en": "Newsreels · German",
         "blurb": "Nr. 754 am 16. März: der Rhein als Strom des geordneten Rückzugs. Nr. 755 am 22. März, die letzte: Hitler und zwanzig Hitlerjungen, nichts aus dem Westen. In der Zeitung vom 20. März stand beides untereinander.",
         "blurb_en": "No. 754 on 16 March: the Rhine as the river of an orderly withdrawal. No. 755 on 22 March, the last: Hitler and twenty Hitler Youths, nothing from the west. In the newspaper of 20 March both stood one below the other.",
         "films": ["dw754", "dw755"], "units": S4},
    ],
}
(D / "wochenschauen.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")

P = json.loads((D / "plates.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "universal_gefangene", "side": "film", "titel": "Gefangene", "titel_en": "Prisoners",
     "caption": "Eine lange Kolonne deutscher Gefangener auf einer Straße, bewacht von amerikanischen Soldaten. Standbild aus der Universal-Wochenschau vom 26. März 1945.",
     "caption_en": "A long column of German prisoners on a road, guarded by American soldiers. Still from the Universal newsreel of 26 March 1945.",
     "source": "Universal Newsreel, „Allies Drive Across Rhine to Victory“, 26.3.1945, 3:35; Internet Archive, als gemeinfrei gekennzeichnet."},
    {"id": "united_bruecke", "side": "film", "titel": "Die Brücke von unten", "titel_en": "The bridge from below",
     "caption": "Ein Pfeiler und der Bogen der Ludendorff-Brücke, vom Ufer aus. Standbild aus der Wochenschau United News, März 1945.",
     "caption_en": "A pier and the arch of the Ludendorff Bridge, from the bank. Still from the United News newsreel, March 1945.",
     "source": "United News, „Bridgehead Extended“ (National Archives, ARC 39162), 4:40; Internet Archive gov.archives.arc.39162 (CC0)."},
]
ids = {p["id"] for p in NEW}
P["plates"] = [p for p in P["plates"] if p["id"] not in ids] + NEW
(D / "plates.json").write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")

M = json.loads((D / "modules.json").read_text(encoding="utf-8"))
m = next((x for x in M["planned"] if x["id"] == "wochenschauen"), None) or next(x for x in M["shipped"] if x["id"] == "wochenschauen")
M["planned"] = [x for x in M["planned"] if x["id"] != "wochenschauen"]
m.update({"datei": "wochenschauen", "zk": "Universal · United · Britisch · Deutsch", "zk_en": "Universal · United · British · German",
          "kurz": "8 · Zwei Wochenschauen", "kurz_en": "8 · Two newsreels",
          "warum": "Die amerikanischen und britischen Wochenschauen zeigten die Brücke, die Gefangenen, den Einsturz und die Rettung, und weniger, als gefilmt war. Die Deutsche Wochenschau zeigte den Rhein als Strom des Rückzugs und in ihrer letzten Ausgabe Hitler mit Hitlerjungen; Remagen nicht.",
          "warum_en": "The American and British newsreels showed the bridge, the prisoners, the collapse and the rescue, and less than had been filmed. The German newsreel showed the Rhine as the river of withdrawal and in its last issue Hitler with Hitler Youths; not Remagen.",
          "quelle": "Universal Newsreel 26.3.1945; United News 1945; IWM-Katalog zu britischen Wochenschauen; Deutsche Wochenschau Nr. 754 und 755 (nur Inhaltsangabe); Erzgebirgischer Volksfreund 20.3.1945.",
          "quelle_en": "Universal Newsreel 26 March 1945; United News 1945; IWM catalogue on British newsreels; Die Deutsche Wochenschau nos. 754 and 755 (summary only); Erzgebirgischer Volksfreund 20 March 1945."})
order = ["bruecke", "siebter", "warum", "brueckenkopf", "standgericht", "angriffe", "einsturz", "wochenschauen"]
M["shipped"] = sorted([x for x in M["shipped"] if x["id"] != "wochenschauen"] + [m], key=lambda x: order.index(x["id"]) if x["id"] in order else 99)
M["missing"] = [x for x in M["missing"] if x["id"] != "dw"] + [next(x for x in M["missing"] if x["id"] == "dw")] if any(x["id"] == "dw" for x in M["missing"]) else M["missing"]
(D / "modules.json").write_text(json.dumps(M, ensure_ascii=False, indent=1), encoding="utf-8")

C = json.loads((D / "compare.json").read_text(encoding="utf-8"))
PAIRS = [
    {"id": "spalte", "titel": "Eine Spalte, eine Wochenschau", "titel_en": "One column, one newsreel",
     "frage": "Was nahm die Wochenschau aus der Zeitung, was ließ sie weg?", "frage_en": "What did the newsreel take from the newspaper, and what did it leave out?",
     "note": "Am 20. März druckte der Erzgebirgische Volksfreund zwei Meldungen untereinander: Hitler empfängt zwanzig Hitlerjungen; die Brücke von Remagen ist eingestürzt. Die letzte Deutsche Wochenschau vom 22. März brachte die erste, fast wörtlich, und nicht die zweite.",
     "note_en": "On 20 March the Erzgebirgischer Volksfreund printed two reports one below the other: Hitler receives twenty Hitler Youths; the bridge at Remagen has collapsed. The last German newsreel of 22 March brought the first, almost word for word, and not the second.",
     "voices": [{"text": "wochenschauen", "sec": "deutsch", "n": [8], "wer": "Erzgebirgischer Volksfreund, 20. März 1945", "wer_en": "Erzgebirgischer Volksfreund, 20 March 1945"},
                {"text": "wochenschauen", "sec": "deutsch", "n": [7], "wer": "Deutsche Wochenschau Nr. 755 (Inhaltsangabe)", "wer_en": "Die Deutsche Wochenschau no. 755 (summary)"}]},
    {"id": "gefechtssterne", "titel": "Keine Gefechtssterne", "titel_en": "No battle stars",
     "frage": "Wie sprechen Wochenschau und Army-Geschichte von den toten Pionieren?", "frage_en": "How do the newsreel and the Army's history speak of the dead engineers?",
     "note": "United News macht aus den Toten ein Opfer „für hundert Kameraden“, MacDonald gibt eine Zahl, 28 Tote und 93 Verletzte. Die Wochenschau zeigt Rettung, nicht Tote; MacDonald zeigt nichts.",
     "note_en": "United News makes the dead a sacrifice ‘for a hundred comrades’, MacDonald gives a figure, 28 killed and 93 injured. The newsreel shows rescue, not the dead; MacDonald shows nothing.",
     "voices": [{"text": "wochenschauen", "sec": "united", "n": [3], "wer": "United News, 1945", "wer_en": "United News, 1945"},
                {"text": "einsturz", "sec": "nachmittag", "n": [2], "wer": "MacDonald 1973", "wer_en": "MacDonald 1973"}]},
]
pid = {p["id"] for p in PAIRS}
C["pairs"] = [p for p in C["pairs"] if p["id"] not in pid] + PAIRS
(D / "compare.json").write_text(json.dumps(C, ensure_ascii=False, indent=1), encoding="utf-8")

FF = json.loads((D / "films.json").read_text(encoding="utf-8"))
for f in FF["films"]:
    if f["id"] == "dw754":
        f["beschreibung"] = "Nach Sichtung: aus dem Westen eine Behauptung, auch am Rhein sei die amerikanische Umklammerung gescheitert, das Gros mit den schweren Waffen über den Strom gegangen, dazu Kämpfe an der Rur; sonst Streiks in England und den USA, Wlassow, Kurland, Flüchtlinge, Marienburg, Lauban und Görlitz mit Goebbels, Hitler im Osten. Remagen kommt nicht vor (Modul 8)."
        f["beschreibung_en"] = "After viewing: from the west a claim that on the Rhine too the American encirclement had failed and the bulk had crossed the river with its heavy weapons, together with fighting on the Roer; otherwise strikes in Britain and the US, Vlasov, Courland, refugees, Marienburg, Lauban and Görlitz with Goebbels, Hitler in the east. Remagen does not appear (module 8)."
    if f["id"] == "dw755":
        f["beschreibung"] = "Nach Sichtung: Feuerwerker, Panzerfaust, Hitler mit Axmann und zwanzig Hitlerjungen, ein Volkssturmführer, Breslau, Königsberg, Kriegsmarine, Stettin; nichts aus dem Westen. Remagen kommt nicht vor (Modul 8)."
        f["beschreibung_en"] = "After viewing: bomb disposal officer, Panzerfaust, Hitler with Axmann and twenty Hitler Youths, a Volkssturm commander, Breslau, Königsberg, the navy, Stettin; nothing from the west. Remagen does not appear (module 8)."
(D / "films.json").write_text(json.dumps(FF, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", sum(len(s["units"]) for s in T["sections"]), "units")
