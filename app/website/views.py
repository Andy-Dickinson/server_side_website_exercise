# blueprint of website (contains routes - URLs)
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user # anything on current user can be accessed via current_user
from .models import Note
from . import db
import json

# set up a blueprint for our application
views = Blueprint('views', __name__)


# defines routes for views

# home page route (using blueprint 'views')
@views.route('/', methods=['GET', 'POST']) # argument here must match URL that is called (unless prefixed when blueprint registered), argument 'methods=[]' defines what type of requests that route can accept - default > can only accept 'GET' requests
@login_required # this means home page cannot be accessed unless logged in
def home():

    # adds new note to database
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')


    return render_template("home.html", user=current_user) # 1st argument here must match filename of html file in 'templates' directory, sub-directories should be prepended either here or when blueprint registered
    # following arguments can be variables which can be accessed from within the templates using Jinja {{ var ... restricted Python code }}
    # user=current_user parameter allows us to reference current_user and check they are authenticated

# delete_note() only POST's, does not accept 'GET' requests
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # takes request data containing stringified noteId from deleteNote() in index.js, turns it into Python dictionary obj
    noteId = note['noteId'] # accesses noteId field
    note = Note.query.get(noteId) # find note in db

    if note:
        # validation
        if note.user_id == current_user.id:
            # deletes note
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})