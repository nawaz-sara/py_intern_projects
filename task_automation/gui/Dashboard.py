from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from automation.file_organizer import organize_files
from automation.reminder_manager import ReminderManager

class SmartTaskDashboard:

    def __init__(self, root):
        

        self.root = root
        
        self.root.title("SmartTask - Automation System")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)
        self.root.configure(bg="#101827")

        self.selected_folder = None
        self.reminder_manager = ReminderManager()
        self.create_sidebar()
        self.create_main_area()

    # Sidebar
    def create_sidebar(self):

        sidebar = tk.Frame(
            self.root,
            bg="#172338",
            width=230
        )

        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        title = tk.Label(
            sidebar,
            text="SmartTask",
            font=("Arial", 23, "bold"),
            fg="white",
            bg="#172338"
        )

        title.pack(pady=35)

        buttons = [
            "Dashboard",
            "File Organizer",
            "Reminders",
            "Website Launcher",
            "Backup Manager",
            "Email Automation"
        ]

        for name in buttons:

            btn = tk.Button(
                sidebar,
                text=name,
                font=("Arial", 11),
                fg="white",
                bg="#22334D",
                activebackground="#34527A",
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=20,
                pady=12,
                command=lambda n=name: self.show_page(n)
            )

            btn.pack(fill="x", padx=12, pady=5)

    # Main dashboard
    def create_main_area(self):

        self.main = tk.Frame(
            self.root,
            bg="#101827"
        )

        self.main.pack(
            side="left",
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        self.show_page("Dashboard")
        self.root.after(1000, self.check_due_reminders)

    # Page content
    def show_page(self, page_name):

        for widget in self.main.winfo_children():
            widget.destroy()

        heading = tk.Label(
            self.main,
            text=page_name,
            font=("Arial", 25, "bold"),
            fg="white",
            bg="#101827"
        )

        heading.pack(anchor="w", pady=(10, 5))

        description = tk.Label(
            self.main,
            text="Manage your daily tasks with SmartTask.",
            font=("Arial", 11),
            fg="#AAB7C8",
            bg="#101827"
        )

        description.pack(anchor="w", pady=(0, 25))

        if page_name == "Dashboard":
            self.create_dashboard_cards()

        elif page_name == "File Organizer":
            self.create_file_organizer_page()

        elif page_name == "Reminders":
            self.create_reminder_page()
        else:
            tk.Label(
                self.main,
                text=page_name + " module coming soon!",
                font=("Arial", 15),
                fg="#AAB7C8",
                bg="#101827"
                ).pack(anchor="w", pady=30)
   
   
    # Dashboard cards
    def create_dashboard_cards(self):

        tasks = [
            ("File Organizer", "Organize your files"),
            ("Reminders", "Schedule important reminders"),
            ("Website Launcher", "Open your favorite websites"),
            ("Backup Manager", "Back up important folders")
        ]

        card_area = tk.Frame(
            self.main,
            bg="#101827"
        )

        card_area.pack(fill="both", expand=True)

        for i, (title, description) in enumerate(tasks):

            card = tk.Frame(
                card_area,
                bg="#1D2B40",
                padx=20,
                pady=20
            )

            card.grid(
                row=i // 2,
                column=i % 2,
                padx=12,
                pady=12,
                sticky="nsew"
            )

            tk.Label(
                card,
                text=title,
                font=("Arial", 15, "bold"),
                fg="white",
                bg="#1D2B40"
            ).pack(anchor="w")

            tk.Label(
                card,
                text=description,
                font=("Arial", 10),
                fg="#AAB7C8",
                bg="#1D2B40"
            ).pack(anchor="w", pady=12)

            tk.Button(
                card,
                text="Open Module",
                bg="#2563EB",
                fg="white",
                relief="flat",
                padx=15,
                pady=8,
                command=lambda t=title: self.show_page(t)
            ).pack(anchor="w")

        card_area.columnconfigure(0, weight=1)
        card_area.columnconfigure(1, weight=1)
        card_area.rowconfigure(0, weight=1)
        card_area.rowconfigure(1, weight=1)
    
    def create_file_organizer_page(self):
       
        tk.Label(
            self.main,
            text="Organize your files automatically",
            font=("Arial", 12),
            fg="#AAB7C8",
            bg="#101827"
        ).pack(anchor="w", pady=10)

        self.folder_label = tk.Label(
            self.main,
            text="No folder selected",
            font=("Arial", 11),
            fg="white",
            bg="#101827"
        )

        self.folder_label.pack(anchor="w", pady=15)

        tk.Button(
              self.main,
              text="Select Folder",
              bg="#2563EB",
              fg="white",
              relief="flat",
              padx=20,
              pady=10,
              command=self.select_folder
        ).pack(anchor="w", pady=10)

        tk.Button(
             self.main,
             text="Organize Files",
             bg="#16A34A",
             fg="white",
             relief="flat",
             padx=20,
             pady=10,
             command=self.run_organizer
        ).pack(anchor="w", pady=10)

        self.result_box = tk.Text(
            self.main,
            height=12,
            bg="#1D2B40",
            fg="white",
            font=("Consolas", 10),
            relief="flat"
        )

        self.result_box.pack(
            fill="both",
            expand=True,
            pady=20
        )
    
    
    def select_folder(self):
        folder = filedialog.askdirectory(
            title="Select folder to organize")

        if folder:
            self.selected_folder = folder

            self.folder_label.config(
                text=f"Selected: {folder}"
            )
    
    def run_organizer(self):

        if not self.selected_folder:
            messagebox.showwarning(
                "Warning",
                "Please select a folder first."
            )
            return

        try:
            result = organize_files(self.selected_folder)

            self.result_box.delete("1.0", tk.END)

            self.result_box.insert(
                 tk.END,
                "FILE ORGANIZATION REPORT\n"
             )

            self.result_box.insert(tk.END, "=" * 35 + "\n\n")

            for filename in result["moved"]:
                 self.result_box.insert(
                    tk.END,
                    f"Moved: {filename}\n"
                 )

            for error in result["errors"]:
                 self.result_box.insert(
                    tk.END,
                    f"Error: {error}\n"
                 )

                 self.result_box.insert(
                    tk.END,
                    f"\nTotal moved: {len(result['moved'])}"
                 )

            messagebox.showinfo(
                "Completed",
                f"Successfully organized "
                f"{len(result['moved'])} files."
            )

        except (ValueError, OSError) as error:
            messagebox.showerror("Error",str(error)) 
    
     
    def create_reminder_page(self):

        # Clear previous page
        for widget in self.main.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.main,
            text="Reminder Manager",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#101827"
        )
        title.pack(pady=20)

        tk.Label(
            self.main,
            text="Reminder Title",
            fg="white",
            bg="#101827"
        ).pack()

        self.reminder_title = tk.Entry(
            self.main,
            font=("Arial", 12),
            width=35
        )
        self.reminder_title.pack(pady=8)

        tk.Label(
            self.main,
            text="Date (YYYY-MM-DD)",
            fg="white",
            bg="#101827"
        ).pack()

        self.reminder_date = tk.Entry(
            self.main,
            font=("Arial", 12),
            width=35
        )
        self.reminder_date.pack(pady=8)

        tk.Label(
            self.main,
            text="Time (HH:MM, 24-hour)",
            fg="white",
            bg="#101827"
        ).pack()

        self.reminder_time = tk.Entry(
            self.main,
            font=("Arial", 12),
            width=35
        )
        self.reminder_time.pack(pady=8)

        tk.Button(
            self.main,
            text="Add Reminder",
            bg="#2563EB",
            fg="white",
            command=self.add_reminder
        ).pack(pady=12)

        self.reminder_list = tk.Listbox(
            self.main,
            width=65,
            height=10
        )
        self.reminder_list.pack(pady=15)

        tk.Button(
            self.main,
            text="Delete Selected",
            command=self.delete_reminder
        ).pack(pady=5)

        self.refresh_reminders()


    def add_reminder(self):

        title = self.reminder_title.get().strip()
        date = self.reminder_date.get().strip()
        time = self.reminder_time.get().strip()

        if not title:
            messagebox.showwarning("Warning", "Enter a reminder title.")
            return

        try:
            reminder = self.reminder_manager.add_reminder(
                title, date, time
            )

            if reminder["datetime"] <= datetime.now():
                self.reminder_manager.delete_reminder(
                    len(self.reminder_manager.get_reminders()) - 1
                )
                messagebox.showwarning(
                    "Invalid time",
                    "Please enter a future date and time."
                )
                return

            messagebox.showinfo("Success", "Reminder added successfully!")

            self.refresh_reminders()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Enter date as YYYY-MM-DD and time as HH:MM."
            )
    def check_due_reminders(self):

        due_reminders = self.reminder_manager.check_reminders()

        for reminder in due_reminders:
            messagebox.showinfo(
                "Reminder Alert",
                f"Reminder: {reminder['title']}"
            )

        self.root.after(1000, self.check_due_reminders)

    def refresh_reminders(self):

        self.reminder_list.delete(0, tk.END)

        for reminder in self.reminder_manager.get_reminders():

            display = (
                reminder["title"] + " - " +
                reminder["datetime"].strftime("%Y-%m-%d %H:%M")
            )

            self.reminder_list.insert(tk.END, display)


    def delete_reminder(self):

        selected = self.reminder_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a reminder to delete."
            )
            return

        self.reminder_manager.delete_reminder(selected[0])

        self.refresh_reminders()


        
