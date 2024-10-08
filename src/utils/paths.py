import os
from pathlib import Path

PROJECT_DIR = Path(os.getcwd().split("nfl-betting/")[0] + "nfl-betting/")

BIN_PATH = PROJECT_DIR / "bin"
LOGO_PATH = BIN_PATH / "logos"

DATA_PATH = PROJECT_DIR / "data"

BETTING_PATH = DATA_PATH / "betting"

HOMERS_PATH = DATA_PATH / "homers"

PFF_PROP_PATH = DATA_PATH / "pff-props"
PFF_RATING_PATH = DATA_PATH / "pff-ratings"

INPREDICABLE_PATH = DATA_PATH / "inpredictable"

NFELO_PATH = DATA_PATH / "nfelo"

SUMER_PATH = DATA_PATH / "sumer"
SUMER_ELO_PATH = SUMER_PATH / "elo"
SUMER_OFFENSE_PATH = SUMER_PATH / "offense"
SUMER_DEFENSE_PATH = SUMER_PATH / "defense"
SUMER_PLAYER_PATH = SUMER_PATH / "player"

UNABATED_PATH = DATA_PATH / "unabated"

ESPN_PATH = DATA_PATH / "espn"
