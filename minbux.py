# Convert a space-separated string of numbers into a dictionary with 1-based indexing.
def convert_from_str_to_dict(s):
    s = s.replace(",", "").split(" ")
    d = {}
    for i in range(len(s)):
        d[i + 1] = int(s[i])
    return d

# Formats the text to be separated per thousands. e.g., 1000 -> 1,000
def format_number(n):
    return f"{n:,}"

# Initialize data for bux required for golfers/hats relative to the level, xp given from buying golfers/hats, and xp required, as well as other variables for tracking purposes for phase 1.
bux = "$5 $6 $7 $8 $10 $15 $25 $30 $35 $40 $50 $60 $80 $100 $150 $200 $250 $300 $400 $500 $600 $800 $1,000 $1,500 $2,000 $3,000 $4,000 $5,000 $6,000 $8,000 $10,000 $12,000 $15,000 $30,000 $45,000 $60,000 $80,000 $100,000 $120,000 $140,000"
xp_given = "4 5 6 7 8 9 10 11 12 14 16 20 25 30 40 50 65 80 100 120 150 200 250 300 350 400 450 500 600 700 800 900 1,000 1,100 1,200 1,300 1,500 1,700 1,900 2,100"
xp_required = "8 10 14 20 28 38 50 65 85 110 140 170 200 240 280 320 360 400 450 500 550 550 650 700 750 800 920 1,100 1,300 1,500 1,700 1,900 2,100 2,300 2,500 2,700 2,900 3,100 3,300 3,500 3,800 4,100 4,500 5,000 6,000 7,000 8,000 10,000 12,000"
bux = bux.replace("$", "")
d_xp_required, d_xp_given, d_bux_required = convert_from_str_to_dict(xp_required), convert_from_str_to_dict(xp_given), convert_from_str_to_dict(bux)
skin_count, sum_skin_count, level, xp, sum_bux, tbux, sum_xp, pu_count = 0, 0, 1, 0, 0, 0, 0, 3

### Phase 1: 
# Simulate leveling up using only golfers/hats until level 41.
# This tracks bux spent per level, cumulative bux spent, golfer bought per level, remaining xp for each level, cumulative xp earned and powerup levels.
print(f"Lvl|    Bux   |  Total Bux  | Skins |  Remaining XP |  Total XP | Power Ups upgrades")
while level < 41:
    xp += d_xp_given.get(level)
    tbux += d_bux_required.get(level)
    skin_count += 1
    if xp >= d_xp_required.get(level):
        xp -= d_xp_required.get(level)
        sum_xp = xp + sum(d_xp_required.get(i) for i in d_xp_required if i <= level)
        sum_skin_count += skin_count
        sum_bux += tbux
        print(f"{level:>2} |  {format_number(tbux):>7} |  {format_number(sum_bux):>9}  |  {skin_count:>2}   |     {format_number(xp):>5}     |   {format_number(sum_xp):>6}  | {pu_count:>2}x lv 1")
        level += 1
        tbux, skin_count = 0, 0
        if level in [5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]:
            pu_count += 1

# Initialize powerup level tracking for phase 2. This initializes the data for bux, xp given for powerups and xp required for phase 2.
bux = "$5 $10 $30 $80 $250 $750 $2,300 $8,000 $30,000 $80,000"
xp_given = "4 5 6 8 16 40 100 300 700 1,500"
bux = bux.replace("$", "")
d_xp_given, d_bux_required = convert_from_str_to_dict(xp_given), convert_from_str_to_dict(bux)
powerup_level = {1: 21}
for i in range(2, 12):
    powerup_level[i] = 0
all_powerup_level = 1

### Phase 2 - Segment 1:
# Simulate leveling up using power-ups from level 41 to level 45.
# This tracks bux spent per level, cumulative bux spent, golfer bought per level, remaining xp for each level, cumulative xp earned and powerup levels.
def phase2(target_level):
    global level, xp, sum_bux, tbux, sum_xp, all_powerup_level
    while level < target_level:
        xp += d_xp_given.get(all_powerup_level)
        tbux += d_bux_required.get(all_powerup_level)
        powerup_level[all_powerup_level] -= 1
        powerup_level[all_powerup_level+1] += 1
        if powerup_level[all_powerup_level] == 0:
            all_powerup_level += 1
        if xp >= d_xp_required.get(level):
            xp -= d_xp_required.get(level)
            sum_xp = xp + sum(d_xp_required.get(i) for i in d_xp_required if i <= level)
            sum_bux += tbux
            pu_string = ""
            for pu_lvl in powerup_level:
                if powerup_level[pu_lvl] > 0:
                    pu_string += f"{powerup_level[pu_lvl]}x lv {pu_lvl}, "
            pu_string = pu_string.rstrip(", ")
            print(f"{level:>2} |  {format_number(tbux):>7} |  {format_number(sum_bux):>9}  |  {0:>2}   |     {format_number(xp):>5}     |   {format_number(sum_xp):>6}  | {pu_string:>2}")
            level += 1
            tbux = 0

phase2(45)

### Phase 2 - Bonus segment:
# Additional powerup added at level 45, so we account for that here.
powerup_level[all_powerup_level] += 1
xp += sum(d_xp_given.get(i) for i in d_xp_given if i < all_powerup_level)
tbux += sum(d_bux_required.get(i) for i in d_bux_required if i < all_powerup_level)

### Phase 2 - Segment 2:
# Simulate leveling up using power-ups from level 45 to level 50.
phase2(50)

### Final Summary:
# Print out the final summary of total bux spent, total xp earned, powerup levels and total cards purchased.
print(f"""
Total Bux: {format_number(sum_bux)}
Total XP: {format_number(sum_xp)}
Power Ups: 22x lv 11
Total cards: {sum_skin_count} cards purchased""")
