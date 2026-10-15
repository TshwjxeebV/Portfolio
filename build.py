"""Builds the portfolio pages from shared pieces. Run: python3 build.py

Edit the SETTINGS below, then run again to update every page.
"""
import html

# ---------------- SETTINGS (edit me) ----------------
EMAIL = "TshwjxeebKVaaj@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/tshwjxeebvaaj/"
RESUME = "#"                               # TODO: link to your résumé PDF (e.g. assets/resume.pdf)
COACHING_URL = "play/coaching/"
PIP_URL = "play/pip/"
TV_URL = "play/tv-wall/"
SW_URL = "play/scheduling/"
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
      {link("how-i-work.html", "How I work", "how")}
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
    {f'<a href="{e(LINKEDIN)}" target="_blank" rel="noopener">LinkedIn</a>' if LINKEDIN not in ("", "#") else ""}
    {f'<a href="{e(RESUME)}" target="_blank" rel="noopener">Résumé (PDF)</a>' if RESUME not in ("", "#") else ""}
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


def objectives(intro, items, note=""):
    """Measurable learning objectives: (behavior, criterion) pairs."""
    lis = "".join(f'<li><span class="obj-n">{i:02d}</span><div><p class="obj-b">{e(b)}</p><p class="obj-c">{e(c)}</p></div></li>'
                  for i, (b, c) in enumerate(items, 1))
    n = f'<p class="obj-note">{e(note)}</p>' if note else ""
    return f"""<section id="objectives"><div class="wrap reveal">
  <p class="eyebrow">Learning objectives</p>
  <h2 class="h-md">What learners will be able to do</h2>
  <p class="lead">{e(intro)}</p>
  <ol class="objectives">{lis}</ol>
  {n}
</div></section>
"""


def process_strip(steps):
    """ADDIE strip: (phase, what I did, href or None, thumb or None)."""
    cards = []
    for i, (phase, did, href, thumb) in enumerate(steps):
        img = f'<img src="{thumb}" alt="" loading="lazy">' if thumb else ""
        inner = f'{img}<span class="ph">{e(phase)}</span><p>{e(did)}</p>'
        if href:
            inner += f'<span class="see">See it {ARROW}</span>'
            cards.append(f'<a class="step-card{" has-img" if thumb else ""}" href="{href}">{inner}</a>')
        else:
            cards.append(f'<div class="step-card{" has-img" if thumb else ""}">{inner}</div>')
    return f"""<section class="process" aria-labelledby="process-h"><div class="wrap reveal">
  <p class="eyebrow">My process</p>
  <h2 class="h-md" id="process-h">From problem to prototype</h2>
  <div class="steps-row c{len(steps)}">{"".join(cards)}</div>
</div></section>
"""


def evaluation(heading, intro, levels, extra=""):
    """Kirkpatrick-style table: (level, what we look for, how measured, status)."""
    rows = "".join(f'<div class="ev-row"><span class="ev-l">{e(l)}</span><p class="ev-w">{e(w)}</p><p class="ev-h">{e(h)}</p>'
                   f'<span class="tag {"done" if s.lower().startswith(("done", "observed", "built")) else "plan"}">{e(s)}</span></div>'
                   for l, w, h, s in levels)
    return f"""<section id="evaluation"><div class="wrap reveal">
  <h2 class="h-md">{e(heading)}</h2>
  <p>{e(intro)}</p>
  <div class="ev-table" role="table" aria-label="Evaluation plan">
    <div class="ev-row ev-head" role="row"><span>Level</span><span>What I look for</span><span>How it's measured</span><span>Status</span></div>
    {rows}
  </div>
  {extra}
</div></section>
"""


def access(built, nxt):
    """Accessibility & UDL: what's built in, and the next pass."""
    b = "".join(f"<li>{e(x)}</li>" for x in built)
    n = "".join(f"<li>{e(x)}</li>" for x in nxt)
    return f"""<section id="accessibility"><div class="wrap reveal">
  <p class="eyebrow">Accessibility &amp; UDL</p>
  <h2 class="h-md">Designed so more learners can get in</h2>
  <div class="two acc">
    <div><h3 class="h-sm">Built in</h3><ul class="checks">{b}</ul></div>
    <div><h3 class="h-sm">Next accessibility pass</h3><ul class="checks todo">{n}</ul></div>
  </div>
</div></section>
"""


def write(name, content):
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)



# ======================= TESTIMONIALS =======================
# Quotes are word for word from each recommendation. "pull" is an exact excerpt.
TESTIMONIALS = [
    {"name": "Chong Shrock", "role": "Science Department Chair · Mentor teacher", "img": "assets/img/testimonials/chong-shrock.jpg",
     "bold": ["mastery of incorporating technology", "lessons were engaging", "worked cooperatively", "manage his time effectively"],
     "pull": "Because of his enthusiasm for the subject, his lessons were engaging and students enjoyed his lessons.",
     "full": ["…When Mr. Vaaj took responsibility for planning and implementing lesson in chemistry, he demonstrated mastery of incorporating technology in many of his lessons. He used a variety of applications to deliver his agenda, standards, lessons, and assessments. Because of his enthusiasm for the subject, his lessons were engaging and students enjoyed his lessons. The student’s also showed understanding in the content and standards through their grades on quizzes, labs, exit tickets, and tests.",
              "Mr. Vaaj displayed many personal and professional qualities to become an outstanding teacher. He was very responsible and dependable taking his responsibilities as a teacher seriously. He worked cooperatively with me as his mentor teacher but also engaged with other teachers and professionals at our school to observe and ask advise. Even with his busy schedule coaching volleyball, he attended both school, department, chemistry team, and district meetings with me whenever he could to get the overall experience of a teacher. His ability to manage his time effectively as a student teacher and coach shows his dedication to the profession."]},
    {"name": "John Harney", "role": "Athletics Director", "img": "assets/img/testimonials/john-harney.jpg",
     "bold": ["helped grow the boys' volleyball program significantly", "more than 20 student-athletes", "communicates effectively with athletes, parents, referees, and administrators", "calm presence and ability to manage challenging situations"],
     "pull": "His calm presence and ability to manage challenging situations make him a respected mentor and role model for students.",
     "full": ["Coach Vaaj has demonstrated a strong commitment to our athletic program and to the athletes he serves. Through his leadership and dedication, he has helped grow the boys' volleyball program significantly. One of his most notable accomplishments has been the development of a successful JVR developmental program that consistently attracts more than 20 student-athletes, creating opportunities for growth and participation at multiple levels.",
              "Beyond his success in building the program, Coach Vaaj has an exceptional ability to connect with students. He maintains a positive and professional demeanor, communicates effectively with athletes, parents, referees, and administrators, and consistently models strong character and leadership. His calm presence and ability to manage challenging situations make him a respected mentor and role model for students."]},
    {"name": "Joe Schnake", "role": "Head Coach, La Sierra Men's Volleyball", "img": "assets/img/testimonials/joe-schnake.jpg",
     "bold": ["exceptional quick learner", "adapt to new situations and challenges", "work within a team environment", "strong ability to communicate"],
     "pull": "He is an exceptional quick learner and has a keen ability to adapt to new situations and challenges.",
     "full": ["Vaaj has consistently demonstrated a strong work ethic and a high level of commitment to his academic and professional pursuits. He is an exceptional quick learner and has a keen ability to adapt to new situations and challenges. Apart from his academic and professional skills, Vaaj possesses excellent interpersonal skills and can work within a team environment and excel. He is a born natural leader and will inspire and motivate others to give their very best. Another great trait is Vaaj’s superb positive attitude and strong ability to communicate which is instrumental in every situation that he encounters."]},
]


