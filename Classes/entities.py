import classes as cl

# name, level, maxhp, atk, df, spd, id
normal_enemies = {
    1 : cl.Unit("Rat", 
                lambda w: round(3*(1.05**w) + 1),
                lambda l: round(3*(1.15**l) + 7),
                lambda l: round(3*(1.05**l) + 2),
                lambda l: round(4*(1.10**l) + 4),
                lambda l: round(4*(1.10**l) + 3),
                1
                ),
    
    2 : cl.Unit("Slime", 
                lambda w: round(3*(1.10**w) + 2),
                lambda l: round(4*(1.2**l) + 5),
                lambda l: round(5*(1.10**l) + 1),
                lambda l: round(3*(1.10**l) + 4),
                lambda l: round(2*(1.05**l) + 2),
                2
                ),
    3 : cl.Unit("Sword-wielding Undead", 
                lambda w: round(5*(1.1**(w-1)) + 5),
                lambda l: round(4*(1.1**l) + 3),
                lambda l: round(3*(1.1**l) + 2),
                lambda l: round(5*(1.15**l) + 5),
                lambda l: round(4*(1.01**l) + 3),
                3
                ),
    4 : cl.Unit("Treant", 
                lambda w: round(3*(1.1**w) + 3),
                lambda l: round(4*(1.1**l) + 3),
                lambda l: round(3.5*(1.1**l) + 2),
                lambda l: round(5*(1.15**l) + 5),
                lambda l: round(4*(1.05**l) + 3),
                4
                ),
    5 : cl.Unit("Shielded Undead", 
                lambda w: round(5*(1.1**(w-1)) + 5),
                lambda l: round(4*(1.1**l) + 3),
                lambda l: round(3.5*(1.03**l) + 1),
                lambda l: round(5*(1.15**l) + 5),
                lambda l: round(3.5*(1.13**l) + 3),
                5
                ),
    6 : cl.Unit("Mimic", 
                lambda w: round(4*(1.1**w) + 2),
                lambda l: round(3.5*(1.15**l) + 5),
                lambda l: round(2.5*(1.05**l) + 1),
                lambda l: round(5*(1.15**l) + 5),
                lambda l: round(4*(1.05**l) + 3),
                6
                ),
    7 : cl.Unit("Wolf", 
                lambda w: round(3*(1.05**w) + 2),
                lambda l: round(3*(1.05**l) + 3),
                lambda l: round(4*(1.1**l) + 1),
                lambda l: round(2*(1.03**l) + 3),
                lambda l: round(3.5*(1.13**l) + 4),
                7
                ),
    8 : cl.Unit("Skeleton", 
                lambda w: round(2*(1.15**w) + 5),
                lambda l: round(3*(1.05**l) + 3),
                lambda l: round(4*(1.1**l) + 1),
                lambda l: round(2*(1.01**l) + 5),
                lambda l: round(4*(1.15**l) + 3),
                8
                ),
    9 : cl.Unit("Bat", 
                lambda w: round(3*(1.05**w) + 3),
                lambda l: round(2*(1.07**l) + 3),
                lambda l: round(3*(1.1**l) + 1),
                lambda l: round(2*(1.05**l) + 3),
                lambda l: round(3.5*(1.15**l) + 7),
                8
                ),
}