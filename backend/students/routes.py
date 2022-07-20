from flask import  jsonify, request, Blueprint
# from flask_jwt_extended import jwt_required,get_jwt_identity
from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend import db
from backend.models.students import Student

students = Blueprint('students', __name__,url_prefix="/students")



#retrieving all students 
@students.route("/", methods=['GET'])
def all_students():
    #ensuring that a user has logged in
    all_students = Student.query.all()
    return jsonify(all_students),200


#retrieving all students for a user
@students.route("/students/<int:student_id>", methods=['GET'])
# @jwt_required()
def all_user_students(student_id):
    #ensuring that a user has logged in
    # user_id= get_jwt_identity()
    all_students = Student.query.filter_by(id=student_id).all()
    return jsonify(all_students),200


#retrieving single student
@students.route("/<int:student_id>", methods=['GET'])
def single_student(student_id):
    single_student = Student.query.filter_by(id=student_id).first()
    
    #Student that does'nt exist
    if not single_student:
        return jsonify({'message': '  Student not found'}), 404
    return jsonify(single_student),200


#creating students
@students.route("/register", methods=['POST','GET'])
# @jwt_required()
# def new_students():
def register_students():
    
    if request.method == "POST":
        
        # user_id = get_jwt_identity()
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        # user_name = request.json['user_name']
        gender = request.json['gender']
        address = request.json['address']
        age = request.json['age']
        email = request.json['email']
        password = request.json['password']
        guardian_name = request.json['guardian_name']
        guardian_contact = request.json['guardian_contact']
        is_admitted = request.json['is_admitted']
        image = request.json['image']
       
     


       #empty fields
      
        if not first_name:
                 
          return jsonify({'error': 'Please provide your firstname'}), 400 #bad request
        if not last_name:
                 
          return jsonify({'error': 'Please provide your lastname'}), 400 #bad request
        # if not user_name:
                 
        #   return jsonify({'error': 'Please provide your username'}), 400 #bad request
        if not email:
                 
          return jsonify({'error': 'Please provide your email'}), 400 #bad request
        if not password:
                 
          return jsonify({'error': 'Please provide your password'}), 400 #bad request
          
        if not gender:
                return jsonify({'error': 'Please provide your gender'}), 400
        
        if not address:
                return jsonify({'error': 'Please provide your address'}), 400
            
        if not age:
                return jsonify({'error': 'Please provide your age'}), 400
            
        if not guardian_name:
                return jsonify({'error': 'Please provide your guardian name'}), 400
            
        if not guardian_contact:
                return jsonify({'error': 'Please provide your guardian contact'}), 400
        
        # if not image:
        #         return jsonify({'error': 'Please provide your image'}), 400
            
              
        if not validate_email(email):
            return jsonify({'error': "Invalid email address"}), 400

        if Student.query.filter_by(email=email).first() is not None:
         return jsonify({'error': "Email is already in use"}), 409 #conflicts

    
        if Student.query.filter_by(guardian_contact=guardian_contact).first() is not None:
         return jsonify({'error': "Phone number is already in use"}),409
    
        
        # #checking if username exists
        # if Student.query.filter_by(user_name=user_name).first():
        #         return jsonify({
        #         'error': 'Username already exists'
        #     }), 409
        
           

        #inserting values into the students_list
         #creating a hashed password in the database
        hashed_password = generate_password_hash(password,method="sha256")
      
        new_student= Student(email=email,password=password,first_name=first_name,last_name=last_name,guardian_name=guardian_name,guardian_contact=guardian_contact,age=age,gender=gender,image=image,is_admitted=is_admitted)
        db.session.add(new_student)
        db.session.commit()
        
         
  
    return jsonify({'message':'new student created','email':email,'password':password,'first_name':first_name,'last_name':last_name,'guardian_name':guardian_name,'guardian_contact':guardian_contact,'age':age,'gender':gender,'image':image,'is_admitted':is_admitted}),200
    

# #login endpoint
@students.route('/login', methods= ['POST'])

def login_student():
        
   
         if request.method == 'POST':
           email = request.json["email"]
           password = request.json['password']
        
          #empty fields
      
           if not email:
                 
                return jsonify({'error': 'Please provide your email '}), 400
          
           if not password:
                return jsonify({'error': 'Please provide your password '}), 400
          
          #check if email exits
           student = Student.query.filter_by(email=email).first()
           if student:
            is_pass_correct = check_password_hash(student.password, password)

            if is_pass_correct:
              # login_student(student)


              return jsonify({
                'student': {
                    
                    'message':'You successfully logged into your account',
                    'first_name': student.first_name,
                     'last_name': student.last_name,
                    'email': student.email
                 }

                }), 200
            else:
                return jsonify({'error':'Wrong password please try again'})  
 
                
           return jsonify({'error': 'Wrong email address please try again'}), 401

      

#update students endpoint ie admin and staff
@students.route('/update/<int:student_id>', methods= ['PUT','GET'])
def update_students(student_id):
  
  if request.method == "PUT":
      student = Student.query.filter_by(id=student_id).first()
        
      student.first_name = request.json['first_name']
      student.last_name = request.json['last_name']
      student.email = request.json['email']
    #   student.user_name = request.json['user_name']
      student.password = request.json['password']
      student.guardian_name = request.json['guardian_name']
      student.guardian_contact = request.json['guardian_contact']
      student.is_admitted = request.json['is_admitted']
      student.image = request.json['image']

      #creating a hashed password in the database
      hashed_password = generate_password_hash(student.password,method="sha256")
      edit_student = student(first_name=student.first_name,last_name=student.last_name,email=student.email,guardian_contact=student.guardian_contact,guardian_name=student.guardian_name,is_admitted=student.is_admitted,image=student.image,password=hashed_password) 
      
      #saving updates
      db.session.commit()
      return jsonify({'message':'student updated successfully','id':student.id,'first_name':student.first_name,'last_name':student.last_name,'email':student.email,'guardian_contact':student.guardian_contact,'guardian_name':student.guardian_name,'password':student.password,'is_admitted':student.is_admitted,'image':student.image}),200
  return jsonify({'error':'Failed to updated'}),400
  

#deleting a student by an id
@students.route("/<int:student_id>", methods=['DELETE'])
def deleted_user(student_id):
    #ensuring that a user has logged in
    student = Student.query.filter_by(id=student_id).first()
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message":"Student deleted successfully"}),200

    