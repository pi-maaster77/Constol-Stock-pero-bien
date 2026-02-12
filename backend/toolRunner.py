# backend/toolRunner.py

from tools import TOOLS


def main():
    tools = list(TOOLS.values())

    while True:
        print("\nHerramientas:\n")

        for i, tool in enumerate(tools, start=1):
            print(f"{i}. {tool.NAME}")

        try:
            choice = int(input("\n> "))

            tools[choice - 1].main()

        except (ValueError, IndexError):
            print("Opción inválida")

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
