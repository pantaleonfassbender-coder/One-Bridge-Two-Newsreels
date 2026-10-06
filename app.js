/* Eine Brücke, zwei Wochenschauen. Remagen 1945 — One Bridge, Two Newsreels. Ein zweisprachiger
   Quellenapparat mit kommentierten Filmen. Vanilla JS, Hash-Routen. Filme werden nur eingebettet
   (Internet Archive, offizieller YouTube-Player) und erst auf Klick geladen. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, films: null, texts: {} };

/* ------------------------------------------------------------ language */
let ui = "de";
try { ui = localStorage.getItem("bridge_ui") || ""; } catch (e) { /* storage blocked */ }
if (ui !== "de" && ui !== "en") ui = /^de\b/i.test(navigator.language || "") ? "de" : "en";
let langPref = null;
try { langPref = localStorage.getItem("bridge_lang"); } catch (e) { /* storage blocked */ }

const T = {
  de: {
    title: "Eine Brücke, zwei Wochenschauen", nav: { "": "Übersicht", texts: "Texte", films: "Filme", compare: "Vergleich", timeline: "Zeitleiste", plates: "Tafeln", sources: "Quellen" },
    switchTo: "English", loading: "Wird geladen…", allTexts: "← Alle Texte", allCmp: "← Alle Vergleiche", citeAs: "zitiert als", cite: "Zitieren als",
    orig: "Original", both: "Original + Übersetzung", trans: "Übersetzung", or: " oder ",
    srcNote: "Quelle und Editionsnotiz", source: "Quelle", planned: "geplant", notTaken: "nicht aufgenommen",
    shipped: "Abgedruckt", plannedH: "Geplant", missingH: "Geprüft und nicht aufgenommen",
    textsTag: "Texte", textsH: "Das Korpus", textsLede: "Jedes Modul ist vollständig lesbar, im Original neben einer Übersetzung: englische Quellen mit deutscher, deutsche mit englischer Übersetzung. Was geprüft und nicht aufgenommen wurde, steht unten mit Begründung.",
    cmpTag: "Vergleich", cmpH: "Stimmen nebeneinander", tlTag: "Zeitleiste", tlH: "1916–1945, mit Ausblick", platesTag: "Tafeln", platesH: "Photographien, Karten, Ansichten",
    filmsTag: "Filme", filmsH: "Die Wochenschauen und die Rohaufnahmen", filmsLede: "Was die Kameras im März 1945 an der Brücke aufnahmen, und was gezeigt wurde. Die amerikanischen Aufnahmen sind Werke der US-Regierung und hier aus dem Internet Archive eingebettet; die britischen Wochenschauen nur über den offiziellen Player ihrer Rechteinhaber. Die Deutsche Wochenschau zeigte Remagen nicht.",
    load: "Film laden", loadNote: "Der Film wird erst auf Klick vom Internet Archive oder von YouTube geladen; dabei erhalten diese Dienste Ihre IP-Adresse.",
    marks: "Kommentar an Zeitmarken", ton: "Der Ton: Abschrift mit Übersetzung", silent: "Kein Film: Die Ausgabe zeigt Remagen nicht.", dur: "Dauer", rights: "Rechte",
    fail: "Der Apparat konnte nicht geladen werden: "
  },
  en: {
    title: "One Bridge, Two Newsreels", nav: { "": "Overview", texts: "Texts", films: "Films", compare: "Compare", timeline: "Timeline", plates: "Plates", sources: "Sources" },
    switchTo: "Deutsch", loading: "Loading…", allTexts: "← All texts", allCmp: "← All comparisons", citeAs: "cited as", cite: "Cite as",
    orig: "Original", both: "Original + translation", trans: "Translation", or: " or ",
    srcNote: "Source and editorial note", source: "Source", planned: "planned", notTaken: "not included",
    shipped: "Printed here", plannedH: "Planned", missingH: "Examined and not included",
    textsTag: "Texts", textsH: "The corpus", textsLede: "Every module can be read in full, the original beside a translation: English sources with a German translation, German sources with an English one. What was examined and not included is listed below, with the reason.",
    cmpTag: "Compare", cmpH: "Voices side by side", tlTag: "Timeline", tlH: "1916–1945, with an epilogue", platesTag: "Plates", platesH: "Photographs, maps, views",
    filmsTag: "Films", filmsH: "The newsreels and the raw footage", filmsLede: "What the cameras recorded at the bridge in March 1945, and what was shown. The American footage is a work of the US government and is embedded here from the Internet Archive; the British newsreels only through the official player of their rights holders. The German newsreel did not show Remagen.",
    load: "Load film", loadNote: "The film is only loaded from the Internet Archive or YouTube when you click; those services then receive your IP address.",
    marks: "Commentary at time marks", ton: "The soundtrack: transcript", silent: "No film: this issue does not show Remagen.", dur: "Length", rights: "Rights",
    fail: "The apparatus could not be loaded: "
  }
};
const S = k => T[ui][k];
const SIDES = {
  bruecke: { de: "Die Brücke", en: "The bridge" },
  deutsch: { de: "Deutsche Seite", en: "German side" },
  us: { de: "Amerikanische Seite", en: "American side" },
  film: { de: "Wochenschau", en: "Newsreel" },
  menschen: { de: "Menschen und Lager", en: "People and camps" }
};
const LANGS = { de: { de: "Deutsch", en: "German" }, en: { de: "Englisch", en: "English" } };
/* a field in the reader's language: o.k_en in English if present, else o.k */
const L = (o, k) => (o && ui === "en" && o[k + "_en"] != null) ? o[k + "_en"] : (o ? o[k] : "");

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] ? SIDES[s][ui] : s)}</span>`;
const lname = l => LANGS[l] ? LANGS[l][ui] : l;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const filmOf = id => (D.films.films || []).find(f => f.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });
const secs = t => { const [m, s] = String(t).split(":").map(Number); return s == null ? m : m * 60 + s; };

function setUI(lang) {
  ui = lang;
  try { localStorage.setItem("bridge_ui", ui); } catch (e) { /* storage blocked */ }
  applyUI();
  route();
}

function applyUI() {
  document.documentElement.lang = ui;
  document.title = S("title");
  document.querySelectorAll(".top nav a[data-k]").forEach(a => a.textContent = S("nav")[a.dataset.k]);
  const b = document.getElementById("uiBtn");
  b.textContent = S("switchTo");
  b.lang = ui === "de" ? "en" : "de";
}

async function boot() {
  applyUI();
  document.getElementById("uiBtn").onclick = () => setUI(ui === "de" ? "en" : "de");
  [D.mods, D.plates, D.timeline, D.compare, D.films] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json", "data/films.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, films, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
const OVERVIEW = {
  de: {
    tag: "7.–17. März 1945 · Remagen · Erpel · Ludendorff-Brücke",
    h: "Eine Brücke, zwei Wochenschauen",
    lede: "Am Nachmittag des 7. März 1945 erreichten amerikanische Panzer die Höhen über Remagen und sahen unter sich die Ludendorff-Brücke noch stehen. Die deutsche Sprengung hob sie an, aber sie fiel nicht; Infanterie ging hinüber. Zehn Tage lang hielt die Brücke unter Artillerie, Bomben, V-2-Raketen und Kampfschwimmern, dann stürzte sie ein. Die amerikanischen und britischen Wochenschauen brachten die Brücke ins Kino. Die Deutsche Wochenschau schwieg; ein fliegendes Standgericht ließ vier Offiziere erschießen.",
    body: "Dieser Apparat folgt den Tagen an der Brücke durch Texte und Filme ihrer Zeit, in beiden Sprachen: die Darstellung der US Army, die Berichte der Divisionen und Ingenieure, deutsche Stimmen, wo sie gemeinfrei vorliegen, und die Filmaufnahmen, kommentiert an Zeitmarken. Er endet nicht mit dem Einsturz, sondern mit den Lagern, in denen im Frühjahr 1945 Hunderttausende deutsche Gefangene am Rhein lagen.",
    q: [
      ["Warum stand die Brücke noch?", "Ein Zündkabel, das nach deutscher Meinung ein amerikanischer Treffer durchschlug; Sabotage, die sich nicht ausschließen ließ; ein Sprengbefehl, der erst schriftlich vorliegen musste; Geschütze, die noch über den Fluss sollten. Die Quellen geben mehrere Antworten; keine allein genügt."],
      ["Was zeigten die Wochenschauen?", "Die amerikanische Universal-Wochenschau vom 26. März hieß „Allies Drive Across Rhine to Victory“; eine britische zeigt in Großaufnahme das Schild, das auch eine amerikanische Rohaufnahme festhält: „Cross the Rhine with dry feet – Courtesy of 9th Armd. Div.“ Die beiden letzten Ausgaben der Deutschen Wochenschau zeigten Remagen nicht. Das Schweigen ist selbst ein Befund."],
      ["Wer bezahlte dafür?", "Amerikanische Soldaten und Pioniere, deutsche Soldaten und Zivilisten im Tunnel der Erpeler Ley, vier Offiziere vor einem Standgericht, und die Gefangenen in den Lagern von Remagen und Sinzig."],
      ["Lässt sich das spielen?", "Das Begleitspiel Zehn Tage am Rhein ist in Vorbereitung: zwei Rollen, Hauptmann Willi Bratge und der amerikanische Brückenkopf, vom 7. bis zum 17. März. Gewertet wird, was die Tage an Menschenleben kosteten."]
    ],
    none: "Die ersten Module sind in Arbeit; die Seite „Texte“ nennt sie mit ihren Quellen, die Seite „Filme“ die Aufnahmen.",
    have: "Was der Apparat enthält", qs: "Die Fragen"
  },
  en: {
    tag: "7–17 March 1945 · Remagen · Erpel · Ludendorff Bridge",
    h: "One Bridge, Two Newsreels",
    lede: "On the afternoon of 7 March 1945 American tanks reached the heights above Remagen and saw the Ludendorff Bridge still standing below them. The German demolition lifted it, but it did not fall; infantry went across. For ten days the bridge held under artillery, bombs, V-2 rockets and frogmen, then it collapsed. The American and British newsreels brought the bridge to the cinema. The German newsreel was silent; a flying court-martial had four officers shot.",
    body: "This apparatus follows the days at the bridge through the texts and films of the time, in both languages: the US Army's history, the reports of the divisions and engineers, German voices where they are in the public domain, and the film footage, with commentary at time marks. It does not end with the collapse but with the camps in which hundreds of thousands of German prisoners lay along the Rhine in the spring of 1945.",
    q: [
      ["Why was the bridge still standing?", "A firing cable that Germans believed an American hit had cut; sabotage that could not be ruled out; an order to blow that first had to be in writing; guns that were still meant to cross the river. The sources give several answers; none is enough on its own."],
      ["What did the newsreels show?", "The American Universal newsreel of 26 March was called ‘Allies Drive Across Rhine to Victory’; a British one shows in close-up the sign that American raw footage also records: ‘Cross the Rhine with dry feet – Courtesy of 9th Armd. Div.’ The last two issues of the German newsreel did not show Remagen. The silence is itself a finding."],
      ["Who paid for it?", "American soldiers and engineers, German soldiers and civilians in the tunnel of the Erpeler Ley, four officers before a court-martial, and the prisoners in the camps at Remagen and Sinzig."],
      ["Can it be played?", "The companion game Ten Days on the Rhine is in preparation: two roles, Captain Willi Bratge and the American bridgehead, from 7 to 17 March. The score is what those days cost in human lives."]
    ],
    none: "The first modules are in preparation; the Texts page lists them with their sources, the Films page the footage.",
    have: "What the apparatus contains", qs: "The questions"
  }
};

function overview() {
  const O = OVERVIEW[ui];
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">${esc(O.tag)}</span>
      <h1>${esc(O.h)}</h1>
      <p class="lede">${esc(O.lede)}</p>
      <p class="readable">${esc(O.body)}</p>
    </div>
  </div>

  <h2>${esc(O.have)}</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">${esc(O.none)}</p>`}

  <h2>${esc(O.qs)}</h2>
  <div class="grid g2">${O.q.map(([h, p]) => `<div class="panel"><h3>${esc(h)}</h3><p>${esc(p)}</p></div>`).join("")}</div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(L(m, "zk"))}</span></div>
    <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  const other = (list, label) => list.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">${esc(label)}</span></div>
      <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p><p class="fine"><b>${esc(S("source"))}:</b> ${esc(L(m, "quelle"))}</p></div>`).join("");
  view.innerHTML = `
    <span class="tag">${esc(S("textsTag"))}</span><h1>${esc(S("textsH"))}</h1>
    <p class="lede">${esc(S("textsLede"))}</p>
    ${D.mods.shipped.length ? `<h2>${esc(S("shipped"))}</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>${esc(S("plannedH"))}</h2><div class="grid g2">${other(D.mods.planned, S("planned"))}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">${esc(S("missingH"))}</h2><div class="grid g2">${other(D.mods.missing, S("notTaken"))}</div>` : ""}`;
}

/* The translation of a unit into the reader's language, if its original is in the other one. */
function trOf(u, ul) { return ul === ui ? null : (u[ui] || null); }

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">${esc(S("loading"))}</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const ulOf = u => u.lang || t.orig_sprache;
  const bilingual = sec.units.some(u => u.orig && trOf(u, ulOf(u)));
  const lang = bilingual ? (langPref || "both") : "orig";
  const labels = { orig: S("orig"), both: S("both"), tr: S("trans") };
  view.innerHTML = `
    <p class="fine"><a href="#/texts">${esc(S("allTexts"))}</a></p>
    <span class="tag">${side(m.side)} ${esc(L(t, "jahr"))} · ${esc(S("citeAs"))} ${esc(L(sec, "zk"))} [n]</span>
    <h1>${esc(L(t, "titel"))}</h1>
    <p class="fine">${esc(L(t, "autor"))}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(L(s, "titel"))}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(L(sec, "titel"))}</h3><p>${esc(L(sec, "blurb"))}</p></div>
    ${(sec.plates || []).length ? `<div class="grid g4 secplates">${sec.plates.map(plateOf).filter(Boolean).map(plateFig).join("")}</div>` : ""}
    ${sec.viz ? `<div class="viz" id="viz"><p class="fine">${esc(S("loading"))}</p></div>` : ""}
    ${(sec.films || []).map(filmBlock).join("")}
    ${bilingual ? `<div class="langbar" id="langbar">
      ${["orig", "both", "tr"].map(k => `<button data-l="${k}" class="${k === lang ? "on" : ""}">${esc(labels[k])}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">${esc(S("srcNote"))}</span>
      <p><b>${esc(S("source"))}.</b> ${esc(L(t, "quelle"))}</p><p>${esc(L(t, "hinweis"))}</p></div>`;
  bindPlates(view);
  bindFilms(view);
  if (sec.viz) fetch(`assets/viz/${sec.viz}${ui === "en" ? "-en" : ""}.svg`).then(r => r.ok ? r.text() : "").then(svg => {
    const el = document.getElementById("viz");
    if (el) el.innerHTML = svg || "";
  });
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const ul = ulOf(u), tr = trOf(u, ul);
    const showO = u.orig && (!tr || lang !== "tr"), showT = tr && lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="${esc(S("cite"))} ${esc(L(sec, "zk"))} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(L(u, "titel"))} <span class="fine">(${esc(lname(ul))})</span></h4>` : ""}
          <div class="cols ${showO && showT ? "" : "one"}">
            ${showO ? `<div class="orig" lang="${esc(ul)}">${esc(u.orig)}</div>` : ""}
            ${showT ? `<div class="text" lang="${ui}">${esc(tr)}</div>` : ""}
          </div></div>
        ${L(u, "note") ? `<div class="note">${esc(L(u, "note"))}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("bridge_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ films */
function embedUrl(f, start, end) {
  if (f.ia) return `https://archive.org/embed/${encodeURIComponent(f.ia)}${start != null ? `?start=${secs(start)}${end != null ? `&end=${secs(end)}` : ""}` : ""}`;
  if (f.yt) return `https://www.youtube-nocookie.com/embed/${encodeURIComponent(f.yt)}${start != null ? `?start=${secs(start)}${end != null ? `&end=${secs(end)}` : ""}` : ""}`;
  return null;
}
/* A film block: a section may reference a film with its own excerpt (start, end) and comments. */
function filmBlock(ref) {
  const f = typeof ref === "string" ? filmOf(ref) : Object.assign({}, filmOf(ref.film), ref);
  if (!f || !f.id) return "";
  const marks = f.marks || [];
  const url = embedUrl(f, f.start, f.end);
  return `<div class="film panel" data-film="${esc(f.id)}" data-start="${esc(f.start || "")}" data-end="${esc(f.end || "")}">
    <div class="filmhead">${side("film")} <b>${esc(L(f, "titel"))}</b> <span class="fine">${esc(L(f, "datum") || "")}${f.dauer ? ` · ${esc(S("dur"))} ${esc(f.dauer)}` : ""}</span></div>
    <p class="fine">${esc(L(f, "beschreibung") || "")}</p>
    ${url ? `<div class="frame"><button class="loadfilm" type="button">▶ ${esc(S("load"))}${f.start ? ` (${esc(f.start)}${f.end ? `–${esc(f.end)}` : ""})` : ""}</button><p class="fine">${esc(S("loadNote"))}</p></div>`
      : `<div class="frame silent"><p>${esc(S("silent"))}</p></div>`}
    ${marks.length ? `<h4>${esc(S("marks"))}</h4><ol class="marks">${marks.map(mk => `<li><button class="mark" type="button" data-t="${esc(mk.t)}"${url ? "" : " disabled"}>${esc(mk.t)}</button> ${esc(L(mk, "text"))}${mk.cite ? ` <a href="${mk.cite}">✦</a>` : ""}</li>`).join("")}</ol>` : ""}
    ${(f.ton || []).length ? `<details class="ton"><summary>${esc(S("ton"))}</summary><p class="fine">${esc(L(f, "tonhinweis"))}</p>
      <ol class="marks">${f.ton.map(z => `<li><button class="mark" type="button" data-t="${esc(z.t)}"${url ? "" : " disabled"}>${esc(z.t)}</button>
        <span lang="en">${esc(z.en)}</span>${ui === "de" ? `<br><i lang="de">${esc(z.de)}</i>` : ""}</li>`).join("")}</ol></details>` : ""}
    <p class="fine"><b>${esc(S("rights"))}:</b> ${esc(L(f, "rechte") || "")}${f.link ? ` · <a href="${esc(f.link)}" target="_blank" rel="noopener">${esc(f.ia ? "archive.org" : f.yt ? "YouTube" : "Link")}</a>` : ""}</p>
  </div>`;
}
function bindFilms(root) {
  root.querySelectorAll("div.film[data-film]").forEach(box => {
    const f = filmOf(box.dataset.film);
    const play = (start, end) => {
      const url = embedUrl(f, start || null, end || null);
      if (!url) return;
      box.querySelector(".frame").innerHTML = `<iframe src="${url}" allow="fullscreen; encrypted-media; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" title="${esc(L(f, "titel"))}"></iframe>`;
    };
    const b = box.querySelector(".loadfilm");
    if (b) b.onclick = () => play(box.dataset.start, box.dataset.end);
    box.querySelectorAll(".mark").forEach(m => m.onclick = () => play(m.dataset.t, null));
  });
}
function films() {
  const F = D.films;
  view.innerHTML = `
    <span class="tag">${esc(S("filmsTag"))}</span><h1>${esc(S("filmsH"))}</h1>
    <p class="lede">${esc(S("filmsLede"))}</p>
    ${(F.films || []).map(f => filmBlock(f.id)).join("")}`;
  bindFilms(view);
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(S("cmpH"))}</h1>
      <p class="lede">${esc(L(CMP, "lede"))}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(L(p, "titel"))}</h3><p class="fine">${esc(L(p, "frage"))}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p><p class="fine">${esc(S("loading"))}</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(L(t, "autor"))}</b><br><span class="fine">${esc(L(t, "jahr"))} · ${esc(L(sec, "titel"))}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(L(sec, "zk"))} [${u.n}]</a>${u.titel ? ` · ${esc(L(u, "titel"))}` : ""}</div>
        <div class="text">${esc(trOf(u, u.lang || t.orig_sprache) || u.orig)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p>
    <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(L(pair, "titel"))}</h1>
    <p class="lede">${esc(L(pair, "frage"))}</p>
    <div class="panel readable"><p>${esc(L(pair, "note"))}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const TL = D.timeline;
  view.innerHTML = `
    <span class="tag">${esc(S("tlTag"))}</span><h1>${esc(S("tlH"))}</h1>
    <p class="lede">${esc(L(TL, "lede"))}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${TL.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(L(s, "d"))} · ${side(s.side)}</div><h3>${esc(L(s, "titel"))}</h3><p>${esc(L(s, "text"))}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(L(s, "citeLabel"))}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}" title="${esc(L(p, "titel"))}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">${esc(S("platesTag"))}</span><h1>${esc(S("platesH"))}</h1>
    <p class="lede">${esc(L(D.plates, "lede"))}</p>
    <div class="grid g4">${D.plates.plates.map(plateFig).join("")}</div>
    <p class="fine">${esc(L(D.plates, "credit"))}</p>`;
  bindPlates(view);
}
function plateFig(p) {
  return `<figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}"></a>
      <figcaption>${side(p.side)} <b>${esc(L(p, "titel"))}</b><br>${esc(L(p, "caption"))}<br><i>${esc(p.source)}</i></figcaption></figure>`;
}
function bindPlates(root) {
  root.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(L(p, "titel"))}"><figcaption class="cap"><b>${esc(L(p, "titel"))}.</b> ${esc(L(p, "caption"))}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
