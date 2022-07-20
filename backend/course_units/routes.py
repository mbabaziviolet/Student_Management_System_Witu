from flask import  jsonify, request, Blueprint
from backend import db
from backend.models.course_unit import CourseUnit


course_units = Blueprint('course_units', __name__,url_prefix="/course_units")



#retrieving all course_units 
@course_units.route("/", methods=['GET'])
def all_course_units():
    #ensuring that a user has logged in
    all_course_units = CourseUnit.query.all()
    return jsonify(all_course_units),200



#retrieving a single course_unit
@course_units.route("/<int:course_unit_id>", methods=['GET'])
def single_course_unit(course_unit_id):
    course_unit = CourseUnit.query.filter_by(id=course_unit_id).first()
    
    #Program that does'nt exist
    if not course_unit:
        return jsonify({'message': '  Course Unit not found'}), 404
    return jsonify(course_unit),200


#creating course_units
@course_units.route("/", methods=["POST"])
def new_course_units():
    
    if request.method == "POST":
        
        title = request.json['title']
        description = request.json['description']
        file = request.json['file']
    
    
        

       #empty fields for validations
      
        if not title:
                 
          return jsonify({'error': 'Course unit title is required'}), 400 #bad request
          
        if not description:
            return jsonify({'error': 'Description is required'}), 400

        if not file:
            return jsonify({'error': 'File is required'}), 400    
       
        
        
        #checking if name exists
        if CourseUnit.query.filter_by(title=title).first():
                return jsonify({
                'error': 'Course unit title already exists'
            }), 409 #conflicts
      
           
        #For valid data
        #inserting values into the course_units_list
        new_course_unit = CourseUnit(title=title,description=description,file=file)
        db.session.add(new_course_unit)
        db.session.commit()
        
         
  
    return jsonify({'message':'Added a new course_unit','file':file,'title':title,'description':description}),200
    



#update course_units endpoint ie admin and staff
@course_units.route('/update/<int:course_unit_id>', methods= ['PUT','GET'])
def update_course_units(course_unit_id):
  
  if request.method == "PUT":
      course_unit = CourseUnit.query.filter_by(id=course_unit_id).first()
        
      course_unit.title = request.json['title']
      course_unit.description = request.json['description']
      course_unit.file = request.json['file']

      

      edit_course_unit = CourseUnit(title=course_unit.title,description=course_unit.description,file=course_unit.file.contact) 
      
      #saving updates
      db.session.commit()
      return jsonify({'message':'course_unit updated successfully','title':course_unit.title,'file':course_unit.file,'description':course_unit.description}),200
  return jsonify({'error':'Failed to updated'}),400
  






#deleting a course_unit by an id
@course_units.route("/<int:course_unit_id>", methods=['DELETE'])
def deleted_course_unit(course_unit_id):
    #ensuring that a user has logged in
    course_unit = CourseUnit.query.filter_by(id=course_unit_id).first()
    db.session.delete(course_unit)
    db.session.commit()
    return jsonify({"message":"Course unit deleted successfully"}),200
 

