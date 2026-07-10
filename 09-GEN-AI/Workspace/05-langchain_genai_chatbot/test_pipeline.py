from database import initialize_database
from pipeline import ask_chatbot
from rag import build_or_load_vector_store


if __name__ == "__main__":
    initialize_database()
    build_or_load_vector_store()

    response = ask_chatbot(
        {
            "question": (
                "I am student 101. What course am I enrolled in, "
                "how much fee is due, and what topics does the course cover?"
            ),
            "student_id": 101,
        }
    )
    print(response)
