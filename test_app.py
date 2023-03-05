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
    BLENDER = "/opt/blender-3.4.1-linux-x64/blender"
    path = Path(__file__).parent
    TESTS = path / 'tests'


    # def test_simple(self, args):
    #     """Test Simple Blender Image"""

    #     path = self.TESTS / 'test_simple.py'
    #     
    #     # Always receive three agrs.
    #     # get args and pass it to string as a string. Later in test will manipulate with args.
    #     subprocess.run(
    #         f"{self.BLENDER} --background\
    #         --python {path}\
    #         -- {args[0].strip()} {args[1].strip()} {args[2].strip()}",
    #         shell = True,
    #         text = True,
    #         )

    def test_two(self, args):
    #     """Test Blender image with colors"""

        path = self.TESTS / 'test_material.py'
        subprocess.run(
            f"{self.BLENDER} --background\
            --python {path}\
            -- {args[0].strip()} {args[1].strip()} {args[2].strip()}",
            shell = True,
            text = True,
            )

    # def test_three(self):
    #     """Test Three"""
    #     assert 3 == 3

    # def test_print_name(self, args):
    #     print (f"Displaying name: {args}")

