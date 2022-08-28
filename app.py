#!/usr/bin/env python
import click


@click.command()
def hello():
    click.echo('Walexkino Docker cruise')
    
    
    
if __name__ == '__main__':
    hello()