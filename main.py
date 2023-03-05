import pytest
import sys
import getopt

# App's root. Reads command line and starts pythest Test Suite.
def main():
    blender_path = '/opt/blender-3.4.1-linux-x64/blender'
    output_path = './test_result'
    x_resolutiontry = 200
    y_resolution = 200
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ho:e:x:y:")
        for opt, arg in opts:
            if opt == '-h':
                print ('-e --path to blender executable (required)\n'
                '-o  patch to test result dir, default = ./test_result\n'
                '-x  result image x resolution, defaut = 0\n'
                '-y result image y resolution, default = 0')
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

    exit_code = pytest.main(['test_app.py', '-s', '--json-report', '--json-report-indent=2'])
    print(exit_code)

main()