def _bolded(t):
    out = []
    for para in t["full"]:
        h = e(para)
        for phrase in t.get("bold", []):
            ph = e(phrase)
            if ph in h:
                h = h.replace(ph, f"<strong>{ph}</strong>", 1)
        out.append(f"<p>{h}</p>")
    return "\n".join(out)


def testimonials():
    cards = []
    for t in TESTIMONIALS:
        cards.append(f"""<figure class="t-card" role="group" aria-label="{e(t['name'])}">
          <img class="t-photo" src="{t['img']}" alt="Portrait of {e(t['name'])}" loading="lazy" width="240" height="240">
          <blockquote>{_bolded(t)}</blockquote>
          <figcaption><strong>{e(t['name'])}</strong><span>{e(t['role'])}</span></figcaption>
        </figure>""")
    return f"""<section id="testimonials" class="testimonials" aria-labelledby="testimonials-h">
  <div class="wrap">
    <p class="eyebrow reveal">Testimonials</p>
    <h2 class="h-lg reveal" id="testimonials-h">What people are saying.</h2>
    <div class="t-carousel reveal">
      <button class="t-arrow prev" type="button" aria-label="Previous testimonial" aria-controls="t-track">{ARROW}</button>
      <div class="t-track" id="t-track" tabindex="0" aria-label="Testimonials, scroll for more">
        {"".join(cards)}
      </div>
      <button class="t-arrow next" type="button" aria-label="Next testimonial" aria-controls="t-track">{ARROW}</button>
    </div>
  </div>
</section>
"""


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
      <div class="hero-btns reveal d2">{pill("coaching.html", "Featured project")}{pill("how-i-work.html", "How I work", ghost=True)}</div>
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
    <h2 class="h-lg reveal" id="work-h">Four projects, four kinds of learners.</h2>
    <div class="tiles c4">
      <a class="tile reveal" href="coaching.html"><div class="shot"><img src="assets/img/tile-coaching.jpg" alt="Coaching Through Conflict on a laptop at home" loading="lazy"></div><h3>Coaching Through Conflict</h3><span class="role">Scenario-based training →</span></a>
      <a class="tile reveal d1" href="pip.html"><div class="shot"><img src="assets/img/tile-pip.jpg" alt="Pip's Number Garden on a phone on a wooden table" loading="lazy"></div><h3>Pip's Number Garden</h3><span class="role">Game-based learning →</span></a>
      <a class="tile reveal d2" href="tv-wall.html"><div class="shot"><img src="assets/img/tile-tv.jpg" alt="The TV Wall Sales Simulator on a laptop in an office" loading="lazy"></div><h3>The TV Wall Sales Simulator</h3><span class="role">Sales simulation →</span></a>
      <a class="tile reveal d2" href="software-training.html"><div class="shot"><img src="assets/img/tile-software.jpg" alt="A software-training screen from the Schedule a Patient Follow-Up module" loading="lazy"></div><h3>Schedule a Patient Follow-Up</h3><span class="role">Software training →</span></a>
    </div>
  </div>
</section>

<section aria-labelledby="fit-h">
  <div class="wrap">
    <p class="eyebrow reveal">Who I build for</p>
    <h2 class="h-lg reveal" id="fit-h">Find the work that fits your team.</h2>
    <div class="fit">
      <div class="fit-card glass reveal"><h3>K-12 &amp; EdTech</h3><p>Standards-aligned practice for young learners, from a chemistry teacher with an NGSS classroom background.</p><a href="pip.html">Pip's Number Garden {ARROW}</a></div>
      <div class="fit-card glass reveal d1"><h3>Corporate L&amp;D &amp; enablement</h3><p>Sales practice and software training that measure what the business cares about: kept sales and correct bookings.</p><a href="tv-wall.html">The TV Wall Sales Simulator {ARROW}</a><a href="software-training.html">Schedule a Patient Follow-Up {ARROW}</a></div>
      <div class="fit-card glass reveal d2"><h3>Leadership &amp; people development</h3><p>Branching scenarios for leaders who have to handle the hard conversation in the moment.</p><a href="coaching.html">Coaching Through Conflict {ARROW}</a></div>
    </div>
  </div>
</section>

{testimonials()}
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
# Photos appear automatically once these files exist in assets/img/.
import os
def _photo(path, alt, cls="reveal d1"):
    return f'<img class="about-photo {cls}" src="{path}" alt="{e(alt)}" loading="lazy">' if os.path.exists(path) else ""
