from pathlib import Path

file = Path("data/Test.xlsx")

print("Exists:", file.exists())
print("Size:", file.stat().st_size)

with open(file, "rb") as f:
    first16 = f.read(16)

print("First 16 bytes:", first16)