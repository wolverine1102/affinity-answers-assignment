def save_to_file(records: dict):
    with open("static/results.txt", "w") as f:
        for key, value in records.items():
            f.write(f"{key} : {value}\n")
        f.close()