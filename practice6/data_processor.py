# data_processor.py — мини-пайплайн генерации/аналитики данных и JSON I/O.
from __future__ import annotations
import json
import random
import statistics
from typing import Dict, List

def generate_students(n: int) -> List[Dict]:
    rng = random.Random(1337)
    return [{"id": i, "name": f"Student {i}", "score": rng.randint(40, 100)} for i in range(1, n + 1)]

def save_to_json(data: List[Dict], filename: str = "students.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_from_json(filename: str = "students.json") -> List[Dict]:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_top_students(data: List[Dict], threshold: int = 90) -> List[Dict]:
    return [s for s in data if s["score"] >= threshold]

def average_score(data: List[Dict]) -> float:
    return statistics.mean(s["score"] for s in data) if data else 0.0

def median_score(data: List[Dict]) -> float:
    scores = [s["score"] for s in data]
    return statistics.median(scores) if scores else 0.0

def grade(score: int) -> str:
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def grade_distribution(data: List[Dict]) -> Dict[str, int]:
    grades = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for s in data:
        g = grade(s["score"])
        grades[g] += 1
    return grades

def curve_scores(data: List[Dict], bonus: int = 5, cap: int = 100) -> List[Dict]:
    curved = []
    for s in data:
        val = min(s["score"] + bonus, cap)
        curved.append({**s, "score": val})
    return curved

def percentile(data: List[Dict], p: float) -> float:
    if not (0 <= p <= 100):
        raise ValueError("p in [0,100]")
    scores = sorted(s["score"] for s in data)
    if not scores:
        return 0.0
    k = (len(scores) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(scores) - 1)
    if f == c:
        return scores[int(k)]
    return scores[f] + (scores[c] - scores[f]) * (k - f)

def print_report(data: List[Dict]) -> None:
    print("Students:", len(data))
    print("Average:", round(average_score(data), 2))
    print("Median:", round(median_score(data), 2))
    print("Grades:", grade_distribution(data))
    print("P90:", percentile(data, 90))

def export_csv(data: List[Dict], filename: str = "students.csv") -> None:
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "score", "grade"])
        for s in data:
            w.writerow([s["id"], s["name"], s["score"], grade(s["score"])])

def main() -> None:
    data = generate_students(30)
    save_to_json(data)
    print_report(data)
    print("Top students:", len(filter_top_students(data)))
    curved = curve_scores(data, bonus=7)
    export_csv(curved)

if __name__ == "__main__":
    main()
