#!/usr/bin/python3
# coding:utf-8

from flask import request, flash, Blueprint
from flask_restplus import Api
from werkzeug.utils import secure_filename
import os

api = Blueprint('api', __name__, url_prefix='/api')
api_rest = Api(api)


UPLOAD_FOLDER = '/Users/dongjianqiang/Pictures/py_test/'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return 'success'
        else:
            return 'only image'


@api.route('/batch_upload_file', methods=['POST'])
def batch_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No file part'
        file_list = request.files.getlist('file')
        print(file_list)
        # print(request.form)
        for file in file_list:
            print(file.filename)
            # if user does not select file, browser also
            # submit an empty part without filename
            # if file.filename == '':
            #     flash('No selected file')
            #     return 'No selected file'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                return '只能传图片类型'
        return 'success'
