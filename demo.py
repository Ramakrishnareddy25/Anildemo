"""Simple module demonstrating clean Python code."""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Main function to execute the script."""
    user_name = "World"
    message = greet(user_name)
    print(message)


if __name__ == "__main__":
    main()
