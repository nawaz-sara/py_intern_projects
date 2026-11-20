
from datetime import datetime


class ReminderManager:

    def __init__(self):
        self.reminders = []

    def add_reminder(self, title, date, time):

        reminder_datetime = datetime.strptime(
            f"{date} {time}",
            "%Y-%m-%d %H:%M"
        )

        reminder = {
            "title": title,
            "datetime": reminder_datetime,
            "completed": False
        }

        self.reminders.append(reminder)

        return reminder

    def get_reminders(self):
        return self.reminders

    def delete_reminder(self, index):
        if 0 <= index < len(self.reminders):
            self.reminders.pop(index)

    def check_reminders(self):

        current_time = datetime.now()

        due_reminders = []

        for reminder in self.reminders:

            if (
                reminder["datetime"] <= current_time
                and not reminder["completed"]
            ):
                due_reminders.append(reminder)
                reminder["completed"] = True

        return due_reminders
