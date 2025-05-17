# 📝 To-Do List CLI

## 📖 Overview
This is a simple command-line to-do list application built with Python. It lets you manage tasks by adding, updating, deleting, viewing, and listing them — all from the terminal. Tasks are saved locally using JSON files, ensuring your data persists between sessions.

---

## ✨ Features

- Fully interactive CLI
- Automatically create JSON storage files on first run
- Add new tasks
- Automatically assign unique task IDs
- Timestamps for task creation and updates
- Update task status: to do, in progress, completed
- Automatically archive completed tasks
- Delete tasks
- View individual tasks or categorized lists
- Data persistence with `.json` files

---

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/frankyan53/to-do-list.git
cd to-do-list
```

2. Run the program:

```bash
python to-do-list.py
```

---

## 📦 Requirements

- Python 3.6 or higher (no external libraries required)

---

## 🗂 Project Structure

```
📁 to-do-list/
├── to-do-list.py         # Full logic of the CLI app
├── current_tasks.json    # Auto-created: stores active tasks
├── archived_tasks.json   # Auto-created: stores completed tasks
├── id_counter.json       # Auto-created: tracks next task ID
├── README.md             # Project documentation
└── LICENSE               # MIT license for project reuse
```

---

## 💾 Data Storage

- `current_tasks.json` – Active tasks
- `archived_tasks.json` – Completed tasks
- `id_counter.json` – Tracks task ID count

All files are created automatically if they don't exist when the program starts.

---

## 💡 Example Task Flow

1. **Add a task**: Provide a name and description
2. **Update task**: Mark as "to do", "in progress", or "completed"
3. **Delete task**: Permanently remove a task
4. **Archive task**: Automatically triggered when a task is marked completed
5. **List/View tasks**: Filter tasks by status or view full task details

---

## 🧠 Future Improvements

- Edit task name/description  
- Add due dates or deadlines  
- Search tasks by keyword  
- Export to CSV  
- Color-coded terminal output  

---

## 🛠️ Tech Stack

- Language: Python
- Storage: JSON
- Interface: Command-Line Interface (CLI)

---

## 🧑‍💻 Author

**Frank Yan**

Stanford University, Class of 2029  
- Email: frankyan53@gmail.com
- GitHub: [@frankyan53](https://github.com/frankyan53)
- LinkedIn: [linkedin.com/in/frank-yan-9a0974267](https://www.linkedin.com/in/frank-yan-9a0974267/)

---

## 🪪 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
