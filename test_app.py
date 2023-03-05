import time
import subprocess

# Test suite. Call blender in process and pass script to run.
class TestBpy:
    """Test class for blender."""

    def test_simple(self):
        """Test One"""

        subprocess.run(
            "/opt/blender-3.4.1-linux-x64/blender --background  \
            --python /home/ferrislav/projects/python/labs/luxsoft/tests/test_simple.py \
            -- --verbose"
            ,
            shell = True,
            text = True,
            )
        assert 100 != 1

    def test_two(self):
        """Test Two"""
        assert 2 == 2

    def test_three(self):
        """Test Three"""
        assert 3 == 3
