
import click

def resolve_subnet(service, addresses):
    result = []
    for addr in addresses:
        result.append(service.show_subnet(addr.subnetId))
    return result

def show_ip(addresses, subnets):
    click.echo(f"{'IP': <20} {'HOSTNAME': <20} {'SUBNET': <20} {'DESCRIPTION': <30}")
    if isinstance(addresses, list):
        for addr, subnet in zip(addresses, subnets):
            output = "{ip: <20} {hostname: <20} {subnet: <20} {description: <30}".format(
                ip=addr.ip,
                hostname=addr.hostname if addr.hostname else '-',
                subnet=f"{subnet.subnet}/{subnet.mask}",
                description=f"{f'{addr.description[:20] !r}' if addr.description else '-'}"
            )
            click.echo(output)
    else:
        output = "{ip: <20} {hostname: <20} {subnet: <20} {description: <30}".format(
            ip=addresses.ip,
            hostname=addresses.hostname if addresses.hostname else '-',
            subnet=f"{subnet.subnet}/{subnet.mask}",
            description=f"{f'{addresses.description[:20] !r}' if addresses.description else '-'}"
        )
        click.echo(output)