def log(log):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log)
def show_log():
    with open("log.txt", "r", encoding="utf-8") as f:
        file = f.read()
        print(file)