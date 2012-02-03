# DAS BLOG CONFIGURATION
import os.path

# Protocol used to access the blog
PROTOCOL	= "http"

# Full path to upload directory
UPLOAD_TO 	= os.path.join(os.path.dirname(__file__,"public/media/post-uploads")

# Tags to be stripped
HTML_TAGS = "html body div span applet object iframe h1 h2 h3 h4 h5 h6 p blockquote pre a abbr acronym address big cite code del dfn em img ins kbd q s samp small strike strong sub sup tt var b u i center dl dt dd ol ul li fieldset form label legend table caption tbody tfoot thead tr th td article aside canvas details embed figure figcaption footer header hgroup menu nav output ruby section summary time mark audio video font br"

# Import XML-RPC metaWeblog API settings
import xmlrpc