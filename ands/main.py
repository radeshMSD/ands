#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run this file to run all runnable scripts within `ands`.
"""

def main():
    import glob
    from subprocess import CalledProcessError, check_output, call

    def check():
        passed = 0
        failed = 0
        # Only works for Python 3.5+
        for filename in glob.iglob('./**/*.py', recursive=True):

            if filename.endswith("main.py") or filename.endswith("__init__.py"):
                continue
            
            call(["chmod", "-R", "+x", filename])            
            print(filename, "is now EXECUTABLE.")
            try:
                output = check_output("./" + filename)
                returncode = 0
                print(filename, " PASSED.")
                passed += 1
            except CalledProcessError as e:
                output = e.output
                returncode = e.returncode
                print(filename, " FAILED with status code: ", returncode)
                failed += 1
            except OSError as e:
                print("Probably missing shebang line at the beginning of", filename)

        print("Total scripts passed:", passed)
        print("Total scripts failed:", failed)

    check()

if __name__ == "__main__":
    main()
