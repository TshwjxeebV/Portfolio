/* TV screen illustrations — the same night-sky scene rendered as each technology would show it.
   v1 = first pass (subtle, realistic differences). v2 = current (exaggerated, one signature trait each).
   Both are kept so the design process page can show the iteration. */
window.TVScreens = (function () {
  "use strict";
  let uid = 0;
  const id = (p) => `${p}${++uid}`;
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const frame = (inner, label, cls) => `<svg class="screen ${cls || ""}" viewBox="0 0 200 124" role="img" aria-label="${esc(label)}">
      ${inner}
      <rect x="94" y="116" width="12" height="5" fill="#0B1F3A"/><rect x="78" y="120" width="44" height="4" rx="2" fill="#0B1F3A"/>
    </svg>`;

  /* ---------- v1: subtle ---------- */
  const V1 = {
    "OLED":        { bg: "#000000", halo: 0,  haloOp: 0,   zones: false, star: 1,   caption: "Pure black · no glow" },
    "Mini-LED":    { bg: "#05060A", halo: 18, haloOp: .22, zones: true,  star: 1,   caption: "Deep black · faint halo" },
    "QLED":        { bg: "#161A22", halo: 24, haloOp: .28, zones: false, star: 1,   caption: "Dark gray · soft glow" },
    "Crystal LED": { bg: "#272B35", halo: 34, haloOp: .34, zones: false, star: .85, caption: "Gray · wide glow" }
  };
  function v1(name, cls) {
    const c = V1[name]; if (!c) return "";
    const g = id("h1-");
    let zones = "";
    if (c.zones) { for (let x = 30; x < 194; x += 23.5) zones += `<line x1="${x}" y1="6" x2="${x}" y2="110"/>`; for (let y = 32; y < 110; y += 26) zones += `<line x1="6" y1="${y}" x2="194" y2="${y}"/>`; }
    return frame(`
      <defs><radialGradient id="${g}"><stop offset="0" stop-color="#fff" stop-opacity="${c.haloOp}"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>
      <rect x="0" y="0" width="200" height="116" rx="8" fill="#0B1F3A"/>
      <rect x="6" y="6" width="188" height="104" rx="3" fill="${c.bg}"/>
      ${zones ? `<g stroke="#fff" stroke-opacity=".07" stroke-width="1">${zones}</g>` : ""}
      ${c.halo ? `<circle cx="128" cy="46" r="${c.halo}" fill="url(#${g})"/><ellipse cx="74" cy="90" rx="${c.halo + 26}" ry="${Math.round(c.halo / 2) + 4}" fill="url(#${g})"/>` : ""}
      <circle cx="128" cy="46" r="5" fill="#fff" fill-opacity="${c.star}"/>
      <path d="M128 36v20M118 46h20" stroke="#fff" stroke-opacity="${c.star * .7}" stroke-width="1.2"/>
      <circle cx="60" cy="30" r="1.2" fill="#fff" fill-opacity="${c.star * .8}"/><circle cx="160" cy="80" r="1" fill="#fff" fill-opacity="${c.star * .8}"/><circle cx="40" cy="64" r="1" fill="#fff" fill-opacity="${c.star * .7}"/>
      <rect x="44" y="88" width="60" height="4" rx="2" fill="#fff" fill-opacity="${c.star * .9}"/>`, `${name} (version 1): ${c.caption}`, cls);
  }

  /* ---------- v2: exaggerated — one signature trait per TV ----------
     OLED      → pitch black + razor-sharp light (pixels switch off)
     Mini-LED  → brightest light + visible blocky zone glow (dimming zones)
     QLED      → most vivid color, but blacks are clearly gray-blue
     Crystal   → washed out: gray blacks, dull color, big wide glow, haze */
  const V2 = {
    "OLED":        { bg: "#000000", aurora: ["#22D3EE", "#A855F7"], auroraOp: .85, sat: 1,   star: 1,   starR: 4.5, rays: 0,  halo: 0,  haloOp: 0,   zones: false, haze: 0,   textOp: 1,
                     caption: "Pitch black · razor-sharp light", short: "Pitch black · sharp", alt: "OLED: a pitch-black sky with razor-sharp stars and subtitles and no glow at all." },
    "Mini-LED":    { bg: "#030305", aurora: ["#38BDF8", "#C084FC"], auroraOp: 1,   sat: 1,   star: 1,   starR: 7,   rays: 16, halo: 0,  haloOp: 0,   zones: true,  haze: 0,   textOp: 1,
                     caption: "Brightest light · blocky zone glow", short: "Brightest · blocky glow", alt: "Mini-LED: the brightest star with long light rays, deep black sky, and visible square blocks of glow around bright objects from the dimming zones." },
    "QLED":        { bg: "#1F2735", aurora: ["#06F0FF", "#FF2BD6"], auroraOp: 1,   sat: 1.4, star: 1,   starR: 5,   rays: 6,  halo: 22, haloOp: .3,  zones: false, haze: 0,   textOp: 1,
                     caption: "Most vivid color · gray-blue blacks", short: "Most vivid · gray blacks", alt: "QLED: the most vivid, saturated colors in the sky, but the black background is clearly gray-blue, with a soft glow around the star." },
    "Crystal LED": { bg: "#3B414D", aurora: ["#7A8A99", "#8E8399"], auroraOp: .55, sat: .3,  star: .7,  starR: 5,   rays: 0,  halo: 44, haloOp: .38, zones: false, haze: .1,  textOp: .75,
                     caption: "Washed out · dull color · wide glow", short: "Washed out · wide glow", alt: "Crystal LED: a washed-out gray sky, dull faded colors, a dimmer star and a wide hazy glow around everything." }
  };
  function v2(name, cls) {
    const c = V2[name]; if (!c) return "";
    const g = id("h2-"), au = id("au-"), cl = id("cl-");
    // Mini-LED: light up whole zone blocks near bright objects (the "blooming" signature, exaggerated)
    let zones = "";
    if (c.zones) {
      const cols = 12, rows = 7, cw = 188 / cols, ch = 104 / rows;
      const bright = [[128, 46, 1], [74, 90, .8]];
      for (let r = 0; r < rows; r++) for (let k = 0; k < cols; k++) {
        const cx = 6 + k * cw + cw / 2, cy = 6 + r * ch + ch / 2;
        let op = 0;
        bright.forEach(([bx, by, w]) => { const d = Math.hypot(cx - bx, cy - by); op = Math.max(op, w * Math.max(0, .34 - d / 95)); });
        if (op > .02) zones += `<rect x="${(6 + k * cw).toFixed(1)}" y="${(6 + r * ch).toFixed(1)}" width="${cw.toFixed(1)}" height="${ch.toFixed(1)}" fill="#BFD8FF" fill-opacity="${op.toFixed(2)}"/>`;
      }
      zones = `<g>${zones}</g><g stroke="#fff" stroke-opacity=".09" stroke-width=".6">${Array.from({ length: cols - 1 }, (_, i) => `<line x1="${(6 + (i + 1) * cw).toFixed(1)}" y1="6" x2="${(6 + (i + 1) * cw).toFixed(1)}" y2="110"/>`).join("")}${Array.from({ length: rows - 1 }, (_, i) => `<line x1="6" y1="${(6 + (i + 1) * ch).toFixed(1)}" x2="194" y2="${(6 + (i + 1) * ch).toFixed(1)}"/>`).join("")}</g>`;
    }
    const rays = c.rays ? `<g stroke="#fff" stroke-linecap="round" stroke-opacity="${c.star}">
        <path d="M128 ${46 - c.rays}V${46 + c.rays}M${128 - c.rays} 46H${128 + c.rays}" stroke-width="1.6"/>
        <path d="M${128 - c.rays * .55} ${46 - c.rays * .55}L${128 + c.rays * .55} ${46 + c.rays * .55}M${128 - c.rays * .55} ${46 + c.rays * .55}L${128 + c.rays * .55} ${46 - c.rays * .55}" stroke-width=".9" stroke-opacity="${c.star * .7}"/></g>` : "";
    const stars = [[34, 22], [60, 30], [92, 18], [160, 24], [178, 60], [160, 80], [40, 64], [20, 46]]
      .map(([x, y]) => `<circle cx="${x}" cy="${y}" r="${c.zones ? 1.3 : 1.1}" fill="#fff" fill-opacity="${c.star * .9}"/>`).join("");
    return frame(`
      <defs>
        <clipPath id="${cl}"><rect x="6" y="6" width="188" height="104" rx="3"/></clipPath>
        <radialGradient id="${g}"><stop offset="0" stop-color="#fff" stop-opacity="${c.haloOp}"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
        <linearGradient id="${au}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="${c.aurora[0]}"/><stop offset="1" stop-color="${c.aurora[1]}"/></linearGradient>
        <filter id="${au}b" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="5"/><feColorMatrix type="saturate" values="${c.sat}"/></filter>
      </defs>
      <rect x="0" y="0" width="200" height="116" rx="8" fill="#0B1F3A"/>
      <g clip-path="url(#${cl})">
        <rect x="6" y="6" width="188" height="104" fill="${c.bg}"/>
        <path d="M-10 70 C 30 40, 70 62, 100 46 S 160 30, 210 44 L 210 58 C 160 46, 120 70, 90 64 S 30 60, -10 84 Z" fill="url(#${au})" opacity="${c.auroraOp}" filter="url(#${au}b)"/>
        ${zones}
        ${c.halo ? `<circle cx="128" cy="46" r="${c.halo}" fill="url(#${g})"/><ellipse cx="74" cy="90" rx="${c.halo + 22}" ry="${Math.round(c.halo / 2) + 6}" fill="url(#${g})"/>` : ""}
        ${stars}
        <circle cx="128" cy="46" r="${c.starR}" fill="#fff" fill-opacity="${c.star}"/>
        ${rays}
        <rect x="44" y="88" width="60" height="4.5" rx="2" fill="#fff" fill-opacity="${c.textOp}"/>
        ${c.haze ? `<rect x="6" y="6" width="188" height="104" fill="#fff" fill-opacity="${c.haze}"/>` : ""}
      </g>`, c.alt, cls);
  }

  return {
    v1, v2,
    caption: (name, version) => ((version === 1 ? V1 : V2)[name] || {}).caption || "",
    short: (name) => (V2[name] || {}).short || "",
    alt: (name) => (V2[name] || {}).alt || "",
    names: Object.keys(V2)
  };
})();
