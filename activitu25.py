

cyclops = ["skill1 : stardust shock - cast two stardust discs to the target"/
           "skill2 : plannet attack - summons orbiting  spheres around cyclops that boost movement speed"/
           "ultimate : star power lockdown - launches a planetary sphere that tracks the enemy"]
lunox = ["order(light) / power of order converts her magic penetriation to a spell vamp and chaos(dark) / ""power of chaos converts her spell vamp into magic penetration ",
         "cosmic fusion / channels order and chaos along a path to deal magic damage and slow enemies","brilliance / grants invincibility and deal continuous damage or darkening / "
         "grants blink and reset chaos assault cooldown" ]
mid_lane = lunox, cyclops, "eudora", "pharsa"
mobile_legend = "roamer", "gold", "exp", mid_lane, "core"
mobile_games = {"old school": "dota", "adventure": "temple run", "new game": "HOK", "popular":mobile_legend}
print(mobile_games["popular"][3][0][1])