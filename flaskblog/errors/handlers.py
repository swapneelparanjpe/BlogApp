from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404      # return 404.html and 404 status code

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403      # return 403.html and 403 status code


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500      # return 500.html and 500 status code
