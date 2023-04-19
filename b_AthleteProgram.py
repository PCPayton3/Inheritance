import b_AthleteClass as ac

generic_athlete = ac.Athlete(6, 220, 0.2)

quarterback = ac.Football_Player(6.2, 250, 0.15, 'quarterback', 'offense')

pointgaurd = ac.Basketball_Player(6.4, 220, 0.13, 'pointgaurd', 'offense', '7')


print("The height for the generic athlete is:", generic_athlete.get_ht())

# print("The team of the generic athlete is:", generic_athlete.get_team())

print("The weight for the football player is:", quarterback.get_wt())

print("The position of the football player is:", quarterback.get_position())

print("The position of the Point Gaurd is:", pointgaurd.get_spot())
print("The height of the point Gaurd is:", pointgaurd.get_ht())
print("the weight of the point Gaurd is:", pointgaurd.get_wt())
