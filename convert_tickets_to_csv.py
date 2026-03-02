import json
import csv
import re
from pathlib import Path

def convert_jsonl_to_csv() -> None:
    input_file = Path("tickets.jsonl")
    output_file = Path("tickets.csv")
    
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    data = []
    object_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.finditer(object_pattern, content, re.DOTALL)
    
    for match in matches:
        try:
            obj = json.loads(match.group())
            data.append(obj)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar: {e}")
    
    if not data:
        print("Nenhum ticket encontrado.")
        return
    
    fieldnames = data[0].keys()
    
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✓ Arquivo convertido com sucesso!")
    print(f"✓ Total de tickets: {len(data)}")
    print(f"✓ Arquivo salvo em: {output_file.absolute()}")

if __name__ == "__main__":
    convert_jsonl_to_csv()
