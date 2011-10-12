from web import form

IpDateForm = form.Form(form.Textbox("IP Address:"),
                       form.Textbox("Date:"))

IncidentForm = form.Form(form.Textbox("Network:"),
                         form.Textbox("Media:"),
                         form.Textbox("Comapany:"),
                         form.Textbox("Comapany Email:"),
                         form.Checkbox("Settlement Letter:"),
                         form.Textbox("Date/Time:"),
                         form.Textbox("Incident #:"),
                         form.Textbox("W#:"),
                         form.Textbox("Registration type:", value="wired"),
                         form.Textbox("Room #:"),
                         form.Textbox("Hall Code:"),
                         form.Textarea("Description:"))
