import os
import time
import config
import analyzer
import logger
import utilities
import validator
import sorter

file_database = {}

def run_scan():
    TARGET_DIR = config.TARGET_DIR
    SORTED_DIR = config.SORTED_DIR
    ALL_EXTS = config.ALL_EXTENSIONS
    TEXT_EXTS = config.TEXT_EXTENSIONS
    LOG_FILE = config.LOG_FILE
    ERROR_PATTERNS = config.ERROR_PATTERNS

    logger.write_log("Starting File Guardian system scan...", log_file=LOG_FILE)

    if not os.path.exists(TARGET_DIR):
        logger.write_log(f"Directory {TARGET_DIR} is missing!", level="CRITICAL", log_file=LOG_FILE)
        return

    files_to_watch = analyzer.scan_files(TARGET_DIR, extensions=ALL_EXTS)
    total_errors = 0

    for file_path in files_to_watch:
        current_hash = utilities.get_file_hash(file_path)
        stored_hash = file_database.get(file_path)
        status = validator.check_integrity(current_hash, stored_hash)

        if status == "NEW":
            print(f"[NEW] File detected: {file_path}")
            file_database[file_path] = current_hash
        elif status == "CORRUPTED":
            alert_msg = f"SECURITY ALERT: File {file_path} has been MODIFIED"
            print(alert_msg)
            logger.write_log(alert_msg, level="CRITICAL", log_file=LOG_FILE)
            file_database[file_path] = current_hash

        if any(file_path.lower().endswith(ext) for ext in TEXT_EXTS):
            report = analyzer.analyze_file(file_path, ERROR_PATTERNS)
            
            if report["status"] == "analyzed":
                total_errors += report["error_lines"]
                if report["error_lines"] > 0:
                    message = f"File: {report['file']} | Errors: {report['error_lines']} | %: {report['error_percentage']}"
                    print(f"[REPORT] {message}")
                    logger.write_log(message, log_file=LOG_FILE)
            elif report["status"] == "permission_denied":
                logger.write_log(f"Permission denied: {report['file']}", level="ERROR", log_file=LOG_FILE)

        new_path = sorter.sort_files_by_extension(file_path, SORTED_DIR)
        if new_path != file_path:
            file_database[new_path] = current_hash
            if file_path in file_database:
                del file_database[file_path]

    logger.write_log(f"Scan complete. Total errors found: {total_errors}", log_file=LOG_FILE)

def main():
    print("--- File Guardian is Running ---")
    try:
        while True:
            run_scan()
            print(f"--- Sleeping {config.SCAN_INTERVAL}s ---")
            time.sleep(config.SCAN_INTERVAL)
    except KeyboardInterrupt:
        print("\n[STOP] Closing File Guardian...")

if __name__ == "__main__":
    main()