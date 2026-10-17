#!/usr/bin/env python3
"""Load and query FinanceOS net-worth exports in a local SQLite database."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "private-data" / "finance.sqlite"
MIGRATIONS = ROOT / "database" / "migrations"
RESERVE_DEFINITIONS = ROOT / "data" / "operating-reserves.csv"
RESERVE_ENTRIES = ROOT / "data" / "reserve-ledger.csv"
RESERVE_TARGETS = ROOT / "data" / "reserve-targets.csv"
CURRENT_UPDATES = ROOT / "data" / "current-balance-observations.csv"


def latest_export() -> Path:
    candidates = [
        path for path in (ROOT / "reviews").glob("*/net-worth-export.csv")
        if path.parent.name != "2026-06-example"
    ]
    if not candidates:
        raise FileNotFoundError("No review net-worth export exists")
    return max(candidates, key=lambda path: path.parent.name)


def minor(value: str) -> int:
    return int((Decimal(value) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def initialize(connection: sqlite3.Connection) -> None:
    for migration in sorted(MIGRATIONS.glob("*.sql")):
        connection.executescript(migration.read_text(encoding="utf-8"))
        connection.execute(
            "INSERT OR IGNORE INTO schema_migrations(version) VALUES (?)", (migration.stem,)
        )
    connection.commit()


def load_export(connection: sqlite3.Connection, path: Path) -> int:
    count = 0
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            connection.execute(
                """
                INSERT INTO balance_observations(
                    component_key, source_record_id, as_of_date, owner, component_name,
                    category, balance_kind, native_currency, native_value_minor,
                    gbp_value_minor, inclusion_scope, valuation_status, source_ref,
                    source_date, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_record_id, as_of_date) DO UPDATE SET
                    component_key=excluded.component_key,
                    owner=excluded.owner,
                    component_name=excluded.component_name,
                    category=excluded.category,
                    balance_kind=excluded.balance_kind,
                    native_currency=excluded.native_currency,
                    native_value_minor=excluded.native_value_minor,
                    gbp_value_minor=excluded.gbp_value_minor,
                    inclusion_scope=excluded.inclusion_scope,
                    valuation_status=excluded.valuation_status,
                    source_ref=excluded.source_ref,
                    source_date=excluded.source_date,
                    notes=excluded.notes
                """,
                (
                    row["component_key"], row["source_record_id"], row["as_of_date"], row["owner"],
                    row["component_name"], row["category"], row["balance_kind"], row["currency"],
                    minor(row["native_value"]), minor(row["gbp_value"]), row["inclusion_scope"],
                    row["valuation_status"], row["source_ref"], row["source_date"], row["notes"],
                ),
            )
            count += 1
    connection.commit()
    return count


def load_reserves(
    connection: sqlite3.Connection,
    definitions_path: Path,
    entries_path: Path,
    targets_path: Path,
) -> tuple[int, int, int]:
    definition_count = entry_count = target_count = 0
    with definitions_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            connection.execute(
                """
                INSERT INTO operating_reserves(
                    reserve_key, reserve_name, owner, currency, purpose,
                    authoritative_source, status, linked_component_key, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(reserve_key) DO UPDATE SET
                    reserve_name=excluded.reserve_name,
                    owner=excluded.owner,
                    currency=excluded.currency,
                    purpose=excluded.purpose,
                    authoritative_source=excluded.authoritative_source,
                    status=excluded.status,
                    linked_component_key=excluded.linked_component_key,
                    notes=excluded.notes
                """,
                (
                    row["reserve_key"], row["reserve_name"], row["owner"], row["currency"],
                    row["purpose"], row["authoritative_source"], row["status"],
                    row["linked_component_key"] or None, row["notes"],
                ),
            )
            definition_count += 1
    with entries_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            connection.execute(
                """
                INSERT INTO reserve_entries(
                    entry_key, reserve_key, effective_date, location_key, entry_type,
                    amount_minor, verification_status, source_system, source_ref,
                    source_date, transfer_group_key, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(entry_key) DO UPDATE SET
                    reserve_key=excluded.reserve_key,
                    effective_date=excluded.effective_date,
                    location_key=excluded.location_key,
                    entry_type=excluded.entry_type,
                    amount_minor=excluded.amount_minor,
                    verification_status=excluded.verification_status,
                    source_system=excluded.source_system,
                    source_ref=excluded.source_ref,
                    source_date=excluded.source_date,
                    transfer_group_key=excluded.transfer_group_key,
                    notes=excluded.notes
                """,
                (
                    row["entry_key"], row["reserve_key"], row["effective_date"],
                    row["location_key"], row["entry_type"], minor(row["amount"]),
                    row["verification_status"], row["source_system"], row["source_ref"],
                    row["source_date"] or None, row["transfer_group_key"] or None, row["notes"],
                ),
            )
            entry_count += 1
    with targets_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            connection.execute(
                """
                INSERT INTO reserve_target_observations(
                    target_key, reserve_key, as_of_date, target_minor,
                    verification_status, source_system, source_ref, source_date, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(target_key) DO UPDATE SET
                    reserve_key=excluded.reserve_key,
                    as_of_date=excluded.as_of_date,
                    target_minor=excluded.target_minor,
                    verification_status=excluded.verification_status,
                    source_system=excluded.source_system,
                    source_ref=excluded.source_ref,
                    source_date=excluded.source_date,
                    notes=excluded.notes
                """,
                (
                    row["target_key"], row["reserve_key"], row["as_of_date"],
                    minor(row["target_amount"]), row["verification_status"],
                    row["source_system"], row["source_ref"], row["source_date"] or None,
                    row["notes"],
                ),
            )
            target_count += 1
    connection.commit()
    return definition_count, entry_count, target_count


def report(connection: sqlite3.Connection) -> None:
    rows = connection.execute(
        """
        SELECT component_key, component_name, owner, category, as_of_date,
               valuation_status, gbp_value_minor
        FROM current_balances ORDER BY category, component_name
        """
    ).fetchall()
    for row in rows:
        print("\t".join(str(value) for value in (*row[:-1], f"{row[-1] / 100:.2f}")))
    print(f"TOTAL_GBP\t{sum(row[-1] for row in rows) / 100:.2f}")


def reserve_report(connection: sqlite3.Connection) -> None:
    rows = connection.execute(
        """
        SELECT reserve_key, reserve_name, booked_minor, pending_minor,
               projected_minor, target_minor, variance_minor
        FROM current_operating_reserves ORDER BY reserve_key
        """
    ).fetchall()
    for row in rows:
        formatted = list(row[:2]) + [
            "" if value is None else f"{value / 100:.2f}" for value in row[2:]
        ]
        print("\t".join(str(value) for value in formatted))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", choices=("init", "import", "import-reserves", "refresh", "report", "reserve-report")
    )
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--definitions", type=Path, default=RESERVE_DEFINITIONS)
    parser.add_argument("--entries", type=Path, default=RESERVE_ENTRIES)
    parser.add_argument("--targets", type=Path, default=RESERVE_TARGETS)
    args = parser.parse_args()

    args.db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(args.db) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        initialize(connection)
        if args.command == "import":
            source = args.input or latest_export()
            print(f"Imported {load_export(connection, source)} FinanceOS balances from {source}")
        elif args.command == "import-reserves":
            counts = load_reserves(connection, args.definitions, args.entries, args.targets)
            print(f"Imported {counts[0]} reserves, {counts[1]} entries and {counts[2]} targets")
        elif args.command == "refresh":
            source = args.input or latest_export()
            balance_count = load_export(connection, source)
            update_count = load_export(connection, CURRENT_UPDATES) if CURRENT_UPDATES.exists() else 0
            counts = load_reserves(connection, args.definitions, args.entries, args.targets)
            print(
                f"Imported {balance_count} locked balances, {update_count} operational updates, "
                f"{counts[0]} reserves, {counts[1]} entries and {counts[2]} targets"
            )
        elif args.command == "report":
            report(connection)
        elif args.command == "reserve-report":
            reserve_report(connection)


if __name__ == "__main__":
    main()
