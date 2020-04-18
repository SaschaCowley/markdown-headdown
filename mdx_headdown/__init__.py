"""
Downgrade headings.

Supports a single optional argument, `offset`, which sets the number of 
heading levels to offset by. This will automatically be absolutised and 
integerised.

(c) 2018-2020, Sascha Cowley and contributors under the MIT Licence.
"""

# Import relevant modules.
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from xml.etree import ElementTree as ET
import re

name = "mdx_headdown"

class DowngradeHeadingsPostprocessor(Postprocessor):
    """ Downgrade headings via the Preprocessor interface. """
    def run(self, text):
        # Ensure the offset value is a positive (or zero) integer.
        self.offset = abs(int(self.config['offset']))

        # Match headings 1-6 case insensitively, and capture the heading number.
        heading_pattern = re.compile(r'<h([1-6])[^>]*>([^<]*)</h\1>', re.I)

        return re.sub(heading_pattern, self.downgrade, text)

    def downgrade(self, match):
        element = ET.fromstring(match.group(0))

        # Only process this heading if 'headdown="1"' (or missing...)
        if element.attrib.get('headdown', 1) == 1:
            # For all headings, increase their heading number by `offset`.
            # If the new heading number is > 6, use 6 instead.
            element.tag = 'h%d' % min(6, int(match.group(1))+self.offset)

        return ET.tostring(element, encoding="unicode")

class DowngradeHeadingsExtension(Extension):
    """ Setup the extension for usage. """
    def __init__(self, **kwargs):
        # Default configuration.
        self.config = {
            'offset': [1, 'Number of heading levels to offset by.'],
        }
        # Initialise superclass, allowing configuration to be overridden.
        super(DowngradeHeadingsExtension, self).__init__(**kwargs)
    
    def extendMarkdown(self, md):
        # Register the plugin as a Postprocessor. """
        md.postprocessors.register(
            DowngradeHeadingsPostprocessor(md),
            'downgradeheadings', 5
        )
        # And give the actual processor access to the configuration.
        DowngradeHeadingsPostprocessor.config = self.getConfigs()


def makeExtension(*args, **kwargs):
    # Tell Markdown to make this an extension.
    return DowngradeHeadingsExtension(*args, **kwargs)
