import webapp2
import jinja2

import os


#============jinja2 templating environment============
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
#================================
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


class MainHandler(webapp2.RequestHandler):
	def render(self, template, **kw):
		self.response.out.write(render_str(template, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

class MainPage(MainHandler):
	def get(self):
		self.render('index.html')
		


app = webapp2.WSGIApplication([ ('/', MainPage), 
								], debug=True)