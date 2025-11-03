# math_utils.py — набор численных утилит, в т.ч. статистика и линал.
from __future__ import annotations
import math
import random
from typing import Iterable, List, Tuple

def factorial_sum(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    total = 0
    for i in range(1, n + 1):
        total += math.factorial(i)
    return total

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_upto(limit: int) -> List[int]:
    return [x for x in range(2, limit + 1) if is_prime(x)]

def random_prime(limit: int) -> int:
    pool = primes_upto(limit)
    if not pool:
        raise ValueError("no primes found up to limit")
    return random.choice(pool)

def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def average(numbers: Iterable[float]) -> float:
    numbers = list(numbers)
    if not numbers:
        raise ValueError("empty sequence")
    return sum(numbers) / len(numbers)

def variance(numbers: Iterable[float]) -> float:
    xs = list(numbers)
    m = average(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

def stdev(numbers: Iterable[float]) -> float:
    return math.sqrt(variance(numbers))

def normalize(values: Iterable[float]) -> List[float]:
    vals = list(values)
    mx = max(vals)
    mn = min(vals)
    if mx == mn:
        return [0.0 for _ in vals]
    return [(v - mn) / (mx - mn) for v in vals]

def random_vector(size: int, limit: int) -> List[int]:
    return [random.randint(1, limit) for _ in range(size)]

def dot(a: Iterable[float], b: Iterable[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def magnitude(vec: Iterable[float]) -> float:
    return math.sqrt(sum(v * v for v in vec))

def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    ma = magnitude(a)
    mb = magnitude(b)
    if ma == 0 or mb == 0:
        return 0.0
    return dot(a, b) / (ma * mb)

def project(u: List[float], v: List[float]) -> List[float]:
    # Проекция u на v
    denom = dot(v, v)
    if denom == 0:
        return [0.0 for _ in v]
    scale = dot(u, v) / denom
    return [scale * vi for vi in v]

def gram_schmidt(vectors: List[List[float]]) -> List[List[float]]:
    # Ортогонализация
    ortho: List[List[float]] = []
    for v in vectors:
        w = v[:]
        for u in ortho:
            proj = project(w, u)
            w = [wi - pi for wi, pi in zip(w, proj)]
        if magnitude(w) > 1e-12:
            # нормируем
            m = magnitude(w)
            ortho.append([wi / m for wi in w])
    return ortho

def corrcoef(x: List[float], y: List[float]) -> float:
    if len(x) != len(y):
        raise ValueError("length mismatch")
    xm = average(x); ym = average(y)
    num = sum((xi - xm) * (yi - ym) for xi, yi in zip(x, y))
    den = math.sqrt(sum((xi - xm) ** 2 for xi in x) * sum((yi - ym) ** 2 for yi in y))
    return 0.0 if den == 0 else num / den

def print_statistics(numbers: Iterable[float]) -> None:
    xs = list(numbers)
    print(f"Count: {len(xs)}")
    print(f"Min: {min(xs)}, Max: {max(xs)}, Avg: {average(xs):.3f}")
    print(f"Var: {variance(xs):.3f}, Std: {stdev(xs):.3f}")

if __name__ == "__main__":
    vec = random_vector(12, 50)
    print_statistics(vec)
    print("Fibonacci(10):", fibonacci(10))
    print("Random prime up to 200:", random_prime(200))
    print("Cosine sim:", round(cosine_similarity([1,2,3], [3,2,1]), 5))
    base = [[1.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
    print("GS basis:", gram_schmidt(base))
