#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    filename_list = {}
    os.chdir('/Users/zhouhuan/Desktop/files')
    for filename in os.listdir():
        with open(filename) as f:
            filename_list[filename[:-5]] = json.load(f)

    title_list = [item['title'] for item in filename_list.values()]
    return render_template('index.html', title_list=title_list)


@app.route('/files/<filename>')
def file(filename):
    filename_list = {}
    os.chdir('/Users/zhouhuan/Desktop/files')
    for filename in os.listdir():
        with open(filename) as f:
            file_item = filename_list[filename[:-5]] = json.load(f)
    if not file_item:
        abort(404)
    return render_template('file.html', file_item=file_item)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
