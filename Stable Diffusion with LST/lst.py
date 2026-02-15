# Minimal LST Block
# GroupNorm -> SiLU -> Conv2d
def make_lst_module(channels):
    return nn.Sequential(
        nn.GroupNorm(32, channels),
        nn.SiLU(),
        nn.Conv2d(channels, channels, kernel_size=1)
    )