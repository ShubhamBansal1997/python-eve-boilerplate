# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-19 01:09:30
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-19 02:34:19
"""Fabric file for managing this project.

See: http://www.fabfile.org/

"""
from __future__ import absolute_import, unicode_literals, with_statement

# Standard Library
from contextlib import contextmanager as _contextmanger
from functools import partial
from os.path import dirname, isdir, join

# Third party Stuff
from fabric.api import local as fabric_local, env
from fabric import api as fab

local = partial(fabric_local, shell='/bin/bash')

HERE = dirname(__file__)

# ==============================================================================
# Settings
# ==============================================================================
env.project_name = 'python-eve-boilerplate'
env.apps_dir = join(HERE, env.project_name)
env.docs_dir = join(HERE, 'docs')
env.virtualenv_dir = join(HERE, 'venv')
env.requirements_file = join(HERE, 'requirements/development.txt')
env.shell = '/bin/bash -l -i -c'

env.use_ssh_config = True
env.dotenv_path = join(HERE, '.env')
env.config_setter = local


def init(vargant=False):
    """ Prepare a local machine for development."""

    install_requirements()


def install_requirements(file=env.requirements_file):
    """Install project dependencies"""
    verify_virtualenv()
    # activate virtualenv and install
    with virtualenv():
        local('pip install -r %s' % file)


def serve_docs(options=''):
    """Start a local server to view documentation changes."""
    with fab.lcd(HERE) and virtualenv():
        local('mkdocs server {}'.format(options))


def shell():
    manage('shell_plus')


def test(options='--pdb --cov'):
    """
    Run tests locally. By Default, it runs the test using --ipdb.
    You can skip running it using --ipdb by running - `fab test:""`
    """
    with virtualenv():
        local('flake8 .')
        local('py.test %s' % options)


def serve():
    """
    Run local development server, making sure that dependencies are
    upto date.
    """
    install_requirements()
    local('python main.py')




# Helpers
# -------------------------------------------------------------------------


@_contextmanger
def virtualenv():
    """
    Activates virtualenv context for other commands to run inside it
    """
    with fab.cd(HERE):
        with fab.prefix('source %(virtualenv_dir)s/bin/activate' % env):
            yield


def verify_virtualenv():
    """
    This modules check and install virtualenv if it not present
    It also creates local virtualenv directory if it's not present
    """
    from distutils import spawn
    if not spawn.find_executable('virtualenv'):
        local('sudo pip install virtualenv')

    if not isdir(env.virtualenv_dir):
        local('virtualenv %(virtualenv_dir)s -p $(which python3)' % env)
