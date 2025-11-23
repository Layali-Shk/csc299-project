# StudyBuddy AI — Final Project (PKMS + Task Manager + AI Agents)

This is the final, fully-featured version of your CSC 299 project.  
It combines a **Personal Knowledge Management System (PKMS)**, an **Advanced Task Manager**, a **Chat-style CLI interface**, and **AI agents** powered through the OpenAI API.

---

## Features

### **PKMS (Notes System)**
From earlier versions:
- Add notes  
- List notes  
- Search notes  
- Delete notes  
- Store notes in JSON  

**New in Final Version:**
- Update notes  
- Tag notes  
- Categorize notes  
- Search notes by keyword  
- Optional AI-powered note summarization  
- Optional AI summary of all notes  
- Notes stored in structured JSON with IDs

---

### **Task Management System**
From earlier versions:
- Add tasks  
- List tasks  
- Search tasks  
- Store tasks in JSON  

**New in Final Version:**
- **Task Priorities** (Low / Medium / High)  
- **Due Dates**  
- **Recurring Tasks** (daily / weekly / monthly)  
- **Mark tasks done**  
- **Tag tasks**  
- **Filter tasks** by keyword, tags, or status  
- **Sort tasks** by priority or due date  
- **Overdue tasks highlighted**  
- **Next Task Recommendation (AI)**  
- JSON-based task storage with IDs

---

### **AI Agents (Optional)**
Uses the OpenAI API if an API key is provided.  
You can still run the entire program **without AI**.

AI features:
- Summarize a single note  
- Summarize all notes  
- Generate a study plan (based on all notes + tasks)  
- Suggest the next most important task  
- Clean JSON output formatting

---

### **Chat-Based CLI Interface**
Includes:
- Clean formatted help menu  
- Guided prompts when adding tasks/notes  
- Colorized output (via `colorama`)  
- Error handling  
- JSON loading safety checks  

---

## Project Structure
```
final_app/
├── main.py # Chat-style CLI interface
├── pkms.py # Notes system
├── tasks.py # Task manager
├── agents.py # AI helper functions
└── data/
├── notes.json
└── tasks.json
```

---

## Setup

1. Navigate to the project folder:
   ```bash
   cd final_app
2. Install dependencies:
  ```bash
  pip install colorama openai
```
3. Ensure the data folder exists:
 ```bash
 mkdir data
```
4. Create empty JSON files if needed:
```bash
[]
```
5. (Optional) Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-key"
```
## Usage 
Start the program:
```bash
python main.py
```
This will open the chat-style interface:
```bash
Welcome to StudyBuddy AI (Enhanced). Type 'help' for commands.
>
```
## Notes 
-The app is fully portable across Windows, macOS, and Linux.

-No external database is required.

-AI features only activate when an API key is available.

-Core functionality works without internet access.
## Final Thoughts

This project includes:

-PKMS
-Task Manager
-Chat Interface
-AI Agents
-JSON persistence
-Modular Python design
