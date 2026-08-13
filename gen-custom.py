#!/usr/bin/env python3
"""Generate 4 custom exercise illustrations in the same clean style as the
Wikimedia ExRx line drawings: white background, dark gray figure, simple
dumbbell shapes. Output as PNG via cairosvg if available, else SVG."""
import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(OUT, exist_ok=True)

# Style constants matching the Commons illustrations
BG = "#ffffff"
FIG = "#2b2b2b"   # dark gray figure
FILL = "#cfcfcf"  # light gray muscle fill
DB = "#3a3a3a"    # dumbbell

def dumbbell(cx, cy, angle=0, size=1.0):
    """A small dumbbell, optionally rotated."""
    w = 26*size; r = 7*size
    return f'''<g transform="translate({cx},{cy}) rotate({angle})">
      <rect x="{-w/2}" y="-2" width="{w}" height="4" fill="{DB}"/>
      <circle cx="{-w/2}" cy="0" r="{r}" fill="{DB}"/>
      <circle cx="{w/2}" cy="0" r="{r}" fill="{DB}"/>
    </g>'''

def head(cx, cy, r=11):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{FILL}" stroke="{FIG}" stroke-width="2.5"/>'

# limb macro
def L(x1,y1,x2,y2, w=4.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{FIG}" stroke-width="{w}" stroke-linecap="round"/>'

def torso(pts):
    return f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{FILL}" stroke="{FIG}" stroke-width="2.5" stroke-linejoin="round"/>'

def svg(body, vb="0 0 220 320"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="220" height="320">
  <rect width="100%" height="100%" fill="{BG}"/>
  {body.strip()}
</svg>'''

POSES = {}

# HAMMER CURL — standing, one arm curled up with neutral grip, dumbbell vertical
POSES["hammer-curls"] = svg(f"""
  {head(110, 50)}
  {torso([(92,60),(128,60),(124,160),(96,160)])}
  {L(96,75,72,150)}       <!-- left arm straight down -->
  {L(72,150,72,185)}
  {L(128,75,140,110)}     <!-- right upper arm -->
  {L(140,110,150,80)}     <!-- forearm curled up -->
  {L(96,160,80,230)}      <!-- left leg -->
  {L(80,230,78,280)}
  {L(124,160,140,230)}    <!-- right leg -->
  {L(140,230,142,280)}
  {dumbbell(150, 70, angle=90, size=0.9)}  <!-- vertical hammer grip -->
""")

# RUSSIAN TWIST — seated, leaning back, torso twisted, holding one DB with both hands to side
POSES["russian-twists"] = svg(f"""
  {head(95, 90)}
  {torso([(80,100),(112,100),(120,170),(88,175)])}  <!-- torso leaning -->
  {L(96,110,70,150)}    <!-- left arm reaching across -->
  {L(70,150,60,150)}
  {L(100,110,80,145)}   <!-- right arm -->
  {L(80,145,60,150)}
  {L(105,175,150,210)}  <!-- thighs up (V-sit) -->
  {L(150,210,155,255)}
  {L(95,175,60,205)}    <!-- other leg -->
  {L(60,205,58,250)}
  {dumbbell(58, 150, size=0.85)}  <!-- DB held to the side -->
""")

# WEIGHTED CRUNCH — lying on floor, knees bent, holding DB on chest, shoulders lifted
POSES["weighted-crunches"] = svg(f"""
  <!-- bench/floor line -->
  <line x1="20" y1="250" x2="200" y2="250" stroke="{FIG}" stroke-width="2.5"/>
  {head(70, 210)}      <!-- head up, curled -->
  {torso([(58,220),(88,220),(110,250),(50,250)])}  <!-- curled torso -->
  {L(78,228,105,232)}  <!-- arm holding DB on chest -->
  {L(105,232,108,235)}
  {L(72,228,98,232)}
  {L(98,232,108,235)}
  {L(105,250,150,235)} <!-- thigh up (bent knee) -->
  {L(150,235,168,250)}
  {L(95,250,70,235)}   <!-- other thigh -->
  {L(70,235,55,250)}
  {dumbbell(108, 230, size=0.8)}  <!-- DB on chest -->
""")

# TRICEPS KICKBACK — bent over, one arm bracing, other arm extended back with DB
POSES["triceps-kickbacks"] = svg(f"""
  {head(70, 120)}
  {torso([(60,130),(84,130),(130,170),(110,180)])}  <!-- hinged torso horizontal -->
  {L(72,140,55,175)}   <!-- near arm reaching down to bench -->
  {L(55,175,60,195)}
  {L(80,145,120,165)}  <!-- far upper arm along torso -->
  {L(120,165,165,155)} <!-- forearm extended straight back -->
  {L(118,178,95,215)}  <!-- near leg (front) -->
  {L(95,215,95,250)}
  {L(122,172,150,200)} <!-- far leg (back) -->
  {L(150,200,158,245)}
  <!-- bench -->
  <rect x="40" y="195" width="40" height="8" rx="3" fill="#cfcfcf" stroke="{FIG}" stroke-width="2"/>
  {dumbbell(170, 155, angle=0, size=0.9)}  <!-- DB at end of extended arm -->
""")

# BICEP CURL — standing, both arms curled up with dumbbells at shoulder height
POSES["bicep-curls"] = svg(f"""
  {head(110, 50)}
  {torso([(92,60),(128,60),(124,165),(96,165)])}
  {L(96,72,72,110)}     <!-- left upper arm -->
  {L(72,110,72,75)}     <!-- left forearm curled up -->
  {L(128,72,148,110)}   <!-- right upper arm -->
  {L(148,110,148,75)}   <!-- right forearm curled up -->
  {L(96,165,82,235)}    <!-- left leg -->
  {L(82,235,80,285)}
  {L(124,165,138,235)}  <!-- right leg -->
  {L(138,235,140,285)}
  {dumbbell(72, 68, angle=90, size=0.9)}
  {dumbbell(148, 68, angle=90, size=0.9)}
""")

# TRICEP OVERHEAD EXTENSION — standing, both hands holding one DB overhead, arms extended up
POSES["tricep-overhead-extension"] = svg(f"""
  {head(110, 70)}
  {torso([(92,80),(128,80),(124,180),(96,180)])}
  {L(110,82,92,55)}     <!-- left upper arm up -->
  {L(92,55,110,35)}     <!-- left forearm to top -->
  {L(110,82,128,55)}    <!-- right upper arm up -->
  {L(128,55,110,35)}    <!-- right forearm to top -->
  {L(96,180,82,250)}    <!-- left leg -->
  {L(82,250,80,295)}
  {L(124,180,138,250)}  <!-- right leg -->
  {L(138,250,140,295)}
  {dumbbell(110, 28, angle=0, size=1.0)}  <!-- DB held overhead -->
""")

# Try cairosvg for PNG; fall back to SVG
try:
    import cairosvg
    fmt = "png"
except ImportError:
    fmt = "svg"
    print("cairosvg not available -> writing SVG (still renders fine in browsers)")

for name, s in POSES.items():
    if fmt == "png":
        path = os.path.join(OUT, name + ".png")
        cairosvg.svg2png(bytestring=s.encode(), write_to=path, output_width=300, output_height=436)
    else:
        path = os.path.join(OUT, name + ".svg")
        with open(path,"w") as f: f.write(s)
    print("wrote", path)