const METHOD = {
  de: {
    tag: "Quellen, Methode, Grenzen", h: "Wie dieser Apparat gemacht ist",
    p: [
      ["Nur Gemeinfreies, und was eingebettet werden darf.", "Die Texte stammen aus Werken der US-Regierung (die Darstellung der US Army, Berichte der Divisionen und Ingenieure, freigegebene Studien) und aus deutschen Drucken, deren Schutzfrist abgelaufen ist; die Quelle steht auf jeder Seite. Die Filme sind nicht auf dieser Site gespeichert: Amerikanische Aufnahmen werden aus dem Internet Archive eingebettet, britische Wochenschauen nur über den offiziellen Player ihrer Rechteinhaber. Die Deutsche Wochenschau wird weder gezeigt noch eingebettet; ihre Ausgaben vom März 1945 sind nur nach ihrem Inhalt beschrieben."],
      ["Die Quelle ist maßgeblich.", "Texte werden am Seitenbild gelesen, Filme an der Aufnahme selbst; die Zeitmarken beziehen sich auf die eingebettete Fassung. Was nur die neuere Literatur weiß, ist als solches gekennzeichnet; geschützte Darstellungen werden nur referiert."],
      ["Zwei Sprachen.", "Jede Quelle steht im Original. Englische Quellen haben eine deutsche, deutsche eine englische Übersetzung; die Übersetzungen sind eigene Arbeit, nah am Original und gemeinfrei (CC0). Die Oberfläche lässt sich umschalten."],
      ["NS-Material.", "Wo Dokumente des NS-Staates zitiert werden (Wehrmachtbericht, Urteile des Standgerichts), geschieht es zur Aufklärung über die Geschichte und mit Einordnung. Kennzeichen verfassungswidriger Organisationen werden, wo es sich vermeiden lässt, nicht gezeigt."],
      ["Zahlen.", "Wo die Quellen sich widersprechen, etwa bei den Toten des Einsturzes oder in den Lagern, stehen die Angaben mit ihrer Herkunft nebeneinander. Widerlegte Zahlen werden genannt und als widerlegt bezeichnet."]
    ],
    printed: "Abgedruckte Quellen", plates: "Tafeln"
  },
  en: {
    tag: "Sources, method, limits", h: "How this apparatus is made",
    p: [
      ["Public domain only, and what may be embedded.", "The texts come from works of the US government (the US Army's history, reports of divisions and engineers, released studies) and from German prints whose term of protection has expired; the source is named on every page. The films are not stored on this site: American footage is embedded from the Internet Archive, British newsreels only through the official player of their rights holders. The German newsreel is neither shown nor embedded; its issues of March 1945 are described by their contents only."],
      ["The source decides.", "Texts are read against the page images, films against the footage itself; time marks refer to the embedded version. What only recent literature knows is marked as such; protected accounts are only summarized."],
      ["Two languages.", "Every source stands in the original. English sources have a German translation, German sources an English one; the translations are my own, close to the original and in the public domain (CC0). The interface can be switched."],
      ["Nazi material.", "Where documents of the Nazi state are quoted (the Wehrmacht report, the sentences of the court-martial), this serves historical education and comes with context. Symbols of unconstitutional organizations are not shown where this can be avoided."],
      ["Numbers.", "Where the sources disagree, as on the dead of the collapse or in the camps, the figures stand side by side with their origin. Disproved figures are named and called disproved."]
    ],
    printed: "Sources printed here", plates: "Plates"
  }
};

function sources() {
  const M = METHOD[ui];
  view.innerHTML = `
    <span class="tag">${esc(M.tag)}</span><h1>${esc(M.h)}</h1>
    <div class="readable">${M.p.map(([b, p]) => `<p><b>${esc(b)}</b> ${esc(p)}</p>`).join("")}</div>
    ${D.mods.shipped.length ? `<h2>${esc(M.printed)}</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(L(m, "kurz"))}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : ""}
    ${(D.plates.plates || []).length ? `<h2>${esc(M.plates)}</h2><p class="fine readable">${esc(L(D.plates, "credit"))}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = L(t, "quelle");
  });
}

boot().catch(e => { view.innerHTML = `<p>${esc(S("fail"))}${esc(e.message)}</p>`; });
