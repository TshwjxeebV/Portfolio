"""Builds the portfolio pages from shared pieces. Run: python3 build.py

Edit the SETTINGS below, then run again to update every page.
"""
import html

# ---------------- SETTINGS (edit me) ----------------
EMAIL = "TshwjxeebKVaaj@gmail.com"
LINKEDIN = "#"                             # TODO: your LinkedIn URL
RESUME = "#"                               # TODO: link to your résumé PDF (e.g. assets/resume.pdf)
COACHING_URL = "https://www.figma.com/proto/dQfAXwxr1hTJab9ClCiHmL/Coach-Conflict-Simulation?node-id=8-2&starting-point-node-id=8%3A2&scaling=scale-down"
PIP_URL = "https://claude.ai/artifact/PaPuKJDkMRTBDFS2QdzKYD"
TV_URL = "https://www.figma.com/proto/w9wKmXGWE0hztSUz83MSDh?node-id=5-474&starting-point-node-id=5%3A474&scaling=scale-down"
# ----------------------------------------------------

e = html.escape
ARROW = '<span class="arrow" aria-hidden="true">→</span>'


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="assets/img/tile-coaching.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='32' fill='%230a0f1e'/%3E%3Ctext x='32' y='43' font-family='Georgia' font-size='34' text-anchor='middle' fill='%23e0a672'%3ET%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<div class="ambient" aria-hidden="true"><span class="a1"></span><span class="a2"></span><span class="a3"></span><span class="a4"></span></div>
"""


def nav(current):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f"""<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html">Tshwjxeeb Vaaj</a>
    <ul class="nav-links" id="nav-links">
      {link("index.html#work", "Work", "work")}
      {link("about.html", "About", "about")}
      {link("index.html#contact", "Contact", "contact")}
    </ul>
    <a class="pill ghost talk" href="index.html#contact">Let's talk</a>
    <button class="menu-btn" aria-label="Open menu" aria-controls="nav-links" aria-expanded="false">☰</button>
  </div>
</header>
"""


def footer():
    return f"""<footer class="footer">
  <div class="wrap">
    <a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a>
    <a href="{e(LINKEDIN)}" target="_blank" rel="noopener">LinkedIn</a>
    <a href="{e(RESUME)}" target="_blank" rel="noopener">Résumé (PDF)</a>
    <span>© <span id="year">2026</span> Tshwjxeeb Vaaj</span>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def pill(href, label, ghost=False, external=False):
    cls = "pill ghost" if ghost else "pill"
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return f'<a class="{cls}" href="{href}"{tgt}>{label} {ARROW}</a>'


def video(src, poster, label, cls="player"):
    return (f'<div class="{cls}"><video src="{src}" poster="{poster}" autoplay muted loop playsinline '
            f'preload="metadata" aria-label="{e(label)}"></video></div>')


def paras(*ps):
    return "\n".join(f"<p>{e(p)}</p>" for p in ps)


def cs_hero(img, quote, by, cta, url, right=False):
    cls = "photo right" if right else "photo"
    return f"""<section class="cs-hero" aria-label="Project hero">
  <div class="{cls}" style="background-image:url('{img}')" role="img" aria-label="Project scene"></div>
  <div class="wrap">
    <div class="quote reveal"><blockquote>{e(quote)}</blockquote><cite>{e(by)}</cite></div>
    <div class="reveal d1">{pill(url, cta, external=True)}</div>
  </div>
</section>
"""


def meta_blocks(items, cols=False):
    c = "meta cols" if cols else "meta"
    inner = "".join(f'<div><h3>{e(h)}</h3><p>{e(b)}</p></div>' for h, b in items)
    return f'<div class="{c}">{inner}</div>'


def next_prev(prev, nxt):
    return f"""<section><div class="wrap next-prev reveal">
  <a href="{prev[1]}"><small>← Previous project</small><strong>{e(prev[0])}</strong></a>
  <a href="{nxt[1]}"><small>Next project →</small><strong>{e(nxt[0])}</strong></a>
</div></section>
"""


