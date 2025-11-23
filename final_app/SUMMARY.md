# SUMMARY.md — Development Process for StudyBuddy AI (Final Project)

This document summarizes the full development workflow for **StudyBuddy AI** (Tasks3), a terminal-based Personal Knowledge Management System (PKMS) and advanced task manager that integrates optional AI-powered agents. It explains planning, iterations, testing, use of AI coding tools, challenges, false starts, and final design decisions.

---

## 1. Initial Planning and Requirements

The project started as an enhancement of a simple task manager used in prior course assignments (Tasks1 and Tasks2). The goal was to transform a basic script into a more realistic software system for the final project. Key objectives included:

- Building a **portable command-line interface (CLI)** running on Windows, macOS, and Linux.  
- Supporting a **personal knowledge management system (PKMS)** for notes and a **task manager** with priorities, due dates, tags, and status.  
- Integrating **AI agents** for note summarization, task summarization, and study plan generation.  
- Storing all state in **JSON files** for simplicity and portability.  

Initial planning used **ChatGPT in brainstorming mode** to explore possible feature enhancements, including:

- Sorting, filtering, and search by tags or keywords  
- Task priorities, due dates, and overdue highlighting  
- AI-powered summarization of notes and tasks  
- Polished CLI with descriptive help menus and formatting  
- Modular, class-based design for maintainability  

This planning phase acted as a lightweight software specification document, guiding architecture decisions and implementation order.

---

## 2. AI Coding Assistance

### **ChatGPT — Macro-level guidance**

ChatGPT was used extensively to plan, design, debug, and implement features:

- **Feature design:** Proposed ideas for AI integration, note/task schema, CLI layout, and error handling.  
- **Debugging:** Helped resolve errors related to JSON file handling, missing fields, and API response changes.  
- **Rewrites:** Assisted in restructuring files (`tasks.py`, `pkms.py`, `agents.py`) to a clean class-based design.  
- **UX and formatting:** Suggested improvements to CLI outputs, help menus, and error messages.  

**Strengths:**  
- Accelerated iteration and experimentation  
- Explained complex Python behaviors and errors clearly  
- Produced organized, modular code  

**Limitations:**  
- Occasionally over-complicated file structures or abstractions  
- Sometimes broke Windows path handling or JSON logic  
- Required manual corrections when AI generated outdated OpenAI API calls  

---

### **GitHub Copilot — Micro-level assistance**

Copilot was used for smaller, repetitive tasks:

- Filling in boilerplate and helper function code  
- Auto-generating docstrings and exception handling  
- Refactoring small functions for clarity  

**Strengths:** Fast, helpful for micro-completions.  
**Limitations:** Poor at multi-file consistency and occasionally suggested deprecated API syntax.

---

## 3. Testing and Iteration

Testing was a combination of **manual CLI testing** and lightweight pytest experiments:

- Manual tests covered adding, listing, editing, deleting, filtering, sorting, and marking tasks/notes done or undone.  
- Tested edge cases like missing or malformed JSON files, invalid priority inputs, and overdue tasks.  
- Verified AI functionality (summarization and study plan) handled missing API keys gracefully.  

Testing guided iterative improvements to error handling, CLI formatting, JSON load/save stability, and overall user experience.

---

## 4. False Starts and Challenges

Several challenges arose during development:

- **Directory creation bug:** `os.makedirs()` sometimes ran on empty paths, which broke Windows compatibility. Fixed by checking `if dir_path:` first.  
- **Premature AI integration:** Early attempts to integrate AI agents before stabilizing core functionality caused crashes and inconsistent behavior. Resolved by building a stable core first.  
- **Overly minimal help system:** Initial CLI help lacked explanations and formatting. Updated to include detailed, colorized, and emoji-enhanced command descriptions.  
- **JSON structure errors:** Some rewrites caused duplicated entries or misaligned IDs, requiring safer save/load logic.  

These false starts helped refine the architecture and development process, improving robustness and maintainability.

---

## 5. Final Development Stage

The final project includes:

- **PKMS**: Add, list, search, delete notes; store tags; AI summarization.  
- **Task Manager**: Add, list, filter, delete tasks; support priorities, due dates, recurring tasks; highlight overdue tasks; AI-generated study plan suggestions.  
- **CLI**: Clear, colorful, user-friendly interface with detailed help.  
- **AI Integration**: Summarization and plan generation using OpenAI API when a valid key is present.  
- **JSON-backed storage**: Ensures portability and simplicity.  

This version reflects multiple iterations, careful planning, debugging, and feature expansion.

---

## 6. Reflection and Lessons Learned

- Combining **ChatGPT for high-level reasoning** and **Copilot for micro-level coding** dramatically accelerated development.  
- Manual testing remained critical for catching logic errors and validating the AI interactions.  
- Iterative design allowed for graceful integration of AI features without breaking the core system.  
- The final project demonstrates real software engineering practices: modularity, abstraction, error handling, documentation, and modern AI-assisted development.

The project successfully meets course objectives while delivering a polished, functional, and extensible software system suitable for demonstration and further expansion.



