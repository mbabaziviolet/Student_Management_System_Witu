from flask import  jsonify, request, Blueprint
from validate_email import validate_email
# from flask_jwt_extended import jwt_required,get_jwt_identity
from werkzeug.security import check_password_hash,generate_password_hash
from backend import db
from backend.models.tutor import Tutor

tutors = Blueprint('tutors', __name__,url_prefix="/tutors")



#retrieving all tutors 
@tutors.route("/", methods=['GET'])
def all_tutors():
    #ensuring that a tutor has logged in
    all_tutors = Tutor.query.all()
    return jsonify(all_tutors),200


#retrieving all tutors for a tutor
@tutors.route("/tutors/<int:tutor_id>", methods=['GET'])
# @jwt_required()
def all_tutor_tutors(tutor_id):
    #ensuring that a tutor has logged in
    # tutor_id= get_jwt_identity()
    all_tutors = Tutor.query.filter_by(id=tutor_id).all()
    return jsonify(all_tutors),200


#retrieving single tutors 
@tutors.route("/<int:tutor_id>", methods=['GET'])
def single_tutor(tutor_id):
    single_tutor = Tutor.query.filter_by(id=tutor_id).first()
    
    #Tutor does'nt exist
    if not single_tutor:
        return jsonify({'message': '  Tutor not found'}), 404
    return jsonify(single_tutor),200


#retrieving single tutors  for a tutor
@tutors.route("/<string:tutor_id>", methods=['GET'])
# @jwt_required()
def single_tutor_tutor(tutor_id):
    # current_tutor = get_jwt_identity()
    single_tutor = Tutor.query.filter_by(id=tutor_id).first()
    
    #if a tutor doesnt exist
    if not single_tutor:
        return jsonify({'message': '  Tutor not found'}), 404
    return jsonify(single_tutor),200 


#creating tutors
@tutors.route("/register", methods=['POST','GET'])
def register_tutors():
#def new_tutors():
    
    if request.method == "POST":
      name = request.json['name']
      email = request.json['email']
      contact = request.json['contact']
      password = request.json['password']

      #validations
      if not contact:
              return jsonify({'error':"Contact is required"})
      
      if not name:
              return jsonify({'error':" Name is required"})
      

      if len(password) < 6:
            return jsonify({'error': "Password is too short"}), 400

      if not validate_email(email):
        return jsonify({'error': "Invalid email address"}), 400

      if Tutor.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is already in use"}), 409

    
      if Tutor.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': "Phone number is already in use"}),409
       

      #creating a hashed password in the database
      hashed_password = generate_password_hash(password,method="sha256")
      new_tutor = Tutor(name=name,email=email,contact=contact,password=hashed_password) 
      
      #inserting values
      db.session.add(new_tutor)
      db.session.commit()
      return jsonify({'message':'New tutor created','id':new_tutor.id,'name':name,'email':email,'contact':contact,'password':password}),200
    return jsonify({'error':'Failed to register'}),400
  





# #tutors login endpoint
@tutors.route('/login', methods= ['POST'])

def login_tutor():
        
   
         if request.method == 'POST':
           email = request.json["email"]
           password = request.json['password']
        
          #empty fields
      
           if not email:
                 
                return jsonify({'error': 'Please provide your email '}), 400
          
           if not password:
                return jsonify({'error': 'Please provide your password '}), 400
          
          #check if email exits
           tutor = Tutor.query.filter_by(email=email).first()
           if tutor:
            is_pass_correct = check_password_hash(tutor.password, password)

            if is_pass_correct:
              # login_tutor(tutor)


              return jsonify({
                'tutor': {
                    
                    'message':'You successfully logged into your account',
                    'name': tutor.name,
                     'contact': tutor.contact,
                    'email': tutor.email
                 }

                }), 200
            else:
                return jsonify({'error':'Wrong password please try again'})  
 
                
           return jsonify({'error': 'Wrong email address please try again'}), 401

      
          

#update tutors endpoint
@tutors.route('/update/<int:tutor_id>', methods= ['PUT','GET'])
def update_tutors(tutor_id):
  
  if request.method == "PUT":
      tutor = Tutor.query.filter_by(id=tutor_id).first()
        
      tutor.name = request.json['name']
      tutor.email = request.json['email']
      tutor.contact = request.json['contact']
      tutor.password = request.json['password']

      #creating a hashed password in the database
      hashed_password = generate_password_hash(tutor.password,method="sha256")
      edit_tutor = Tutor(name=tutor.name,email=tutor.email,contact=tutor.contact,password=hashed_password) 
      
      #saving updates
      db.session.commit()
      return jsonify({'message':'Tutor updated successfully','id':tutor.id,'name':tutor.name,'email':tutor.email,'contact':tutor.contact,'password':tutor.password}),200
  return jsonify({'error':'Failed to updated'}),400
  

#deleting a tutor by an id
@tutors.route("/<int:tutor_id>", methods=['DELETE'])
def deleted_tutor(tutor_id):
    #ensuring that a tutor has logged in
    tutor = Tutor.query.filter_by(id=tutor_id).first()
    db.session.delete(tutor)
    db.session.commit()
    return jsonify({"message":"Tutor deleted successfully"}),200







       


 

    


