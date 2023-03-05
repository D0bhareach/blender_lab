import time
import subprocess
import pytest
from pathlib import Path

@pytest.fixture
def args():
    path = Path('./.tmp').resolve()
    assert path.exists(), 'Path {path} to temporary file doesn\'t existst'
    assert path.is_file()
    res = list()
    with path.open() as f:
        res.extend(f.readlines())
    return res

# Test suite. Call blender in process and pass script to run.
class TestBpy:
    """Test class for blender."""


    def test_simple(self, args):
        """Test One"""

        
        # Always receive three agrs.
        # get args and pass it to string as a string. Later in test will manipulate with args.
        subprocess.run(
            f"/opt/blender-3.4.1-linux-x64/blender --background  \
            --python /home/ferrislav/projects/python/labs/luxsoft/tests/test_simple.py\
            -- {args[0].strip()} {args[1].strip()} {args[2].strip()}",
            shell = True,
            text = True,
            )

    # def test_two(self):
    #     """Test Two"""
    #     assert 2 == 2

    # def test_three(self):
    #     """Test Three"""
    #     assert 3 == 3

    # def test_print_name(self, args):
    #     print (f"Displaying name: {args}")

