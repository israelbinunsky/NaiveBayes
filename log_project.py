def log(log):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log)