ABOUT_MAIN = _photo("assets/img/about-main.jpg", "Tshwjxeeb Vaaj outside of work")
_trio = [_photo("assets/img/about-volleyball.jpg", "Volleyball", "reveal"), _photo("assets/img/about-hobbies.jpg", "Gaming and mechanical keyboards"), _photo("assets/img/about-travel.jpg", "Travel and nature", "reveal d2")]
ABOUT_TRIO = f'<div class="trio">{"".join(_trio)}</div>' if any(_trio) else ""
about = head("About · Tshwjxeeb Vaaj", "Learning designer with a background in chemistry education, program leadership and coaching.")
about += nav("about")
about += f"""<main>
<section class="about-intro">
  <div class="wrap">
    <div>
      <p class="eyebrow reveal">About me</p>
      <h1 class="h-xl reveal d1" style="margin-bottom:22px">I'm Tshwjxeeb Vaaj.</h1>
      <p class="lead reveal d1">Hi, I'm Tshwjxeeb, a learning designer with five years of designing and leading training as a program director and head coach, and a background in chemistry education. I hold a degree in chemistry, a master's in chemistry education and a teaching credential in chemistry.</p>
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

<section aria-labelledby="xp-h">
  <div class="wrap">
    <p class="eyebrow reveal">Experience at a glance</p>
    <h2 class="h-lg reveal" id="xp-h" style="margin-bottom:28px">Where I've designed learning.</h2>
    <div class="xp">
      <div class="xp-row reveal"><div><h3>Learning Designer</h3><span class="role">Portfolio projects · about 1 year</span></div>
        <ul><li>Designed and built four learning experiences end to end: a 68-screen branching simulation, a sales simulator, a game-based math module and a software-training module.</li>
        <li>Ran each one from analysis through action mapping, storyboards, style guides, prototyping and an evaluation plan.</li>
        <li>Work in Figma, Articulate Storyline 360, HTML/CSS/JavaScript and AI tools (Claude, Midjourney, Flora AI).</li></ul></div>
      <div class="xp-row reveal"><div><h3>Program Director &amp; Head Coach</h3><span class="role">High school boys' volleyball · 5 years</span></div>
        <ul><li>Designed the program's coaching materials and practice plans, breaking complex motor skills into steps athletes could practice and master.</li>
        <li>Trained and mentored the coaches on my staff so they could lead on their own with confidence.</li>
        <li>Led the program from 0–10 and last in the league to 6–3 and the school's first-ever semifinal.</li></ul></div>
      <div class="xp-row reveal"><div><h3>Chemistry Teacher</h3><span class="role">Credentialed in chemistry</span></div>
        <ul><li>Taught chemistry curriculum aligned to the Next Generation Science Standards (NGSS).</li>
        <li>Applied Universal Design for Learning (UDL) to give every student more than one way in.</li></ul></div>
      <div class="xp-row reveal"><div><h3>Sales Associate</h3><span class="role">Best Buy</span></div>
        <ul><li>Turned my own onboarding gap into the TV Wall Sales Simulator, and grew my TV unit, accessory and service sales.</li></ul></div>
      <div class="xp-row reveal"><div><h3>Education</h3><span class="role">Chemistry &amp; education</span></div>
        <ul><li>Degree in chemistry · Master's in chemistry education · Teaching credential in chemistry</li></ul></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow reveal">More about me</p>
    <div class="life{'' if ABOUT_MAIN else ' solo'}">
      <div class="reveal">
        <h2 class="h-md" style="margin-bottom:20px">Life off the clock.</h2>
        {paras("Outside of work, you'll find me deep in an RPG or a cozy game, tinkering with retro handhelds, or building yet another mechanical keyboard.",
               "Volleyball is still part of my life, and I love getting out into nature and traveling whenever I can.",
               "I believe the best learning happens when people feel safe to try, miss, and try again. That guides me professionally as much as it does personally.")}
      </div>
      {ABOUT_MAIN}
    </div>
    {ABOUT_TRIO}
  </div>
</section>

<section class="center"><div class="wrap reveal">{pill("index.html#contact", "Let's connect")}</div></section>
</main>
"""
about += footer()
write("about.html", about)

# ======================= COACHING =======================
C = COACHING_URL
COACH_PROCESS = process_strip([
    ("Analyze", "Used my own 0–10 season as the needs analysis, then action-mapped the goal down to on-court behaviors.", "#action-map", "assets/img/action-map.png"),
    ("Design", "Wrote a text-based storyboard for every screen and built a style guide so all 68 screens stay consistent.", "#storyboard", "assets/img/storyboard.png"),
    ("Develop", "Went from grey-box wireframes to a 68-screen branching prototype in Figma, then started the build in Articulate Storyline 360.", "#wireframes", "assets/img/wireframes.png"),
    ("Evaluate", "Planned a pilot with other high school volleyball coaches, measured at all four Kirkpatrick levels.", "#evaluation", "assets/img/coaching-decision.jpg"),
])
COACH_OBJ = objectives(
    "Given a player-conflict moment in practice or a match (a distracted huddle, a disengaged star, a teammate's frustration boiling over), a new head coach will:",
    [("Pause and name a likely cause behind the behavior before reacting.",
      "Measured by: the learner's mental-timeout guess, shown beside the real cause on the next screen."),
     ("Address the player with an SBI (Situation–Behavior–Impact) and “I” statement instead of a public correction.",
      "Measured by: choosing the SBI-based response at each decision point."),
     ("Ask an open question that makes the player part of the solution.",
      "Mastery: reaching the success screen in all three sets.")],
    "Each objective comes straight from a highlighted sub-action on the action map.")
COACH_ACCESS = access(
    ["Feedback never relies on color alone: every outcome carries a written label like “Point lost” and a plain explanation of why.",
     "Story text sits on solid, light cards over the photos, so it stays readable against busy gym scenes.",
     "The “My clipboard” memory aid keeps the three core ideas one click away on every decision, which lowers the load on working memory.",
     "Multiple means of representation (UDL): the ideas are taught on a whiteboard, written onto the clipboard, then practiced in scenes.",
     "“Replay the point” lets learners retry any decision without restarting, so mistakes become practice."],
    ["Check every card and button against WCAG 2.2 AA contrast (4.5:1 for body text).",
     "Add alt text and screen-reader descriptions for each scene in the final build.",
     "Finish the Storyline 360 build with full keyboard navigation and a logical focus order (Figma prototypes are mouse-first).",
     "Offer narrated chalk talks with captions as an option."])
