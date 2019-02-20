
import click
from ipammanager import utils

def resolve_subnet(service, addresses):
    result = []
    for addr in addresses:
        result.append(service.show_subnet(addr.subnetId))
    return result

def show_ip(addresses, subnets):
    data = []
    if isinstance(addresses, list):
        for addr, subnet in zip(addresses, subnets):
            temp = [
                addr.ip, 
                f"{addr.hostname if addr.hostname else '-'}", 
                f"{subnet.subnet}/{subnet.mask}",
                f"{f'{addr.description[:20] !r}' if addr.description else '-'}"
            ]
            data.append(temp)
    else:
        temp = [
            addr.ip, 
            f"{addr.hostname if addr.hostname else '-'}", 
            f"{subnet.subnet}/{subnet.mask}", 
            f"{f'{addr.description[:20] !r}' if addr.description else '-'}"
        ]
        data.append(temp)

    output = utils.Formatter.from_arr(
        data,
        headers=["IP", "HOSTNAME", "SUBNET", "DESCRIPTION"]
    )
    click.echo("\n".join(output))