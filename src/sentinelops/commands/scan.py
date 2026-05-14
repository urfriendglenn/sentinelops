import click
from sentinelops.core.scanner import run_scan
# from sentinelops.reporters.console import print_scan_result

@click.command()
@click.option(
        "--target",
        required=True,
        help="Target domain to scan",
        )
def scan(target: str) -> None:
    """
    Run a basic scan against a target
    """
    result = run_scan(target)
    if result == "Invalid Response":
        click.echo("Error: Received Invalid Response")
    else:
        click.echo(result)
    # print_scan_result(result)
