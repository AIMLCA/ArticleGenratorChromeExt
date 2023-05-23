from flask import Flask, render_template, request, jsonify, redirect, Response
import pandas as pd
from sqlalchemy import create_engine
import openai
# from flask_mysqldb import MySQL
import mysql.connector
from flask_cors import CORS
import json

app = Flask(__name__)

openai.api_key = "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"
@app.route("/")
def dashboard():
    return render_template("dashbaord.html")

@app.route("/anser",methods=['POST'])
def answer():
    subject = request.form.get('subject')
    topic = request.form.get('topic')
    where = request.form.get('where')
    who = request.form.get('who')
    when = request.form.get('when')
    how = request.form.get('how')
    why = request.form.get('why')
    noofword = request.form.get('noofword')
    keyword = request.form.get('keyword')

    pmt="As a Article Writting Experts Provde me some articles where Article Subject is :- "+subject+" Topic is:- "+ topic+" Country is:- "+ where+", and time is: - "+when+", For the Person "+who+"and how to write"+how
    model_name = 'text-davinci-003'  # or use 'text-davinci-003' for the older version
    response = openai.Completion.create(
        engine=model_name,
        prompt="Provde me some articles where Article Subject is :- ",
        max_tokens=1000,
        temperature=0.5,
        n=1,
        stop=None,
      
    )
    reply = response.choices[0].text.strip()
    return reply

app.run(debug=True)