import re
from flask import  jsonify, request, Blueprint
from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend.models.user import User
from backend.db import db
from flask_login import (login_user,current_user,logout_user,login_required,)
from backend import login_manager

users = Blueprint('users', __name__, url_prefix='/users')

#user loader,This keeps the current user object loaded in that current session based on the stored id.
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



#register users endpoint ie admin and staff
@users.route('/register', methods= ['POST','GET'])
def register_users():
  
  if request.method == "POST":
        
      first_name = request.json['first_name']
      last_name = request.json['last_name']
      email = request.json['email']
      contact = request.json['contact']
      password = request.json['password']

      #username
      user_name = last_name.upper() + " " + first_name.upper()

  
      #validations
      if not contact:
              return jsonify({'error':"Contact is required"})
      
      if not first_name:
              return jsonify({'error':"First name is required"})
      
      if not last_name:
              return jsonify({'error':"Last name is required"})

      if len(password) < 6:
            return jsonify({'error': "Password is too short"}), 400

      if not validate_email(email):
        return jsonify({'error': "Invalid email address"}), 400

      if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is already in use"}), 409

    
      if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': "Phone number is already in use"}),409
       

      #creating a hashed password in the database
      hashed_password = generate_password_hash(password,method="sha256")
      new_user = User(first_name=first_name,last_name=last_name,email=email,contact=contact,password=hashed_password) 
      
      #inserting values
      db.session.add(new_user)
      db.session.commit()
      return jsonify({'message':'New user created','id':new_user.id,'first_name':first_name,'last_name':last_name,'email':email,'contact':contact,'user_name':user_name,'password':password}),200
  return jsonify({'error':'Failed to register'}),400
  


# #login endpoint
@users.route('/login', methods= ['POST'])

def login_user():
        
   
         if request.method == 'POST':
           email = request.json["email"]
           password = request.json['password']
        
          #empty fields
      
           if not email:
                 
                return jsonify({'error': 'Please provide your email '}), 400
          
           if not password:
                return jsonify({'error': 'Please provide your password '}), 400
          
          #check if email exits
           user = User.query.filter_by(email=email).first()
           if user:
            is_pass_correct = check_password_hash(user.password, password)

            if is_pass_correct:
              # login_user(user)

               #username
              user_name = user.first_name.upper() + " " + user.last_name.upper()


              return jsonify({
                'user': {
                    
                    'message':'You successfully logged into your account',
                    'first_name': user.first_name,
                     'last_name': user.last_name,
                     'user_name':user_name,
                    'email': user.email
                 }

                }), 200
            else:
                return jsonify({'error':'Wrong password please try again'})  
 
                
           return jsonify({'error': 'Wrong email address please try again'}), 401

      
          
        

# #retrieving all users
@users.route("/")
def all_users():
    users= User.query.all()
    return jsonify({"users":users}),200


#retrieving users by an id
@users.route("/<int:user_id>", methods=['GET'])
def user_id(user_id):
    #ensuring that a user has logged in
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user),200



#update users endpoint ie admin and staff
@users.route('/update/<int:user_id>', methods= ['PUT','GET'])
def update_users(user_id):
  
  if request.method == "PUT":
      user = User.query.filter_by(id=user_id).first()
        
      user.first_name = request.json['first_name']
      user.last_name = request.json['last_name']
      user.email = request.json['email']
      user.contact = request.json['contact']
      user.password = request.json['password']

      #username
      user_name = user.last_name.upper() + " " + user.first_name.upper()

      #creating a hashed password in the database
      hashed_password = generate_password_hash(user.password,method="sha256")
      edit_user = User(first_name=user.first_name,last_name=user.last_name,email=user.email,contact=user.contact,password=hashed_password) 
      
      #saving updates
      db.session.commit()
      return jsonify({'message':'User updated successfully','id':user.id,'first_name':user.first_name,'last_name':user.last_name,'email':user.email,'contact':user.contact,'user_name':user_name,'password':user.password}),200
  return jsonify({'error':'Failed to updated'}),400
  

#deleting a user by an id
@users.route("/<int:user_id>", methods=['DELETE'])
def deleted_user(user_id):
    #ensuring that a user has logged in
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"User deleted successfully"}),200


