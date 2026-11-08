"""The Genetic Industry (fork) logo, 40x40 (saved at 40 and 520 px), painted in the house style of the Fundamentum and Ostentum logos
with the shared kit H:/AI_MC_Modding/_toolkit/logokit/logokit.py. A neutral logo for our fork; it does not copy the original mod's logo. Not wired into mods.toml yet: that waits for
Oculifelis's verdict on the review page.

    python branding/genetic_industry_logo.py            # writes branding/genetic_industry_logo_<option>_40.png and _520.png
"""
import math
import os
import sys

sys.path.insert(0, 'H:/AI_MC_Modding/_toolkit/logokit')
from logokit import *  # noqa: E402,F403

def genetic_industry():
    img = backdrop(glow=(110, 200, 230), dark=(12, 20, 30))
    L = layer()
    # a glass vial with a bee inside and a helix etched behind it
    G = ramp((170, 220, 240))
    for y in range(6, 37):
        for x in range(10, 31):
            dx = (x + 0.5 - 20) / 9.0
            if abs(dx) <= 1 and (y > 9 or abs(dx) < 0.55):
                if abs(dx) > 0.85 or y < 10 or y > 35:
                    put(L, x, y, pick(G, 2.4 - dx * 1.4))
                else:
                    put(L, x, y, mix((40, 80, 110), (120, 190, 220), 0.25 + 0.3 * (1 - abs(dx))), 200)
    for y in range(11, 35):
        for k in (0, 1):
            x = 20 + 5 * math.sin(y * 0.45 + k * math.pi)
            put(L, x, y, (120, 255, 200) if k else (255, 140, 210))
    line(L, 14, 8, 26, 8, (150, 110, 70), 2.0)                       # cork
    finish(img, L)
    B = layer()
    bee(B, 19, 23, 1.0)
    finish(img, B)
    return img


OPTIONS = {'vial': genetic_industry}

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in OPTIONS.items():
        save(fn(), os.path.join(here, 'genetic_industry_logo_' + name))
