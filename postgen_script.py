"""Add link to Google Colab for each notebook

Ripped from https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/tools/add_navigation.py
"""

import os
import glob
import nbformat
from nbformat.v4.nbbase import new_markdown_cell

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def iter_notebooks():
    """Returns notebook files in all subdirectories"""

    return (filename for filename in glob.iglob(ROOT_DIR + '**/**/*.ipynb', recursive=True))

LINK_COMMENT = "<!--NAVIGATION-->\n"

COLAB_LINK = """
<a href="https://colab.research.google.com/github/bpesquet/machine-learning-katas/blob/master/{notebook_filename}"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open in Google Colaboratory"></a>
"""

def iter_links():
    """Returns paths to notebooks and HTML link to Google Colab for each of them"""

    for nb_path in iter_notebooks():
        link = LINK_COMMENT
        link += COLAB_LINK.format(notebook_filename=os.path.relpath(nb_path))
        yield os.path.join(ROOT_DIR, nb_path), link

def write_links():
    """Add or update a cell in each notebook with a Google Colab link"""

    for nb_name, link in iter_links():
        notebook = nbformat.read(nb_name, as_version=4)
        nb_file = os.path.basename(nb_name)
        is_comment = lambda cell: cell.source.startswith(LINK_COMMENT)

        if is_comment(notebook.cells[0]):
            print("Amending link for {0}".format(nb_file))
            notebook.cells[0].source = link
        else:
            print("Inserting link for {0}".format(nb_file))
            notebook.cells.insert(0, new_markdown_cell(source=link))

        nbformat.write(notebook, nb_name)

if __name__ == '__main__':
    write_links()
