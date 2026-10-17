import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "net_worth_db.py"
EXPORT = ROOT / "reviews" / "2026-09" / "net-worth-export.csv"


class FinanceNetWorthDatabaseTest(unittest.TestCase):
    def test_september_export_reconciles_to_handoff_net_position(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "test.sqlite"
            subprocess.run(
                ["python3", str(SCRIPT), "import", "--db", str(db), "--input", str(EXPORT)],
                check=True,
            )
            with sqlite3.connect(db) as connection:
                total = connection.execute(
                    "SELECT SUM(gbp_value_minor) FROM current_balances"
                ).fetchone()[0]
                balance_transfers = connection.execute(
                    "SELECT SUM(gbp_value_minor) FROM current_balances WHERE category = 'balance_transfer'"
                ).fetchone()[0]
            self.assertEqual(total, 1_008_940)
            self.assertEqual(balance_transfers, -1_408_604)

    def test_refresh_loads_latest_balances_and_operating_reserves(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "test.sqlite"
            subprocess.run(["python3", str(SCRIPT), "refresh", "--db", str(db)], check=True)
            with sqlite3.connect(db) as connection:
                cleared = connection.execute(
                    "SELECT gbp_value_minor FROM current_balances WHERE component_key = ?",
                    ("debt:amex:romeo:credit-card",),
                ).fetchone()
                mands = connection.execute(
                    "SELECT as_of_date, gbp_value_minor, valuation_status FROM current_balances WHERE component_key = ?",
                    ("debt:mands:romeo:balance-transfer",),
                ).fetchone()
                bt = connection.execute(
                    """
                    SELECT booked_minor, pending_minor, projected_minor, target_minor, variance_minor
                    FROM current_operating_reserves WHERE reserve_key = ?
                    """,
                    ("reserve:bt:mands-mbna",),
                ).fetchone()
                lloyds = connection.execute(
                    """
                    SELECT booked_minor, pending_minor
                    FROM reserve_location_balances
                    WHERE reserve_key = ? AND location_key = ?
                    """,
                    ("reserve:bt:mands-mbna", "cash:lloyds:romeo:current"),
                ).fetchone()
                bad_transfers = connection.execute(
                    "SELECT COUNT(*) FROM reserve_transfer_audit WHERE entry_count != 2 OR net_minor != 0"
                ).fetchone()[0]
            self.assertEqual(cleared, (0,))
            self.assertEqual(mands, ("2026-10-17", -351_375, "estimated"))
            self.assertEqual(bt, (1_344_148, -49_700, 1_294_448, 1_344_148, 0))
            self.assertEqual(lloyds, (49_200, -49_700))
            self.assertEqual(bad_transfers, 0)

    def test_reserve_import_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "test.sqlite"
            command = ["python3", str(SCRIPT), "import-reserves", "--db", str(db)]
            subprocess.run(command, check=True)
            subprocess.run(command, check=True)
            with sqlite3.connect(db) as connection:
                counts = tuple(
                    connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                    for table in ("operating_reserves", "reserve_entries", "reserve_target_observations")
                )
            self.assertEqual(counts, (7, 18, 7))


if __name__ == "__main__":
    unittest.main()
