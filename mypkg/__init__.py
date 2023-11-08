import click


@click.group()
# @click.option("--name", help="Enter your name.")
def cli():
    # name = click.prompt("What is your name?")
    # click.echo(f"Hello world {name}")
    pass


@cli.command()
@click.option("--username", is_flag=True, help="What is your username?")
def user(username):
    username = click.prompt("What is your username?")
    click.echo(f"Your username is {username}")


@cli.command()
@click.option("--d", is_flag=True, help="Enter your age")
def dob(d):
    d = click.prompt("How old are you?")
    convert = int(d)
    result = 2023 - convert
    click.echo(f"Your date of birth is {result}")
