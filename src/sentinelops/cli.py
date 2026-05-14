import click
from sentinelops import __version__
from sentinelops.commands.scan import scan

@click.group()
@click.version_option(__version__, prog_name="sentinelops")
def cli():
    """
    SentinelOps security scanning CLI.
    """
    pass

cli.add_command(scan)

def main() -> None:
    cli()