def write(name, content):
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)


# ======================= HOME =======================
home = head("Tshwjxeeb Vaaj · Learning Designer",
            "Learning designer and program manager. I design training that holds up when the real situation stops following the script.")
home += nav("work")
home += f"""<main>
<section class="home-hero">
  <div class="wrap">
    <div class="headshot reveal"><img src="assets/img/headshot.jpg" alt="Portrait of Tshwjxeeb Vaaj in a navy blazer"></div>
    <div>
      <p class="eyebrow reveal">Learning Designer · Program Manager</p>
      <h1 class="h-xl reveal d1">I'm Tshwjxeeb.</h1>
      <p class="lead reveal d1">I design training that holds up when the real situation stops following the script.</p>
      <div class="reveal d2">{pill("coaching.html", "Featured project")}</div>
    </div>
  </div>
</section>

<section aria-labelledby="featured">
  <div class="wrap">
    <div class="spotlight glass reveal">
      <img src="assets/img/tile-coaching.jpg" alt="A coach at home using the Coaching Through Conflict module on a laptop">
      <div>
        <p class="eyebrow">Featured · Scenario-based training</p>
        <h2 class="h-md" id="featured">Coaching Through Conflict</h2>
        <p>A branching simulation built from my own season as a head coach: from 0–10 and last in the league to my school's first-ever semifinal. New coaches practice pausing, reading the moment, and letting players own the fix.</p>
        <ul class="chips"><li>0–10 → 6–3</li><li>First-ever semifinal</li><li>68 screens</li></ul>
        {pill("coaching.html", "Learn more", ghost=True)}
      </div>
    </div>
  </div>
</section>

<section class="center">
  <div class="wrap">
    <h2 class="h-lg reveal">See it in action.</h2>
    <p class="lead reveal">A learner moves through Set 1: the moment, a breath, the mental timeout, and a decision.</p>
    <div class="reveal d1">{video("assets/video/coaching-walkthrough.mp4", "assets/img/poster-coaching.jpg", "Walkthrough of the Coaching Through Conflict module", "player wide")}</div>
  </div>
</section>

<section class="band" style="background-image:url('assets/img/coaching-hero.jpg')">
  <div class="wrap">
    <div class="box reveal">
      <p class="eyebrow">My approach</p>
      <h2 class="h-md">Built from real moments, not theory.</h2>
      <p>Every module starts with something I lived: a team that turned a winless season into a semifinal run, and a sales floor where the training never let me practice. I turn those moments into safe practice that feels real.</p>
      <div class="steps"><span>01 Read</span><span>02 Adapt</span><span>03 Execute</span></div>
    </div>
  </div>
</section>

<section id="work" aria-labelledby="work-h">
  <div class="wrap">
    <p class="eyebrow reveal">Selected work</p>
    <h2 class="h-lg reveal" id="work-h">Three projects, three real problems.</h2>
    <div class="tiles">
      <a class="tile reveal" href="coaching.html"><div class="shot"><img src="assets/img/tile-coaching.jpg" alt="Coaching Through Conflict on a laptop at home" loading="lazy"></div><h3>Coaching Through Conflict</h3><span class="role">Scenario-based training →</span></a>
      <a class="tile reveal d1" href="pip.html"><div class="shot"><img src="assets/img/tile-pip.jpg" alt="Pip's Number Garden on a phone on a wooden table" loading="lazy"></div><h3>Pip's Number Garden</h3><span class="role">Game-based learning →</span></a>
      <a class="tile reveal d2" href="tv-wall.html"><div class="shot"><img src="assets/img/tile-tv.jpg" alt="The TV Wall Sales Simulator on a laptop in an office" loading="lazy"></div><h3>The TV Wall Sales Simulator</h3><span class="role">Sales simulation →</span></a>
    </div>
  </div>
</section>

<section id="contact" class="contact center" aria-labelledby="contact-h">
  <div class="wrap">
    <div class="reveal">{pill("coaching.html", "Featured project", ghost=True)}</div>
    <h2 class="h-xl reveal" id="contact-h" style="margin-top:24px">Let's connect.</h2>
    <p class="lead reveal">I'm open to learning &amp; development and instructional design roles.</p>
    <form class="contact-card glass reveal" id="contact-form" data-email="{e(EMAIL)}">
      <div class="row">
        <label>First name<input name="first" autocomplete="given-name" required></label>
        <label>Last name<input name="last" autocomplete="family-name"></label>
      </div>
      <label>Email<input name="email" type="email" autocomplete="email" required></label>
      <label>Message<textarea name="message" required></textarea></label>
      <button class="pill" type="submit">Submit</button>
    </form>
  </div>
</section>
</main>
"""
home += footer()
write("index.html", home)

