# example map data

#40(가로)X28(세로)
# P = 플레이어, G = Goal(골인영역)
# 0 = 가로 장애물, 1 = 세로 장애물, 2 = 제자리 회전 장애물
# level_map = [
# 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                  P                   X',
# 'X                                      X',
# 'X             0                        X',
# 'X                                      X',
# 'X                 1       G            X',
# 'X                                      X',
# 'X                     2                X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'X                                      X',
# 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# ]

level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X            2              U   D      X',
'X          G    2     D              G X',
'X     D 2 D             L     U    X   X',
'X   XXXXXXXXXX      U      D       X   X',
'X       U    X2                    X   X',
'X   U  U     X    U         L  U   X   X',
'XXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX   X',
'XXXXXXXXXX   XX       L  XX      X2    X',
'XXXXXXXXXX   XX    UR    XX  R   X    2X',
'XX     XXX   XX          XX  XX  X     X',
'XX           XX     XXX  XX  XX  X     X',
'XX  P     G  XX     XXX  XX  XX  X  2  X',
'XX           XX  G  XXX     LXX        X',
'XX     XXXXXXXX     XXXR     XX       LX',
'XXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]

tile_size = 32
screenWidth = 1280
screenHeight = len(level_map) * tile_size
print("len: " + str(len(level_map)))

#가로 40칸(1280픽셀) X 세로28칸(896픽셀)
#level_map = 28이다.



