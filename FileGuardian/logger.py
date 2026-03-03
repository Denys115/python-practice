from datetime import datetime


def write_log(message, level="INFO", log_file="audit.log"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")