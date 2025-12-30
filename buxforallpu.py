def convert_from_str_to_dict(s):
    s = s.replace(",", "").split(" ")
    d = {}
    for i in range(len(s)):
        d[i + 1] = int(s[i])
    return d

def format_number(n):
    return f"{n:,}"

xp_required = "8 10 14 20 28 38 50 65 85 110 140 170 200 240 280 320 360 400 450 500 550 550 650 700 750 800 920 1,100 1,300 1,500 1,700 1,900 2,100 2,300 2,500 2,700 2,900 3,100 3,300 3,500 3,800 4,100 4,500 5,000 6,000 7,000 8,000 10,000 12,000"
bux = "$5 $10 $30 $80 $250 $750 $2,300 $8,000 $30,000 $80,000 $200,000"
xp_given = "4 5 6 8 16 40 100 300 700 1,500 3,000"
bux = bux.replace("$", "")
d_xp_given, d_bux_required, d_xp_required = convert_from_str_to_dict(xp_given), convert_from_str_to_dict(bux), convert_from_str_to_dict(xp_required)
powerup_level = {1: 3}
for i in range(2, 13):
    powerup_level[i] = 0
all_powerup_level = 1
level, xp, sum_bux, tbux, sum_xp = 1, 0, 0, 0, 0
def phase2(target_level):
    global level, xp, sum_bux, tbux, sum_xp, all_powerup_level
    while level < target_level:
        if xp >= d_xp_required.get(level):
            xp -= d_xp_required.get(level)
            sum_xp = xp + sum(d_xp_required.get(i) for i in d_xp_required if i <= level)
            sum_bux += tbux
            pu_string = ""
            for pu_lvl in powerup_level:
                if powerup_level[pu_lvl] > 0:
                    pu_string += f"{powerup_level[pu_lvl]}x lv {pu_lvl}, "
            pu_string = pu_string.rstrip(", ")
            print(f"{level:>2} |  {format_number(tbux):>7} |  {format_number(sum_bux):>9}  |  {0:>2}   |     {format_number(xp):>5}     |   {format_number(sum_xp):>7}  | {pu_string:>2}")
            level += 1
            tbux = 0
            if level in [5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 45]:
                powerup_level[all_powerup_level] += 1
                xp += sum(d_xp_given.get(i) for i in d_xp_given if i < all_powerup_level)
                tbux += sum(d_bux_required.get(i) for i in d_bux_required if i < all_powerup_level)
        xp += d_xp_given.get(all_powerup_level)
        tbux += d_bux_required.get(all_powerup_level)
        powerup_level[all_powerup_level] -= 1
        powerup_level[all_powerup_level+1] += 1
        if powerup_level[all_powerup_level] == 0:
            all_powerup_level += 1
print(f"Lvl|    Bux   |  Total Bux  | Skins |  Remaining XP |  Total XP  | Power Ups upgrades")
phase2(50)