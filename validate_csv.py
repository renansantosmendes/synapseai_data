import csv

with open("tickets.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print(f"Total de tickets no CSV: {len(rows)}")
    print(f"Colunas: {list(rows[0].keys())}")
    print()
    print("Primeiros 3 tickets:")
    for i, row in enumerate(rows[:3]):
        print(f"{i+1}. {row['customer_name']} - {row['product_name']} ({row['opening_date']})")
