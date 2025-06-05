# import subprocess
# import datetime
# from pathlib import Path

# # Run the CLI command
# result = subprocess.run(
#     ["python3", "workflows/cli.py", "run-workflow", "workflows/tmp/county_rec_1.json"],
#     capture_output=True,
#     text=True
# )

# # Print output to console
# print("STDOUT:")
# print(result.stdout)
# print("STDERR:")
# print(result.stderr)

# # Prepare logs directory and filename with timestamp
# logs_dir = Path("./00_data/logs/")
# logs_dir.mkdir(parents=True, exist_ok=True)
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# log_file = logs_dir / f"run_workflow_{timestamp}.log"

# # Save output to log file
# with open(log_file, "w", encoding="utf-8") as f:
#     f.write("STDOUT:\n")
#     f.write(result.stdout)
#     f.write("\nSTDERR:\n")
#     f.write(result.stderr)

# print(f"Logs saved to: {log_file}") 


