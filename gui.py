from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

from pdf_reader import read_pdf_text
from skills import SKILLS
from matcher import (
    extract_skills,
    compare_skills,
    calculate_match_score,
    generate_suggestions,
)


def main():
    root = tk.Tk()
    root.title("JobMatchAI")
    root.geometry("1100x760")
    root.minsize(850, 650)
    root.configure(background="#eef3f8")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TFrame", background="#eef3f8")
    style.configure("TLabel", background="#eef3f8", foreground="#243449", font=("Segoe UI", 10))
    style.configure("Title.TLabel", font=("Segoe UI", 28, "bold"), foreground="#244e73")
    style.configure("Subtitle.TLabel", foreground="#607387")
    style.configure("TLabelframe", background="#eef3f8", bordercolor="#cdd9e5")
    style.configure("TLabelframe.Label", background="#eef3f8", foreground="#244e73", font=("Segoe UI", 11, "bold"))
    style.configure("TButton", font=("Segoe UI", 10), padding=(14, 9))
    style.configure("Accent.TButton", background="#326b8e", foreground="white", font=("Segoe UI", 11, "bold"))
    style.map("Accent.TButton", background=[("active", "#285775"), ("pressed", "#204760")])

    style.configure("Score.TLabel", font=("Segoe UI", 24, "bold"), foreground="#21665d")

    score_display = tk.StringVar(value="?")
    resume_path = tk.StringVar()
    resume_filename = tk.StringVar(value="No PDF selected")

    def choose_resume():
        path = filedialog.askopenfilename(
            title="Choose Resume PDF",
            filetypes=[("PDF files", "*.pdf")],
            parent=root,
        )
        if path:
            resume_path.set(path)
            resume_filename.set(Path(path).name)

    def clear_results():
        score_display.set("?")
        for field in (results_text, suggestions_text):
            field.configure(state="normal")
            field.delete("1.0", tk.END)
            field.configure(state="disabled")

    def clear():
        resume_path.set("")
        resume_filename.set("No PDF selected")
        job_description.delete("1.0", tk.END)
        clear_results()
        job_description.focus_set()

    def analyze():
        clear_results()

        if not resume_path.get():
            messagebox.showerror("Missing resume", "Please choose a resume PDF first.", parent=root)
            return

        job_text = job_description.get("1.0", tk.END).strip()
        if not job_text:
            messagebox.showerror("Missing job description", "Please enter a job description.", parent=root)
            return

        try:
            resume_text = read_pdf_text(resume_path.get())
        except FileNotFoundError:
            messagebox.showerror(
                "PDF not found",
                "The selected PDF could not be found. It may have been moved or deleted. Please choose it again.",
                parent=root,
            )
            return
        except OSError:
            messagebox.showerror(
                "Cannot open PDF",
                "The selected PDF could not be opened. Please check that you have permission to read it, or choose another file.",
                parent=root,
            )
            return
        except Exception:
            messagebox.showerror(
                "Cannot read PDF",
                "Could not read this file. Please choose a valid, readable PDF that is not password-protected.",
                parent=root,
            )
            return

        if not resume_text.strip():
            messagebox.showerror(
                "No resume text",
                "No readable text was found in this PDF. Scanned images are not supported. Please choose a PDF containing selectable text.",
                parent=root,
            )
            return

        resume_skills = extract_skills(resume_text, SKILLS)
        job_skills = extract_skills(job_text, SKILLS)
        matching_skills, missing_skills, extra_skills = compare_skills(resume_skills, job_skills)
        match_score = calculate_match_score(matching_skills, job_skills)
        suggestions = generate_suggestions(missing_skills)

        score_display.set(f"{match_score:.2f}%")
        sections = [
            ("Resume skills", resume_skills),
            ("Job skills", job_skills),
            ("Matching skills", matching_skills),
            ("Missing skills", missing_skills),
            ("Extra skills", extra_skills),
        ]
        results_text.configure(state="normal")
        for title, skills in sections:
            results_text.insert(tk.END, title + "\n", "heading")
            results_text.insert(tk.END, (", ".join(skills) or "None") + "\n\n")
        results_text.configure(state="disabled")

        suggestions_text.configure(state="normal")
        suggestions_text.insert("1.0", "\n".join(suggestions))
        suggestions_text.configure(state="disabled")

    content = ttk.Frame(root, padding=24)
    content.pack(fill="both", expand=True)

    ttk.Label(content, text="JobMatchAI", style="Title.TLabel").pack(anchor="w")
    ttk.Label(content, text="Compare your resume with a job description.", style="Subtitle.TLabel").pack(anchor="w", pady=(2, 18))

    columns = ttk.Frame(content)
    columns.pack(fill="both", expand=True)
    columns.columnconfigure(0, weight=1, uniform="columns")
    columns.columnconfigure(1, weight=1, uniform="columns")
    columns.rowconfigure(0, weight=1)

    left_panel = ttk.Frame(columns)
    left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
    right_panel = ttk.Frame(columns)
    right_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

    resume_frame = ttk.LabelFrame(left_panel, text="Resume PDF", padding=12)
    resume_frame.pack(fill="x", pady=(0, 14))
    ttk.Button(resume_frame, text="Choose Resume PDF", command=choose_resume).pack(anchor="w")
    ttk.Label(resume_frame, textvariable=resume_filename, wraplength=320, style="Subtitle.TLabel").pack(anchor="w", fill="x", pady=(8, 0))

    job_frame = ttk.LabelFrame(left_panel, text="Job description", padding=12)
    job_frame.pack(fill="both", expand=True, pady=(0, 12))
    job_description = ScrolledText(
        job_frame, width=1, height=5, wrap="word", font=("Segoe UI", 11),
        background="white", foreground="#243449", insertbackground="#243449",
        relief="flat", borderwidth=0, padx=10, pady=10,
        highlightthickness=1, highlightbackground="#cdd9e5", highlightcolor="#326b8e",
    )
    job_description.pack(fill="both", expand=True)

    actions = ttk.Frame(left_panel)
    actions.pack(fill="x", pady=(0, 14))
    ttk.Button(actions, text="Analyze", command=analyze, style="Accent.TButton").pack(side="right")
    ttk.Button(actions, text="Clear", command=clear).pack(side="right", padx=(0, 8))

    results_frame = ttk.LabelFrame(right_panel, text="Results", padding=12)
    results_frame.pack(fill="both", expand=True)
    score_frame = ttk.Frame(results_frame)
    score_frame.pack(fill="x", pady=(0, 8))
    ttk.Label(score_frame, text="Match score", style="Subtitle.TLabel").pack(side="left")
    ttk.Label(score_frame, textvariable=score_display, style="Score.TLabel").pack(side="right")
    ttk.Separator(results_frame).pack(fill="x", pady=(0, 10))

    results_text = ScrolledText(
        results_frame, width=1, height=8, wrap="word", state="disabled", font=("Segoe UI", 10),
        background="#f9fbfd", foreground="#243449", relief="flat", borderwidth=0,
        padx=12, pady=10, spacing3=5,
    )
    results_text.tag_configure("heading", font=("Segoe UI", 11, "bold"), foreground="#244e73")
    results_text.pack(fill="both", expand=True)

    suggestions_frame = ttk.LabelFrame(right_panel, text="Suggestions", padding=10)
    suggestions_frame.pack(fill="x", pady=(12, 0))
    suggestions_text = ScrolledText(
        suggestions_frame, width=1, height=3, wrap="word", state="disabled",
        font=("Segoe UI", 10), background="#f9fbfd", foreground="#243449",
        relief="flat", borderwidth=0, padx=10, pady=8,
    )
    suggestions_text.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
