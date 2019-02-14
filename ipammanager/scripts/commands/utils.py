
import click

def show_ip(data):
    
    if isinstance(data, list):
        for d in data:
            click.echo(f"| "
                f"{d.ip} | "
                f"{d.hostname if d.hostname else '-'} | "
                f"{d.description if d.description else '-'} | "
                f"{d.note if d.note else '-'} |"
            )
    else:
        click.echo(f"| "
            f"{data.ip} | "
            f"{data.hostname if data.hostname else '-'} | "
            f"{data.description if data.description else '-'} | "
            f"{data.note if data.note else '-'} |"
        )