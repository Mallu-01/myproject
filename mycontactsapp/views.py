from django.http import HttpResponse
from .models import Contact

def index(request):
    # Get all contacts and sort them alphabetically by first name
    contacts = Contact.objects.all().order_by('first_name')

    # Create an HTML list of contacts
    contact_list = "<ul>"
    for contact in contacts:
        contact_list += f"<li>{contact.first_name} {contact.last_name}</li>"
    contact_list += "</ul>"

    # HTML and CSS modifications
    html_content =  f"""
        <html>
        <head>
            <style>
                body {{
                    text-align: center;
                    margin-top: 50px;
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    font-size: 20px;
                    margin-bottom: 15px;
                    background-color: #fff;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }}
                h2 {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h2>All Contacts:</h2>
            {contact_list}
        </body>
        </html>
    """

    return HttpResponse(html_content)

    
