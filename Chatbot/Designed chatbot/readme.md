UI & UX Implementation with Figma & Tkinter
===========================================

This project implements a modern UI/UX demo for Code Sinaia 2025, showcasing the integration of Figma design concepts with a Python Tkinter desktop application.  
The working version of the project is available under the [final-version](https://github.com/inproted/CodeSinaia-2025) branch.  
The main branch contains the core components and structure, while feature branches may contain additional or experimental functionality.

## Project Scope

This project was made for the [Code Sinaia 2025](https://sites.google.com/view/codesinaia/home) programming school.  
The aim of this project is to help students get introduced to Python, Figma, Tkinter, and UI/UX design principles.

## Project Aims

The aims of this project are to introduce students to:
- Component-based UI development in Python with Tkinter
- Translating Figma designs into functional desktop interfaces
- UI/UX best practices (layout, color, typography, feedback, accessibility)
- Event-driven programming and state management in Tkinter
- Modular code structure and reusability

Students will be tasked with:
- Creating custom Tkinter components (widgets)
- Implementing navigation between screens (Splash, Main App, Chatbot, etc.)
- Passing and managing data between components
- Designing and applying consistent styles based on Figma prototypes
- Implementing a simple chatbot with probability-based responses
- Adding interactivity (buttons, input fields, dynamic content)
- (Optional) Extending the app with new features or improved UX

## Documentation

### Main Functionalities

- **Splash Screen:**  
  Displays an animated splash/loading screen on startup.

- **Main Application Window:**  
  The primary interface, styled according to Figma designs, with navigation and content areas.

- **Chatbot Module:**  
  - Accepts user input and displays chatbot responses.
  - Uses probability-based logic to generate responses.
  - Supports clearing the chat and sending messages.

- **Theme & Style Management:**  
  - Centralized color palette and font management.
  - Responsive layout adjustments.

- **Error Handling:**  
  - User-friendly error messages for invalid input or system errors.

- **Extensible Component Structure:**  
  - Easy to add new screens or widgets.

### Data Structure

The main data objects used in the app include:

- **User Message Object:**
  - `text`: The message content (string)
  - `timestamp`: Time sent (datetime)
  - `sender`: "user" or "bot"

- **Chatbot Response Object:**
  - `text`: The response content (string)
  - `probability`: Confidence/probability score (float)
  - `intent`: The detected intent/category (string)

### Project Structure

- `app/`
  - `main.py` — Entry point, launches the app
- `ui/`
  - `splash_screen.py` — Splash screen logic
  - `main_app.py` — Main window and navigation
- `chatbot/`
  - `messages.py` — Message handling logic
  - `probability.py` — Response probability logic
  - `responses.py` — Predefined responses and intent mapping
- `assets/`
  - Images, icons, and Figma exports
- `ux/`
  - `alerts.py` — Alert and error handling
  - `json_handling.py` — JSON data management
  - `messages.py` — User message handling

## References

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Figma](https://www.figma.com/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Code Sinaia 2025](https://sites.google.com/view/codesinaia/home)

---

## How to Start the App

Run the following command from the root directory of the project:

```bash
python app/main.py
```

Or alternatively, run as a module from the project root:

```bash
python -m app.main
```

Make sure you have all dependencies installed and that you are running the command from the project root directory.

---