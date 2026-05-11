import click
from sentinelops import __version__

@click.command("sentinelops")
@click.version_option(__version__, prog_name="sentinelops")
def main():
    click.echo("Welcome to SentinelOps")

if __name__ == "__main__":
    main()
