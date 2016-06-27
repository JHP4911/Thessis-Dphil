"""Script to run through Thesis for 'ToDos' and word count"""
import subprocess
import os

# Set top level directory for the main thesis
MAIN_THESIS_DIR = "C:\Users\jonathan\Documents\UniOfOxford\DPhilWork\Thesis"


def check_empty_line(string):
    """ Check whether a string is empty
    """
    split_string = string.split()
    if not split_string:
        return True
    else:
        return False


def read_thesis_file(filename, todofile):
    """Read a file from the thesis document and look for todos.
    If todos are found then write them to the todo file
    """
    todo_found = False
    with open(filename+".tex", "r") as thesis_file:
        for thesis_line in thesis_file:
            line_empty = check_empty_line(thesis_line)
            if not line_empty:
                if "{TODO:}" in thesis_line:
                    todo_found = True
                    ref_start_index = thesis_line.index("{")
                    ref_end_index = thesis_line.index("}")
                    ref_string = '{' + \
                        thesis_line[ref_start_index+1:ref_end_index] \
                        + '}'
                    todo_string = '{'+thesis_line[ref_end_index+16:-1].strip()
                    todofile.write("        \\item \\hyperlink{}{}\n".format(
                        ref_string, todo_string))
    return todo_found


def run_system_command(command_string):
    """Function used to run the system command and return the log
    """
    process = subprocess.Popen(command_string, stdout=subprocess.PIPE,
                               shell=True)  # Run system command
    output = process.communicate()  # Get the log.
    print output[0]  # return the log file

# ---------------------------
# Main Script
# --------------------------
os.chdir(MAIN_THESIS_DIR)
MAIN_FILENAME = "main.tex"
FILE_KEYWORDS = ["include", "input"]
TODO_FILENAME = "specialpages/todos.tex"

# Open the to TODO_FILE for writing the list of todos from the thesis.
TODO_FILE = open(TODO_FILENAME, "w")
TODO_FILE.write("\\chapter{ToDos}\n")
TODO_FILE.write("\\textcolor{red}{\n")
TODO_FILE.write("    \\begin{enumerate}\n")

any_todos = False
# Read the thesis document
with open(MAIN_FILENAME, "r") as mainfile:  # open mainfile
    for line in mainfile:
        empty_line = check_empty_line(line)
        if not empty_line:
            if "%" in line.lstrip()[0]:  # check if it's a comment line
                pass
            # If "input" or "include" in line then read the file.
            elif (any(x in line for x in FILE_KEYWORDS) and
                  "includeonly" not in line):
                start_index = line.index('{')
                end_index = line.index('}')
                thesis_doc_filename = line[start_index + 1:end_index]
                found_a_todo = read_thesis_file(thesis_doc_filename, TODO_FILE)
                if not any_todos and found_a_todo:
                    any_todos = True

# Finish the list and close the TODO_FILE
TODO_FILE.write("    \\end{enumerate}\n")
TODO_FILE.write("}\n")
TODO_FILE.close()

# If there are no todos then just create an empty file
if not any_todos and os.path.isfile(TODO_FILENAME):
    os.remove(TODO_FILENAME)

# Run TeXCount to get the word count for the thesis
TEXCOUNT_OPTIONS = "-inc"
TEXCOUNT_COMMAND_STRING = "texcount {} {}".format(TEXCOUNT_OPTIONS,
                                                  MAIN_FILENAME)
run_system_command(TEXCOUNT_COMMAND_STRING)
