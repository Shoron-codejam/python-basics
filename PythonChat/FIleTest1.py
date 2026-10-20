from pathlib import Path

file_path = Path(__file__).parent / "myname.txt"

file = open(file_path, "w")
file.write("My name is Khalid\nI am learning Python.")
file.close()