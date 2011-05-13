import web

urls = (
	"/", "index",
	"/issues", "issues"
)
app = web.application(urls, globals())
render = web.template.render('/home/patrick/Documents/code/robotics/issuetracker/templates/', base='base')
module = web.template.render('/home/patrick/Documents/code/robotics/issuetracker/templates/')

class issues:
    def GET(self):
        return render.issues(module.sideuser())

class index:
    def GET(self):
        return render.index(module.sideuser())

if __name__ == "__main__":
    app.run()