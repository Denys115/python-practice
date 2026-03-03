import os
import analyzer
import logger

def main():
    TARGET_DIR = "logs"
    ERROR_PATTERNS = ["ERROR", "FATAL", "CRITICAL"]
    logger.write_log("Starting File Guardian system scan...")

    if not os.path.isdir(TARGET_DIR):
        logger.write_log(
            f"Directory {TARGET_DIR} is missing!",
            level="CRITICAL")
        return
    results = analyzer.analyze_directory(TARGET_DIR, ERROR_PATTERNS)
    total_errors = 0

    for report in results:
        if report["status"] == "analyzed":
            total_errors += report["error_lines"]
            message = (
                f"File: {report['file']} | "
                f"Errors: {report['error_lines']} | "
                f"Error %: {report['error_percentage']}")
            logger.write_log(message)
            print(message)
        elif report["status"] == "permission_denied":
            logger.write_log(
                f"Permission denied: {report['file']}",
                level="ERROR")

        elif report["status"] == "error":
            logger.write_log(
                f"Error processing {report['file']}: {report['message']}",
                level="ERROR")

    logger.write_log(f"Scan complete. Total errors found: {total_errors}")

if __name__ == "__main__":
    main()