# ======================= ABOUT =======================
about = head("About · Tshwjxeeb Vaaj", "Learning designer with a background in chemistry education, program leadership and coaching.")
about += nav("about")
about += f"""<main>
<section class="about-intro">
  <div class="wrap">
    <div>
      <p class="eyebrow reveal">About me</p>
      <h1 class="h-xl reveal d1" style="margin-bottom:22px">I'm Tshwjxeeb Vaaj.</h1>
      <p class="lead reveal d1">Hi, I'm Tshwjxeeb, a learning designer with a background in chemistry education, program leadership and coaching. I hold a degree in chemistry, a master's in chemistry education and a teaching credential in chemistry.</p>
      <p class="pull reveal d2">I help people build skills they can use right away by designing practice that feels like the real moment.</p>
    </div>
    <div class="headshot reveal"><img src="assets/img/headshot.jpg" alt="Portrait of Tshwjxeeb Vaaj"></div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow reveal">My background</p>
    <h2 class="h-lg reveal" style="margin-bottom:28px">From the court to the training room.</h2>
    <div class="two">
      <p class="reveal">As program director and head coach of a boys' volleyball program, I designed learning well beyond the classroom. In the classroom, I taught chemistry curriculum aligned to the Next Generation Science Standards (NGSS) adopted by California. On the court, I taught motor skills, breaking complex movements into steps athletes could practice and master. I worked with learners from kindergarten through high school graduation, and I trained and mentored the coaches on my staff so they could lead on their own with confidence.</p>
      <p class="reveal d1">Instructional design brings both sides of my experience together. I understand how learning works from my time in the classroom and my graduate study, and I've applied Universal Design for Learning (UDL) principles on the court as well as in a lab. That foundation lets me partner with subject matter experts in any field: they bring the expertise, and I bring the strategies and tools that turn it into training people can actually apply. I'm a creative at heart, and I'm excited to build learning that helps teams and organizations perform. Let's connect and explore what we can create together.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow reveal">More about me</p>
    <div class="life">
      <div class="reveal">
        <h2 class="h-md" style="margin-bottom:20px">Life off the clock.</h2>
        {paras("Outside of work, you'll find me deep in an RPG or a cozy game, tinkering with retro handhelds, or building yet another mechanical keyboard.",
               "Volleyball is still part of my life, and I love getting out into nature and traveling whenever I can.",
               "I believe the best learning happens when people feel safe to try, miss, and try again. That guides me professionally as much as it does personally.")}
      </div>
      <!-- TODO: replace with <img src="assets/img/about-main.jpg" alt="..."> -->
      <div class="photo-slot reveal d1" style="min-height:460px">Photo coming soon</div>
    </div>
    <!-- TODO: swap these placeholders for real photos -->
    <div class="trio">
      <div class="photo-slot reveal">Volleyball photo coming soon</div>
      <div class="photo-slot reveal d1">Gaming &amp; keyboards photo coming soon</div>
      <div class="photo-slot reveal d2">Travel or nature photo coming soon</div>
    </div>
  </div>
</section>

<section class="center"><div class="wrap reveal">{pill("index.html#contact", "Let's connect")}</div></section>
</main>
"""
about += footer()
write("about.html", about)

