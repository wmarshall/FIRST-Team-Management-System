import web, time

urls = (
    "/", "index",
    "/issues", "issues",
    "/getcomments", "getcomments"
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
        starttime = time.time()
        issuesfile = open(root + 'issues', 'r')
        issuelines = issuesfile.readlines()
        issuesfile.close()

        i = 0
        appending = ''
        subissues = {'programming': '', 'endeffector': '', 'electrical': '', 'drivetrain': '', 'cad': ''}
        
        while i < len(issuelines):
            issuelines[i] = issuelines[i].replace('\n', '')
            if i % 5 == 0:
                subteam = issuelines[i]
                i += 1
                issuelines[i] = issuelines[i].replace('\n', '')
                appending += '<tr class="issue" id="' + str(int(i/4)+1) + '"><td width="600px">' + issuelines[i] + '</td>'
            else:
                appending += '<td width="100px">' + issuelines[i] + '</td>'
            i += 1

            if i % 5 == 0:
                appending += '</tr><tr style="display:none" class="issuedetail" id="comments' + str(int(i/4)) + '"><td width="600px"></td></tr>'
                subissues[subteam] += appending
                appending = ''
        print 'return time: ' + str(time.time() - starttime) + '\n'
        return render.issues(modules, subissues)

    def POST(self):
        issuedata = web.input()
        
        issuesfile = open(root + 'issues', 'r')
        old = issuesfile.read()
        oldlinenum = len(issuesfile.readlines())
        issuesfile.close()
        
        issuesfile = open(root + 'issues', 'w')
        issuedata['issuetext'] = issuedata['issuetext'].replace('\n', '<br />')
        issuesfile.write(issuedata['issuesubteam'] + '\n' + issuedata['issuetext'] + '\n' + issuedata['issuepriority'] + '\n5/11\nPat')
        if old != "":
            issuesfile.write('\n')
        issuesfile.write(old)
        issuesfile.close()
        return str(oldlinenum+1)

class getcomments:
    def POST(self):
		try:
			commentfile = open(root + 'comments/comment' + web.input()['id'])
			commentlines = commentfile.readlines()
			commenthtml = ''
			for i in range(0, len(commentlines), 2):
				commenthtml += '<div class="commenttext">' + commentlines[i] + '</div><div class="commentuser">-' + commentlines[i+1] + '</div>'
		except:
			commenthtml = ''
		return modules.issueviewer(commenthtml)

if __name__ == "__main__":
    app.run()