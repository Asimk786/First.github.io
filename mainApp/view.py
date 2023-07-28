from django.shortcuts import render

def homePage(Request):
    return  render(Request,"index.html")

def aboutPage(Request):
    return  render(Request,"about.html")

def profilePage(Request):
    return  render(Request,"profile.html")

def contactPage(Request):
    return  render(Request,"contact.html",{
        "name":"Asim Khan",
        "dsg":"Software Developer" 
    })
