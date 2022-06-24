import keyboard_handler
import click
from packs import Pack

@click.group()
def cli(): pass

@cli.command()
@click.argument('name', nargs=-1)
@click.argument('path', type=click.Path(exists=True))
def add(name, path):
    pass

def run():
    # TODO: Load packs here.
    pack = Pack("Test Sound Pack", "testsoundpack")
    pack.load_keymapping()

    keyboard_handler.main(pack)

if __name__ == "__main__":
    run()