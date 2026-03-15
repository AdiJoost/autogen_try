from dotenv import load_dotenv

from src.coder import chat

def main():
    load_dotenv()
    chat()


if __name__ == "__main__":
    main()