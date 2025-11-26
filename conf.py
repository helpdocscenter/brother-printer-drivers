# Configuration file for the Sphinx documentation builder.

import os
import sys

project = 'Brother Printer Drivers'
copyright = '2025, Brother'
author = 'Brother Support Team'
release = '1.0.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Disable sidebar for clean full-width layout
html_sidebars = {
    '**': []
}

# HTML output setup
html_theme = 'alabaster'  # simple clean theme
html_title = "Brother Printer Drivers – Official Setup Guide"
html_short_title = "Brother Drivers Guide"
html_favicon = 'favicon.ico'
html_show_sourcelink = False
html_allow_unsafe = True

# Force homepage to use custom HTML layout
html_additional_pages = {
    'index': 'custom_layout.html'
}

html_theme_options = {
    'show_powered_by': False,
}
