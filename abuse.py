import web

from forms import IpDateForm, IncidentForm

render = web.template.render('templates/', base='base')

urls = ('/', 'index')
app = web.application(urls, globals())

class index: 
    def GET(self): 
        form = IpDateForm()
        return render.index(form)

    def POST(self): 
        data = IpDateForm()
        if not data.validates():
            return render.index(data)
        elif data['IP Address:'].value == '0.0.0.0':
            form = IncidentForm()
            return render.incident(form, data)
        data['IP Address:'].value = 'No'
        data['Date:'].value = 'Match'
        return render.index(data)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