COACH_EVAL = evaluation(
    "Evaluation plan",
    "The method is proven on my own team. The module is the next test, so I've planned how I'll measure it with a pilot group of high school volleyball coaches, using Kirkpatrick's four levels.",
    [("1 · Reaction", "Coaches find the scenarios realistic and useful.", "Short survey after the module: realism, relevance and confidence (1–5).", "Planned"),
     ("2 · Learning", "Coaches spot the cause and pick the SBI and open-question responses.", "First-try choices at each decision; mental-timeout guess vs. the real cause.", "Built into the prototype"),
     ("3 · Behavior", "Coaches use the habits at real practices.", "Two-week self-check against the clipboard habits, plus an assistant coach's observation.", "Planned"),
     ("4 · Results", "Calmer huddles and players who own the fix.", "Program director check-in at season's end, compared with my own 0–10 → 6–3 baseline.", "Observed on my team")])
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
                    ("Responsibilities", "Instructional Design, Action Mapping, Text-Based Storyboard, Scriptwriting, Visual Design, AI Image Generation, Figma Prototyping, Storyline Development"),
                    ("Tools Used", "Figma, Articulate Storyline 360, Midjourney, Flora AI (Nano Banana), Gemini, Claude")])}
    </div>
    <div class="visual reveal d1">
      <img src="assets/img/coaching-desk.jpg" alt="A coach at a home desk with the module's title screen on the monitor">
      {pill(C, "Experience the project", external=True)}
    </div>
  </div>
</section>

{COACH_PROCESS}
<section><div class="wrap reveal">
  <h2 class="h-md">The Problem</h2>
  {paras("This isn't a hypothetical. I'm the program director and head coach it's based on. In one year my high school boys' program went from 0–10 and last in our league to 6–3, third place, and the first semifinal appearance in our school's history. The turnaround came from one change in how I coached, and this module turns that change into something other coaches can practice. (The module itself is a concept I'm still testing; the method behind it is proven on the court.)")}
</div></section>

{COACH_OBJ}
<section><div class="wrap reveal">
  <h2 class="h-md">The Process</h2>
  {paras("I followed the ADDIE model (Analyze, Design, Develop, Implement, and Evaluate). My analysis wasn't a survey; it was my own season. My first year, I had a talented group, many of them just up from JV, but the way I coached held them back: I micromanaged every rep, got angry, and my assistants and I piled pressure on kids who mostly lacked varsity experience. We went 0–10. Then I sat in on a friend's college practice and watched him give his athletes real autonomy, and I rebuilt how I coached around that. The next season we went 6–3 and reached the semifinals. I distilled what changed into three principles (backed by the SBI and GROW frameworks), then designed a storyboard, built a clickable prototype, and refined it.",
         "Each phase stayed anchored to one question: what does a coach need to do in the moment, not just know? I learned the answer the hard way, and the module exists so other coaches don't have to.")}
</div></section>

<section id="action-map"><div class="wrap split">
  <div class="reveal">
    <h2 class="h-md">Action Map</h2>
    {paras("I served as my own subject matter expert, drawing on five years as a head coach and program director and on what I saw sitting in on a friend's college men's volleyball practices. Using Cathy Moore's Action Mapping model, I started with the goal instead of the content: new head coaches handling player conflict in ways that protect both the player and the team's energy. From there, I mapped the on-court behaviors coaches need to do to reach that goal, rather than what they need to know about conflict theory.",
           "Each behavior then broke down into smaller sub-actions. To keep the training focused, I built the scenarios only around the highest-leverage sub-actions, shown in yellow: looking for the cause behind the behavior, using SBI and “I” statements, and asking open questions so players become part of the solution. Learners practice these in every set because they address the root causes behind most player conflict: unclear expectations, misread effort, and frustration with nowhere to go. If new coaches master these, the larger goal is far more likely to follow.")}
    <p>{pill(C, "Experience the project", external=True)}</p>
  </div>
  <div class="visual reveal d1"><img src="assets/img/action-map.png" alt="Action map: the goal branches into three behaviors and their sub-actions, with the highest-leverage actions highlighted in yellow" loading="lazy"></div>
</div></section>

<section id="storyboard"><div class="wrap split">
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

<section id="wireframes"><div class="wrap">
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

<section id="development"><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Full Development</h2>
    {paras("After several rounds of iteration, I developed the full module as a clickable prototype: 68 screens that move from a story-driven opening through three sets of decisions and a closing season wrap-up with Coach Ramos, each wrong choice with its own aftermath, and a success screen for each set. Each round of changes came from walking through the flow as a learner would. For example, I replaced a text-message exchange with a whiteboard chalk talk, so the mentor teaches the principles directly instead of just encouraging the learner.",
           "I also used Figma's prototyping features to make the experience feel responsive. Prototype links handle the branching, so each choice leads to its own consequence and every “Replay the point” button returns learners to the decision. Smart Animate reveals the whiteboard ideas one at a time, a “mental timeout” screen lets learners tap their best guess about what is behind the behavior, and dissolve transitions carry the story from scene to scene. The clipboard opens as an overlay on top of the current screen and closes right back to the same moment, so checking notes never breaks the flow. A prototype variable also remembers the learner's mental-timeout guess, so the follow-up screen shows that guess beside the real cause.",
           "Once the Figma prototype was final, I rebuilt the module as a web page in HTML, CSS and JavaScript, using the same script, images and branching, so anyone can play it in a browser on a computer or a phone.",
           "I've also started rebuilding the module in Articulate Storyline 360, the authoring tool many L&D teams use. So far I've built the opening story and Coach Ramos's chalk talk in Storyline, using the same script, scene images and style guide. Next, I'll build the three sets of decisions with their aftermaths and Replay the point branching, so the finished module can be published for an LMS.")}
  </div>
  <div class="wide-visual reveal d1">{video("assets/video/coaching-walkthrough.mp4", "assets/img/poster-coaching.jpg", "Walkthrough of the Coaching Through Conflict module", "player wide")}</div>
  <p style="margin-top:28px" class="reveal">{pill(C, "Experience the project", external=True)}</p>
