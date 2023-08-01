import importlib.metadata

project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter.__year }}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"
version = release = importlib.metadata.version("{{ cookiecutter.__project_slug }}")

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "pydata_sphinx_theme",
    "hoverxref.extension",
    "nbsphinx",
]

source_suffix = [".rst", ".md"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

html_theme = "pydata_sphinx_theme"

myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pybamm": ("https://docs.pybamm.org/en/latest/", None),
}

always_document_param_types = True
