import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from bson import ObjectId
from pydantic import ValidationError

from models.event import Event
from services.database.repositories.event_repository import EventRepository


class MainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root.root)
        self.root_window = root
        self.event_repository = EventRepository()
        self.add_content()

    def add_content(self):
        """
        Adding content to frame
        :return:
        """
        self.event_table = ttk.Treeview(self, columns=("ID", "Name", "Description", "Date", "Organizator"),
                                        show="headings")
        self.event_table.heading("ID", text="ID")
        self.event_table.heading("Name", text="Name")
        self.event_table.heading("Description", text="Description")
        self.event_table.heading("Date", text="Date")
        self.event_table.heading("Organizator", text="Organizator")
        self.event_table.pack(fill=tk.BOTH, expand=True)

        self.populate_event_table()

        self.add_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.edit_button = tk.Button(self, text="Edit Event", command=self.edit_event)
        self.edit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def populate_event_table(self):
        """
        Addding data to event table
        :return:
        """
        records = self.event_repository.get_all()
        for record in records:
            values = list(record.dict().values())
            values[0] = str(values[0])
            self.event_table.insert("", "end", values=tuple(values))

    def add_event(self):
        """
        Method to add event
        :return:
        """
        if self.root_window.user:
            event_name = simpledialog.askstring("Add Event", "Enter event name:")
            event_date = simpledialog.askstring("Add Event", "Enter event date (YYYY-MM-DD):")
            event_description = simpledialog.askstring("Add Event", "Enter event description:")
            try:
                event = Event(name=event_name, date=event_date, description=event_description,
                              organizator=ObjectId(self.root_window.user.id))
                if event_name and event_date:
                    event_id = self.event_repository.create(event)
                    record = self.event_repository.get_by_id(str(event_id))
                    if record:
                        self.event_table.insert("", "end", values=tuple(record.dict().values()))
                        messagebox.showinfo("Add Event", "Event added successfully.")
            except ValidationError:
                pass

    def edit_event(self):
        """
        Method to edit event
        :return:
        """
        selected_item = self.event_table.selection()
        if selected_item:
            item = self.event_table.item(selected_item)
            event_id = list(item.values())[2][0]
            if self.event_repository.get_by_id(event_id) is not None:
                selected_event = self.event_repository.get_by_id(event_id)
                if selected_event.organizator == ObjectId(self.root_window.user.id):
                    event_name = simpledialog.askstring("Add Event", "Enter event name:")
                    event_date = simpledialog.askstring("Add Event", "Enter event date (YYYY-MM-DD):")
                    event_description = simpledialog.askstring("Add Event", "Enter event description:")
                    try:

                        event = Event(_id=ObjectId(event_id), name=event_name, date=event_date,
                                      description=event_description,
                                      organizator=ObjectId(self.root_window.user.id))
                        self.event_repository.update(event_id, event)
                        values = list(event.dict().values())
                        print(values)
                        values[0] = str(values[0])
                        self.event_table.item(selected_item, values=tuple(values))
                        messagebox.showinfo("Edit Event", f"Edit event {event_id}")
                    except ValidationError:
                        pass
                else:
                    messagebox.showerror("Error", "This is not your event.")
        else:
            messagebox.showerror("Error", "Please select an event to edit.")

    def delete_event(self):
        selected_item = self.event_table.selection()
        if selected_item:
            item = self.event_table.item(selected_item)
            event_id = list(item.values())[2][0]
            try:
                if self.event_repository.get_by_id(str(event_id)) is not None:
                    selected_event = self.event_repository.get_by_id(event_id)
                    if selected_event.organizator == ObjectId(self.root_window.user.id):
                        if self.event_repository.delete(event_id):
                            self.event_table.delete(selected_item)
                            messagebox.showinfo("Delete Event", "Event deleted successfully.")
                    else:
                        messagebox.showerror("Error", "This is not your event.")
            except Exception as e:
                messagebox.showerror("Error", "Error in deleting Event")
        else:
            messagebox.showerror("Error", "Please select an event to delete.")