</div></section>

{COACH_ACCESS}
<section id="results"><div class="wrap reveal">
  <h2 class="h-md">Results</h2>
  {paras("The method is already proven: holding this standard for myself and my assistants is what took my own program from 0–10 to a 6–3 season and our school's first-ever semifinal appearance. The module that teaches it is still a concept, so the next steps are to finish the Storyline 360 build and test the full module with other high school volleyball coaches.",
         "My biggest takeaway is that the shift had to start with me before it could reach the players: trading control for ownership changed the team only once I changed how I coached. The module is built to pass that lesson on, in the learner's own world of the gym, the whiteboard, and the huddle. These insights will shape how I design future scenario-based training for coaches, teachers, and teams.")}
</div></section>

{COACH_EVAL}
<section><div class="wrap reveal">
  <h2 class="h-md">Lessons Learned</h2>
  {paras("This was my first training module, and I built it with no formal instructional design training. What made it possible was learning to build alongside AI. Through vibe coding and AI tools, I turned the ideas in my head into working drafts quickly: Claude helped me shape the script and structure, Midjourney helped me find the visual style, and Flora AI with Nano Banana generated the scenes.",
         "The biggest lesson was that I didn't need to know everything before I started. I needed a clear goal, a real story, and a willingness to learn the tools as I built. Each round of feedback from the AI taught me something new about learning design, and I could test those ideas right away. I'm excited to keep growing this skill set as AI keeps expanding what's possible in scenario-based learning.")}
  <p style="margin-top:28px">{pill(C, "Experience the project", external=True)}</p>
</div></section>
"""
c += next_prev(("Schedule a Patient Follow-Up", "software-training.html"), ("Pip's Number Garden", "pip.html"))
c += "</main>\n" + footer()
write("coaching.html", c)


# ======================= PIP / TV (shared layout) =======================
def simple_case(file, title, sub, desc, meta, quote, by, hero_img, cta, url, problem, solution, dev, vid, poster, vid_label, prev, nxt, page_desc, extras):
    p = head(f"{title} · Tshwjxeeb Vaaj", page_desc) + nav("work") + '<main class="cs">\n'
    p += cs_hero(hero_img, quote, by, cta, url, right=True)
    p += f"""<section class="cs-intro"><div class="wrap reveal">
  <h1>{e(title)}</h1>
  <p class="sub">{e(sub)}</p>
  <p>{e(desc)}</p>
  {meta_blocks(meta, cols=True)}
  {pill(url, cta, external=True)}
</div></section>
{extras["process"]}
<section><div class="wrap two">
  <div class="reveal"><h2 class="h-md">The Problem</h2><p>{e(problem)}</p></div>
  <div class="reveal d1"><h2 class="h-md">The Solution</h2><p>{e(solution)}</p></div>
</div></section>
{extras["objectives"]}
<section id="development"><div class="wrap">
  <div class="reveal"><h2 class="h-md">Full Development</h2>{paras(*dev)}</div>
  <div class="wide-visual reveal d1">{video(vid, poster, vid_label)}</div>
  <p style="margin-top:28px" class="reveal">{pill(url, cta, external=True)}</p>