# ======================= COACHING =======================
C = COACHING_URL
c = head("Coaching Through Conflict · Tshwjxeeb Vaaj", "A scenario-based simulation for new head coaches, built from a real 0–10 to semifinal turnaround.")
c += nav("work")
c += "<main class=\"cs\">\n"
c += cs_hero("assets/img/coaching-hero.jpg", "“Control doesn't come from running every rep. It comes from building players who can run it without you.”",
             "— Coach Ramos, Coaching Through Conflict", "Experience the project", C)
c += f"""<section class="cs-intro">
  <div class="wrap split">
    <div class="reveal">
      <h1>Coaching Through Conflict</h1>
      <p class="sub">A scenario-based simulation for new head coaches</p>
      <p>Coaching Through Conflict is a scenario-based training module that teaches new varsity volleyball head coaches to handle the moments that test every coach: a distracted huddle, a disengaged star, a match on the line. Learners choose how to respond and see how each choice affects the team, without real players paying the price.</p>
      {meta_blocks([("Audience", "New varsity volleyball head coaches, assistants stepping into a head role, and the program directors who train them to handle player conflict with confidence."),
                    ("Responsibilities", "Instructional Design, Action Mapping, Text-Based Storyboard, Scriptwriting, Visual Design, AI Image Generation, Figma Prototyping"),
                    ("Tools Used", "Figma, Midjourney, Flora AI (Nano Banana), Gemini, Claude")])}
    </div>
    <div class="visual reveal d1">
      <img src="assets/img/coaching-desk.jpg" alt="A coach at a home desk with the module's title screen on the monitor">
      {pill(C, "Experience the project", external=True)}
    </div>
  </div>
</section>

<section><div class="wrap reveal">
  <h2 class="h-md">The Problem</h2>
  {paras("This isn't a hypothetical. I'm the program director and head coach it's based on. In one year my high school boys' program went from 0–10 and last in our league to 6–3, third place, and the first semifinal appearance in our school's history. The turnaround came from one change in how I coached, and this module turns that change into something other coaches can practice. (The module itself is a concept I'm still testing; the method behind it is proven on the court.)")}
</div></section>

<section><div class="wrap reveal">
  <h2 class="h-md">The Process</h2>
  {paras("I followed the ADDIE model (Analyze, Design, Develop, Implement, and Evaluate). My analysis wasn't a survey; it was my own season. My first year, I had a talented group, many of them just up from JV, but the way I coached held them back: I micromanaged every rep, got angry, and my assistants and I piled pressure on kids who mostly lacked varsity experience. We went 0–10. Then I sat in on a friend's college practice and watched him give his athletes real autonomy, and I rebuilt how I coached around that. The next season we went 6–3 and reached the semifinals. I distilled what changed into three principles (backed by the SBI and GROW frameworks), then designed a storyboard, built a clickable prototype, and refined it.",
         "Each phase stayed anchored to one question: what does a coach need to do in the moment, not just know? I learned the answer the hard way, and the module exists so other coaches don't have to.")}
</div></section>

<section><div class="wrap split">
  <div class="reveal">
    <h2 class="h-md">Action Map</h2>
    {paras("I served as my own subject matter expert, drawing on five years as a head coach and program director and on what I saw sitting in on a friend's college men's volleyball practices. Using Cathy Moore's Action Mapping model, I started with the goal instead of the content: new head coaches handling player conflict in ways that protect both the player and the team's energy. From there, I mapped the on-court behaviors coaches need to do to reach that goal, rather than what they need to know about conflict theory.",
           "Each behavior then broke down into smaller sub-actions. To keep the training focused, I built the scenarios only around the highest-leverage sub-actions, shown in yellow: looking for the cause behind the behavior, using SBI and “I” statements, and asking open questions so players become part of the solution. Learners practice these in every set because they address the root causes behind most player conflict: unclear expectations, misread effort, and frustration with nowhere to go. If new coaches master these, the larger goal is far more likely to follow.")}
    <p>{pill(C, "Experience the project", external=True)}</p>
  </div>
  <div class="visual reveal d1"><img src="assets/img/action-map.png" alt="Action map: the goal branches into three behaviors and their sub-actions, with the highest-leverage actions highlighted in yellow" loading="lazy"></div>
</div></section>

<section><div class="wrap split">
  <div class="reveal">
    <h2 class="h-md">Text-Based Storyboard</h2>
    {paras("Once the action map was set, I wrote a text-based storyboard to plan the whole module, from the visuals and interactions to the exact text on every screen. Every piece was designed to put the learner on the court as the coach, showing consequences through the natural story of a season rather than right-or-wrong pop-ups. Each scenario was built around the core habits from the action map, and the scenarios themselves came from real moments in my own seasons as a head coach: two players laughing in the back of a huddle, a star player whose energy was fading, and a teammate's anger boiling over during a match.",
           "Following Mayer's personalization principle of multimedia learning, the module speaks directly to the learner as “you” and adds a mentor, Coach Ramos, who teaches the three core ideas on a whiteboard before the first scenario. Learners then copy those ideas onto their own clipboard. From that point on, a small “My clipboard” sits in the bottom corner of every decision screen, so the game plan is one click away whenever a choice gets hard, the same way a real coach checks a clipboard on the sideline.")}
  </div>
  <div class="visual reveal d1"><img src="assets/img/storyboard.png" alt="Storyboard tables for the title slide, Introduction A and Set 1 Decision 1" loading="lazy"></div>
</div></section>

<section><div class="wrap split">
  <div class="reveal">
    <h2 class="h-md">Style Guide</h2>
    {paras("Before building the full module, I explored the visual direction in Midjourney, then created an eLearning style guide in Figma so every color, font, button and spacing choice stayed consistent across all 68 screens. The palette pulls navy and gold from the team's jerseys and pads, adds marker colors for Coach Ramos's whiteboard chalk talks, and saves green and red for points won and lost. Every element became a reusable style or component, so one change updates every screen.")}
  </div>
  <div class="visual reveal d1"><img src="assets/img/style-guide.png" alt="Style guide with colors, text styles, buttons, spacing and the clipboard" loading="lazy"></div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Wireframe Progression</h2>
    {paras("Next, I built wireframes and mockups to dial in the layout before adding any visuals. I started with grey boxes to place the story card, the four choices, the scoreboard and the clipboard, then moved to a mid-fidelity version with the real script to check reading length and flow. For the final screens, I set the look and mood in Midjourney, then generated the photorealistic gym scenes in Flora AI with Nano Banana, finished with a warm gold tint and a soft dark fade so the cards stay easy to read.")}
  </div>
  <div class="wide-visual reveal d1"><img src="assets/img/wireframes.png" alt="The same decision screen as a wireframe, a mid-fidelity mockup and the final design" loading="lazy"></div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">AI Image Generation &amp; Character Consistency</h2>
    {paras("From the start, I wanted the module to feel like you were standing in the gym with your own team, so I used AI to build the scenes: Midjourney to explore the style and mood, then Flora AI with Nano Banana, plus Gemini, to generate the images themselves. AI imagery brings its own creative and iterative challenges, so my wireframes worked as loose guides that I adjusted or threw out as the scenes came together. The biggest challenge was consistency: the same players had to appear across three sets, from a practice huddle to a packed match night. I kept the navy-and-gold uniforms, jersey numbers and gym details steady from scene to scene, so learners can follow Austin (#8), Troy (#14) and Eli (#12) from one moment to the next.")}
  </div>
  <div class="wide-visual reveal d1"><img src="assets/img/coaching-ai-grid.jpg" alt="Six AI-generated scenes showing the same players across practice and game night" loading="lazy"></div>
</div></section>

<section><div class="wrap split">
  <div class="reveal">
    <h2 class="h-md">Visual Mockups</h2>
    {paras("To create a consistent design, I started with a clean, neutral wireframe in Figma to test the layout and flow before committing to a style. I then studied how story-driven scenario modules pace their openings, and used what I learned to build a visual identity rooted in the sport itself.",
           "The final style pairs photorealistic gym scenes, styled in Midjourney and generated in Flora AI with Nano Banana, and story cards designed as coach's whiteboards, in navy and gold drawn from the team's pads and jerseys. Headings use a condensed athletic typeface, while the chalk-talk screens use marker fonts and hand-drawn doodles. A scoreboard chip tracks progress, and jersey numbers stand in for player portraits, so the module never needs photos of real student-athletes. I built every color, type style, and button as a reusable style or component, so one change updates every screen.")}
  </div>
  <div class="visual reveal d1">
    <img src="assets/img/coaching-decision.jpg" alt="Decision screen: What do you do? with four choices" loading="lazy">
    <div class="stack-arrow" aria-hidden="true">↓</div>
    <img src="assets/img/coaching-point-lost.jpg" alt="Point lost aftermath screen" loading="lazy">
  </div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Interactive Prototype</h2>
    {paras("I built an interactive prototype in Figma to test the flow and functionality of the module before building out every scenario. The first version included the opening story, Coach Ramos's chalk talk and the first huddle decision, so I could gather feedback and refine the design early.",
           "To support learners the whole way through, I added a mentor and a memory aid. Coach Ramos, a college coach whose players run their own practices, teaches the three core ideas on a whiteboard before the first scenario. Learners then copy those ideas onto their own clipboard. On every decision screen, a small “My clipboard” sits in the corner; selecting it opens the full game plan as an overlay, and “Back to the court” returns the learner to the same moment. Learners can check their notes whenever a choice gets hard without losing their place, the same way a real coach glances at a clipboard on the sideline.")}
  </div>
  <div class="pair">
    <figure class="reveal"><img src="assets/img/coaching-chalk-talk.jpg" alt="Coach Ramos's whiteboard chalk talk" loading="lazy"><figcaption>The mentor: Coach Ramos's chalk talk</figcaption></figure>
    <figure class="reveal d1"><img src="assets/img/coaching-clipboard.jpg" alt="The My game plan clipboard opened over a decision screen" loading="lazy"><figcaption>The clipboard: the game plan opens on any decision</figcaption></figure>
  </div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Full Development</h2>
    {paras("After several rounds of iteration, I developed the full module as a clickable prototype: 68 screens that move from a story-driven opening through three sets of decisions and a closing season wrap-up with Coach Ramos, each wrong choice with its own aftermath, and a success screen for each set. Each round of changes came from walking through the flow as a learner would. For example, I replaced a text-message exchange with a whiteboard chalk talk, so the mentor teaches the principles directly instead of just encouraging the learner.",
           "I also used Figma's prototyping features to make the experience feel responsive. Prototype links handle the branching, so each choice leads to its own consequence and every “Replay the point” button returns learners to the decision. Smart Animate reveals the whiteboard ideas one at a time, a “mental timeout” screen lets learners tap their best guess about what is behind the behavior, and dissolve transitions carry the story from scene to scene. The clipboard opens as an overlay on top of the current screen and closes right back to the same moment, so checking notes never breaks the flow. A prototype variable also remembers the learner's mental-timeout guess, so the follow-up screen shows that guess beside the real cause.")}
  </div>
  <div class="wide-visual reveal d1">{video("assets/video/coaching-walkthrough.mp4", "assets/img/poster-coaching.jpg", "Walkthrough of the Coaching Through Conflict module", "player wide")}</div>
  <p style="margin-top:28px" class="reveal">{pill(C, "Experience the project", external=True)}</p>
</div></section>

<section><div class="wrap reveal">
  <h2 class="h-md">Results</h2>
  {paras("The method is already proven: holding this standard for myself and my assistants is what took my own program from 0–10 to a 6–3 season and our school's first-ever semifinal appearance. The module that teaches it is still a concept, so the next step is to add final artwork and test the full prototype with other high school volleyball coaches.",
         "My biggest takeaway is that the shift had to start with me before it could reach the players: trading control for ownership changed the team only once I changed how I coached. The module is built to pass that lesson on, in the learner's own world of the gym, the whiteboard, and the huddle. These insights will shape how I design future scenario-based training for coaches, teachers, and teams.")}
</div></section>

<section><div class="wrap reveal">
  <h2 class="h-md">Lessons Learned</h2>
  {paras("This was my first training module, and I built it with no formal instructional design training. What made it possible was learning to build alongside AI. Through vibe coding and AI tools, I turned the ideas in my head into working drafts quickly: Claude helped me shape the script and structure, Midjourney helped me find the visual style, and Flora AI with Nano Banana generated the scenes.",
         "The biggest lesson was that I didn't need to know everything before I started. I needed a clear goal, a real story, and a willingness to learn the tools as I built. Each round of feedback from the AI taught me something new about learning design, and I could test those ideas right away. I'm excited to keep growing this skill set as AI keeps expanding what's possible in scenario-based learning.")}
  <p style="margin-top:28px">{pill(C, "Experience the project", external=True)}</p>
</div></section>
"""
c += next_prev(("The TV Wall Sales Simulator", "tv-wall.html"), ("Pip's Number Garden", "pip.html"))
c += "</main>\n" + footer()
write("coaching.html", c)


