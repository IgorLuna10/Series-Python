# 🐍 Python Exercises — IMIE Paris

> A collection of Python programming exercises completed as part of the **Titre Professionnel DWWM** training at IMIE Paris.

---

## 📁 Structure

```
Series-Python/
├── Serie 1 Python/     # Variables, types, input/output, conditions, loops, functions
├── Serie 2 Python/     # Strings, lists, dicts, files, JSON
├── Serie 4 Python/     # Error handling, custom exceptions
├── Serie 5 Python/     # LBYL vs EAFP, type hints, docstrings
├── Serie 6 Python/     # OOP — classes, inheritance, composition, Matplotlib
├── Serie 7 Python/     # Data visualisation with Matplotlib + CSV
└── Serie 10 Python/    # OOP advanced, HTTP requests, REST API
```

---

## 📚 Serie 1 — Fundamentals

| Exercise | Description |
|----------|-------------|
| `serie01_exercice01.py` | Rectangle — area and perimeter from user input |
| `serie01_exercice02.py` | TVA calculator — compute TTC from HT price and tax rate |
| `serie01_exercice03.py` | Cinema ticket pricing by age with error handling |
| `serie01_exercice04.py` | Multiplication table (`for`) + sum 1 to 10 (`while`) |
| `serie01_exercice05.py` | List of prices — iterate, sum, average |
| `serie01_exercice06.py` | Functions — `est_pair()`, `calculer_tva()`, `moyenne()` |

**Concepts:** variables, arithmetic, `input()`, conditionals, loops, functions, lists

---

## 📚 Serie 2 — Data Structures & Files

| Exercise | Description |
|----------|-------------|
| `serie02_exercice01.py` | Password validator — length, uppercase, lowercase, digit checks |
| `serie02_exercice02.py` | Grade analysis — min, max, average, pass rate |
| `serie02_exercice03.py` | Order management — filter by status, count, total per client |
| `serie02_exercice05.py` | Read grades from `notes.txt` — file I/O + statistics |
| `serie02_exercice06.py` | Parse CSV-like `text.txt` → list of dicts, use `structures.py` |
| `serie02_exercice07.py` | JSON export/import — save and reload orders with `json` module |
| `serie02_exercice08.py` | Dashboard — revenue, status counts, top clients sorted by spend |
| `structures.py` | Shared module — `total_paid()`, `count_status()`, `total_spent_by_client()` |

**Data files:** `notes.txt`, `text.txt`, `commandes.json`

**Concepts:** strings, lists, dicts, file I/O, JSON, modules, sorting

---

## 📚 Serie 4 — Error Handling & Exceptions

| Exercise | Description |
|----------|-------------|
| `serie04_exercice01.py` | Age input loop — `ValueError`, negative/over-110 guard |
| `serie04_exercice02.py` | Division — handle `ValueError` and `ZeroDivisionError` |
| `serie04_exercice03.py` | Product list index — handle `ValueError` and `IndexError` |
| `serie04_exercice04.py` | Safe file reader — `FileNotFoundError` with graceful fallback |
| `serie04_exercice05.py` | Custom exception `CommandeInvalideError` for order validation |

**Concepts:** `try/except/else`, custom exceptions, input validation, file safety

---

## 📚 Serie 5 — Best Practices & Type Hints

| Exercise | Description |
|----------|-------------|
| `serie05_exercice01.py` | LBYL vs EAFP — two approaches to dict key access |
| `serie05_exercice02.py` | File existence — `os.path.exists()` vs `try/except` |
| `serie05_exercice03.py` | Type-annotated functions — `calculer_moyenne()`, `filtrer_notes_suffisantes()`, `formater_message()` |
| `serie05_exercice04.py` | Documented functions — `appliquer_remise()`, `compter_commandes_superieures()`, `normaliser_email()` |

**Concepts:** LBYL, EAFP, type hints (`list[float]`, `str`, `int`), docstrings, `help()`

---

## 📚 Serie 6 — Object-Oriented Programming

| Exercise | Description |
|----------|-------------|
| `serie06_exercice01.py` | `Rectangle` class — `surface()`, `perimetre()`, `afficher()` |
| `serie06_exercice02.py` | `CompteBancaire` — `deposer()`, `retirer()` with validation |
| `serie06_exercice03.py` | `Produit` — `prix_ttc()`, `valeur_stock_ttc()`, catalogue loop |
| `serie06_exercice04.py` | Inheritance — `Employe` → `Developer` + `Manager` with `super()` |
| `serie06_exercice05.py` | Composition — `Client`, `LigneCommande`, `Commande` with `total()` |
| `dashboard_viz.py` | E-commerce dashboard — reads CSV, 4-panel Matplotlib chart |

**Concepts:** classes, `__init__`, methods, inheritance, `super()`, composition, Matplotlib

---

## 📚 Serie 7 — Data Visualisation

| Exercise | Description |
|----------|-------------|
| `serie07_exercice01.py` | Line chart — 7-day website traffic with `plt.plot()` |
| `serie07_exercice02.py` | Bar chart — smartphone prices by brand with `plt.bar()` |
| `serie07_exercice03.py` | Scatter plot — traffic vs revenue correlation |
| `serie07_exercice04.py` | Histogram — revenue distribution with `plt.hist()` |
| `serie07_exercice05.py` | Line chart from CSV — daily revenue from `ventes_journalieres.csv` |
| `serie07_exercice06.py` | Subplots — traffic and revenue side by side with `plt.subplot()` |
| `serie07_exercice07.py` | Bar chart — weekly revenue aggregation from CSV |
| `serie07_exercice08.py` | Box plot — revenue distribution weeks 1-2 vs 3-4 |
| `serie07_exercice09.py` | Moving average — 3-day rolling mean overlaid on daily revenue |

**Data files:** `ventes_journalieres.csv`

**Concepts:** Matplotlib (`plot`, `bar`, `scatter`, `hist`, `boxplot`, `subplot`), CSV reading, moving averages

---

## 📚 Serie 10 — Advanced OOP & HTTP Requests

| Exercise | Description |
|----------|-------------|
| `serie10_exercice01.py` | `Produit` + `Catalogue` classes — filter by category, stock check, average price |
| `serie10_exercice02.py` | HTTP GET with `requests` — fetch posts from JSONPlaceholder API |
| `serie10_exercice03.py` | API stats — posts per user, average title length, top 3 most active users |
| `serie10_exercice04.py` | `JsonPlaceholderClient` class — `requests.Session`, `get_posts()`, `get_post(id)` |

**Concepts:** advanced OOP, `requests`, REST APIs, `Session`, error handling, data aggregation

---

## ▶️ Running an exercise

Most exercises require only Python 3:

```bash
python3 "Serie 1 Python/serie01_exercice01.py"
```

Serie 7, `dashboard_viz.py` require Matplotlib:

```bash
pip install matplotlib
python3 "Serie 7 Python/serie07_exercice01.py"
```

Serie 10 requires the `requests` library:

```bash
pip install requests
python3 "Serie 10 Python/serie10_exercice02.py"
```

Some Serie 2 and 7 exercises require data files in the same directory:

```bash
cd "Serie 2 Python"
python3 serie02_exercice05.py
```

---

## 👨‍💻 Author

**Igor Luna de Oliveira** — Candidat DWWM · Session Mai 2026 · IMIE Paris
[github.com/IgorLuna10](https://github.com/IgorLuna10)
