import web, re

urls = (
	"/", "index",
	"/issues", "issues",
)
app = web.application(urls, globals())

root = '/home/patrick/Documents/code/robotics/FIRST-Team-Management-System/' #change when needed
render = web.template.render(root + 'templates/', base='base')
modules = web.template.render(root + 'templates/')

class index:
    def GET(self):
        return render.index(modules)

class issues:
	def GET(self):
		issuesfile = open(root + 'issues', 'r')
		issuelines = issuesfile.readlines()
		issuesfile.close()

		i = 0
		appending = ''
		while i < len(issuelines):
			issuelines[i].replace('\n', '')
			if i % 4 == 0:
				appending += '<tr><td width="600px">' + issuelines[i] + '</td>'
			else:
				appending += '<td>' + issuelines[i] + '</td>'
			i += 1

			if i % 4 == 0:
				appending += '</tr>'
		return render.issues(modules, appending)

	def POST(self):
		issuedata = web.input()
		
		issuesfile = open(root + 'issues', 'r')
		old = issuesfile.read()
		issuesfile.close
		
		issuesfile = open(root + 'issues', 'w')
		issuesfile.write(issuedata['issuetext'] + '\n' + issuedata['issuepriority'] + '\n5/11\nPat')
		if old != "":
			issuesfile.write('\n')
		issuesfile.write(old)
		issuesfile.close()

if __name__ == "__main__":
    app.run()