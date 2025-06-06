import json
from datetime import datetime, timedelta

def calculate_gantt_chart_mermaid(tasks_json_path, output_mermaid_path):
    try:
        with open(tasks_json_path, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print(f"Error: {tasks_json_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {tasks_json_path}.")
        return

    task_end_dates = {}
    task_start_dates = {}

    tasks_by_id = {task['id']: task for task in tasks}
    task_ids_in_order = [task['id'] for task in tasks] # Keep original order for output if needed

    project_start_date = datetime(2024, 1, 1)

    processed_count_last_iteration = -1
    while len(task_end_dates) < len(tasks):
        current_processed_count = len(task_end_dates)
        for task_id in task_ids_in_order: # Process in original order, but dependencies dictate timing
            task = tasks_by_id[task_id]
            if task_id in task_end_dates:
                continue

            dependencies = task['dependencies']
            can_process = True
            calculated_start_date_for_current_task = project_start_date

            if dependencies:
                dep_end_dates_found = []
                all_deps_processed = True
                for dep_id in dependencies:
                    if dep_id in task_end_dates:
                        dep_end_dates_found.append(task_end_dates[dep_id])
                    else:
                        all_deps_processed = False
                        break

                if all_deps_processed and dep_end_dates_found:
                    latest_dependency_finish_date = max(dep_end_dates_found)
                    calculated_start_date_for_current_task = latest_dependency_finish_date + timedelta(days=1)
                elif not all_deps_processed:
                    can_process = False # Skip this task for now

            if can_process:
                task_start_dates[task_id] = calculated_start_date_for_current_task
                # A 1-day task finishes on the day it starts.
                task_end_dates[task_id] = task_start_dates[task_id]
                # print(f"Processed {task_id}: Starts {task_start_dates[task_id].strftime('%Y-%m-%d')}, Ends {task_end_dates[task_id].strftime('%Y-%m-%d')}")

        if len(task_end_dates) == current_processed_count: # No progress in this iteration
            print(f"Warning: Stuck. Could not resolve dates for all tasks. Processed: {len(task_end_dates)}/{len(tasks)}")
            missing_tasks = [t_id for t_id in task_ids_in_order if t_id not in task_end_dates]
            print(f"Missing tasks: {missing_tasks}")
            for mt_id in missing_tasks:
                mt_task = tasks_by_id[mt_id]
                print(f"  Task {mt_id} dependencies: {mt_task['dependencies']}")
                for dep_id in mt_task['dependencies']:
                    if dep_id not in task_end_dates:
                        print(f"    - Dependency {dep_id} for {mt_id} is also missing/unprocessed.")
            return # Avoid infinite loop

    dev_tasks_mermaid_entries = {'A': [], 'B': [], 'C': [], 'All': []}
    # Sort tasks by start date for coherent output within sections
    sorted_task_ids_by_date = sorted(task_start_dates.keys(), key=lambda tid: task_start_dates[tid])

    for task_id in sorted_task_ids_by_date:
        task = tasks_by_id[task_id]
        dev = task['developer']

        mermaid_task_entry = f"    {task_id} ({dev}) :{task_id}, {task_start_dates[task_id].strftime('%Y-%m-%d')}, 1d"
        if dev in dev_tasks_mermaid_entries:
            dev_tasks_mermaid_entries[dev].append(mermaid_task_entry)
        else:
            dev_tasks_mermaid_entries['All'].append(mermaid_task_entry)

    mermaid_lines = [
        "gantt",
        "    title Frontend Development Gantt Chart",
        "    dateFormat  YYYY-MM-DD",
        "    axisFormat %Y-%m-%d" # Changed for clarity with YYYY
    ]

    if dev_tasks_mermaid_entries['A']:
        mermaid_lines.append("\n    section Developer A")
        mermaid_lines.extend(dev_tasks_mermaid_entries['A'])
    if dev_tasks_mermaid_entries['B']:
        mermaid_lines.append("\n    section Developer B")
        mermaid_lines.extend(dev_tasks_mermaid_entries['B'])
    if dev_tasks_mermaid_entries['C']:
        mermaid_lines.append("\n    section Developer C")
        mermaid_lines.extend(dev_tasks_mermaid_entries['C'])
    if dev_tasks_mermaid_entries['All']:
        mermaid_lines.append("\n    section General/Shared Tasks")
        mermaid_lines.extend(dev_tasks_mermaid_entries['All'])

    mermaid_output = "\n".join(mermaid_lines)

    try:
        with open(output_mermaid_path, 'w') as f:
            # No markdown triple quotes, just pure mermaid syntax as per original thought
            f.write(mermaid_output)
        print(f"Mermaid Gantt chart syntax saved to {output_mermaid_path}")
    except IOError:
        print(f"Error: Could not write to {output_mermaid_path}.")

if __name__ == "__main__":
    calculate_gantt_chart_mermaid('parsed_tasks.json', 'gantt_chart.mmd') # Changed extension to .mmd
