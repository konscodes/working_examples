from flask import Flask

def say_hello(username="World"):
    return f"Hello {username}!" 


# Some bits of text for the page
header_text = '''
    <html><head><title>EB Flask Test</title></head><body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! 
    Append a username to the URL (for example: <code>/example</code>) 
    to say hello to someone specific.</p>'''
home_link = '<p><a href="/">Back</a></p>'
footer_text = '</body></html>'

# EB looks for an 'application' callable by default
application = Flask(__name__)

# Add a rule for the index page
application.add_url_rule('/', 'index', (lambda: 
    header_text + say_hello() + instructions + footer_text))

# Add a rule when the page is accessed with a name appended to the site URL
application.add_url_rule('/<username>', 'hello', (lambda username: 
    header_text + say_hello(username) + home_link + footer_text))

# Run the app
if __name__ == "__main__":
    # Setting debug to True enables debug output
    # This line should be removed before deploying a production app
    application.debug = True
    application.run()