import os
import sys
from datetime import datetime


class TodoApp:
    def __init__(self, filename="tasks.txt"):
        """Initialize the To-Do application with a filename for storage"""
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from the text file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    for line in file:
                        line = line.strip()
                        if line:
                            # Parse task format: [STATUS] TASK - DATE
                            if line.startswith('['):
                                status_end = line.find(']')
                                if status_end != -1:
                                    status = line[1:status_end]
                                    task_content = line[status_end + 2:]  # Skip '] '
                                    # Split task and date
                                    if ' - ' in task_content:
                                        task, date = task_content.rsplit(' - ', 1)
                                    else:
                                        task = task_content
                                        date = datetime.now().strftime("%Y-%m-%d %H:%M")
                                    
                                    task_dict = {
                                        'task': task,
                                        'status': status,
                                        'date': date
                                    }
                                    self.tasks.append(task_dict)
            else:
                # Create empty file if it doesn't exist
                with open(self.filename, 'w') as file:
                    pass
                        
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to the text file"""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"[{task['status']}] {task['task']} - {task['date']}\n")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task_description):
        """Add a new task to the list"""
        if not task_description.strip():
            print("❌ Task description cannot be empty!")
            return
        
        new_task = {
            'task': task_description.strip(),
            'status': 'PENDING',
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Task added successfully: '{task_description}'")
    
    def remove_task(self, task_number):
        """Remove a task by its number"""
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"🗑️  Task removed: '{removed_task['task']}'")
            else:
                print(f"❌ Invalid task number! Please enter a number between 1 and {len(self.tasks)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def mark_completed(self, task_number):
        """Mark a task as completed"""
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                if self.tasks[task_number - 1]['status'] == 'COMPLETED':
                    print("ℹ️  Task is already marked as completed!")
                else:
                    self.tasks[task_number - 1]['status'] = 'COMPLETED'
                    self.save_tasks()
                    print(f"✅ Task marked as completed: '{self.tasks[task_number - 1]['task']}'")
            else:
                print(f"❌ Invalid task number! Please enter a number between 1 and {len(self.tasks)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def mark_pending(self, task_number):
        """Mark a task as pending"""
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                if self.tasks[task_number - 1]['status'] == 'PENDING':
                    print("ℹ️  Task is already marked as pending!")
                else:
                    self.tasks[task_number - 1]['status'] = 'PENDING'
                    self.save_tasks()
                    print(f"⏳ Task marked as pending: '{self.tasks[task_number - 1]['task']}'")
            else:
                print(f"❌ Invalid task number! Please enter a number between 1 and {len(self.tasks)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_tasks(self, filter_status=None):
        """View all tasks or filter by status"""
        if not self.tasks:
            print("📝 No tasks found! Add some tasks to get started.")
            return
        
        # Filter tasks if status is specified
        tasks_to_show = self.tasks
        if filter_status:
            tasks_to_show = [task for task in self.tasks if task['status'].upper() == filter_status.upper()]
            if not tasks_to_show:
                print(f"📝 No {filter_status.lower()} tasks found!")
                return
        
        print("\n" + "="*60)
        if filter_status:
            print(f"           {filter_status.upper()} TASKS")
        else:
            print("                ALL TASKS")
        print("="*60)
        
        for i, task in enumerate(tasks_to_show, 1):
            status_icon = "✅" if task['status'] == 'COMPLETED' else "⏳"
            original_index = self.tasks.index(task) + 1
            print(f"{original_index:2d}. {status_icon} {task['task']}")
            print(f"     Status: {task['status']} | Added: {task['date']}")
            print("-" * 60)
    
    def clear_completed_tasks(self):
        """Remove all completed tasks"""
        completed_count = len([task for task in self.tasks if task['status'] == 'COMPLETED'])
        if completed_count == 0:
            print("ℹ️  No completed tasks to clear!")
            return
        
        self.tasks = [task for task in self.tasks if task['status'] != 'COMPLETED']
        self.save_tasks()
        print(f"🗑️  Cleared {completed_count} completed task(s)!")
    
    def get_statistics(self):
        """Display task statistics"""
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task['status'] == 'COMPLETED'])
        pending_tasks = total_tasks - completed_tasks
        
        print("\n" + "="*40)
        print("           TASK STATISTICS")
        print("="*40)
        print(f"📊 Total Tasks:     {total_tasks}")
        print(f"✅ Completed:       {completed_tasks}")
        print(f"⏳ Pending:         {pending_tasks}")
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"📈 Completion Rate: {completion_rate:.1f}%")
        print("="*40)
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("              📝 TO-DO APPLICATION")
        print("="*50)
        print("1. ➕ Add Task")
        print("2. 🗑️  Remove Task")
        print("3. 📋 View All Tasks")
        print("4. ✅ Mark Task as Completed")
        print("5. ⏳ Mark Task as Pending")
        print("6. 📊 View Statistics")
        print("7. 🔍 View Pending Tasks")
        print("8. 🔍 View Completed Tasks")
        print("9. 🗑️  Clear All Completed Tasks")
        print("0. 🚪 Exit")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("🎉 Welcome to the To-Do Application!")
        print(f"📁 Tasks are stored in: {self.filename}")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (0-9): ").strip()
                
                if choice == '1':
                    task = input("Enter task description: ")
                    self.add_task(task)
                
                elif choice == '2':
                    if not self.tasks:
                        print("📝 No tasks to remove!")
                    else:
                        self.view_tasks()
                        task_num = input("Enter task number to remove: ")
                        self.remove_task(task_num)
                
                elif choice == '3':
                    self.view_tasks()
                
                elif choice == '4':
                    if not self.tasks:
                        print("📝 No tasks to mark as completed!")
                    else:
                        self.view_tasks()
                        task_num = input("Enter task number to mark as completed: ")
                        self.mark_completed(task_num)
                
                elif choice == '5':
                    if not self.tasks:
                        print("📝 No tasks to mark as pending!")
                    else:
                        self.view_tasks()
                        task_num = input("Enter task number to mark as pending: ")
                        self.mark_pending(task_num)
                
                elif choice == '6':
                    self.get_statistics()
                
                elif choice == '7':
                    self.view_tasks('PENDING')
                
                elif choice == '8':
                    self.view_tasks('COMPLETED')
                
                elif choice == '9':
                    confirm = input("Are you sure you want to clear all completed tasks? (y/n): ")
                    if confirm.lower() in ['y', 'yes']:
                        self.clear_completed_tasks()
                    else:
                        print("❌ Operation cancelled!")
                
                elif choice == '0':
                    print("\n🎉 Thank you for using the To-Do Application!")
                    print("👋 Goodbye!")
                    break
                
                else:
                    print("❌ Invalid choice! Please enter a number between 0 and 9.")
            
            except KeyboardInterrupt:
                print("\n\n⚠️  Program interrupted by user.")
                print("🎉 Thank you for using the To-Do Application!")
                print("👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")


def main():
    """Main function to run the To-Do application"""
    # You can specify a custom filename here if needed
    app = TodoApp("my_tasks.txt")
    app.run()


if __name__ == "__main__":
    main()
