import os
import subprocess
import urllib.request

# List of example tools (you can replace with actual tools)
tools = [
    {"name": "ACEshark", "description": "A utility for extracting and analyzing Windows service configurations.", "download_url": "https://example.com/ACEshark.tar.gz"},
    {"name": "XSRFProbe", "description": "An advanced CSRF/XSRF audit and exploitation toolkit.", "download_url": "https://example.com/XSRFProbe.tar.gz"},
    {"name": "Tool C", "description": "A tool to automate reconnaissance.", "download_url": "https://example.com/ToolC.tar.gz"}
]

favorites = []

def install_dependencies(tool):
    """Install dependencies for a given tool."""
    print(f"\nInstalling dependencies for {tool['name']}...")
    requirements_path = os.path.join(tool['name'], 'requirements.txt')
    if os.path.exists(requirements_path):
        subprocess.run(["pip", "install", "-r", requirements_path])
        print("Dependencies installed successfully!")
    else:
        print("No requirements.txt found. Ensure dependencies are installed manually.")

def search_tool():
    """Allow the user to search for a tool by name or keyword."""
    query = input("\nEnter a keyword to search for a tool: ").lower()
    matches = [tool for tool in tools if query in tool['name'].lower() or query in tool['description'].lower()]
    if matches:
        print("\nSearch Results:")
        for tool in matches:
            print(f"- {tool['name']}: {tool['description']}")
    else:
        print("No tools found matching your search criteria.")

def download_tool(tool):
    """Download the tool to the current working directory."""
    print(f"\nDownloading {tool['name']}...")
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # The download URL for the tool
        download_url = tool['download_url']

        # The filename is the last part of the URL, usually after the last slash
        file_name = download_url.split("/")[-1]

        # Full path where the tool will be saved
        download_path = os.path.join(current_directory, file_name)

        # Download the tool
        urllib.request.urlretrieve(download_url, download_path)

        print(f"Download completed: {file_name} saved to {current_directory}")
    except Exception as e:
        print(f"Failed to download the tool: {e}")

def execute_tool(tool):
    """Execute a tool from the list."""
    print(f"\nExecuting {tool['name']}...")
    try:
        if tool['name'] == 'XSRFProbe':
            # For XSRFProbe, run the tool with necessary arguments
            subprocess.run(["xsrfprobe", "--help"], check=True)
        else:
            subprocess.run(["python", os.path.join(tool['name'], "main_script.py")], check=True)
    except Exception as e:
        print(f"Failed to execute the tool: {e}")

def add_to_favorites(tool):
    """Add a tool to the favorites list."""
    if tool not in favorites:
        favorites.append(tool)
        print(f"{tool['name']} added to favorites.")
    else:
        print(f"{tool['name']} is already in favorites.")

def view_favorites():
    """Display the list of favorite tools."""
    if favorites:
        print("\nFavorites List:")
        for tool in favorites:
            print(f"- {tool['name']}")
    else:
        print("No tools in favorites.")

def show_help():
    """Display a help guide for the user."""
    print("\n--- Help Menu ---")
    print("1. Select a tool from the menu by entering its number.")
    print("2. Choose to download or run the tool.")
    print("3. Follow the instructions displayed on the screen.")
    print("4. Use the search option to find tools by keywords.")
    print("5. Add tools to favorites for quick access.")
    print("6. For more information about a tool, follow the setup steps listed in the description.")

def display_advanced_menu():
    """Display the advanced tool menu with options for searching, favorites, and help."""
    # ASCII Art Title
    ascii_art = """
██╗░░░██╗░██╗░░░░░░░██╗██╗░░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░███╗░░░███╗░█████╗░██████╗░███████╗
██║░░░██║░██║░░██╗░░██║██║░░░██║██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝
██║░░░██║░╚██╗████╗██╔╝██║░░░██║███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝██╔████╔██║██║░░██║██║░░██║█████╗░░
██║░░░██║░░████╔═████║░██║░░░██║██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░
╚██████╔╝░░╚██╔╝░╚██╔╝░╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██║░╚═╝░██║╚█████╔╝██████╔╝███████╗
░╚═════╝░░░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝
    """

    # Display the ASCII Art title
    print(ascii_art)

    print("\n--- Tool Menu ---")
    for i, tool in enumerate(tools, start=1):
        print(f"{i}. {tool['name']} - {tool['description']}")
    print(f"{len(tools) + 1}. Search for a tool")
    print(f"{len(tools) + 2}. View favorites")
    print(f"{len(tools) + 3}. Help")
    print(f"{len(tools) + 4}. Exit")

def tool_menu():
    """Main menu to manage the user's interaction with the tools."""
    while True:
        display_advanced_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= len(tools):
                selected_tool = tools[choice - 1]
                print(f"\nYou selected: {selected_tool['name']}")
                action = input(f"Would you like to download (d) or run (r) {selected_tool['name']}? (d/r): ").lower()
                if action == 'd':
                    download_tool(selected_tool)
                elif action == 'r':
                    print(f"Running {selected_tool['name']}...")
                    execute_tool(selected_tool)
                else:
                    print("Invalid choice.")
            elif choice == len(tools) + 1:
                search_tool()
            elif choice == len(tools) + 2:
                view_favorites()
            elif choice == len(tools) + 3:
                show_help()
            elif choice == len(tools) + 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tool_menu()
