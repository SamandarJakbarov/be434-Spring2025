"""Tests for blastomatic.py"""

import csv
import os
import random
import re
import string
from subprocess import getstatusoutput

PRG = './blastomatic.py'
HITS1 = './inputs/hits1.csv'
HITS2 = './inputs/hits2.csv'
META = './inputs/meta.csv'


def test_exists() -> None:
    """Ensure required files exist."""
    for file in [PRG, HITS1, HITS2, META]:
        assert os.path.isfile(file)


def test_usage() -> None:
    """Test -h and --help flags show usage."""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage:')


def test_bad_annotations() -> None:
    """Fail when given bad annotation file."""
    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} --annotations {bad} -b {HITS1}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


def test_bad_input_file() -> None:
    """Fail when given bad input file."""
    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} --blasthits {bad} -a {META}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


def test_good_input() -> None:
    """Pass on good input and output correct file."""
    outfile = 'out.csv'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{PRG} -a {META} -b {HITS1}'
        rv, out = getstatusoutput(cmd)
        expected = f'Exported 500 to "{outfile}".'
        assert rv == 0
        assert out == expected
        assert os.path.isfile(outfile)

        with open(outfile, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            expected_fields = {'qseqid', 'pident', 'depth', 'lat_lon'}
            assert set(reader.fieldnames or '') == expected_fields
            records = sorted(list(reader), key=lambda d: d['qseqid'])
            assert len(records) == 500
            assert records[0]['qseqid'] == 'CAM_READ_0234442157'
            assert records[-1]['lat_lon'] == '42.503056,-67.24'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


def test_delimiter() -> None:
    """Check that user-specified delimiter works."""
    outfile = 'out.xxx'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        delim = ','
        cmd = f'{PRG} -a {META} -b {HITS1} -d "{delim}" -o {outfile}'
        rv, out = getstatusoutput(cmd)
        expected = f'Exported 500 to "{outfile}".'
        assert rv == 0
        assert out == expected
        assert os.path.isfile(outfile)

        with open(outfile, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=delim)
            expected_fields = {'qseqid', 'pident', 'depth', 'lat_lon'}
            assert set(reader.fieldnames or '') == expected_fields
            records = sorted(list(reader), key=lambda d: d['qseqid'])
            assert len(records) == 500
            assert records[0]['qseqid'] == 'CAM_READ_0234442157'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


def test_guess_delimiter() -> None:
    """Test automatic delimiter guessing based on file extension."""
    tsv_ext = random.choice(['.txt', '.tab', '.tsv'])
    outfile, delim = ('out.csv', ',') if random.choice([0, 1]) else (
        'out' + tsv_ext, '\t'
    )

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{PRG} -a {META} -b {HITS2} -o {outfile}'
        rv, out = getstatusoutput(cmd)
        expected = f'Exported 252 to "{outfile}".'
        assert rv == 0
        assert out == expected
        assert os.path.isfile(outfile)

        with open(outfile, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=delim)
            expected_fields = {'qseqid', 'pident', 'depth', 'lat_lon'}
            assert set(reader.fieldnames or '') == expected_fields
            records = list(reader)
            assert len(records) == 252
            assert records[-1]['qseqid'] == 'JCVI_READ_1100018174123'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


def test_pctid() -> None:
    """Test filtering by percent identity (-p)."""
    outfile = 'out.tsv'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{PRG} -a {META} -b {HITS2} -p 90 -o {outfile}'
        rv, out = getstatusoutput(cmd)
        expected = f'Exported 101 to "{outfile}".'
        assert rv == 0
        assert out == expected
        assert os.path.isfile(outfile)

        with open(outfile, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            expected_fields = {'qseqid', 'pident', 'depth', 'lat_lon'}
            assert set(reader.fieldnames or '') == expected_fields
            records = list(reader)
            assert all(float(r['pident']) >= 90 for r in records)
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


def random_string() -> str:
    """Generate a random string for fake filenames."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
