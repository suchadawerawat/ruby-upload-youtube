import re
import json

# Corrected task_pattern:
# Example: *   **TASK-FE-001 (A):** Initialize Frontend Project
# Bold text is "**TASK-FE-001 (A):**"
task_pattern = re.compile(r"^\*\s+\*\*(TASK-FE-\d{3})\s+\(([A-C]|All)\):\*\*\s*(.*)")
dependency_pattern = re.compile(r"^\s+\*\s+\*\*Depends on:\*\*\s*(.*)")
task_id_in_dependency_pattern = re.compile(r"TASK-FE-\d{3}")

tasks = []
current_task_data = {}

backlog_file_path = "frontend/FRONTEND_BACKLOG.md"
print(f"Attempting to parse {backlog_file_path}")

try:
    with open(backlog_file_path, "r") as f:
        for i, line_content in enumerate(f):
            line = line_content.rstrip("\n")
            # print(f"Line {i+1}: '{line}'") # Uncomment for full line-by-line debugging

            task_match = task_pattern.match(line)

            if task_match:
                # print(f"DEBUG: Task matched on line {i+1}: {line}")
                if current_task_data.get("id"): # If there's data for a previous task, store it
                    tasks.append(current_task_data)

                task_id = task_match.group(1)
                developer = task_match.group(2)
                title = task_match.group(3).strip()
                current_task_data = {
                    "id": task_id,
                    "developer": developer,
                    "title": title, # Storing title for context, not in final required JSON
                    "dependencies": []
                }
            elif current_task_data.get("id"): # Only look for dependencies if we are "inside" a task
                dependency_match = dependency_pattern.match(line)
                if dependency_match:
                    # print(f"DEBUG: Dependency matched on line {i+1}: {line}")
                    dependencies_str = dependency_match.group(1)
                    current_task_data["dependencies"] = task_id_in_dependency_pattern.findall(dependencies_str)

        # After the loop, if current_task_data holds the last processed task, save it.
        if current_task_data.get("id"):
            tasks.append(current_task_data)

    # Prepare final list of dictionaries as per requirements (id, developer, dependencies)
    output_tasks = []
    for task in tasks:
        output_tasks.append({
            "id": task["id"],
            "developer": task["developer"],
            "dependencies": task["dependencies"]
        })

    output_file_path = "parsed_tasks.json"
    with open(output_file_path, "w") as f:
        json.dump(output_tasks, f, indent=2)

    print(f"Tasks parsed and saved to {output_file_path}")
    if not output_tasks:
        print("Warning: No tasks were extracted. Review patterns and file content.")
    else:
        print(f"Successfully extracted {len(output_tasks)} tasks.")
        # print(json.dumps(output_tasks, indent=2)) # Print JSON to stdout for immediate check

except FileNotFoundError:
    print(f"Error: File not found at {backlog_file_path}")
    import os
    print(f"Current working directory: {os.getcwd()}")
except Exception as e:
    print(f"An error occurred: {e}")
