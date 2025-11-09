from openai import OpenAI

def summarize_task(task_descriptions):
    client = OpenAI()

    summaries = []
    for description in task_descriptions:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes tasks into short phrases."},
                {"role": "user", "content": f"Summarize this task in a few words:\n\n{description}"}
            ]
        )
        summary = response.choices[0].message.content.strip()
        summaries.append(summary)
    return summaries


if __name__ == "__main__":
    # Two sample paragraph-length descriptions
    tasks = [
        """Develop a Python program that tracks student grades for a semester.
        The program should allow adding new students, recording grades for different assignments,
        calculating averages, and exporting reports to CSV format.""",

        """Design a simple to-do list web application using Flask.
        Users should be able to add, update, and delete tasks, mark them as complete,
        and the interface should update dynamically using JavaScript."""
    ]

    summaries = summarize_task(tasks)

    print("Task Summaries:")
    for i, s in enumerate(summaries, start=1):
        print(f"{i}. {s}")
