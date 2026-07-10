import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).parent / "data" / "chatbot.db"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with get_connection() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                course TEXT NOT NULL,
                fee_paid REAL NOT NULL,
                fee_due REAL NOT NULL,
                batch_time TEXT NOT NULL,
                enrollment_status TEXT NOT NULL
            );

            INSERT OR IGNORE INTO students
                (student_id, name, email, course, fee_paid, fee_due,
                 batch_time, enrollment_status)
            VALUES
                (101, 'Ravi Kumar', 'ravi@example.com',
                 'GEN AI & Agentic AI with Python',
                 9000, 9000, '7:00 PM IST', 'ACTIVE'),
                (102, 'Anusha Reddy', 'anusha@example.com',
                 'Java Full Stack',
                 25000, 0, '7:30 AM IST', 'ACTIVE'),
                (103, 'Kiran Rao', 'kiran@example.com',
                 'GEN AI & Agentic AI with Python',
                 18000, 0, '7:00 PM IST', 'COMPLETED');
            """
        )


def fetch_student_context(payload: dict[str, Any]) -> str:
    """Return only the student record explicitly identified in the request."""
    student_id = payload.get("student_id")
    if student_id is None:
        return (
            "No student_id was supplied. No private student database record "
            "was accessed."
        )

    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT student_id, name, course, fee_paid, fee_due,
                   batch_time, enrollment_status
            FROM students
            WHERE student_id = ?
            """,
            (student_id,),
        ).fetchone()

    if row is None:
        return f"No student record exists for student_id={student_id}."

    return (
        f"Student ID: {row['student_id']}\n"
        f"Name: {row['name']}\n"
        f"Course: {row['course']}\n"
        f"Fee paid: INR {row['fee_paid']:.2f}\n"
        f"Fee due: INR {row['fee_due']:.2f}\n"
        f"Batch time: {row['batch_time']}\n"
        f"Enrollment status: {row['enrollment_status']}"
    )
