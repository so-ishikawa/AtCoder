goal_posi, kabe_posi, hammer_posi = map(int, input().split())

# hammer不使用
if 0 < goal_posi and goal_posi < kabe_posi:
    print(abs(goal_posi))
    exit()

if kabe_posi < 0 and 0 < goal_posi:
    print(abs(goal_posi))
    exit()

if 0 > goal_posi and goal_posi > kabe_posi:
    print(abs(goal_posi))
    exit()

if kabe_posi > 0 and 0 > goal_posi:
    print(abs(goal_posi))
    exit()

# hammer使用
## スタートとゴールの間にhammerがある
if 0 < hammer_posi and hammer_posi < kabe_posi and kabe_posi < goal_posi:
    print(abs(goal_posi))
    exit()

if 0 > hammer_posi and hammer_posi > kabe_posi and kabe_posi > goal_posi:
    print(abs(goal_posi))
    exit()

## hammerとゴールがスタートを挟んで反対にある
if hammer_posi < 0 and 0 < kabe_posi and kabe_posi < goal_posi:
    print(abs(goal_posi) + 2*abs(hammer_posi))
    exit()

if hammer_posi > 0 and 0 > kabe_posi and kabe_posi > goal_posi:
    print(abs(goal_posi) + 2*abs(hammer_posi))
    exit()

print(-1)
