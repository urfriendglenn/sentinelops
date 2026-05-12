import click
import subprocess
from sentinelops import __version__

@click.command("sentinelops")
@click.version_option(__version__, prog_name="sentinelops")
@click.argument("site")
def main(site):
    if site is None:
        click.echo(f"Welcome to SentinelOps {__version__}. Use --help for more information.")
    else:
        scan_result = subprocess.run(["curl", "-IL", site], capture_output=True, text=True)
        click.echo(scan_result.stdout)

if __name__ == "__main__":
    main()
