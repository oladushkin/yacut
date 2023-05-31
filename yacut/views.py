import random
import string

from flask import render_template, flash, redirect
from .forms import URLMapForm
from .models import URLMap

from . import app, db


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    new_url = ''.join(random.sample(letters_and_digits, 6))
    if URLMap.query.filter_by(short=new_url).first() is None:
        return new_url
    get_unique_short_id()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()
    if form.validate_on_submit():
        short_name = form.custom_id.data
        if short_name == '' or short_name is None:
            new_url = get_unique_short_id()
            url = URLMap(
                original=form.original_link.data,
                short=new_url
            )
        else:
            if URLMap.query.filter_by(short=short_name).first():
                flash(f'Имя {short_name} уже занято!')
                return render_template('сreation_url.html', form=form)
            if ' ' in short_name:
                flash('Пробелы запрещены в URL.')
                return render_template('сreation_url.html', form=form)
            url = URLMap(
                original=form.original_link.data,
                short=short_name
            )
        db.session.add(url)
        db.session.commit()
        context = {'form': form, 'url': url}
        return render_template('сreation_url.html', **context)
    return render_template('сreation_url.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def forwarding(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        return render_template('404.html'), 404
    return redirect(url.original)
