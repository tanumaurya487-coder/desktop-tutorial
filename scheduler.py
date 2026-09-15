from datetime import datetime, timedelta

def get_tasks_from_user():
    """User se tasks input lena with validation"""
    tasks = []
    print("--- Python Task Scheduling Engine ---")
    
    try:
        num = int(input("Kitne tasks add karne hain? : "))
        if num <= 0:
            raise ValueError("Task ki sankhya 0 se badi honi chahiye.")
    except ValueError as e:
        print(f"Error: Invalid number - {e}")
        return []

    for i in range(num):
        print(f"\nTask {i+1}:")
        try:
            name = input("  Task Name: ").strip()
            if not name:
                raise ValueError("Task name khali nahi ho sakta.")

            duration = int(input("  Duration (minutes me, e.g., 30): ").strip())
            if duration <= 0:
                raise ValueError("Duration positive hona chahiye.")

            priority = int(input("  Priority (1=Low, 5=Highest): ").strip())
            if priority not in [1, 2, 3, 4, 5]:
                raise ValueError("Priority 1 se 5 ke beech honi chahiye.")

            tasks.append({
                "name": name,
                "duration": duration,
                "priority": priority
            })
        except ValueError as e:
            print(f"  -> Input Error: {e}. Ye task skip ho gaya.")
            continue
    
    return tasks

def generate_optimized_schedule(tasks, day_start_str="09:00"):
    """
    Tasks ko priority ke hisab se optimize karna
    High priority pehle, same priority me chhota task pehle
    """
    if not tasks:
        print("Koi valid task nahi hai.")
        return []

    # Sorting Logic: Priority High to Low, Duration Low to High
    sorted_tasks = sorted(tasks, key=lambda x: (-x['priority'], x['duration']))

    # Day start time
    try:
        current_time = datetime.strptime(day_start_str, "%H:%M")
    except ValueError:
        print("Time format galat hai, default 09:00 le raha hu.")
        current_time = datetime.strptime("09:00", "%H:%M")

    schedule = []
    for task in sorted_tasks:
        start_time = current_time
        end_time = start_time + timedelta(minutes=task['duration'])

        # Overlap check (sequential hai to overlap nahi hoga, but future ke liye logic)
        schedule.append({
            "name": task['name'],
            "priority": task['priority'],
            "start": start_time.strftime("%I:%M %p"),
            "end": end_time.strftime("%I:%M %p"),
            "duration": task['duration']
        })
        current_time = end_times

    return schedule

def display_schedule(schedule):
    print("\n--- Optimized Daily Timeline ---")
    print(f"{'Time':<20} | {'Task':<20} | {'Priority':<8} | Duration")
    print("-" * 65)
    for item in schedule:
        print(f"{item['start']} - {item['end']:<6} | {item['name']:<20} | {item['priority']:<8} | {item['duration']} min")

if __name__ == "__main__":
    tasks = get_tasks_from_user()
    final_schedule = generate_optimized_schedule(tasks, day_start_str="09:00")
    display_schedule(final_schedule)