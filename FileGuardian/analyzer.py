import os
from datetime import datetime, timedelta

def scan_files(directory, hours=24, extensions=None, recursive=False):
    if not os.path.isdir(directory):
        raise ValueError(f"Directory does not exist: {directory}")
    recent_files = []
    now = datetime.now()
    cutoff = now - timedelta(hours=hours)

    walker = os.walk(directory) if recursive else [
        (directory, [], os.listdir(directory))
    ]

    for root, _, files in walker:
        for file in files:
            full_path = os.path.join(root, file)
            if extensions:
                if not any(file.lower().endswith(ext.lower()) for ext in extensions):
                    continue
            try:
                modification_time = datetime.fromtimestamp(
                    os.path.getmtime(full_path)
                )

                if modification_time >= cutoff:
                    recent_files.append(full_path)

            except PermissionError:
                continue

            except OSError:
                continue

    return recent_files


def analyze_file(file_path, patterns):
    if not patterns:
        raise ValueError("Patterns list cannot be empty")

    results = {pattern: 0 for pattern in patterns}
    total_lines = 0
    total_error_lines = 0

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                total_lines += 1
                line_has_error = False

                for pattern in patterns:
                    if pattern.lower() in line.lower():
                        results[pattern] += 1
                        line_has_error = True

                if line_has_error:
                    total_error_lines += 1

    except PermissionError:
        return {"file": file_path, "status": "permission_denied"}

    except Exception as e:
        return {
            "file": file_path,
            "status": "error",
            "message": str(e)
        }
    percentage = (total_error_lines / total_lines * 100) if total_lines else 0

    return {
        "file": file_path,
        "status": "analyzed",
        "total_lines": total_lines,
        "error_lines": total_error_lines,
        "error_percentage": round(percentage, 2),
        "patterns": results
    }

def analyze_directory(directory, patterns, hours=24, extensions=None, recursive=False):
    files = scan_files(directory, hours, extensions, recursive)
    results = []
    for file_path in files:
        results.append(analyze_file(file_path, patterns))
    return results