</div></section>
{extras["access"]}
{extras["evaluation"]}
"""
    p += next_prev(prev, nxt) + "</main>\n" + footer()
    write(file, p)


PIP_EXTRAS = {
    "process": process_strip([
        ("Analyze", "Coached a student teacher through a small-group place-value lesson and saw where students got stuck: mixing up places and guessing which way the sign points.", None, None),
        ("Design", "Mapped the 2nd grade comparison standard (2.NBT.A.4) to a three-step routine, with a color, block and label for each place.", "#objectives", None),
        ("Develop", "Built a single-page game with Claude AI in HTML, CSS and JavaScript: four levels, hint feedback and a For grown-ups page.", "#development", None),
        ("Evaluate", "A 2nd grade student teacher played it and gave feedback, and first-try accuracy gates every level.", "#evaluation", None),
    ]),
    "objectives": objectives(
        "Given two 2- or 3-digit numbers, a 2nd grade student will:",
        [("Compare the numbers starting from the greatest place: hundreds, then tens, then ones.",
          "Practiced as step one of every round: check the biggest place first."),
         ("Decide which number is greater, or whether the two are equal.",
          "Practiced as step two, with a hint from Pip after a wrong answer."),
         ("Choose the correct sign: >, < or =.",
          "Mastery: 4 of 5 correct on the first try unlocks the next level, from Sprout to Sunflower.")],
        "Aligned to Common Core 2.NBT.A.4, part of California's math standards."),
    "access": access(
        ["Place value never relies on color alone: hundreds, tens and ones each get their own block, color and written label.",
         "A hint after every wrong answer, then another try, so mistakes turn into practice instead of a dead end.",
         "Short, kid-friendly prompts and a friendly guide keep the reading load low for young readers.",
         "Self-paced levels that unlock on mastery, not on time.",
         "A For grown-ups page explains the design, so teachers can use the game in their own small groups."],
        ["Add a read-aloud option for prompts, for early and emerging readers.",
         "Check every color pair against WCAG 2.2 AA contrast.",
         "Support full keyboard play and screen-reader labels for the number blocks.",
         "Add a switch to turn off sounds and sparkles for students who are sensitive to them."]),
    # TODO(Tshwjxeeb): add one line on what your wife flagged in the playtest and what you changed because of it.
    "evaluation": evaluation(
        "Testing & evaluation",
        "The game already collects the most honest learning signal for 2nd graders: whether they get it right on the first try. Seeds are only earned on a first-try answer, so the garden itself is the progress report.",
        [("1 · Reaction", "Students want to keep playing.", "Teacher notes on engagement during independent practice.", "Planned"),
         ("2 · Learning", "Students compare by place value, not by guessing.", "First-try accuracy on each level; 4 of 5 unlocks the next.", "Built into the game"),
         ("3 · Behavior", "Students use the place-by-place routine in class.", "A short paper comparison task in small group.", "Planned"),
         ("4 · Results", "Fewer place-value mix-ups across the class.", "Exit tickets on comparing three-digit numbers, before and after.", "Planned")],
        '<p class="ev-extra"><strong>Playtest.</strong> My wife, a 2nd grade student teacher, played through the game and gave feedback on it from a classroom point of view.</p>'),
}

TV_EXTRAS = {
    "process": process_strip([
        ("Analyze", "Turned my own first weeks on the Best Buy sales floor into a learning need: knowing the tech wasn't the same as matching a TV to a customer.", None, None),
        ("Design", "Mapped D.I.S.C. into a practice loop and wrote five customer personas, each with their own room, habits and ideal panel.", "#objectives", None),
        ("Develop", "Built it in HTML, CSS and JavaScript, then rebuilt the core loop as a clickable Figma prototype.", "#development", None),
        ("Evaluate", "Every recommendation is checked 30 days later: kept or returned. Then I tracked my own sales.", "#evaluation", None),
    ]),
    "objectives": objectives(
        "Given a customer on the sales floor, a new TV associate will:",
        [("Ask at least three discovery questions about the customer's room and viewing habits before recommending a TV.",
          "Built into the simulator: associates can't move on until they've asked three."),
         ("Recommend the panel type (LED, QLED, Mini-LED or OLED) that fits the customer's room and habits.",
          "Mastery target: at least 4 of 5 customers keep their TV at the 30-day check."),
         ("Explain installation and add-on services in terms of what the customer shared in discovery.",
          "Measured by: the choices made in the Solve and Close steps.")]),
    "access": access(
        ["Every customer answer and every choice is written on screen, so nothing depends on audio.",
         "Low-stakes practice: associates can make a wrong match and see the 30-day return without a real customer paying for it.",
         "A required discovery step builds the habit of asking before telling.",
         "Five personas with different rooms and habits give varied examples of the same skill (UDL: multiple means of representation)."],
        ["Check every color pair against WCAG 2.2 AA contrast.",
         "Add full keyboard navigation and visible focus states to the HTML version.",
         "Add screen-reader labels to the TV wall and customer cards.",
         "Add a plain-language glossary for panel types and room terms."]),
    "evaluation": evaluation(
        "Results & evaluation",
        "The simulator already measures what the store cares about most: whether the TV stays sold. Here's how I'd evaluate it with a real onboarding class, using Kirkpatrick's four levels.",
        [("1 · Reaction", "Associates feel ready for their first sale.", "Confidence rating before and after (1–5).", "Planned"),
         ("2 · Learning", "Associates match the right panel to each customer.", "Kept vs. returned on the final scorecard.", "Built into the simulator"),
         ("3 · Behavior", "Associates run D.I.S.C. on the real floor.", "A lead observes one live sale with a D.I.S.C. checklist.", "Planned"),
         ("4 · Results", "Fewer returns and more attached services.", "Return rate and service attach rate vs. the previous new-hire class.", "Planned")],
        '<p class="ev-extra"><strong>What I saw myself.</strong> After building and practicing with the simulator, my TV unit sales, accessory sales and service sales all grew.</p>'),
}

simple_case("pip.html","Pip's Number Garden", "A game-based learning garden for 2nd grade math",
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
    "A cozy, self-paced garden game that helps 2nd graders compare numbers using place value.", PIP_EXTRAS)

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
    ("Pip's Number Garden", "pip.html"), ("Schedule a Patient Follow-Up", "software-training.html"),
    "A practice-first sales simulator for new TV associates using the D.I.S.C. model.", TV_EXTRAS)


# ======================= SOFTWARE TRAINING =======================
S = SW_URL
sw = head("Schedule a Patient Follow-Up · Tshwjxeeb Vaaj",
          "A show me, try me, test me software-training module for new front-desk staff, built in Figma.")
sw += nav("work") + '<main class="cs">\n'
sw += cs_hero("assets/img/tile-software.jpg", "“Check the provider before you pick a time.”",
              "— The one habit this module is built around", "Try the prototype", S, right=True)


def fig(src, alt, cap):
    return f'<figure class="reveal"><img src="{src}" alt="{e(alt)}" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>'


sw += f"""<section class="cs-intro"><div class="wrap reveal">
  <h1>Schedule a Patient Follow-Up</h1>
  <p class="sub">A software-training module for new front-desk staff</p>
  <p>A short, practice-first module that teaches new front-desk staff to book a follow-up visit in a clinic scheduling system. Learners watch the task once with callouts, then do it themselves from a blank patient search, working around a pre-filled wrong provider and a patient who can only come in mornings. Two workplace questions and a one-page job aid close it out.</p>
  {meta_blocks([("Audience", "New front-desk and scheduling staff at an outpatient clinic, and the supervisors who onboard them."),
                ("Responsibilities", "Instructional Design, Learning Objectives, Scenario Writing, Show me / Try me / Test me Structure, Feedback Design, UI Mockups, Figma Component Library, Branching Prototype, Job Aid"),
                ("Tools Used", "Figma, Claude")], cols=True)}
  <p class="cs-note">Brightwell Clinic, the ScheduleDesk app, and every patient and provider in this module are fictional. It's a portfolio concept built to show how I design software training.</p>
  {pill(S, "Try the prototype", external=True)}
