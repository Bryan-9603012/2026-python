import unittest
from pathlib import Path

from chibi_battle import ChibiBattle


class TestChibiBattle(unittest.TestCase):
    def setUp(self):
        self.base = Path(__file__).resolve().parent.parent
        self.game = ChibiBattle()
        self.game.load_generals(str(self.base / "generals.txt"))
        self.game.load_battles(str(self.base / "battles.txt"))

    def test_load_generals_from_file(self):
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn("劉備", self.game.generals)
        self.assertIn("曹操", self.game.generals)

    def test_parse_general_attributes(self):
        general = self.game.generals["關羽"]
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self):
        factions = {}
        for general in self.game.generals.values():
            factions[general.faction] = factions.get(general.faction, 0) + 1
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        self.assertEqual(len(self.game.generals), 9)

    def test_load_battle_config(self):
        self.assertEqual(self.game.battle_config["battle_name"], "赤壁")
        self.assertEqual(self.game.battle_config["waves"], 3)

    def test_battle_order_by_speed(self):
        battle_order = self.game.get_battle_order()
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)

    def test_calculate_damage(self):
        damage = self.game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

    def test_damage_counter_accumulation(self):
        self.game.calculate_damage("關羽", "夏侯惇")
        self.game.calculate_damage("關羽", "曹操")
        self.assertEqual(self.game.stats["damage"]["關羽"], 26)

    def test_simulate_one_wave(self):
        self.game.simulate_wave(1)
        total_damage = sum(self.game.stats["damage"].values())
        self.assertGreater(total_damage, 0)

    def test_simulate_three_waves(self):
        self.game.simulate_battle()
        alliance_damage = sum(
            dmg
            for name, dmg in self.game.stats["damage"].items()
            if self.game.generals[name].faction in ["蜀", "吳"]
        )
        self.assertGreater(alliance_damage, 0)

    def test_troop_loss_tracking(self):
        self.game.simulate_battle()
        self.assertGreater(sum(self.game.stats["losses"].values()), 0)

    def test_damage_ranking_most_common(self):
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"], 0)
        self.assertGreater(faction_stats["吳"], 0)

    def test_defeated_generals(self):
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        self.assertIsInstance(defeated, list)

    def test_render_battle_start(self):
        output = self.game.render_battle_start()
        self.assertIn("赤壁戰役", output)
        self.assertIn("蜀軍", output)

    def test_render_damage_report(self):
        self.game.simulate_battle()
        output = self.game.render_damage_report()
        self.assertIn("傷害統計報告", output)
        self.assertIn("勢力傷害統計", output)

    def test_run_full_battle(self):
        output = self.game.run_full_battle()
        self.assertIn("赤壁戰役", output)
        self.assertIn("傷害輸出排名", output)


if __name__ == "__main__":
    unittest.main()
