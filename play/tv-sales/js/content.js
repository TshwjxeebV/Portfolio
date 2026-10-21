/* All lesson copy lives here so it can be edited without touching the app logic. */
window.LESSON = {
  icons: {
    pixels: '<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    layers: '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
    tv: '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    chat: '<path d="M4 5h16v10H9l-5 4V5z"/>',
    play: '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M10 8l5 2.5-5 2.5V8z"/>',
    bag: '<path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    minus: '<path d="M5 12h14"/>',
    check: '<path d="M5 13l4 4L19 7"/>',
    x: '<path d="M6 6l12 12M18 6L6 18"/>',
    chevUp: '<path d="M6 15l6-6 6 6"/>',
    download: '<path d="M12 4v11"/><path d="M7 10l5 5 5-5"/><path d="M5 20h14"/>',
    refresh: '<path d="M20 12a8 8 0 1 1-2.34-5.66"/><path d="M20 4v5h-5"/>'
  },

  specs: [
    ["Contrast", "The difference between the brightest white and the darkest black. OLED leads because its pixels switch off; Mini-LED comes close with local dimming; Crystal LED is lowest, with no dimming zones."],
    ["Brightness (nits)", "How much light the screen can produce. Sunny rooms need more — Mini-LED leads and QLED is strong. In a dark bedroom, a very bright screen can cause eye strain at night."],
    ["Viewing angle", "How well color holds up when someone sits off to the side. OLED offers near-perfect angles; Crystal LED is the narrowest."],
    ["Refresh rate (Hz)", "How many times per second the picture updates. OLED reaches up to 144Hz for gaming; Crystal LED is a standard 60Hz."],
    ["Burn-in risk", "Static images left on for hours — news tickers, scoreboards, dashboards — can mark an OLED panel. QLED is fully immune, so it's the pick for TVs left on all day."]
  ],

  preview: [
    { name: "OLED", icon: "pixels", sub: "Self-lit pixels", detail: "Each pixel makes its own light and can switch fully off." },
    { name: "Mini-LED", icon: "sun", sub: "Local dimming zones", detail: "Thousands of tiny LEDs behind an LCD dim in hundreds of zones." },
    { name: "QLED", icon: "layers", sub: "Quantum-dot color", detail: "A quantum-dot layer filters and enhances a standard LED backlight." },
    { name: "Crystal LED", icon: "tv", sub: "Basic LED backlight", detail: "A traditional LCD lit by a simple backlight with no dimming zones." }
  ],

  techs: [
    { name: "OLED", icon: "pixels", tag: "Every pixel makes its own light", best: "Dark rooms & movies",
      how: "No backlight. Each pixel emits its own light and can switch itself off completely.",
      features: "Infinite contrast and perfect blacks with zero blooming. Ultra-fast response (up to 144Hz) for gaming. Near-perfect viewing angles.",
      experience: "The ultimate premium, cinematic picture — crisp motion and rich color depth.",
      bedroom: "Widely considered the best bedroom TV. Dark rooms make perfect blacks shine, and with no big glaring backlight there's less eye fatigue before bed.",
      also: "Dedicated home theaters · dark living rooms",
      watch: "Static images can burn in. Not for bright businesses or all-day tickers." },
    { name: "Mini-LED", icon: "sun", tag: "Thousands of tiny LEDs in dimming zones", best: "Anti-glare & bright rooms",
      how: "Thousands of microscopic LEDs sit behind the LCD panel, grouped into hundreds of dimming zones for precise backlight control.",
      features: "Very high peak brightness while keeping deep blacks — bridges standard LED and OLED.",
      experience: "Intensely vibrant and punchy. HDR highlights pop even when fighting heavy room glare.",
      bedroom: "Less ideal for a dark bedroom — the brightness can be blinding at night. But for huge windows and daytime viewing, this is the solution.",
      also: "Bright, sunlit homes · covered patios · family media rooms",
      watch: "Can show minor halos (blooming) around bright objects on dark backgrounds." },
    { name: "QLED", icon: "layers", tag: "LED backlight + quantum-dot layer", best: "All-day viewing & value",
      how: "Builds on a standard LED backlight by adding a layer of quantum dots to filter and enhance the light.",
      features: "Wider color gamut with rich saturation even at high brightness. Fully immune to burn-in.",
      experience: "Vivid, lifelike color and a great all-around picture.",
      bedroom: "Excellent value bedroom TV — a colorful, punchy picture for a fraction of OLED's cost. Great for kids' and guest rooms.",
      also: "Moderately lit living rooms · sports bars · kitchens · business dashboards",
      watch: "Dark scenes can look slightly gray or washed out next to OLED." },
    { name: "Crystal LED", icon: "tv", tag: "Standard LCD with a basic LED backlight", best: "Tight budgets & busy spaces",
      how: "A traditional LCD screen lit by a basic LED backlight with no dimming zones.",
      features: "Highly affordable and reliable, with lower contrast, narrower viewing angles and a standard 60Hz refresh rate.",
      experience: "Clear and dependable, but without the dynamic range, depth or brightness of premium panels.",
      bedroom: "The ultimate budget choice — dorms, kids' rooms or a simple second TV for the news and casual shows before sleep.",
      also: "Commercial spaces · gyms · bars mounting several affordable screens",
      watch: "Don't pitch it to a customer asking for a “cinematic” or “punchy” picture." }
  ],

  guide: [
    { name: "“Movie before bed”", icon: "chat", img: "assets/img/guide-1-movie-before-bed.jpg", alt: "A couple in bed watching a dark movie scene on a wall-mounted TV in a dark bedroom at night.", sub: "Dark room · eye comfort", detail: "→ OLED. Perfect blacks in the dark and less eye fatigue before sleep." },
    { name: "“Sunlit living room”", icon: "chat", img: "assets/img/guide-2-sunlit-living-room.jpg", alt: "A family on a sofa watching TV in a living room flooded with afternoon sunlight from large windows.", sub: "Fights heavy glare", detail: "→ Mini-LED. The highest peak brightness overcomes natural light." },
    { name: "“Leave it on all day”", icon: "chat", img: "assets/img/guide-3-leave-it-on-all-day.jpg", alt: "Patrons at a neighborhood sports bar watching a baseball game on a TV with a scrolling ticker.", sub: "Sports bars · casual living rooms", detail: "→ QLED. Vivid color, great value and immune to burn-in." },
    { name: "“Just need a cheap screen”", icon: "chat", img: "assets/img/guide-4-cheap-screen.jpg", alt: "A student in a simple dorm room watching a small TV on a dresser, with string lights on the wall.", sub: "Dorms · guest rooms · gyms", detail: "→ Crystal LED. Affordable, reliable and clear for casual viewing." }
  ],

  sale: [
    { name: "Before", icon: "chat", img: "assets/img/sale-1-before-greeting.jpg", alt: "A sales associate in a navy polo greets a customer in a rust-orange jacket as she walks into the TV department.", title: "The customer walks in", points: [
      "Greet within 30 seconds — eye contact, open question.",
      "Discover: Which room? How bright? What do you watch? Who's watching?",
      "Listen for DISC cues: fast & direct, social, cautious, or data-driven." ] },
    { name: "During", icon: "play", img: "assets/img/sale-2-during-demo.jpg", alt: "The same associate points to a large TV showing a soccer game while the customer watches closely.", title: "The demo & recommendation", points: [
      "Match two specs to what they told you — no spec-dumping.",
      "Demo it: dark movie scene on OLED, a sports clip on Mini-LED.",
      "Invite them to step to the side — show viewing angle live." ] },
    { name: "After", icon: "bag", img: "assets/img/sale-3-after-leaving.jpg", alt: "The same customer smiles as she pushes a cart with her boxed TV toward the exit, and the associate waves goodbye.", title: "The close & follow-up", points: [
      "Summarize their needs in one sentence.",
      "Recommend one TV + one alternative; explain the trade-off.",
      "Offer setup, mounting and protection — then thank them by name." ] }
  ],

  precheck: [
    { tech: "OLED", q: "Which TV lets every pixel make its own light — and switch off completely for perfect black?", options: ["QLED", "OLED", "Mini-LED"], correct: 1,
      right: "Each OLED pixel is self-lit, so it can turn fully off — that's where its perfect blacks and zero blooming come from.",
      wrong: "Self-lit pixels that switch fully off are OLED's signature. That's what gives it perfect blacks in a dark room." },
    { tech: "Mini-LED", q: "Which TV uses thousands of tiny LEDs grouped into dimming zones to get bright enough to beat heavy glare?", options: ["OLED", "Crystal LED", "Mini-LED"], correct: 2,
      right: "Mini-LED packs thousands of microscopic LEDs into hundreds of dimming zones — very high brightness for sunlit rooms.",
      wrong: "Thousands of tiny LEDs in dimming zones is Mini-LED. It's the go-to for bright rooms and anti-glare." },
    { tech: "QLED", q: "Which TV adds a quantum-dot layer to an LED backlight, giving vivid color with no burn-in risk?", options: ["QLED", "OLED", "Crystal LED"], correct: 0,
      right: "QLED's quantum-dot layer boosts color, and it's immune to burn-in — great for TVs left on all day.",
      wrong: "The quantum-dot layer is QLED. Vivid color, great value and no burn-in risk." },
    { tech: "Crystal LED", q: "Which TV uses a traditional LCD with a basic backlight and no dimming zones — the most budget-friendly option?", options: ["Mini-LED", "Crystal LED", "QLED"], correct: 1,
      right: "Crystal LED is a standard LCD with a simple backlight — affordable and reliable for dorms, guest rooms and gyms.",
      wrong: "A basic, zone-free backlight is Crystal LED. It's our most affordable, dependable screen." }
  ],

  scenarios: [
    { focus: "Cinematic contrast & zero blooming", initial: "B", persona: "The Basement Home Theater customer",
      desc: "A movie enthusiast finishing a dedicated, windowless space for premium viewing.",
      img: "assets/img/scenario-1-basement-theater.jpg", alt: "A dark basement home theater with a large TV showing a starry space scene.",
      quote: "We're finally finishing our basement as a dedicated home theater. It'll be pitch black down there, just like a real cinema. I watch a lot of sci-fi and moody thrillers, and my biggest pet peeve is when white text or bright stars have a glowing halo around them on a black screen. What's the absolute best panel for a pitch-black room?",
      options: ["Recommend OLED", "Recommend Mini-LED", "Recommend QLED"], correct: 0,
      right: "Spot on. In a pitch-black room, OLED is the undisputed champion. Its self-lit pixels turn off completely, giving perfect blacks and infinite contrast with no haloing (blooming) around stars or credits — exactly the premium cinematic experience they want.",
      wrong: { 1: "Mini-LED is an incredible technology, but it still relies on a zone-based backlight. In a pitch-black basement, an enthusiast watching for “glowing halos” will likely notice minor blooming around bright objects on a dark background. OLED's pixel-level control is the better recommendation here.",
               2: "QLED gives vivid color for the price, but it's still backlit — dark scenes can look slightly gray or washed out next to OLED. For a pitch-black theater and a viewer who hates halos, OLED is the better recommendation." } },
    { focus: "Heavy glare", initial: "N", persona: "The Sunlit Day-Sleeper customer",
      desc: "A night-shift nurse who watches TV during the day in a room with massive windows.",
      img: "assets/img/scenario-2-sunlit-bedroom.jpg", alt: "A bright bedroom with floor-to-ceiling windows and a wall-mounted TV.",
      quote: "I just moved into an apartment with huge windows in the bedroom. I work nights, so I watch TV during the day when the sun is blasting in. I need something that won't look like a mirror.",
      options: ["Recommend OLED", "Recommend Mini-LED", "Recommend QLED"], correct: 1,
      right: "Excellent recommendation. Mini-LEDs use thousands of microscopic LEDs to reach incredibly high peak brightness. That vibrant, punchy image is the champion for overcoming natural light and heavy room glare.",
      wrong: { 0: "OLEDs are highly susceptible to heavy room glare. Recommending one for a room with massive daytime windows will leave a frustrated customer who can't see the screen through the reflections.",
               2: "QLED gets bright and holds its color well, so it's a reasonable thought — but sun blasting through huge windows calls for the highest peak brightness available. Mini-LED is the stronger anti-glare recommendation." } },
    { focus: "Burn-in & value", initial: "G", persona: "The “Leave It On All Day” customer",
      desc: "A casual viewer outfitting a heavily trafficked guest room or home office.",
      img: "assets/img/scenario-3-home-office.jpg", alt: "A home office and guest room with a wall-mounted TV showing a sports broadcast.",
      quote: "I want a really colorful, punchy TV for my home office/guest room. I leave the news or sports tickers running in the background 6 to 8 hours a day while I work. I don't want to spend OLED money, but I want it to look great.",
      options: ["Recommend OLED", "Recommend Crystal LED", "Recommend QLED"], correct: 2,
      right: "Perfect match. QLED delivers vivid, lifelike color and a great all-around picture for a fraction of OLED's cost. And its quantum-dot layer is fully immune to the static-image burn-in a news ticker can cause.",
      wrong: { 0: "OLED looks stunning, but a news ticker left on 6–8 hours a day is exactly the static image that risks burn-in — and the customer already said they don't want to spend OLED money. QLED is the sweet spot.",
               1: "Crystal LED is affordable, but the customer specifically asked for a “colorful, punchy” picture. Crystal LEDs lack the dynamic range and color saturation of premium panels. A value-driven QLED is the sweet spot for this request." } },
    { focus: "Strict budget", initial: "P", persona: "The “Just Need a Cheap Screen” customer",
      desc: "A parent shopping for a college dorm or a secondary kid's room.",
      img: "assets/img/scenario-4-dorm-room.jpg", alt: "A cozy college dorm room with a small TV on a dresser.",
      quote: "My daughter is heading to a dorm, and we just need a basic TV for casual shows or the news. We absolutely don't care about cinematic depth or perfect blacks — we just want something reliable and highly affordable.",
      options: ["Recommend Crystal LED", "Recommend QLED", "Recommend Mini-LED"], correct: 0,
      right: "Great floor awareness. You recognized that cinematic contrast isn't a priority here. A traditional LCD with a basic backlight gives the affordable, clear, dependable picture this customer actually needs.",
      wrong: { 1: "You're over-selling. The customer said they're on a strict budget, don't care about cinematic depth and just want a simple secondary TV. Pushing a QLED here risks losing the sale entirely on price.",
               2: "Mini-LED is a premium panel built to fight glare and deliver HDR punch — far more TV than a dorm needs, and well outside a strict budget. Crystal LED fits what this parent actually asked for." } },
    { focus: "Damage risk & multi-screen value", initial: "M", persona: "The Community Gym Owner",
      desc: "Owner of a small neighborhood strength gym outfitting the training floor with several mounted screens.",
      img: "assets/img/scenario-5-community-gym.jpg", alt: "A small strength gym with several TVs mounted on brick walls above kettlebells and medicine balls.",
      quote: "I'm opening a small strength gym and need five TVs mounted around the floor for class timers, music videos and the game on weekends. Medicine balls and kettlebells get thrown around, it gets humid in the summer with the garage door open, and honestly — a screen or two is going to get hit. I need something reliable that I won't cry over replacing.",
      options: ["Recommend QLED", "Recommend Crystal LED", "Recommend OLED"], correct: 1,
      right: "Smart business call. In a high-risk space with five screens, Crystal LED is the right fit: affordable, reliable and plenty clear for timers, music videos and casual sports. If one takes a hit, replacing it won't wreck the budget. Pair it with heavy-duty locking wall mounts placed high and away from the throwing zone. And remind them standard TVs are indoor-rated: keep screens away from the open garage door, or point them to outdoor-rated displays for that spot.",
      wrong: { 0: "QLED's vivid color and burn-in resistance are great, but here you'd be paying a premium five times over for screens that may take a kettlebell hit. A business buyer cares about cost per screen and easy replacement, and class timers don't need cinematic color. Crystal LED is what this gym actually needs.",
               2: "OLED is the most premium panel on the floor — five of them in a room where screens get hit would be a costly mistake. Static class timers left on for hours also risk burn-in. Crystal LED is the practical business choice." } }
  ],

  exit: {
    passPct: 80,
    topics: ["Specs", "Technologies", "Matching customers", "The sale"],
    questions: [
      { topic: "Specs", q: "Which spec describes the difference between the brightest white and the darkest black on a screen?",
        options: ["Brightness", "Contrast", "Refresh rate"], correct: 1,
        explain: "Contrast is the gap between the brightest white and the darkest black. More contrast means more depth — OLED leads because its pixels switch off." },
      { topic: "Specs", q: "A customer leaves a news ticker on screen 6–8 hours a day. Which TV is fully immune to burn-in?",
        options: ["OLED", "Mini-LED", "QLED"], correct: 2,
        explain: "QLED's quantum-dot layer is fully immune to burn-in. Static images like tickers and scoreboards can mark an OLED panel." },
      { topic: "Technologies", q: "How does a Mini-LED TV control its light?",
        options: ["Thousands of tiny LEDs grouped into dimming zones", "Every pixel makes its own light", "One basic backlight lights the whole screen"], correct: 0,
        explain: "Mini-LED packs thousands of microscopic LEDs behind the LCD, grouped into hundreds of dimming zones for precise control and very high brightness." },
      { topic: "Technologies", q: "Why is OLED widely considered the best TV for a dark bedroom?",
        options: ["It's the brightest panel on the floor", "It's fully immune to burn-in", "Perfect blacks and less eye fatigue, with no glaring backlight"], correct: 2,
        explain: "OLED's self-lit pixels give perfect blacks in a dark room, and without a big backlight there's less eye fatigue before bed." },
      { topic: "Technologies", q: "What's the main trade-off of a Crystal LED TV?",
        options: ["Lower contrast and narrower viewing angles", "A high risk of burn-in", "The highest price on the floor"], correct: 0,
        explain: "Crystal LED is affordable and reliable, but its basic, zone-free backlight means lower contrast, narrower viewing angles and a standard 60Hz refresh rate." },
      { topic: "Matching customers", q: "A customer watches TV in a living room flooded with afternoon sun. What's the best recommendation?",
        options: ["OLED", "Mini-LED", "Crystal LED"], correct: 1,
        explain: "Mini-LED's very high peak brightness overcomes heavy glare. OLEDs are highly susceptible to glare in sun-filled rooms." },
      { topic: "Matching customers", q: "A gym owner needs five affordable screens for class timers in a room where a screen may get hit. What's the best recommendation?",
        options: ["OLED", "QLED", "Crystal LED"], correct: 2,
        explain: "Crystal LED is affordable and reliable, so replacing a damaged screen won't wreck the budget — and class timers don't need cinematic color." },
      { topic: "Matching customers", q: "A movie lover building a pitch-black basement theater hates halos around bright stars and credits. What should you recommend?",
        options: ["OLED", "Mini-LED", "QLED"], correct: 0,
        explain: "OLED's self-lit pixels switch off completely, so there's no blooming around bright objects — exactly what a pitch-black theater needs." },
      { topic: "The sale", q: "A customer has just walked into the TV department. What should you do first?",
        options: ["Point them to the most popular TV", "Greet them within 30 seconds and ask discovery questions", "Start a demo on the brightest TV"], correct: 1,
        explain: "Greet within 30 seconds, then discover: which room, how bright it is, what they watch and who's watching. The recommendation comes after." },
      { topic: "The sale", q: "What's the strongest way to close the sale?",
        options: ["List every spec so they have all the facts", "Offer the most expensive TV first, then step down", "Summarize their needs, recommend one TV plus one alternative, and offer setup"], correct: 2,
        explain: "Summarize their needs in one sentence, recommend one TV and one alternative with the trade-off, then offer setup, mounting and protection." }
    ]
  }
};

