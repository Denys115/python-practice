import os
import time
import config
import analyzer
import logger
import utilities
import validator

file_database = {}

def run_scan():
    TARGET_DIR = config.TARGET_DIR
    ALL_EXTS = config.ALL_EXTENSIONS
    TEXT_EXTS = config.TEXT_EXTENSIONS
    LOG_FILE = config.LOG_FILE

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
            print(f"New file detected: {file_path}")
            file_database[file_path] = current_hash
        elif status == "CORRUPTED":
            alert_msg = f"SECURITY ALERT:File {file_path} has been MODIFIED"
            print(alert_msg)
            logger.write_log(alert_msg, level="CRITICAL", log_file=LOG_FILE)
            file_database[file_path] = current_hash
        if any(file_path.lower().endswith(ext) for ext in TEXT_EXTS):
            report = analyzer.analyze_file(file_path, ERROR_PATTERNS)
            if report["status"] == "analyzed":
                total_errors += report["error_lines"]
                if report["error_lines"] > 0:
                    message = f"File: {report['file']} | Errors: {report['error_lines']} | %: {report['error_percentage']}"
                    print(message)
                    logger.write_log(message, log_file=LOG_FILE)
            elif report["status"] == "permission_denied":
                logger.write_log(f"Permission denied: {report['file']}", level="ERROR", log_file=LOG_FILE)

    logger.write_log(f"Scan complete. Total text errors found: {total_errors}", log_file=LOG_FILE)

def main():
    try:
        while True:
            run_scan()
            print(f"--- Waiting {config.SCAN_INTERVAL} seconds ---")
            time.sleep(config.SCAN_INTERVAL)
    except KeyboardInterrupt:
        print("\nClosing FileGuardian...")
if __name__ == "__main__":
    main()