# this file has the main server handling calls to the LLM service and feature extracting service.

""" two services with this module
1. LLM service
    a. has a prompt engineer module
    b. has a seperate queue handling
2. Feature Extractor Service
    a. does not have prompt engineering, just generate embedding
    b. store embedding into vector database.
    c. has a seperate queue handling

    all 
"""
import json
from flask import Flask, request, jsonify, render_template, make_response
from airesumeeditor.service_helper import generate_resume_pdf
from airesumeeditor.resume_processor import ResumeProcessor

app = Flask(__name__)

# Store data in memory (temporary - better to use a database for persistence)
cv_data = {}
job_descriptions = {}
resume = ResumeProcessor()

@app.route('/upload_cv', methods=['POST'])
def upload_cv():
    try:
        data = request.get_json()
        # TODO: get users cv for seperating
        # cv_id = data.get('id')  # Get an ID for the CV if provided
        # if not cv_id:
        #     return jsonify({'error': 'CV ID is required'}), 400
        cv_data = data.get("cv", None)
        if cv_data:
            resume.cv(cv_data)
        else:
            return jsonify({'error': 'Expected there to be cv'})
        return jsonify({'message': 'CV uploaded successfully'})
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON data'}), 400

@app.route('/upload_jd', methods=['POST'])
def upload_job_description():
    try:
        data = request.get_json()
        # data = json.loads(data)
        # job_id = request.args.get('id')
        # if not job_id:
        #     return jsonify({'error': 'Job ID is required'}), 400
        job_descriptions = data.get('jd', None)
        resume.jd(job_descriptions)
        return jsonify({'message': 'Job description uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_resume', methods=['GET'])
def generate_resume(cv_id):
    if cv_id not in cv_data:
        return jsonify({'error': 'CV not found'}), 404

    try:
        pdf = generate_resume_pdf(resume)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename=resume_{cv_id}.pdf'
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=9002)