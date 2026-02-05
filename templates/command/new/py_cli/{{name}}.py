#!/usr/bin/env python3

import click
import os


@click.group()
@click.pass_context
def main(
    ctx,
):
    """{{description}}"""

    ctx.ensure_object(dict)


{% if commands is defined -%}
{% for command in commands -%}
@main.command()
@click.pass_context
def {{command}}(ctx):
    """<{{command}} description>"""
    pass

{% endfor %}
{%- endif %}


if __name__ == "__main__":
    main()
