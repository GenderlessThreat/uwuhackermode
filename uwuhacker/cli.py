import click
from your_project.downloader import download_tool
from your_project.executor import execute_tool
from your_project.favorites import add_to_favorites, view_favorites

@click.group()
def cli():
    """Tool Management CLI"""
    pass

@cli.command()
@click.argument('tool_name')
def download(tool_name):
    """Download a tool by name."""
    download_tool(tool_name)

@cli.command()
@click.argument('tool_name')
def run(tool_name):
    """Run a tool by name."""
    execute_tool(tool_name)

@cli.command()
@click.argument('tool_name')
def favorite(tool_name):
    """Add a tool to favorites."""
    add_to_favorites(tool_name)

@cli.command()
def favorites():
    """View favorite tools."""
    view_favorites()

if __name__ == '__main__':
    cli()
