import classes as cl

# name, level, maxhp, atk, df, spd, id

atkSp = lambda l: round(3.5*(1.05**l) + 0.2*l+1)
defSp = lambda l: round(2.75*(1.02**l) + 0.15*l + 2)
spdSp = lambda l: round(5*(1.08**l) + l + 5)

atkNsp = lambda l: round(2*((1.05)**l)+0.15*l+1)
defNsp = lambda l: round(2.25*((1.015)**l)+0.1*l)
spdNsp = lambda l: round(4*(1.06**l)+0.8*l+5)

normal_enemies = {
    1 : cl.Unit("Rat", 
                lambda w: round(1.01**w+ 0.43*w ),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkNsp,
                defSp,
                spdSp,
                1
                ),
    
    2 : cl.Unit("Slime", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkSp,
                defSp,
                spdNsp,
                2
                ),
    3 : cl.Unit("Sword-wielding Undead", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkSp,
                defSp,
                spdNsp,
                3
                ),
    4 : cl.Unit("Treant", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkSp,
                defSp,
                spdNsp,
                4
                ),
    5 : cl.Unit("Shielded Undead", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkNsp,
                defSp,
                spdSp,
                5
                ),
    6 : cl.Unit("Mimic", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(9*((1.07)**l)+0.5*l),
                atkNsp,
                defSp,
                spdSp,
                6
                ),
    7 : cl.Unit("Wolf", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(7*(1.06**l)+0.4*l),
                atkSp,
                defNsp,
                spdSp,
                7
                ),
    8 : cl.Unit("Skeleton", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(7*(1.06**l)+0.4*l),
                atkSp,
                defNsp,
                spdSp,
                8
                ),
    9 : cl.Unit("Bat", 
                lambda w: round(1.01**w+ 0.43*w),
                lambda l: round(7*(1.06**l)+0.4*l),
                atkSp,
                defNsp,
                spdSp,
                8
                ),
}