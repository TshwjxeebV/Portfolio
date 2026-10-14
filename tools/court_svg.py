"""Generates the 'roster court' diagram used on the How I work page (site + Figma)."""
W, H = 1120, 600
INK, MUTED, COPPER, PANEL, COURT = "#F7F4EE", "#B8C7DD", "#E0A672", "#111830", "#1A2643"
SERIF = "Instrument Serif, Georgia, serif"
SANS = "Schibsted Grotesk, Arial, sans-serif"

out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="court-t court-d">')
a('<title id="court-t">The team as a volleyball court</title>')
a('<desc id="court-d">A top-down volleyball court. On the bench: the head coach (me), the assistant coach (Claude), the playbook and the timeout whistle. '
  'The morning scouts warm up on our side, the line judge stands at the net post so nothing crosses unchecked, and the finished work goes over the net.</desc>')
a(f'<rect x="0" y="0" width="{W}" height="{H}" rx="28" fill="{PANEL}"/>')
# court
cx0, cy0, cx1, cy1 = 340, 80, 1070, 440
net = (cx0 + cx1) / 2
a(f'<rect x="{cx0}" y="{cy0}" width="{cx1-cx0}" height="{cy1-cy0}" fill="{COURT}" stroke="{COPPER}" stroke-opacity=".7" stroke-width="3"/>')
third = (cx1 - cx0) / 6
for x in (net - third, net + third):
    a(f'<line x1="{x}" y1="{cy0}" x2="{x}" y2="{cy1}" stroke="{COPPER}" stroke-opacity=".35" stroke-width="2"/>')
a(f'<line x1="{net}" y1="{cy0-24}" x2="{net}" y2="{cy1+24}" stroke="{INK}" stroke-width="4" stroke-dasharray="2 7" stroke-linecap="round"/>')
for y in (cy0 - 24, cy1 + 24):
    a(f'<circle cx="{net}" cy="{y}" r="7" fill="{INK}"/>')
a(f'<text x="{net}" y="{cy0-40}" fill="{MUTED}" font-family="{SANS}" font-size="13" text-anchor="middle" letter-spacing="1.5">THE NET · WHAT GOES OUT</text>')
# bench
a(f'<rect x="40" y="110" width="260" height="400" rx="20" fill="#FFFFFF" fill-opacity=".04" stroke="#FFFFFF" stroke-opacity=".12"/>')
a(f'<text x="170" y="98" fill="{MUTED}" font-family="{SANS}" font-size="13" text-anchor="middle" letter-spacing="1.5">THE BENCH</text>')


def node(x, y, name, desc, fill=COPPER, anchor="start", r=13, dx=24):
    a(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
    tx = x + dx if anchor == "start" else x - dx if anchor == "end" else x
    a(f'<text x="{tx}" y="{y-2}" fill="{INK}" font-family="{SERIF}" font-size="24" text-anchor="{anchor}">{name}</text>')
    for i, line in enumerate(desc):
        a(f'<text x="{tx}" y="{y+20+i*18}" fill="{MUTED}" font-family="{SANS}" font-size="14" text-anchor="{anchor}">{line}</text>')


node(70, 160, "Head coach", ["Me: decides and", "signs off"])
node(70, 260, "Assistant coach", ["Claude: runs the", "playbook"], fill=INK)
# playbook clipboard icon
a('<g transform="translate(58,340)"><rect x="0" y="0" width="26" height="34" rx="4" fill="#A8743F"/><rect x="4" y="6" width="18" height="24" rx="2" fill="#FBFBF9"/><rect x="8" y="-3" width="10" height="6" rx="2" fill="#C9CDD3"/></g>')
a(f'<text x="94" y="355" fill="{INK}" font-family="{SERIF}" font-size="24">The Playbook</text>')
a(f'<text x="94" y="375" fill="{MUTED}" font-family="{SANS}" font-size="14">Memory &amp; standards</text>')
# whistle icon
a(f'<g transform="translate(58,438)"><circle cx="12" cy="14" r="11" fill="none" stroke="{COPPER}" stroke-width="4"/><rect x="18" y="4" width="16" height="9" rx="3" fill="{COPPER}"/></g>')
a(f'<text x="100" y="452" fill="{INK}" font-family="{SERIF}" font-size="24">Timeout Whistle</text>')
a(f'<text x="100" y="472" fill="{MUTED}" font-family="{SANS}" font-size="14">One pause stops it all</text>')
# scouts on our side
for (x, y) in ((400, 140), (480, 140), (400, 380), (480, 380)):
    a(f'<circle cx="{x}" cy="{y}" r="11" fill="{INK}" fill-opacity=".9"/>')
a(f'<text x="384" y="242" fill="{INK}" font-family="{SERIF}" font-size="24">The Morning Scouts</text>')
a(f'<text x="384" y="264" fill="{MUTED}" font-family="{SANS}" font-size="14">Scheduled runs that</text>')
a(f'<text x="384" y="282" fill="{MUTED}" font-family="{SANS}" font-size="14">report before I wake</text>')
# line judge at the net post with flag
lx, ly = net, cy1 + 24
a(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly+56}" stroke="{INK}" stroke-width="3"/>')
a(f'<path d="M {lx} {ly+4} L {lx+34} {ly+14} L {lx} {ly+26} Z" fill="{COPPER}"/>')
a(f'<text x="{lx+48}" y="{ly+28}" fill="{INK}" font-family="{SERIF}" font-size="24">The Line Judge</text>')
a(f'<text x="{lx+48}" y="{ly+48}" fill="{MUTED}" font-family="{SANS}" font-size="14">Nothing crosses the net unchecked</text>')
# the work on the far side
bx, by = net + 160, 230
a(f'<circle cx="{bx}" cy="{by}" r="20" fill="none" stroke="{COPPER}" stroke-width="3"/>')
a(f'<path d="M {bx-20} {by} Q {bx} {by-14} {bx+20} {by}" fill="none" stroke="{COPPER}" stroke-width="2"/>')
a(f'<path d="M {bx-6} {by-19} Q {bx+8} {by} {bx-4} {by+19}" fill="none" stroke="{COPPER}" stroke-width="2"/>')
a(f'<text x="{bx+36}" y="{by-2}" fill="{INK}" font-family="{SERIF}" font-size="24">The work</text>')
a(f'<text x="{bx+36}" y="{by+18}" fill="{MUTED}" font-family="{SANS}" font-size="14">Modules, case studies,</text>')
a(f'<text x="{bx+36}" y="{by+36}" fill="{MUTED}" font-family="{SANS}" font-size="14">applications</text>')
# arrow from scouts side over the net
a(f'<path d="M 590 262 C 650 200, 700 210, {bx-30} {by+6}" fill="none" stroke="{COPPER}" stroke-width="2.5" stroke-dasharray="6 6"/>')
a(f'<path d="M {bx-30} {by+6} l -14 -2 l 8 12 z" fill="{COPPER}"/>')
a('</svg>')

svg = "\n".join(out)
if __name__ == "__main__":
    import sys
    open(sys.argv[1] if len(sys.argv) > 1 else "court.svg", "w").write(svg)
