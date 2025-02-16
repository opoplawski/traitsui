# -*- coding: utf-8 -*-
#
# Traits documentation build configuration file, created by
# sphinx-quickstart on Tue Jul 22 10:52:03 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.


import os

from traitsui import __version__ as version

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
# sys.path.append(os.path.abspath('some/directory'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    # Link to code in sphinx generated API docs
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    'traits.util.trait_documenter',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = 'traitsui'
copyright = '2008-2023, Enthought'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directories, that shouldn't be searched
# for source files.
# exclude_dirs = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Options for Sphinx copybutton extension
# ---------------------------------------

# Matches prompts - "$ ", ">>>" and "..."
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "TraitsUI {} Documentation".format(version.split('.')[0])

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (within the static path) to place at the top of
# the sidebar.
# html_logo = "e-logo-rev.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', os.path.join('tutorials', 'code_snippets')]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
# html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
# html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Traitsuidoc'

# html theme information
try:
    import enthought_sphinx_theme

    html_theme_path = [enthought_sphinx_theme.theme_path]
    html_theme = 'enthought'
except ImportError as exc:
    import warnings

    msg = '''Can't find Enthought Sphinx Theme, using default.
            Exception was: {}
            Enthought Sphinx Theme can be downloaded from
            https://github.com/enthought/enthought-sphinx-theme'''
    warnings.warn(RuntimeWarning(msg.format(exc)))

    # old defaults
    html_logo = "e-logo-rev.jpg"
    html_favicon = "et.png"
    html_style = 'default.css'
    html_theme = 'classic'

# #html_theme = 'bizstyle'
# html_logo = "e-logo-rev.png"
# #html_style = 'default.css'
# #html_theme = 'classic'

# Useful aliases to avoid repeating long URLs.
extlinks = {
    'github-demo': (
        f'https://github.com/enthought/traitsui/tree/{version}/traitsui/examples/demo/%s',
        'github-demo',
    )
}

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
    (
        'index',
        'TraitsUI.tex',
        'TraitsUI 4 User Manual',
        'Enthought, Inc.',
        'manual',
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = "enthought_logo.jpg"
latex_logo = "e-logo-rev.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

# Autodoc options
autodo_mock_imports = ["wx", "PySide", "PyQt", "PyQt5"]

# Intersphinx configuration
intersphinx_mapping = {
    'traits': ('http://docs.enthought.com/traits', None),
    'pyface': ('http://docs.enthought.com/pyface', None),
}


def autodoc_skip_member(app, what, name, obj, skip, options):
    # Skip load_tests targeting unittest discover
    is_load_tests = what == "module" and name == "load_tests"
    return skip or is_load_tests


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
