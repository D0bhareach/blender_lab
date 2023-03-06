import pytest
import sys
import getopt
from pathlib import Path

# App's root. Reads command line and starts pythest Test Suite.
def main():
    blender_path = '/opt/blender-3.4.1-linux-x64/blender'
    output_path = './test_result'
    x_resolution = 1024
    y_resolution = 1024
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ho:e:x:y:")
        for opt, arg in opts:
            if opt == '-h':
                print ('-e --path to blender executable (required), default = /opt/blender-3.4.1-linux-x64/blender\n'
                '-o  patch to test result dir, default = ./test_result\n'
                '-x  result image x resolution, defaut = 1024\n'
                '-y result image y resolution, default = 1024')
                sys.exit()
            elif opt == "-e":
                blender_path = arg
            elif opt in ("-o"):
                output_path = arg
            elif opt in ("-x"):
                x_resolution = arg
            elif opt in ("-y"):
                y_resolution = arg
            else:
                print(f"Unhandled option {opt}")
                sys.exit(1)
    except getopt.GetoptError as e:
        print(f'Argument parsing error: {e}')
        sys.exit(1)

    # check if output dir exist if not creare
    out_p = Path(output_path).resolve()
    if not out_p.exists():
        out_p.mkdir(mode=0o760)



    # At first I try to pass args with command line using pytest_generate_tests(metafunc)
    # But it inserts memory location to object. So now use tmp file and 
    # test fixture to insert args in tests. 
    # create and write args to .tmp file
    path = Path('.').resolve()
    path = path / '.tmp'
    path.unlink(missing_ok=True)
    path.touch(mode=0o600)
    with path.open('w') as f:
        f.write(str(output_path) + '\n')
        f.write(str(x_resolution) + '\n')
        f.write(str(y_resolution) + '\n')

    exit_code = pytest.main(
        ['test_app.py', '-s', '--json-report', '--json-report-indent=2'])
    # delete tmp file.
    path.unlink(missing_ok=True)
    print(exit_code)

main()