</div></section>
"""
sw += process_strip([
    ("Analyze", "Picked a task where a small slip has a real cost: booking the wrong patient or the wrong provider.", "#objectives", None),
    ("Design", "Wrote three objectives, a Show me / Try me / Test me flow, and feedback for every wrong path.", "#flow", None),
    ("Develop", "Built a reusable component library in Figma, then 29 screens with branching prototype links.", "#flow", None),
    ("Evaluate", "First-try data from Try me and Test me, a readiness check, and a supervisor audit plan.", "#evaluation", None),
])
sw += """<section><div class="wrap two">
  <div class="reveal"><h2 class="h-md">The Problem</h2><p>Software training often stops at “click here, then here.” New staff watch a demo, then meet the real system and miss the one detail that matters. In scheduling, that detail is usually the patient or the provider. Two patients share a last name, or the scheduler quietly fills in the last provider someone booked for. Either slip means a missed follow-up and a second phone call to fix it.</p></div>
  <div class="reveal d1"><h2 class="h-md">The Solution</h2><p>I built the module around the mistakes, not the menus. Show me walks through the task once with numbered callouts on the real screen. Try me hands the learner the same task with no callouts, and the scheduler opens with the wrong provider already selected, just like the real thing might. Test me checks the two habits in new situations, with feedback on every answer. The job aid sums it up in five steps to keep at the desk.</p></div>
</div></section>
"""
sw += objectives(
    "Given a provider's follow-up note, a new front-desk staff member will:",
    [("Find the right patient using two identifiers: name and date of birth.",
      "Measured by: the record they open in Try me, plus Test me question 1."),
     ("Book the follow-up with the right provider and date window from the provider's note, at a time the patient can make.",
      "Mastery: in Try me, find Maria, switch to Dr. Patel, and book the only open slot before 10:00 AM that week."),
     ("Read back the five booking details and send a reminder before finishing.",
      "Practiced in Show me step 4 and kept on the job aid.")],
    "Each objective maps to a screen in the module and a step on the job aid.")
sw += f"""<section id="flow"><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Show me</h2>
    <p>Four guided steps on a realistic app screen. Each step gets an amber focus ring with a number, a matching callout in a coaching column, and one short tip on why the step matters. The learner sees the whole task once before they're asked to do it.</p>
  </div>
  <div class="pair">
    {fig("assets/img/sw-showme-1.jpg", "Show me step 1: the matching patient row is ringed and a callout explains matching two identifiers", "Step 1: match two identifiers")}
    {fig("assets/img/sw-showme-3.jpg", "Show me step 3: the provider field and a time slot are ringed with a callout about checking the provider first", "Step 3: provider first, then time")}
  </div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Try me, the way the real job works</h2>
    <p>Try me starts on an empty Patients screen, and scheduling stays locked until the learner finds the patient. They really type: the search fields take keyboard input, so learners enter the last name and the date of birth themselves, then select Search or press Enter. A misspelled name or a wrong birthday gets its own feedback. A name-only search returns three look-alike records, and opening the wrong one brings up a reminder to check the date of birth.</p>
    <p>Then come two realistic constraints. The scheduler opens with Dr. Michael Chen already in the Provider field, carried over from the last booking, so learners have to open the dropdown and switch to Dr. Patel. And Maria can only come in before 10:00 AM. Dr. Patel's week is mostly booked, so learners have to scan every day to find the one open morning slot, Friday at 9:40. A 10:00 slot is there as a near miss. Every wrong choice gets specific feedback and a way forward.</p>
  </div>
  <div class="trio-figs">
    {fig("assets/img/sw-tryme-search.jpg", "Try me patient search showing three similar Lopez records after a name-only search", "Find the patient first")}
    {fig("assets/img/sw-tryme-wrong.jpg", "Try me feedback when the learner books with the wrong provider", "Wrong provider: specific, corrective feedback")}
    {fig("assets/img/sw-tryme-right.jpg", "Try me success with Friday 9:40 AM selected, the only open morning slot", "The only open slot before 10:00 AM")}
  </div>
</div></section>

<section><div class="wrap">
  <div class="reveal">
    <h2 class="h-md">Test me &amp; job aid</h2>
    <p>Two scenario questions move the habits into new situations: a phone call from a different Lopez, and a scheduler that opens on the wrong provider. The answer review explains every option, not just the right one. The module ends with a one-question readiness check and a five-step job aid that matches the order of the task.</p>
  </div>
  <div class="pair">
    {fig("assets/img/sw-testme-review.jpg", "Test me answer review with the correct option highlighted and feedback for every option", "Feedback for every option")}
    {fig("assets/img/sw-jobaid.jpg", "Wrap-up screen with objectives recap, readiness check and five-step job aid", "Wrap-up, readiness check and job aid")}
  </div>
</div></section>

<section><div class="wrap reveal">
  <h2 class="h-md">Full Development</h2>
  <p>I built the module in Figma, starting with a small component library: a module header that tracks Show me, Try me and Test me, numbered callouts, an amber focus ring, buttons, answer options with correct and incorrect states, and the app's sidebar and top bar. Every screen is assembled from those pieces, so one change updates the whole module. Everything the tutorial points at works: learners can select the ringed patient row, the Schedule follow-up button, a time slot or Book appointment, or use Next step. In Try me, the patient search takes real keyboard input through Figma variables and key-press triggers. The app's sidebar and the Provider, Visit type and Week dropdowns all respond, and a wrong patient, a booked time or a slot after 10:00 AM brings up a short pop-up that explains why. Buttons and answers respond on hover. In all, there are 29 screens, 14 feedback pop-ups and more than 350 interactions.</p>
  <p style="margin-top:28px">{pill(S, "Try the prototype", external=True)}</p>