/* Visuals: same scene on every screen (a bright star on a night sky), how each TV makes light, and relative ratings. */
window.LESSON.visuals = {
  "OLED": {
    screen: { bg: "#000000", halo: 0, haloOp: 0, zones: false, star: 1 },
    alt: "OLED screen: a bright star on a perfectly black sky with no glow around it.",
    caption: "Pure black · no glow",
    layers: [["Front glass", ""], ["Self-lit pixels", "Each pixel makes its own light and can switch fully off", true]],
    glance: [["Contrast", 5], ["Brightness", 3], ["Viewing angle", 5], ["Budget-friendly", 1]]
  },
  "Mini-LED": {
    screen: { bg: "#05060A", halo: 18, haloOp: .22, zones: true, star: 1 },
    alt: "Mini-LED screen: a very bright star on a deep black sky with a faint halo and visible dimming zones.",
    caption: "Deep black · faint halo",
    layers: [["LCD panel", "Shapes the picture"], ["Thousands of tiny LEDs", "Grouped in hundreds of dimming zones", true]],
    glance: [["Contrast", 4], ["Brightness", 5], ["Viewing angle", 3], ["Budget-friendly", 2]]
  },
  "QLED": {
    screen: { bg: "#161A22", halo: 24, haloOp: .28, zones: false, star: 1 },
    alt: "QLED screen: a bright star on a dark gray sky with a soft glow.",
    caption: "Dark gray · soft glow",
    layers: [["LCD panel", "Shapes the picture"], ["Quantum-dot layer", "Boosts color"], ["LED backlight", "Lights the whole screen", true]],
    glance: [["Contrast", 3], ["Brightness", 4], ["Viewing angle", 3], ["Budget-friendly", 4]]
  },
  "Crystal LED": {
    screen: { bg: "#272B35", halo: 34, haloOp: .34, zones: false, star: .85 },
    alt: "Crystal LED screen: a dimmer star on a washed-out gray sky with a wide glow.",
    caption: "Gray · wide glow",
    layers: [["LCD panel", "Shapes the picture"], ["Basic LED backlight", "One light for the whole screen, no zones", true]],
    glance: [["Contrast", 2], ["Brightness", 2], ["Viewing angle", 2], ["Budget-friendly", 5]]
  }
};
