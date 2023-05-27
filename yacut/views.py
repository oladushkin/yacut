import random
import string
from . import app, db
from models import URLMap
from forms import URLMapForm
from flask import redirect, render_template, url_for


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    new_url = ''.join(random.sample(letters_and_digits, 6))
    if URLMap.query.get(short=new_url) is None:
        return new_url
    get_unique_short_id()


@app.route('/', methods=['POST'])
def index():
    form = URLMapForm()
    if form.validate_on_submit():
        if form.custom_id.data is None:
            url = URLMap(
                original=form.original_link.data,
                short=get_unique_short_id()
            )
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('opinion_view', id=url.id))
    return render_template('add_opinion.html', form=form)


@app.route('/<int:id>')
def opinion_view(id):
    url = URLMap.query.get_or_404(id)
    return render_template('opinion.html', url=url)
