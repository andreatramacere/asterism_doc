# -*- coding: utf-8 -*-
#
# asterism documentation build configuration file, created by
# sphinx-quickstart on Thu Apr 21 10:33:01 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os



# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../'))
import asterism
import sphinx_bootstrap_theme
import sphinx_rtd_theme

print asterism.__file__
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.bibtex',
    #'sphinxcontrib.napoleon',
    'matplotlib.sphinxext.plot_directive',
    'numpydoc',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary'
]


#autosummary_generate = True

#autodoc_default_flags = ['members']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'asterism'
copyright = u'2016, andrea tramacere'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.a'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinxdoc'

#html_theme = 'scipy'
#html_theme_path=['themes']

#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
#html_logo = "head.png"
# Theme options are theme-specific and customize the look and feel of a
# theme further.
#html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    #'navbar_title': "Demo",

    # Tab name for entire site. (Default: "Site")
    #'navbar_site_name': "Site",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    #'navbar_links': [
    #    ("Examples", "examples"),
    #    ("Link", "http://example.com", True),
    #],

    # Render the next and previous page links in navbar. (Default: true)
    #'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    #'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    #'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    #'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    #'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    #'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    #'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    #    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #'bootswatch_theme': "united",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    #'bootstrap_version': "3",
#}


#html_theme = "sphinx_rtd_theme"
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions.append('sphinxjp.themes.basicstrap')
html_theme = 'basicstrap'
html_logo = "head.png"

html_theme_options = {

    # Set the lang attribute of the html tag. Defaults to 'en'
    'lang': 'en',
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': False,
    # Show header searchbox. Defaults to false. works only "nosidber=True",
    'header_searchbox': True,

    # Put the sidebar on the right side. Defaults to false.
    'rightsidebar': True,
    # Set the width of the sidebar. Defaults to 3
    'sidebar_span': 3,

    # Fix navbar to top of screen. Defaults to true
    'nav_fixed_top': True,
    # Fix the width of the sidebar. Defaults to false
    'nav_fixed': True,
    # Set the width of the sidebar. Defaults to '900px'
    'nav_width': '1200px',
    # Fix the width of the content area. Defaults to false

    'content_fixed': True,
    # Set the width of the content area. Defaults to '900px'
    'content_width': '1200px',
    # Fix the width of the row. Defaults to false
    'row_fixed': True,

    # Disable the responsive design. Defaults to false
    'noresponsive': False,
    # Disable the responsive footer relbar. Defaults to false
    'noresponsiverelbar': False,
    # Disable flat design. Defaults to false.
    # Works only "bootstrap_version = 3"
    'noflatdesign': False,

    # Enable Google Web Font. Defaults to false
    'googlewebfont': False,
    # Set the URL of Google Web Font's CSS.
    # Defaults to 'http://fonts.googleapis.com/css?family=Text+Me+One'
    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Lily+Script+One',  # NOQA
    # Set the Style of Google Web Font's CSS.
    # Defaults to "font-family: 'Text Me One', sans-serif;"
    'googlewebfont_style': u"font-family: 'Lily Script One' cursive;",

    # Set 'navbar-inverse' attribute to header navbar. Defaults to false.
    'header_inverse': False,
    # Set 'navbar-inverse' attribute to relbar navbar. Defaults to false.
    'relbar_inverse': False,

    # Enable inner theme by Bootswatch. Defaults to false
    'inner_theme':False,
    # Set the name of innner theme. Defaults to 'bootswatch-simplex'
    'inner_theme_name': 'bootswatch-simplex',

    # Select Twitter bootstrap version 2 or 3. Defaults to '3'
    'bootstrap_version': '3',

    # Show "theme preview" button in header navbar. Defaults to false.
    #'theme_preview': True,

    # Set the Size of Heading text. Defaults to None
     'h1_size': '1.6em',
     'h2_size': '1.5em',
     'h3_size': '1.4em',
     'h4_size': '1.3em',
     'h5_size': '1.2em',
     'h6_size': '1.1em',
}

#html_theme="asterism_theme"
#html_theme_path = ['themes']

#html_theme="test_theme"
#html_theme_path = ['themes']

html_static_path = ['_static']


htmlhelp_basename = 'asterismdoc'




# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'asterism.tex', u'asterism Documentation',
   u'andrea tramacere', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'asterism', u'asterism Documentation',
     [u'andrea tramacere'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'asterism', u'asterism Documentation',
   u'andrea tramacere', 'asterism', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'asterism'
epub_author = u'andrea tramacere'
epub_publisher = u'andrea tramacere'
epub_copyright = u'2016, andrea tramacere'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'asterism'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.

#------ InterSphinx -------------------------------------------------------------
intersphinx_mapping = {'sklearn': ('http://scikit-learn.org/stable', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy/', None),}

