"""Baut data/bruecke.json (Modul 1: Die Brücke, 1916–1945).
Quellen: Zeitungen 1918–1935 im Deutschen Zeitungsportal (Meldungen ohne Verfasser, mehr als 70 Jahre
nach Erscheinen gemeinfrei; die Telegramme Wilhelms II. und Ludendorffs ebenfalls gemeinfrei), wo möglich
am Seitenbild gelesen; Zeitungen aus Nordrhein-Westfalen nur nach dem Volltext des Portals, weil das
Portal zeitpunkt.nrw Zugriffe von hier sperrt. MacDonald, The Last Offensive (1973), S. 213 und 230.
Übersetzungen: eigene Arbeit (CC0).
Aufruf aus dem Wurzelverzeichnis: python tools/build-bruecke.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
DZP = "https://www.deutsche-digitale-bibliothek.de/newspaper/item/"
NRW = ("Nach dem Volltext des Deutschen Zeitungsportals; das Seitenbild liegt bei zeitpunkt.nrw und war von hier nicht zugänglich. "
       "Offensichtliche Lesefehler der Texterkennung sind stillschweigend berichtigt, Fraktur in Antiqua. ")
NRW_EN = ("After the full text of the Deutsches Zeitungsportal; the page image is held by zeitpunkt.nrw and could not be accessed from here. "
          "Obvious text-recognition errors have been corrected silently. ")


def u(n, pg, lang, orig, tr, titel=None, titel_en=None, note=None, note_en=None):
    x = {"n": n, "pg": pg, "lang": lang}
    if titel: x["titel"], x["titel_en"] = titel, titel_en
    x["orig"] = orig
    x["en" if lang == "de" else "de"] = tr
    if note: x["note"], x["note_en"] = note, note_en
    return x


S1 = [
    u(1, "MacDonald, S. 213", "en",
      "Built in 1916, the railroad bridge at Remagen was named for the World War I hero, Erich Ludendorff. Wide enough for two train tracks, plus footpaths on either side, the bridge had three symmetrical arches resting on four stone piers. The over-all length was 1,069 feet. At each end stood two stone towers, black with grime, giving the bridge a fortresslike appearance. Only a few yards from the east end of the bridge, the railroad tracks entered a tunnel through the black rock of a clifflike hill, the Erpeler Ley.",
      "Die Eisenbahnbrücke bei Remagen, 1916 gebaut, war nach dem Helden des Ersten Weltkriegs, Erich Ludendorff, benannt. Breit genug für zwei Gleise und dazu Fußwege an beiden Seiten, ruhte sie mit drei gleichen Bögen auf vier Steinpfeilern. Die Gesamtlänge betrug 1 069 Fuß. An jedem Ende standen zwei Steintürme, schwarz vor Ruß, die der Brücke das Aussehen einer Festung gaben. Nur wenige Meter hinter dem Ostende führten die Gleise in einen Tunnel durch den schwarzen Fels eines steilen Berges, der Erpeler Ley.",
      "Die Brücke, wie sie 1945 aussah", "The bridge as it looked in 1945",
      "1 069 Fuß sind rund 326 Meter. „Built in 1916“: Nach den Zeitungen von 1918 (Einheiten 2–4) war die Brücke 1918 fertig, aber noch nicht in Betrieb. Nach neuerer Literatur begann der Bau 1916, der regelmäßige Bahnbetrieb 1919; die Erbauer nennt keine der hier abgedruckten Quellen.",
      "‘Built in 1916’: according to the newspapers of 1918 (units 2–4) the bridge was complete in 1918 but not yet in service. According to recent literature construction began in 1916 and regular rail service in 1919; none of the sources printed here names the builders."),
    u(2, "Tägliche Rundschau, 2.5.1918, S. 6", "de",
      "Die neuen Rheinbrücken. […]\n\nDas Telegramm des Kaisers an den Ersten Generalquartiermeister, General der Infanterie Ludendorff, lautete:\nEs ist Mir eine große Freude, Ihnen mitzuteilen, daß Ich der Rheineisenbahnbrücke bei Remagen, welche als Zuführung zur Ahrtalbahn demnächst dem Betrieb übergeben werden soll, heute den Namen Ludendorff-Brücke beigelegt habe. Die Rheinfahrer aller Zeiten sollen sich erinnern, was wir den Beschützern des Rheinstromes verdanken. gez. Wilhelm I. R.\n\n[…]\n\nSeiner Majestät dem Kaiser und König!\nEurer Majestät wage ich meinen alleruntertänigsten Dank für die neue große Ehrung in tiefster Ehrerbietung zu Füßen zu legen. Daß mein Name mit dem Rheinstrom auf Eurer Majestät Befehl für alle Zeiten verbunden sein soll, erhöht meine tiefe Dankbarkeit gegenüber Eurer Majestät, erfüllt mich zugleich mit Stolz und Freude. Ludendorff, General der Infanterie.",
      "The new Rhine bridges. […]\n\nThe Kaiser's telegram to the First Quartermaster General, General of Infantry Ludendorff, read:\nIt is a great pleasure to Me to inform you that I have today given the name Ludendorff Bridge to the Rhine railway bridge at Remagen, which as a feeder to the Ahr valley railway is soon to be put into service. Rhine travellers of all times shall remember what we owe to the protectors of the Rhine. Signed Wilhelm I. R.\n\n[…]\n\nTo His Majesty the Emperor and King!\nI venture to lay my most humble thanks for this new great honour at Your Majesty's feet in deepest reverence. That my name shall by Your Majesty's command be joined with the Rhine for all time heightens my deep gratitude towards Your Majesty and fills me at the same time with pride and joy. Ludendorff, General of Infantry.",
      "Der Name, Mai 1918", "The name, May 1918",
      "Im selben Bericht erhalten die Brücke bei Engers den Namen des Kronprinzen und die bei Rüdesheim den Hindenburgs; der Kronprinz wünscht „seinem“ Bauwerk, es möge „die Unantastbarkeit der Westgrenzen“ sichern. Die drei Brücken wurden im Krieg gebaut, für den Krieg. Fraktursatz, am Seitenbild der Staatsbibliothek zu Berlin gelesen (Public Domain Mark). Zeitungsseite: " + DZP + "CSHP2WRILAJB7VFN3IXKX26FRAL243ES",
      "In the same report the bridge at Engers receives the Crown Prince's name and the one at Rüdesheim Hindenburg's; the Crown Prince wishes ‘his’ structure to secure ‘the inviolability of the western frontiers’. All three bridges were built in the war, for the war. Set in Fraktur, read against the page image of the Staatsbibliothek zu Berlin (Public Domain Mark). Newspaper page: " + DZP + "CSHP2WRILAJB7VFN3IXKX26FRAL243ES"),
    u(3, "Gießener Zeitung, 31.8.1918, S. 3", "de",
      "Koblenz. In Anwesenheit des Ministers von Breitenbach, des Oberpräsidenten, des stellvertr. Kommandierenden Generals des 8. Armeekorps und anderer Vertreter der militärischen und bürgerlichen Behörden fand die Einweihung der Kronprinz-Wilhelm-Brücke bei Engers statt, zugleich mit der für die Hindenburgbrücke bei Rüdesheim und die Ludendorffbrücke bei Remagen.",
      "Koblenz. In the presence of Minister von Breitenbach, the Oberpräsident, the deputy commanding general of the 8th Army Corps and other representatives of the military and civil authorities, the Crown Prince Wilhelm Bridge at Engers was dedicated, together with that of the Hindenburg Bridge at Rüdesheim and the Ludendorff Bridge at Remagen.",
      "Die Einweihung, August 1918", "The dedication, August 1918",
      "Die Einweihung fand für alle drei Brücken an einem Ort statt, in Engers; Zeitungen in Nordrhein-Westfalen meldeten sie ab dem 15. August 1918. Breitenbach war preußischer Minister der öffentlichen Arbeiten. Fraktursatz, am Seitenbild der Universitätsbibliothek Gießen gelesen. Zeitungsseite: " + DZP + "QODW6A5OPPAYEK2FIGW3QK7FTF2DJPQ3",
      "The dedication of all three bridges took place in one place, at Engers; newspapers in North Rhine-Westphalia reported it from 15 August 1918. Breitenbach was the Prussian Minister of Public Works. Set in Fraktur, read against the page image of the Gießen University Library. Newspaper page: " + DZP + "QODW6A5OPPAYEK2FIGW3QK7FTF2DJPQ3"),
]

S2 = [
    u(4, "Deutsche Reichs-Zeitung (Bonn), 13.11.1918", "de",
      "Remagen: Die hiesige neugebaute Ludendorffbrücke ist vom 10. Nov. ab für den Fußgangverkehr frei gegeben worden.",
      "Remagen: The newly built Ludendorff Bridge here has been opened to foot traffic from 10 November.",
      "10. November 1918: für Fußgänger frei", "10 November 1918: open to pedestrians",
      NRW + "Gleichlautend in der Rheinischen Volksstimme vom selben Tag. Die nächste Meldung der Spalte, unter „Revolution“, berichtet von einem Arbeiter- und Soldatenrat in Bonn. Am Tag darauf, dem 11. November, endete der Krieg. Zeitungsseite: " + DZP + "VE57U6NKK56Y6WMQBNRDAKQUQLY2245T",
      NRW_EN + "Identical in the Rheinische Volksstimme of the same day. The next item in the column, headed ‘Revolution’, reports a workers' and soldiers' council in Bonn. The next day, 11 November, the war ended. Newspaper page: " + DZP + "VE57U6NKK56Y6WMQBNRDAKQUQLY2245T"),
    u(5, "Wittener Volks-Zeitung, 26.11.1918", "de",
      "Bonn, 23. Nov. In der heutigen Sitzung des Arbeiter-, Bürger- und Soldatenrates teilte der Vertreter der hier durchmarschierenden Achtzehnten Armee mit, daß die 7. Armee, die ursprünglich zum größten Teil auch über Bonn geleitet werden sollte, nun die neue Brücke bei Remagen benutzen werde. Nur die schweren Kraftwagenzüge, die die neuen Brückenrampen nicht tragen können, sollen in Bonn über den Rhein gehen. Es sollen für den Uebergang der 18. Armee noch Notbrücken bei Mondorf und Niederdollendorf geschlagen werden.",
      "Bonn, 23 Nov. At today's meeting of the Workers', Citizens' and Soldiers' Council the representative of the Eighteenth Army, which is marching through here, announced that the 7th Army, most of which was originally also to be routed through Bonn, would now use the new bridge at Remagen. Only the heavy motor convoys, which the new bridge ramps cannot carry, are to cross the Rhine at Bonn. For the crossing of the 18th Army, emergency bridges are also to be built at Mondorf and Niederdollendorf.",
      "November 1918: das Heer kehrt zurück", "November 1918: the army comes back",
      NRW + "„gehen. Es“ ergänzt nach dem Abdruck derselben Meldung im Echo der Gegenwart vom selben Tag, dessen Volltext hier lückenhaft ist. Die Brücke, gebaut, um Truppen nach Westen zu bringen, diente zuerst ihrem Rückmarsch nach dem Waffenstillstand. Zeitungsseite: " + DZP + "ULJEBRXNAMG2MQB2RZNFFF6J3DITCTX7",
      NRW_EN + "‘gehen. Es’ supplied from the printing of the same report in the Echo der Gegenwart of the same day. The bridge, built to bring troops westward, first served their return march after the armistice. Newspaper page: " + DZP + "ULJEBRXNAMG2MQB2RZNFFF6J3DITCTX7"),
    u(6, "General-Anzeiger (Bonn), 9.12.1925, S. 10", "de",
      "Remagen, 8. Dez. Gestern vormittag ist die Wachmannschaft, die seit der Besetzung auf der Ludendorff-Brücke zwischen Remagen—Erpel stationiert war, abgezogen. Die Brücke ist somit wieder frei.",
      "Remagen, 8 Dec. Yesterday morning the guard detachment that had been stationed on the Ludendorff Bridge between Remagen and Erpel since the occupation was withdrawn. The bridge is thus free again.",
      "Dezember 1925: die Wache zieht ab", "December 1925: the guard leaves",
      NRW + "Wessen Wache es war, sagt die Meldung nicht. Das Rheinland war nach dem Waffenstillstand von den Alliierten besetzt; Remagen lag 1919 im amerikanisch besetzten Gebiet des Brückenkopfes Koblenz (Zeitungsmeldungen vom September 1919). Zeitungsseite: " + DZP + "Q4NVPVKOI2VZZLKXBKW5PSIU67LFC3QI",
      NRW_EN + "Whose guard it was, the report does not say. After the armistice the Rhineland was occupied by the Allies; in 1919 Remagen lay in the American-occupied area of the Koblenz bridgehead (newspaper reports of September 1919). Newspaper page: " + DZP + "Q4NVPVKOI2VZZLKXBKW5PSIU67LFC3QI"),
]

S3 = [
    u(7, "Münchner Neueste Nachrichten, 22.3.1928, S. 8", "de",
      "In der Nacht zum Mittwoch brach auf der Ludendorff-Brücke zwischen Remagen und Erpel ein Feuer aus, das wahrscheinlich durch Schlacken einer Güterzuglokomotive, die den Holzbelag der Brücke in Brand setzten, verursacht war. Die Feuerwehren der umliegenden Ortschaften hatten Mühe, das Feuer auf seinen Herd zu beschränken. Aus Köln und Koblenz waren von der Reichsbahn Hilfszüge angefordert worden. Der Brand konnte gelöscht werden.",
      "On the night before Wednesday a fire broke out on the Ludendorff Bridge between Remagen and Erpel, probably caused by cinders from a goods-train locomotive which set the bridge's wooden decking alight. The fire brigades of the surrounding villages had difficulty confining the fire to where it started. Relief trains had been called for by the Reichsbahn from Cologne and Koblenz. The fire was put out.",
      "März 1928: die Brücke brennt", "March 1928: the bridge burns",
      "Der Bonner General-Anzeiger vom selben Tag (nach dem Volltext) nennt Einzelheiten: Das Feuer begann gegen 23 Uhr am Remagener Pfeiler, das Holz war mit Karbolineum getränkt, es herrschte Sturm, die dreifach gelegten Bohlen ließen sich nicht aufreißen, gegen 3 Uhr war der Brand gelöscht. Fraktursatz, am Seitenbild der Bayerischen Staatsbibliothek gelesen. Zeitungsseite: " + DZP + "75OIZY7ZDRLKDI32IHQVLMMBDP2PWP26",
      "The Bonn General-Anzeiger of the same day (from its full text) gives details: the fire began around 11 p.m. at the Remagen pier, the wood was soaked in carbolineum, a gale was blowing, the triple layer of planks could not be torn up, by 3 a.m. the fire was out. Set in Fraktur, read against the page image of the Bavarian State Library. Newspaper page: " + DZP + "75OIZY7ZDRLKDI32IHQVLMMBDP2PWP26"),
    u(8, "Deutsche Reichs-Zeitung (Bonn), 20.11.1928", "de",
      "Erpel: Die Instandsetzungsarbeiten auf der Rheinbrücke Erpel—Remagen, die infolge des Brandes notwendig geworden waren, sind nunmehr beendet. Die Arbeiten gestalteten sich sehr schwierig. Anstatt des bisherigen Bohlenbelages ist die Brücke nunmehr mit dicken Eisenplatten belegt worden, damit weitere Brände infolge Ausschlackens der Maschinen vermieden werden.",
      "Erpel: The repairs to the Rhine bridge Erpel–Remagen made necessary by the fire have now been completed. The work proved very difficult. Instead of the former planking the bridge has now been covered with thick iron plates, so that further fires caused by locomotives discharging cinders may be avoided.",
      "November 1928: Eisen statt Holz", "November 1928: iron instead of wood",
      NRW + "Im Oktober 1928 meldete dasselbe Blatt weitere kleine Brände im trockenen Sommer und einen Wachtposten der Reichsbahn bei Tag und Nacht. Der Fußweg behielt seinen Holzbelag. Zeitungsseite: " + DZP + "YPEBPKVJEMUNSO5ISDEMLQ566Z5E236F",
      NRW_EN + "In October 1928 the same paper reported further small fires in the dry summer and a Reichsbahn watchman posted day and night. The footpath kept its wooden decking. Newspaper page: " + DZP + "YPEBPKVJEMUNSO5ISDEMLQ566Z5E236F"),
    u(9, "General-Anzeiger (Bonn), 18.4.1935", "de",
      "Stärkerer Eisenbahnverkehr über die Erpeler Rheinbrücke?\n(Erpel): Die Ludendorffbrücke bei Erpel wurde bekanntlich bisher nur von wenigen durchgehenden Güterzügen und in der Sommersaison von einem Personenzug, der von Unkel aus zur Ahr fuhr, benutzt. Der Eisenbahnverkehr über die vor dem Weltkrieg erbaute Rheinbrücke soll in Zukunft erheblich verstärkt werden. Die Reichsbahn hat die Absicht, neue Zugverbindungen von der Kölner Strecke aus zur Ahr und auch nach Koblenz zu schaffen.",
      "Heavier rail traffic over the Erpel Rhine bridge?\n(Erpel): As is well known, the Ludendorff Bridge at Erpel has so far been used only by a few through goods trains and, in the summer season, by one passenger train running from Unkel to the Ahr. Rail traffic over the Rhine bridge built before the World War is to be increased considerably in future. The Reichsbahn intends to create new train connections from the Cologne line to the Ahr and also to Koblenz.",
      "1935: eine Brücke mit wenig Verkehr", "1935: a bridge with little traffic",
      NRW + "„vor dem Weltkrieg erbaut“ so im Text; tatsächlich im Krieg gebaut (Einheiten 1–3). Dass die Brücke nach dem Ersten Weltkrieg wenig befahren war, passt zu ihrem Zweck: Sie war für den Aufmarsch gebaut, nicht für den Alltag. Zeitungsseite: " + DZP + "ZNPVIUQPQ5F6GH6CLOU746OPEPII737L",
      NRW_EN + "‘Built before the World War’ thus in the text; in fact it was built during the war (units 1–3). That the bridge carried little traffic after the First World War fits its purpose: it was built for deploying troops, not for everyday use. Newspaper page: " + DZP + "ZNPVIUQPQ5F6GH6CLOU746OPEPII737L"),
]

S4 = [
    u(10, "MacDonald, S. 230", "en",
      "As far back as 1940 Allied planes had launched sporadic attacks against the bridge, and in late 1944 had damaged it to such an extent that it was unserviceable for fifteen days. Then came the heavy planking to convert the bridge for vehicles […].",
      "Schon seit 1940 hatten alliierte Flugzeuge die Brücke gelegentlich angegriffen und sie Ende 1944 so schwer beschädigt, dass sie fünfzehn Tage lang unbenutzbar war. Dann kamen die schweren Bohlen, die die Brücke für Fahrzeuge befahrbar machten […].",
      "Wieder eine Brücke für den Krieg", "A bridge for war again",
      "Aus MacDonalds Aufzählung der Ursachen des Einsturzes (Modul 7). Den Sprengplan von 1938 und den Befehl des OKW schildert Modul 3; die Bohlen, mit denen die Brücke Anfang März 1945 für den Rückzug befahrbar gemacht wurde, Modul 3, Einheit 8. Die beiden Luftbilder dieses Abschnitts zeigen die Brücke im Oktober 1944 und im Februar 1945, aufgenommen von alliierten Aufklärern.",
      "From MacDonald's list of the causes of the collapse (module 7). The demolition scheme of 1938 and the OKW order are described in module 3; the planks that made the bridge passable for the retreat in early March 1945 in module 3, unit 8. The two aerial photographs in this section show the bridge in October 1944 and February 1945, taken by Allied reconnaissance."),
]

T = {
    "id": "bruecke",
    "titel": "Die Brücke, 1916–1945", "titel_en": "The bridge, 1916–1945",
    "autor": "Zeitungen 1918–1935; Wilhelm II. und Ludendorff (1918); MacDonald (1973)",
    "autor_en": "Newspapers 1918–1935; Wilhelm II and Ludendorff (1918); MacDonald (1973)",
    "jahr": "1916–1945", "jahr_en": "1916–1945",
    "sprache": "de", "orig_sprache": "de", "pg_label": "", "pg_label_en": "",
    "quelle": "Meldungen aus der Tägliche Rundschau (Berlin, 2.5.1918), der Gießener Zeitung (31.8.1918), der Deutschen Reichs-Zeitung (Bonn, 13.11.1918 und 20.11.1928), der Wittener Volks-Zeitung (26.11.1918), dem General-Anzeiger (Bonn, 9.12.1925 und 18.4.1935) und den Münchner Neuesten Nachrichten (22.3.1928), über das Deutsche Zeitungsportal; Meldungen ohne Verfasser und die Telegramme Wilhelms II. und Ludendorffs, gemeinfrei. Die Berliner, Gießener und Münchner Blätter am Seitenbild gelesen, die aus Nordrhein-Westfalen nach dem Volltext des Portals. Charles B. MacDonald, The Last Offensive (1973), S. 213 und 230, am Seitenbild gelesen.",
    "quelle_en": "Reports from the Tägliche Rundschau (Berlin, 2 May 1918), the Gießener Zeitung (31 Aug 1918), the Deutsche Reichs-Zeitung (Bonn, 13 Nov 1918 and 20 Nov 1928), the Wittener Volks-Zeitung (26 Nov 1918), the General-Anzeiger (Bonn, 9 Dec 1925 and 18 Apr 1935) and the Münchner Neueste Nachrichten (22 Mar 1928), via the Deutsches Zeitungsportal; unsigned reports and the telegrams of Wilhelm II and Ludendorff, in the public domain. The Berlin, Gießen and Munich papers read against the page image, those from North Rhine-Westphalia after the portal's full text. Charles B. MacDonald, The Last Offensive (1973), pp. 213 and 230, read against the page images.",
    "hinweis": "Die Brücke vor dem März 1945: im Krieg für den Krieg gebaut und nach Ludendorff benannt, zuerst vom zurückkehrenden Heer benutzt, unter Besatzung bewacht, in den Jahren danach eine wenig befahrene Nebenbahn, die einmal brannte, und ab 1940 wieder ein Ziel. Ein gemeinfreier Baubericht der Jahre 1916–1919 ließ sich nicht finden; wer die Brücke entwarf und baute, sagen die hier abgedruckten Quellen nicht. Texte nach dem Druck, Fraktur in Antiqua, Auslassungen […]; Übersetzungen eigene Arbeit (CC0).",
    "hinweis_en": "The bridge before March 1945: built in the war for the war and named after Ludendorff, first used by the returning army, guarded under occupation, in the following years a little-used branch line that once caught fire, and from 1940 a target again. No public-domain construction report of 1916–1919 could be found; who designed and built the bridge, the sources printed here do not say. Texts after the print, Fraktur set in roman type, omissions […]; translations my own (CC0).",
    "sections": [
        {"id": "bau", "titel": "Eine Brücke für den Krieg", "titel_en": "A bridge for the war", "zk": "Brücke · Bau", "zk_en": "Bridge · Building",
         "blurb": "Drei Rheinbrücken entstehen im Ersten Weltkrieg, bei Engers, Rüdesheim und Remagen. Im Mai 1918 gibt der Kaiser ihnen die Namen des Kronprinzen, Hindenburgs und Ludendorffs; im August werden sie eingeweiht.",
         "blurb_en": "Three Rhine bridges are built in the First World War, at Engers, Rüdesheim and Remagen. In May 1918 the Kaiser gives them the names of the Crown Prince, Hindenburg and Ludendorff; in August they are dedicated.",
         "plates": ["tr1918_telegramm"], "viz": "bruecke", "units": S1},
        {"id": "kriegsende", "titel": "Kriegsende und Besatzung", "titel_en": "End of the war and occupation", "zk": "Brücke · Kriegsende", "zk_en": "Bridge · War's end",
         "blurb": "Einen Tag vor dem Waffenstillstand wird die Brücke für Fußgänger freigegeben, zwei Wochen später marschiert die 7. Armee über sie heim. Danach steht eine Wache auf ihr, bis Dezember 1925.",
         "blurb_en": "A day before the armistice the bridge is opened to pedestrians, two weeks later the 7th Army marches home across it. Afterwards a guard stands on it, until December 1925.",
         "units": S2},
        {"id": "alltag", "titel": "Eine Nebenbahn über den Rhein", "titel_en": "A branch line across the Rhine", "zk": "Brücke · Alltag", "zk_en": "Bridge · Everyday",
         "blurb": "Wenige Güterzüge, ein Ausflugszug im Sommer, ein Fußweg zwischen Remagen und Erpel. 1928 brennt der Holzbelag; danach liegen Eisenplatten auf den Gleisen.",
         "blurb_en": "A few goods trains, an excursion train in summer, a footpath between Remagen and Erpel. In 1928 the wooden decking burns; afterwards iron plates cover the tracks.",
         "plates": ["mtb1938_linz"], "units": S3},
        {"id": "krieg", "titel": "Wieder für den Krieg", "titel_en": "For war again", "zk": "Brücke · Krieg", "zk_en": "Bridge · War",
         "blurb": "Ab 1940 greifen alliierte Flugzeuge die Brücke an, Ende 1944 ist sie fünfzehn Tage gesperrt. Die Aufklärer photographieren sie aus der Luft.",
         "blurb_en": "From 1940 Allied aircraft attack the bridge, at the end of 1944 it is closed for fifteen days. Reconnaissance aircraft photograph it from the air.",
         "plates": ["nara1944_erpel", "nara1945_erpel"], "units": S4},
    ],
}
(D / "bruecke.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")

P = json.loads((D / "plates.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "tr1918_telegramm", "side": "bruecke", "titel": "„… heute den Namen Ludendorff-Brücke beigelegt“", "titel_en": "‘… today given the name Ludendorff Bridge’",
     "caption": "Das Telegramm Wilhelms II. an Ludendorff in der Berliner Täglichen Rundschau vom 2. Mai 1918.",
     "caption_en": "Wilhelm II's telegram to Ludendorff in the Berlin Tägliche Rundschau of 2 May 1918.",
     "source": "Tägliche Rundschau, 2.5.1918, S. 6 (Ausschnitt); Staatsbibliothek zu Berlin, ZEFYS SNP30744556-19180502, Public Domain Mark."},
    {"id": "mtb1938_linz", "side": "bruecke", "titel": "Die Brücke auf dem Messtischblatt, um 1938", "titel_en": "The bridge on the ordnance map, c. 1938",
     "caption": "Remagen, Erpel und die Bahnlinien zur Brücke; in der Mitte die Strecke über den Rhein und in den Tunnel der Erpeler Ley. Ausschnitt aus dem Messtischblatt Linz.",
     "caption_en": "Remagen, Erpel and the railway lines to the bridge; in the middle the line across the Rhine and into the tunnel of the Erpeler Ley. Detail of the Linz ordnance map sheet.",
     "source": "Landesarchiv Nordrhein-Westfalen, RW Karten Nr. 8601 (Messtischblatt 5409 Linz, um 1938), über Wikimedia Commons; CC BY-SA 4.0 (Landesarchiv NRW)."},
    {"id": "nara1944_erpel", "side": "us", "titel": "Erpel, Remagen und die Brücke, 28. Oktober 1944", "titel_en": "Erpel, Remagen and the bridge, 28 October 1944",
     "caption": "Alliiertes Luftbild: links Erpel unter der Ley, rechts Remagen, dazwischen die Brücke. Ausschnitt.",
     "caption_en": "Allied aerial photograph: Erpel below the Ley on the left, Remagen on the right, the bridge between them. Detail.",
     "source": "U.S. Department of Defense, Defense Intelligence Agency (National Archives, NAID 531347349), über Wikimedia Commons; gemeinfrei."},
    {"id": "nara1945_erpel", "side": "us", "titel": "Die Brücke bei Erpel, 15. Februar 1945", "titel_en": "The bridge at Erpel, 15 February 1945",
     "caption": "Alliiertes Luftbild drei Wochen vor dem 7. März; unten die Brücke, darüber Erpel und die Bahnlinie am Ufer. Ausschnitt.",
     "caption_en": "Allied aerial photograph three weeks before 7 March; below, the bridge, above it Erpel and the riverside railway. Detail.",
     "source": "U.S. Department of Defense, Defense Intelligence Agency (National Archives, NAID 291982353), über Wikimedia Commons; gemeinfrei."},
]
ids = {p["id"] for p in NEW}
P["plates"] = [p for p in P["plates"] if p["id"] not in ids] + NEW
P["credit"] = "Photographien und Karten aus MacDonald, The Last Offensive (1973), nach den Seitenbildern des Internet Archive; Standbilder aus Rollen des Signal Corps und der Wochenschau United News (National Archives) im Internet Archive; Luftbilder der US-Regierung und ein Farbdia des Corps of Engineers über Wikimedia Commons: Werke der US-Regierung, gemeinfrei (17 U.S.C. § 105). Ein Zeitungsausschnitt von 1918 nach der Staatsbibliothek zu Berlin (Public Domain Mark); das Messtischblatt um 1938 nach dem Landesarchiv NRW (CC BY-SA 4.0)."
P["credit_en"] = "Photographs and maps from MacDonald, The Last Offensive (1973), after the page images of the Internet Archive; stills from Signal Corps reels and the United News newsreel (National Archives) in the Internet Archive; US government aerial photographs and a Corps of Engineers colour slide via Wikimedia Commons: works of the US government, in the public domain (17 U.S.C. § 105). A newspaper clipping of 1918 after the Staatsbibliothek zu Berlin (Public Domain Mark); the ordnance map of c. 1938 after the Landesarchiv NRW (CC BY-SA 4.0)."
P["lede"] = "Photographien, Karten, Luftbilder, Filmstandbilder und ein Zeitungsausschnitt. Jede Tafel nennt ihre Vorlage und ihre Rechte."
P["lede_en"] = "Photographs, maps, aerial photographs, film stills and a newspaper clipping. Each plate names its original and its rights."
(D / "plates.json").write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")

M = json.loads((D / "modules.json").read_text(encoding="utf-8"))
m = next((x for x in M["planned"] if x["id"] == "bruecke"), None) or next(x for x in M["shipped"] if x["id"] == "bruecke")
M["planned"] = [x for x in M["planned"] if x["id"] != "bruecke"]
m.update({"datei": "bruecke", "zk": "Bau · Kriegsende · Alltag · Krieg", "zk_en": "Building · War's end · Everyday · War",
          "kurz": "1 · Die Brücke, 1916–1945", "kurz_en": "1 · The bridge, 1916–1945",
          "warum": "Im Krieg für den Krieg gebaut und im Mai 1918 nach Ludendorff benannt, nach dem Waffenstillstand vom heimkehrenden Heer benutzt, unter Besatzung bewacht, in den Jahren danach eine wenig befahrene Nebenbahn, die 1928 brannte, und ab 1940 wieder ein Ziel.",
          "warum_en": "Built in the war for the war and named after Ludendorff in May 1918, used by the returning army after the armistice, guarded under occupation, in the following years a little-used branch line that burned in 1928, and from 1940 a target again.",
          "quelle": "Zeitungen 1918–1935 (Deutsches Zeitungsportal), Telegramme Wilhelms II. und Ludendorffs (1918); MacDonald (1973), S. 213, 230.",
          "quelle_en": "Newspapers 1918–1935 (Deutsches Zeitungsportal), telegrams of Wilhelm II and Ludendorff (1918); MacDonald (1973), pp. 213, 230."})
order = ["bruecke", "siebter", "warum", "brueckenkopf", "standgericht"]
M["shipped"] = sorted([x for x in M["shipped"] if x["id"] != "bruecke"] + [m], key=lambda x: order.index(x["id"]) if x["id"] in order else 99)
(D / "modules.json").write_text(json.dumps(M, ensure_ascii=False, indent=1), encoding="utf-8")

TL = json.loads((D / "timeline.json").read_text(encoding="utf-8"))
ss = TL["stations"]
s0 = next(s for s in ss if s["d"] == "1916")
s0.update({"d": "1916–1918", "d_en": "1916–1918", "titel": "Eine Brücke für den Krieg", "titel_en": "A bridge for the war",
           "text": "Im Ersten Weltkrieg gebaut, als Zuführung zur Ahrtalbahn. Am 1. oder 2. Mai 1918 gibt Wilhelm II. ihr den Namen Ludendorff-Brücke, „die Rheinfahrer aller Zeiten sollen sich erinnern“; im August 1918 wird sie mit den Brücken bei Engers und Rüdesheim eingeweiht.",
           "text_en": "Built in the First World War as a feeder to the Ahr valley railway. On 1 or 2 May 1918 Wilhelm II gives it the name Ludendorff Bridge, ‘Rhine travellers of all times shall remember’; in August 1918 it is dedicated together with the bridges at Engers and Rüdesheim.",
           "cite": "#/text/bruecke/bau/2", "citeLabel": "Die Brücke [2]", "citeLabel_en": "The bridge [2]", "plate": "tr1918_telegramm"})
for t in ("Heimkehr und Besatzung", "Der Brand"):
    ss[:] = [s for s in ss if s["titel"] != t]
i = ss.index(s0) + 1
ss.insert(i, {"d": "1918–1925", "d_en": "1918–1925", "side": "bruecke", "titel": "Heimkehr und Besatzung", "titel_en": "Homecoming and occupation",
              "text": "Am 10. November 1918 für Fußgänger freigegeben; Ende November marschiert die 7. Armee über die Brücke zurück. Danach steht eine Wache auf ihr, bis zum 7. Dezember 1925.",
              "text_en": "Opened to pedestrians on 10 November 1918; at the end of November the 7th Army marches back across the bridge. Afterwards a guard stands on it, until 7 December 1925.",
              "cite": "#/text/bruecke/kriegsende/5", "citeLabel": "Die Brücke [5]", "citeLabel_en": "The bridge [5]"})
ss.insert(i + 1, {"d": "1928", "d_en": "1928", "side": "bruecke", "titel": "Der Brand", "titel_en": "The fire",
                  "text": "In der Nacht zum 21. März brennt der Holzbelag, entzündet von Lokomotivschlacken; bis November erhält die Brücke Eisenplatten.",
                  "text_en": "On the night of 20–21 March the wooden decking burns, set alight by locomotive cinders; by November the bridge has iron plates.",
                  "cite": "#/text/bruecke/alltag/7", "citeLabel": "Die Brücke [7]", "citeLabel_en": "The bridge [7]"})
(D / "timeline.json").write_text(json.dumps(TL, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", sum(len(s["units"]) for s in T["sections"]), "units")
