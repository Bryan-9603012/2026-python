from collections import Counter, defaultdict, namedtuple
from pathlib import Path
import unicodedata

General = namedtuple("General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"])


def display_width(text):
    width = 0
    for ch in text:
        width += 2 if unicodedata.east_asian_width(ch) in {"W", "F"} else 1
    return width


def ljust_display(text, width):
    return text + " " * max(0, width - display_width(text))


class ChibiBattleEasy:
    def __init__(self):
        self.generals = {}
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def load_generals(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                faction, name, hp, atk, def_, spd, is_leader = line.split()
                self.generals[name] = General(
                    faction, name, int(hp), int(atk), int(def_), int(spd), is_leader == "True"
                )

    def get_battle_order(self):
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)

    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        return damage

    def simulate_battle(self):
        shu = [g for g in self.generals.values() if g.faction == "蜀"]
        wu = [g for g in self.generals.values() if g.faction == "吳"]
        wei = [g for g in self.generals.values() if g.faction == "魏"]
        attackers = shu + wu
        for i, attacker in enumerate(attackers):
            target = wei[i % len(wei)]
            self.calculate_damage(attacker.name, target.name)

    def get_damage_ranking(self, top_n=5):
        return self.stats["damage"].most_common(top_n)


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    game = ChibiBattleEasy()
    game.load_generals(str(base / "generals.txt"))
    game.simulate_battle()
    for idx, (name, dmg) in enumerate(game.get_damage_ranking(), start=1):
        print(f"{ljust_display(str(idx) + '. ' + name, 10)} {dmg:3} HP")
