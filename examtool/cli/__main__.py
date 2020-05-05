import click

from examtool.cli.check_dupes import check_dupes
from examtool.cli.compile_all import compile_all
from examtool.cli.deploy import deploy
from examtool.cli.download import download
from examtool.cli.gradescope_upload import gradescope_upload
from examtool.cli.login import login
from examtool.cli.logs import logs
from examtool.cli.send import send


@click.group()
def cli():
    """
    This is the CLI for the 61A examtool.
    An equivalent GUI is available at https://exam.cs61a.org/admin/.
    To write an exam, visit https://write.final.cs61a.org, and export the JSON.
    Contact Rahul Arya on the EECS Crossroads Slack for help.
    """
    pass


cli.add_command(check_dupes)
cli.add_command(compile_all)
cli.add_command(deploy)
cli.add_command(download)
cli.add_command(gradescope_upload)
cli.add_command(logs)
cli.add_command(send)
cli.add_command(login)

if __name__ == '__main__':
    cli()
