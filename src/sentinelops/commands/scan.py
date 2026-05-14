import click
import subprocess

@click.command()
@click.argument("site")
def scan(site:str):
    scan_result = subprocess.run(["curl", "-IL", site], capture_output=True, text=True)
    click.echo(scan_result.stdout)
