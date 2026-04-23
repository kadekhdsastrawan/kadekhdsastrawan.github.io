AUTHOR = 'Kadek Hendra Darma Sastrawan'
SITENAME = 'Hendra Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10
THEME = 'themes/Flex'

SITETITLE = 'Kadek Hendra'
SITESUBTITLE = 'Senior Data Analyst | Marketing Analytics'

# Social links (These show up as icons in Flex)
SOCIAL = (
    ('github', 'https://github.com/kadekhdsastrawan'),
    ('linkedin', 'https://www.linkedin.com/in/hendra16'),
)

# Sidebar links
LINKS = (
    ('Projects', '/category/projects.html'),
    ('About', '/pages/about.html'),
)

COPYRIGHT_NAME = 'Kadek Sastrawan'
COPYRIGHT_YEAR = 2026

FOOTER_SKIP_PELICAN = True

PYGMENTS_STYLE = 'monokai' # Style for code highlighting

BROWSER_COLOR = '#334155' # This sets the browser's theme color, which can affect how the site looks on mobile devices and in some browsers. Adjust as needed for your design.

STATIC_PATHS = ['images', 'css'] # This tells Pelican to look for static files (like images and CSS) in these directories. Make sure you have these directories in your content folder and that they contain the appropriate files.
# Tell Flex to use this specific CSS file
CUSTOM_CSS = 'css/custom.css'

# This ensures the file is copied to output/css/custom.css
EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'css/custom.css'},
}