# ======================= PIP / TV (shared layout) =======================
def simple_case(file, title, sub, desc, meta, quote, by, hero_img, cta, url, problem, solution, dev, vid, poster, vid_label, prev, nxt, page_desc):
    p = head(f"{title} · Tshwjxeeb Vaaj", page_desc) + nav("work") + '<main class="cs">\n'
    p += cs_hero(hero_img, quote, by, cta, url, right=True)
    p += f"""<section class="cs-intro"><div class="wrap reveal">
  <h1>{e(title)}</h1>
  <p class="sub">{e(sub)}</p>
  <p>{e(desc)}</p>
  {meta_blocks(meta, cols=True)}
  {pill(url, cta, external=True)}
</div></section>

<section><div class="wrap two">
  <div class="reveal"><h2 class="h-md">The Problem</h2><p>{e(problem)}</p></div>
  <div class="reveal d1"><h2 class="h-md">The Solution</h2><p>{e(solution)}</p></div>
</div></section>

<section><div class="wrap">
  <div class="reveal"><h2 class="h-md">Full Development</h2>{paras(*dev)}</div>
  <div class="wide-visual reveal d1">{video(vid, poster, vid_label)}</div>
  <p style="margin-top:28px" class="reveal">{pill(url, cta, external=True)}</p>
</div></section>
"""
    p += next_prev(prev, nxt) + "</main>\n" + footer()
    write(file, p)


