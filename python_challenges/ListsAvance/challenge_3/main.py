students = [
    {"name": "Alice", "note": 85},
    {"name": "Abedlhadi", "note": 45},
    {"name": "Bob", "note": 92},
    {"name": "Charlie", "note": 78}
]

print(sorted(students, key= lambda x: x["note"], reverse=False)
)


