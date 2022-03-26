# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import (
    Blueprint, 
    redirect, 
    render_template, 
    request, 
    flash, 
    url_for, 
    redirect,
    current_app)
from app.db import get_db
import sendgrid
from sendgrid.helpers.mail import *


bp = Blueprint('mail', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    search = request.args.get('search')
    if search is None:
        c.execute("SELECT * FROM email;")
    
    else:
        c.execute("SELECT * FROM email WHERE content LIKE %s", ('%' + search + '%',))
    mails = c.fetchall()
    return render_template('mails/index.html', mails = mails)

@bp.route('/create', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []
        if not email:
            errors.append("Email obligario")
        if not subject:
            errors.append("Asunto obligatorio")
        if not content:
            errors.append("Contenido obligatorio")
        
        if len(errors) == 0:
            send_mail(email, subject, content)
            db, c = get_db()
            c.execute("INSERT INTO email (email, subject, content) VALUES (%s,%s,%s)", (email, subject, content))
            db.commit()
            return redirect(url_for('mail.index'))
        
        else:
            for error in errors:
                flash(error)
        
    return render_template('mails/create.html')

def send_mail(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(to)
    content_e = Content('text/plain',content)
    mail = Mail(from_email, to_email,subject, content_e)
    answer = sg.client.mail.send.post(request_body=mail.get())
    if int(answer.status_code) == 202:
        print("OK")
    else:
        error = "No se pudo enviar el mail"
        flash(error)
        print("Error") 
        return render_template('mails/create.html')   