simple_case("pip.html", "Pip's Number Garden", "A game-based learning garden for 2nd grade math",
    "A cozy, self-paced garden game that helps 2nd graders compare numbers with >, <, and = by reading place value one place at a time. Students compare two numbers in three focused steps: check the biggest place first, decide which number is greater, then pick the sign. Every first-try answer earns a seed, and five seeds grow a new plant in their garden.",
    [("Audience", "2nd grade students practicing number comparison on their own, and the teachers who run small-group place-value lessons."),
     ("Responsibilities", "Instructional Design Tasks (Coaching a student teacher through her small-group place-value lesson, Identifying where students got stuck, Mapping the 2nd grade standard for comparing numbers, Designing place-value visuals and hint feedback, Writing kid-friendly prompts), Game Development, Teacher Feedback Review."),
     ("Tools Used", "Claude AI, HTML, CSS, JavaScript.")],
    "“The open mouth always faces the bigger number.”", "— Pip, Pip's Number Garden",
    "assets/img/tile-pip.jpg", "Play the game", PIP_URL,
    "In a 2nd grade small-group lesson, students could read two- and three-digit numbers but struggled to compare them. They mixed up the places, skipped straight to the ones, or guessed which way the > and < signs should point. One small-group session wasn't enough practice to make the comparison order stick.",
    "I designed a game students can play on their own. Hundreds, tens, and ones each get their own block, color, and label, and students compare one place at a time before choosing the sign. Four levels build from two-digit numbers (Sprout) to three-digit numbers with tricky ties (Sunflower), and getting 4 of 5 right on the first try unlocks the next level.",
    ["I built Pip's Number Garden with Claude AI as a single web page in HTML, CSS, and JavaScript. Pip, a friendly garden guide, gives a short hint after a wrong answer and lets students try again, while seeds are only earned on the first try so the garden reflects real understanding. Sparkles, a hopping Pip, and soft chimes celebrate correct answers, progress saves in the browser, and a For grown-ups page explains the design choices to teachers. My wife, a 2nd grade student teacher, played through the game and gave feedback on it."],
    "assets/video/pip-gameplay.mp4", "assets/img/poster-pip.jpg", "Gameplay of Pip's Number Garden on a phone",
    ("Coaching Through Conflict", "coaching.html"), ("The TV Wall Sales Simulator", "tv-wall.html"),
    "A cozy, self-paced garden game that helps 2nd graders compare numbers using place value.")

