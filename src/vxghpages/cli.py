__version__ = "0.2.0"
"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mvxghpages` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``vxghpages.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``vxghpages.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
from .creator import Creator

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version: %s' % __version__)
    ctx.exit()

def create_gh(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    creator = Creator()
    creator.run()

@click.command()
@click.argument('names', nargs=-1)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--create', is_flag=1, is_eager=True,
              expose_value=False, callback=create_gh)
def main(names):
    click.echo(repr(names))
