# Console-Based To-Do Application

A comprehensive command-line to-do application that helps you manage your tasks efficiently. Tasks are stored persistently in a text file and include status tracking and timestamps.

## Features

✅ **Add Tasks** - Add new tasks with automatic timestamps  
🗑️ **Remove Tasks** - Delete tasks by number  
📋 **View Tasks** - Display all tasks, or filter by status  
✅ **Mark Completed** - Mark tasks as completed  
⏳ **Mark Pending** - Mark tasks as pending  
📊 **Statistics** - View task completion statistics  
🔍 **Filtering** - View only pending or completed tasks  
🗑️ **Bulk Delete** - Clear all completed tasks at once  
💾 **Persistent Storage** - Tasks saved to text file automatically  

## How to Run

```powershell
python Todo.py
```

## File Structure

The application creates and manages a text file (default: `my_tasks.txt`) where tasks are stored in the following format:

```
[STATUS] TASK_DESCRIPTION - YYYY-MM-DD HH:MM
```

### Example:
```
[PENDING] Buy groceries - 2025-01-15 10:30
[COMPLETED] Complete Python assignment - 2025-01-14 14:20
[PENDING] Call dentist for appointment - 2025-01-15 09:15
```

## Usage Guide

### Main Menu Options

1. **➕ Add Task** - Enter a task description to add to your list
2. **🗑️ Remove Task** - Select a task number to remove from the list
3. **📋 View All Tasks** - Display all tasks with their status and timestamps
4. **✅ Mark Task as Completed** - Change a task's status to completed
5. **⏳ Mark Task as Pending** - Change a task's status back to pending
6. **📊 View Statistics** - See total, completed, and pending task counts
7. **🔍 View Pending Tasks** - Show only tasks that are not yet completed
8. **🔍 View Completed Tasks** - Show only tasks that are finished
9. **🗑️ Clear All Completed Tasks** - Remove all completed tasks from the list
0. **🚪 Exit** - Save and exit the application

### Example Workflow

1. **Start the application:**
   ```
   python Todo.py
   ```

2. **Add some tasks:**
   ```
   Choose option 1
   Enter: "Buy groceries"
   Enter: "Finish homework"
   Enter: "Call mom"
   ```

3. **View your tasks:**
   ```
   Choose option 3 to see all tasks
   ```

4. **Mark a task as completed:**
   ```
   Choose option 4
   Enter the task number you completed
   ```

5. **Check your progress:**
   ```
   Choose option 6 to see statistics
   ```

## File Management

- **Default filename:** `my_tasks.txt`
- **Custom filename:** You can modify the filename in the code
- **Automatic saving:** Tasks are saved automatically after each operation
- **Error handling:** The app handles file errors gracefully

## Data Format

Tasks are stored with the following information:
- **Task Description:** What needs to be done
- **Status:** PENDING or COMPLETED
- **Timestamp:** When the task was added (YYYY-MM-DD HH:MM)

## Error Handling

The application includes robust error handling for:
- ❌ Empty task descriptions
- ❌ Invalid task numbers
- ❌ File read/write errors
- ❌ Invalid menu choices
- ⚠️ Keyboard interrupts (Ctrl+C)

## Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)

## Tips for Best Use

1. **Keep task descriptions clear and specific**
2. **Regularly mark tasks as completed to track progress**
3. **Use the statistics feature to monitor productivity**
4. **Clear completed tasks periodically to keep the list manageable**
5. **Back up your tasks file if you have important long-term tasks**

Enjoy staying organized with your new To-Do application! 📝✨