</div></section>
"""
sw += access(
    ["Feedback never relies on color alone: every result has an icon (✓ or ✕) and a plain-language explanation.",
     "No audio required: every instruction, callout and piece of feedback is on screen as text.",
     "One hint after a miss, plus “Show me again,” so learners can get support without starting over.",
     "Focus rings carry a number that matches the callout, so the cue isn't only the amber color.",
     "A job aid gives learners a way back to the steps after training ends."],
    ["Check the muted gray text and the amber hint panel against WCAG 2.2 AA contrast.",
     "Rebuild in an authoring tool with keyboard navigation, a logical focus order and screen-reader labels.",
     "Add alt text for the app screens and a text-only version of the job aid.",
     "Publish the job aid as an accessible PDF."])
sw += evaluation(
    "Evaluation plan",
    "The module captures its own learning data, and a short supervisor check closes the loop on the job. Here's how I'd measure it with a real onboarding group, using Kirkpatrick's four levels.",
    [("1 · Reaction", "New staff feel ready to book on their own.", "The 1–5 readiness check on the wrap-up screen.", "Built into the module"),
     ("2 · Learning", "Staff check the provider and the date of birth without prompting.", "First-try results in Try me and both Test me questions.", "Built into the prototype"),
     ("3 · Behavior", "Staff use the habits on real bookings.", "A supervisor reviews each new hire's first 10 bookings for patient and provider accuracy.", "Planned"),
     ("4 · Results", "Fewer reschedules caused by booking errors.", "Reschedule calls tied to wrong patient or wrong provider, compared with the previous hiring group.", "Planned")])
sw += next_prev(("The TV Wall Sales Simulator", "tv-wall.html"), ("Coaching Through Conflict", "coaching.html"))
sw += "</main>\n" + footer()
write("software-training.html", sw)


# ======================= HOW I WORK =======================
import json
H = json.load(open("content/how-i-work.json", encoding="utf-8"))
court = open("assets/img/court.svg", encoding="utf-8").read()


def label(t):
    return f'<p class="eyebrow tick reveal">{e(t)}</p>'


def text_block(sec, cls=""):
    return f"""<section class="{cls}"><div class="wrap narrow">
  {label(sec["label"])}
  <h2 class="h-lg reveal d1">{e(sec["title"])}</h2>
  <p class="lead reveal d2">{e(sec["body"])}</p>
</div></section>
"""


R = H["roster"]
w = head("How I work · Tshwjxeeb Vaaj",
         "How I design with AI: a repeatable pipeline where AI does the legwork and I make the calls.")
w += nav("how") + '<main class="hiw">\n'
players = "".join(f'<div class="player-card"><h3>{e(p["name"])}</h3><span class="role">{e(p["role"])}</span><p>{e(p["desc"])}</p></div>' for p in R["players"])
w += f"""<section class="hiw-hero"><div class="wrap">
  {label(R["label"])}
  <h1 class="h-xl reveal d1">{e(R["title"])}</h1>
  <p class="lead reveal d2">{e(R["body"])}</p>
  <div class="roster glass reveal">
    <div class="r-lead"><h3>{e(R["lead"]["name"])} <span class="role">{e(R["lead"]["role"])}</span></h3><p>{e(R["lead"]["desc"])}</p></div>
    <div class="r-chief">
      <h3>{e(R["chief"]["name"])} <span class="role">{e(R["chief"]["role"])}</span></h3><p>{e(R["chief"]["desc"])}</p>
      <div class="players">{players}</div>
    </div>
    <div class="r-stop"><h3>{e(R["stop"]["name"])} <span class="role">{e(R["stop"]["role"])}</span></h3><p>{e(R["stop"]["desc"])}</p></div>
  </div>
  <figure class="court reveal">{court}<figcaption class="swipe">Swipe to see the full court →</figcaption></figure>
  {meta_blocks([("Type", H["meta"]["type"]), ("Status", H["meta"]["status"]), ("Tech stack", H["meta"]["stack"])], cols=True)}
  <div class="hero-btns reveal">{pill("coaching.html", "View Coaching Through Conflict")}{pill("#contact", "Get in touch", ghost=True)}</div>
</div></section>
"""
w += text_block(H["overview"])
P_ = H["pipeline"]
steps = "".join(f'<li><span>{i:02d}</span>{e(s)}</li>' for i, s in enumerate(P_["steps"], 1))
w += f"""<section><div class="wrap">
  {label(P_["label"])}
  <div class="split-even">
    <h2 class="h-lg reveal d1">{e(P_["title"])}</h2>
    <div class="reveal d2"><p class="lead">{e(P_["body"])}</p><blockquote class="callout">“{e(P_["quote"])}”</blockquote></div>
  </div>
  <ol class="pipeline reveal">{steps}</ol>
</div></section>
"""


def numbered(sec, cols):
    items = "".join(f'<div class="num-item reveal{" d1" if i % 2 else ""}"><span class="num">{i+1:02d}</span><h3>{e(h)}</h3><p>{e(b)}</p></div>'
                    for i, (h, b) in enumerate(sec["items"]))
    return f"""<section><div class="wrap">
  {label(sec["label"])}
  <h2 class="h-lg reveal d1">{e(sec["title"])}</h2>
  <div class="num-grid c{cols}">{items}</div>
</div></section>
"""


w += numbered(H["practice"], 3) + numbered(H["rules"], 2)
w += text_block(H["principle"]) + text_block(H["why"])
inside = "".join(f"""<div class="inside-row reveal">
  <img src="{src}" alt="{e(h)}" loading="lazy">
  <div><h3 class="h-sm copper">{e(h)}</h3><p>{e(b)}</p></div>
</div>""" for h, b, src in H["inside"]["items"])
w += f"""<section><div class="wrap">{label(H["inside"]["label"])}{inside}</div></section>
"""
F, C = H["flagship"], H["contact"]
w += f"""<section class="cream" id="contact"><div class="wrap">
  <div class="center flagship">
    {label(F["label"])}
    <h2 class="h-lg reveal d1">{e(F["title"])}</h2>
    <p class="reveal d2">{e(F["body"])}</p>
    <div class="hero-btns reveal">{pill(COACHING_URL, "Experience the project", external=True)}{pill("coaching.html", "Read the case study", ghost=True)}</div>
  </div>
  <div class="cream-contact">
    <div class="reveal"><h2 class="h-lg">{e(C["title"])}</h2><p>{e(C["body"])}</p></div>
    <form class="line-form reveal d1" id="contact-form" data-email="{e(EMAIL)}">
      <label>Name<input name="first" autocomplete="name" required></label>
      <label>Email<input name="email" type="email" autocomplete="email" required></label>
      <label>Message<textarea name="message" required></textarea></label>
      <button class="pill" type="submit">Send message {ARROW}</button>
    </form>
  </div>
</div></section>
</main>
"""
w += footer()
write("how-i-work.html", w)