simple_case("tv-wall.html", "The TV Wall Sales Simulator", "A practice-first sales simulation for new associates",
    "A practice-first sales simulator that helps new associates sell TVs with confidence using the D.I.S.C. model: Discover, Inspire, Solve, and Close. Associates help five customers on a virtual sales floor. They ask discovery questions to learn about each customer's room and habits, inspire a vision, recommend the right panel, and close the sale. Thirty days later, each customer either keeps the TV or returns it.",
    [("Audience", "New sales associates in the TV department of a big-box electronics store, and the leads who onboard them."),
     ("Responsibilities", "Instructional Design Tasks (Turning my own first weeks on the sales floor into a learning need, Mapping the D.I.S.C. sales model into a practice loop, Writing five customer personas with realistic needs, Designing feedback that shows whether a TV was kept or returned), Simulation Development, Figma Prototyping."),
     ("Tools Used", "HTML, CSS, JavaScript, Figma.")],
    "“Knowledge is only half the battle.”", "— Welcome to the Floor, The TV Wall Sales Simulator",
    "assets/img/tile-tv.jpg", "Play the simulation", TV_URL,
    "When I started as a sales associate at Best Buy, I completed the training modules and learned the details of every TV technology, but I never got to practice selling one. On the sales floor there was too much to sort out in my head: panel types, room conditions, installation, and add-on services. Even though I was comfortable with technology, I struggled to match the right TV to the right customer. A wrong match leads to a return, which costs the store and frustrates a customer who trusted my advice.",
    "I designed a simulator where new associates can practice a full TV sale with no real-world consequences. Each customer brings a different room, viewing habit, and need, and associates work through D.I.S.C. They must ask at least three discovery questions before moving on, and every recommendation is checked 30 days later: kept or returned. The goal is the one the store cares about most: the right TV the first time, fewer returns, and customers who trust their associate.",
    ["I built the TV Wall as a web-based simulation in HTML, CSS, and JavaScript, then rebuilt the core simulator as a clickable Figma prototype with a corporate showroom theme. Five customers each have their own discovery answers and an ideal panel (LED, QLED, Mini-LED, or OLED). Choices carry forward through the conversation, and a final scorecard totals TVs kept and returned. Building and using the simulator made the D.I.S.C. model second nature for me. I asked better questions, saw each customer's full picture, and became more confident explaining installation and services. My TV unit sales, accessory sales, and service sales all grew, and my customers left knowing they had the right TV."],
    "assets/video/tv-wall-walkthrough.mp4", "assets/img/poster-tv.jpg", "Walkthrough of the TV Wall Sales Simulator",
    ("Pip's Number Garden", "pip.html"), ("Coaching Through Conflict", "coaching.html"),
    "A practice-first sales simulator for new TV associates using the D.I.S.C. model.")
