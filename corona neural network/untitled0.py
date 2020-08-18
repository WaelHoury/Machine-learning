# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:08:19 2020

@author: waelh
"""

@app.route('/uploader', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':

        f = request.files['image']
        f.save(os.path.join(app.config["IMAGE_UPLOADS"]))
        return render_template('text.html')
    else:
        return render_template('text.html')