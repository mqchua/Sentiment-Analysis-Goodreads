from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required
from project import db
from project.models import Feedback
from project.posts.forms import InputForm


posts = Blueprint('posts', __name__)


@posts.route('/predict', methods=['GET', 'POST'])
@login_required
def home():

    form = InputForm()

    if form.validate_on_submit():
        message = "Positive"
        positive_index = r"99.4%"
        positive_index_float = float(positive_index[:-1])

        review = "From the very beginning Harry Bosch has been one of the most compelling figures ever to inhabit the world of crime fiction and he continues to fill that role twenty-four years down the road from this book. The Black Echo is a great beginning to what has become a fabulous series."
        summary = "The Black Echo is a great beginning to what has become a fabulous series."

        feedback = Feedback(review=review,
                            summary=summary, positivity=positive_index_float)
        db.session.add(feedback)
        db.session.commit()

        flash(f'Review submitted!', 'success')
        return render_template('predict.html', message=message, positive_index=positive_index,
                               text=review, summary=summary, form=form)

    return render_template('home.html', form=form)
