#!/usr/bin/env python3
"""Download the 14 verified clean ExRx-style exercise illustrations from Commons.
The 4 missing (hammer curl, russian twist, crunch, triceps kickback) are
generated separately as matching-style SVGs."""
import os, subprocess, urllib.parse, json, time

OUT = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(OUT, exist_ok=True)
UA = "TrainingTracker/1.0 (https://example.org; educational@example.org)"
API = "https://commons.wikimedia.org/w/api.php"

# 14 verified file titles (clean line-drawing illustrations)
FILES = {
    "dumbbell-bench-press":      "Dumbbell-bench-press-1.png",
    "incline-dumbbell-press":    "Dumbbell-incline-bench-press-1.png",
    "seated-shoulder-press":     "Dumbbell-shoulder-press-1.png",
    "lateral-raises":            "Dumbbell-lateral-raises-1.png",
    "tricep-overhead-extension": "DumbbellTricepsExtension.JPG",
    "pull-ups":                  "Chin-ups-1.png",
    "bent-over-rows":            "Barbell-rear-delt-row-1.png",
    "single-arm-dumbbell-rows":  "Bent-over-rear-delt-row-with-head-on-bench-1.png",
    "reverse-flyes":             "Lying-rear-lateral-raise-1.png",
    "goblet-squats":             "Squats-1.png",
    "bulgarian-split-squats":    "Front-squat-1-857x1024.png",
    "romanian-deadlifts":        "Romanian-deadlift-1.png",
    "lunges":                    "Walking-lunges-1.png",
    # bicep-curls: use the closeup photo (clean, on-topic)
    "bicep-curls":               "Girl doing biceps curls with dumbbell closeup.jpg",
}

def get_url(title):
    params = {
        "action":"query","format":"json","prop":"imageinfo",
        "titles":"File:"+title,"iiprop":"url|size|mime","iiurlwidth":"500",
    }
    qs = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k,v in params.items())
    r = subprocess.run(["curl","-sL","-A",UA,"--max-time","30",f"{API}?{qs}"],
                       capture_output=True,text=True)
    try: d = json.loads(r.stdout)
    except Exception: return None
    for p in d.get("query",{}).get("pages",{}).values():
        ii = p.get("imageinfo")
        if not ii: continue
        return ii[0].get("thumburl") or ii[0].get("url")
    return None

def is_image(path):
    if not os.path.exists(path) or os.path.getsize(path)<4000: return False
    r = subprocess.run(["file","-b",path],capture_output=True,text=True)
    t=r.stdout.lower(); return "image" in t and "html" not in t

ok=0
for key,title in FILES.items():
    dest=os.path.join(OUT,key+".jpg")
    # always re-fetch fresh (clear any stale wrong downloads)
    if os.path.exists(dest): os.remove(dest)
    url=get_url(title)
    if not url:
        print(f"  FAIL  {key}  (no url for {title})"); continue
    subprocess.run(["curl","-sL","-A",UA,"--max-time","30","-o",dest,url],
                   capture_output=True)
    if is_image(dest):
        sz=os.path.getsize(dest)//1024
        print(f"  OK    {key:30s} <- {title}  ({sz}KB)"); ok+=1
    else:
        print(f"  FAIL  {key}  (bad download)")
    time.sleep(0.8)

print(f"\n{ok}/{len(FILES)} ok")
