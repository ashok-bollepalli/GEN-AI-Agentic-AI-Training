from typing import Any
import httpx

API_URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_external_api_context(_: dict[str, Any]) -> str:
    """
    Demonstration HTTP API call.

    Replace API_URL and the mapping below with your real batch, payment,
    CRM, weather, ticket, or other business API.
    """
    try:
        with httpx.Client(timeout=5.0) as client:
            response = client.get(API_URL)
            response.raise_for_status()
            data = response.json()

        return (
            "External service status:\n"
            f"- Service record ID: {data.get('id')}\n"
            f"- Message: {data.get('title')}\n"
            f"- Completed: {data.get('completed')}"
        )
    except (httpx.HTTPError, ValueError) as exc:
        # The whole chatbot should not fail just because one dependency failed.
        return f"External API is currently unavailable: {type(exc).__name__}"
