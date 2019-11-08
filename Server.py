# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:15:39 2019

@author: Kuro Azai
"""

#imports
import markdown
import shelve 
from flask import Flask, g
from flask_restful import Resource, Api, reqparse


#Flask App
app =  Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("trackers.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
@app.route("/")
def index():
    #Open readme 
    with open('README.MD', 'r') as markdown_file:
        
        #read
        content = markdown_file.read()
        
        #
        return markdown.markdown(content)
    
class Get_Trackers(Resource):
    #Get All trackers on the server 
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        trackers = []
        
        for key in keys:
            trackers.append(shelf[key])
            
        return {'message':'Completed','data':trackers}
    
    #Requires security 
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('Device_ID', required=True)
        parser.add_argument('GPS_Coords', required=True)
        parser.add_argument('Motion', required=True)
        parser.add_argument('Battery_Life', required=True)
        parser.add_argument('Mode', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['Device_ID']] = args

        return {'message': 'Device registered', 'data': args}, 201
    
class Get_Tracker(Resource):
    #Get individual Device
    def get(self, Device_ID):
        shelf = get_db()
        
        if not (Device_ID in shelf):
            return {'message':'Device not found', 'Data':{}}, 404
        
        return {'message': 'Device found', 'data': shelf[Device_ID]}, 200
        return '', 204
    
    #Update Current Coordinates
    def post (self, Device_ID):
        parser = reqparse.RequestParser()
        
        parser.add_argument('GPS_Coords', required=True)
         # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['Device_ID']] = args

        return {'message': 'Coordinates Updated', 'data': args}, 201
    #Delete Device from server 
    def delete(self, Device_ID):
        shelf = get_db()

        if not (Device_ID in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        del shelf[Device_ID]
        return '', 204
    
class Folium_Updater(Resource):
    def get(self):
        pass

    
    
    
api.add_resource(Get_Trackers, '/devices/Locate_All')
api.add_resource(Get_Tracker, '/device/<string:Device_ID>')
