""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './howdy.py'


# --------------------------------------------------
    
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

#________

def test_flake8():
    """Run flake8 to check formatting"""
    rv, out = getstatusoutput('flake8 howdy.py')
    assert rv == 0

#________

def test_pylint():
    """Run pylint to check for errors"""
    rv, out = getstatusoutput('pylint howdy.py')
    assert rv == 0



# --------------------------------------------------
def test_defaults():
    """ Prints expected default values """

    rv, out = getstatusoutput(f'{PRG}')
    assert rv == 0
    assert out.strip() == 'Howdy, Stranger.'


# --------------------------------------------------
def test_greeting():
    """ Accepts greeting """

    for opt in ['-g', '--greeting']:
        rv, out = getstatusoutput(f'{PRG} {opt} Hola')
        assert rv == 0
        assert out.strip() == 'Hola, Stranger.'


# --------------------------------------------------
def test_name():
    """ Accepts name """

    for opt in ['-n', '--name']:
        rv, out = getstatusoutput(f'{PRG} {opt} Jorge')
        assert rv == 0
        assert out.strip() == 'Howdy, Jorge.'


# --------------------------------------------------
def test_excited():
    """ Prints bang """

    for flag in ['-e', '--excited']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.strip() == 'Howdy, Stranger!'


# --------------------------------------------------
def test_all_options():
    """ Handles all options """

    rv, out = getstatusoutput(f'{PRG} -e -g Greetings -n Sarah')
    assert rv == 0
    assert out.strip() == 'Greetings, Sarah!'
