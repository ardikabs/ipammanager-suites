
import click

from ipammanager import errors as ipam_err
from ipammanager.scripts.config import ConfigFileProcessor
from ipammanager.scripts.utils import prompt_y_n_question
from .services import init_ipam_service
from .utils import show_ip


def init(ctx):
    config = ctx.obj["CONFIG"]
    phpipam_obj = config["phpipam"]
    service = init_ipam_service(phpipam_obj)
    return service

@click.command("check", help="Check an available ip address in the IPAM server")
@click.argument("subnet_cidr")
@click.option("-r", "--reserve", is_flag=True, help="Reserved an available ip address")
@click.pass_context
def check(ctx, subnet_cidr, reserve):
    
    service = init(ctx)

    try:
        if reserve:
            result = service.reserve_ipaddr(subnet_cidr=subnet_cidr)
        else:
            result = service.check_free_ipaddr(subnet_cidr=subnet_cidr)
    except ipam_err.NotFound as e:
        click.echo(f"Error: {e.message}")
        ctx.exit(1)

    click.echo(f"IPv4 address: {result.data} ({'reserved' if reserve else 'free'})")

@click.command("find", help="Find available ip address in the IPAM server")
@click.argument("ipaddr", required=False)
@click.option("--cidr", help="Subnet CIDR for the address")
@click.option("--hostname", help="Hostname of the address")
@click.option("-y", "--yes", is_flag=True)
@click.pass_context
def find(ctx, ipaddr, cidr, hostname, yes):
    service = init(ctx)

    try:
        if ipaddr:
            result = service.show_ipaddr(address=ipaddr, subnet_cidr=cidr)
        elif hostname:
            result = service.show_ipaddr(hostname=hostname, subnet_cidr=cidr)
    except ipam_err.NotFound as e:
        click.echo(f"Error: {e.message}")
        ctx.exit(1)

    click.echo(f"| IPv4 | Hostname | Description | Note |")
    show_ip(result)

@click.command("new", help="Create a new ip address in the IPAM server")
@click.argument("ipaddr")
@click.option("--cidr", required=True, help="Subnet CIDR for the address")
@click.option("--hostname", help="Hostname of the address")
@click.option("--description", help="Description of the address")
@click.option("--note", help="Note for the address")
@click.option("-y", "--yes", is_flag=True)
@click.pass_context
def new(ctx, ipaddr, cidr, hostname, description, note, yes):
    service = init(ctx)

    try:
        payload = {
            "ip":ipaddr,
            "hostname": hostname,
            "description": description,
            "note": note
        }
        result = service.add_ipaddr(payload=payload, subnet_cidr=cidr, show_result=True)
    except ipam_err.NotFound as e:
        click.echo(f"Error: {e.message}")
        ctx.exit(1)
    
    show_ip(result)

@click.command("put", help="Update existing ip address in the IPAM server")
@click.argument("ipaddr")
@click.option("--cidr", required=True, help="Subnet CIDR for the address")
@click.option("--hostname", help="Hostname of the address")
@click.option("--description", help="Description of the address")
@click.option("--note", help="Note for the address")
@click.option("-y", "--yes", is_flag=True)
@click.pass_context
def update(ctx, ipaddr, cidr, hostname, description, note, yes):
    service = init(ctx)
    try:
        payload = {
            "hostname": hostname,
            "description": description,
            "note": note
        }
        result = service.update_ipaddr(address=ipaddr, payload=payload, subnet_cidr=cidr)
    except ipam_err.NotFound as e:
        click.echo(f"Error: {e.message}")
        ctx.exit(1)
    
    click.echo(f"Info: {result.message} [{ipaddr}]")

@click.command("rm", help="Remove an ip address from IPAM server")
@click.argument("ipaddr")
@click.option("--cidr", required=True, help="Subnet CIDR for the address")
@click.option("-y", "--yes", is_flag=True)
@click.pass_context
def remove(ctx, ipaddr, cidr, yes):
    service = init(ctx)
    try:
        result = service.release_ipaddr(address=ipaddr, subnet_cidr=cidr)
    except ipam_err.NotFound as e:
        click.echo(f"Error: {e.message}")
        ctx.exit(1)
    
    click.echo(f"Info: {result.message} [{ipaddr}]")
