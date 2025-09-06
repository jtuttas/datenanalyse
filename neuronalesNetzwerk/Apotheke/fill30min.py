
"""
Fill 30-minute timeline and set missing counts to 0.

Usage:
  python fill_30min.py \
    --input apotheke_sales.csv \
    --output apotheke_sales_filled.csv \
    --dupe-policy first

Dupe policies: first, sum, mean, median, max
"""
import argparse
import sys
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Fill 30-minute gaps with count=0.")
    parser.add_argument("--input", "-i", default="apotheke_sales.csv",
                        help="Pfad zur Eingabedatei (CSV) mit Spalten: timestamp,count")
    parser.add_argument("--output", "-o", default="apotheke_sales_filled.csv",
                        help="Pfad zur Ausgabedatei (CSV)")
    parser.add_argument("--dupe-policy", "-d", default="first",
                        choices=["first", "sum", "mean", "median", "max"],
                        help="Wie mit doppelten Zeitstempeln umgehen (default: first)")
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"Fehler: Eingabedatei nicht gefunden: {in_path}", file=sys.stderr)
        sys.exit(1)

    # Einlesen
    df = pd.read_csv(in_path, parse_dates=["timestamp"])
    if "timestamp" not in df.columns or "count" not in df.columns:
        print("Fehler: CSV braucht Spalten 'timestamp' und 'count'.", file=sys.stderr)
        sys.exit(1)

    # count numerisch und fehlende/komische Werte behandeln
    df["count"] = pd.to_numeric(df["count"], errors="coerce")

    # Sortieren für stabile Operationen
    df = df.sort_values("timestamp")

    # Duplikate behandeln
    if args.dupe_policy == "first":
        df = df.drop_duplicates(subset=["timestamp"], keep="first")
    else:
        agg_map = {
            "sum": "sum",
            "mean": "mean",
            "median": "median",
            "max": "max",
        }[args.dupe_policy]
        df = df.groupby("timestamp", as_index=False).agg({"count": agg_map})

    # Zeitspanne bestimmen
    if df.empty:
        print("Warnung: Eingabedatei enthält keine Daten. Schreibe leere Ausgabe.")
        pd.DataFrame(columns=["timestamp", "count"]).to_csv(args.output, index=False)
        sys.exit(0)

    start = df["timestamp"].min()
    end = df["timestamp"].max()

    # Auf 30-Minuten-Raster ausrichten (floor/ceil), behält vorhandene Zeitzone bei
    start = start.floor("30min")
    end = end.ceil("30min")

    # Vollständigen Index bauen
    full_index = pd.date_range(start=start, end=end, freq="30min")

    # Reindex, fehlende mit 0 füllen
    out = (
        df.set_index("timestamp")
          .reindex(full_index)
          .rename_axis("timestamp")
          .assign(count=lambda d: d["count"].fillna(0).astype(int))
          .reset_index()
    )

    # Speichern
    out.to_csv(args.output, index=False)
    print(f"Fertig. Geschrieben: {args.output}  (Zeilen: {len(out)})")


if __name__ == "__main__":
    main()
