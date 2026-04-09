from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path
from typing import Dict, List, Tuple

General = namedtuple(
    "General", ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"]
)


class ChibiBattle:
    """三國武將 PK 版 - 赤壁戰役遊戲引擎"""

    def __init__(self) -> None:
        self.generals: Dict[str, General] = {}
        self.battle_config: Dict[str, object] = {}
        self.reset_stats()

    def reset_stats(self) -> None:
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }

    def load_generals(self, filename: str) -> None:
        self.generals.clear()
        path = Path(filename)
        with path.open("r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 7:
                    raise ValueError(f"武將資料格式錯誤: {line}")
                faction, name, hp, atk, def_, spd, is_leader = parts
                self.generals[name] = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                )

    def load_battles(self, filename: str) -> None:
        path = Path(filename)
        with path.open("r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if line == "EOF":
                    break
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 5 or parts[1] != "vs":
                    raise ValueError(f"戰役資料格式錯誤: {line}")
                self.battle_config = {
                    "alliance": parts[0],
                    "enemy": parts[2],
                    "battle_name": parts[3],
                    "waves": int(parts[4]),
                }
                break

    def get_battle_order(self) -> List[General]:
        return sorted(self.generals.values(), key=lambda g: (-g.spd, g.name))

    def get_generals_by_faction(self, faction: str) -> List[General]:
        return sorted(
            [g for g in self.generals.values() if g.faction == faction],
            key=lambda g: (-g.spd, g.name),
        )

    def calculate_damage(self, attacker_name: str, defender_name: str) -> int:
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        return damage

    def is_alive(self, general_name: str) -> bool:
        return self.stats["losses"][general_name] < self.generals[general_name].hp

    def get_alive_generals(self, factions: List[str] | None = None) -> List[General]:
        alive = [g for g in self.generals.values() if self.is_alive(g.name)]
        if factions is not None:
            alive = [g for g in alive if g.faction in factions]
        return sorted(alive, key=lambda g: (-g.spd, g.name))

    def choose_target(self, attacker: General) -> General | None:
        if attacker.faction == "魏":
            enemies = self.get_alive_generals(["蜀", "吳"])
        else:
            enemies = self.get_alive_generals(["魏"])
        if not enemies:
            return None
        return min(
            enemies,
            key=lambda g: (
                self.stats["losses"][g.name] / g.hp,
                g.hp - self.stats["losses"][g.name],
                g.name,
            ),
        )

    def simulate_wave(self, wave_num: int) -> List[Tuple[str, str, int]]:
        logs: List[Tuple[str, str, int]] = []
        active_count = min(len(self.generals), wave_num * 3)
        turn_order = self.get_battle_order()[:active_count]

        for attacker in turn_order:
            if not self.is_alive(attacker.name):
                continue
            target = self.choose_target(attacker)
            if target is None:
                break
            damage = self.calculate_damage(attacker.name, target.name)
            logs.append((attacker.name, target.name, damage))
        return logs

    def simulate_battle(self) -> None:
        self.reset_stats()
        waves = int(self.battle_config.get("waves", 3))
        for wave in range(1, waves + 1):
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n: int = 5):
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self) -> Dict[str, int]:
        faction_damage = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self) -> List[str]:
        defeated = []
        for name, total_loss in self.stats["losses"].items():
            if total_loss >= self.generals[name].hp:
                defeated.append(name)
        return sorted(defeated)

    def render_battle_start(self) -> str:
        lines = []
        lines.append("╔═══════════════════════════════════════════════════════╗")
        lines.append("║        吞食天地 - 赤壁戰役 │ 蜀吳聯軍 vs 曹操魏軍      ║")
        lines.append("╚═══════════════════════════════════════════════════════╝")
        for faction in ["蜀", "吳", "魏"]:
            lines.append("")
            lines.append(f"【{faction}軍】")
            for g in self.get_generals_by_faction(faction):
                hp_blocks = max(1, min(10, g.hp // 10))
                bar = "█" * hp_blocks + "░" * (10 - hp_blocks)
                leader = " (軍師)" if g.is_leader else ""
                lines.append(
                    f"  ⚔ {g.name:4} {bar} 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}"
                )
        return "\n".join(lines)

    def render_damage_report(self) -> str:
        lines = []
        lines.append("╔═══════════════════════════════════════════════════════╗")
        lines.append("║              【赤壁戰役 - 傷害統計報告】               ║")
        lines.append("╚═══════════════════════════════════════════════════════╝")
        lines.append("")
        lines.append("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), start=1):
            bar_len = min(20, max(1, dmg // 3))
            bar = "█" * bar_len + "░" * (20 - bar_len)
            lines.append(f"  {i}. {name:4} {bar} {dmg:3} HP")
        lines.append("")
        lines.append("【兵力損失統計】")
        for name, loss in sorted(self.stats["losses"].items(), key=lambda item: item[1], reverse=True):
            defeated_mark = "✓" if loss >= self.generals[name].hp else " "
            lines.append(f"  {defeated_mark} {name:4} → 損失 {loss:3} 兵力")
        lines.append("")
        lines.append("【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        max_damage = max(faction_stats.values()) if faction_stats else 1
        total_damage = sum(faction_stats.values()) if faction_stats else 1
        for faction in ["蜀", "吳", "魏"]:
            total = faction_stats.get(faction, 0)
            ratio = int((total / max_damage) * 20) if max_damage else 0
            bar = "█" * ratio + "░" * (20 - ratio)
            percentage = (total / total_damage * 100) if total_damage else 0
            lines.append(f"  {faction} {bar} {total:3} HP ({percentage:5.1f}%)")
        return "\n".join(lines)

    def run_full_battle(self) -> str:
        self.simulate_battle()
        return self.render_battle_start() + "\n\n" + self.render_damage_report()


if __name__ == "__main__":
    game = ChibiBattle()
    base = Path(__file__).resolve().parent.parent
    game.load_generals(str(base / "generals.txt"))
    game.load_battles(str(base / "battles.txt"))
    print(game.run_full_battle())
