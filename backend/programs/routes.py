from flask import  jsonify, request, Blueprint
from backend import db
from backend.models.program import Program

programs = Blueprint('programs', __name__,url_prefix="/programs")



#retrieving all programs 
@programs.route("/", methods=['GET'])
def all_programs():
    #ensuring that a user has logged in
    all_programs = Program.query.all()
    return jsonify(all_programs),200



#retrieving a single program
@programs.route("/<int:program_id>", methods=['GET'])
def single_program(program_id):
    program = Program.query.filter_by(id=program_id).first()
    
    #Program that does'nt exist
    if not program:
        return jsonify({'message': '  Program not found'}), 404
    return jsonify(program),200


#creating programs
@programs.route("/", methods=["POST"])
def new_programs():
    
    if request.method == "POST":
        
        name = request.json['name']
        description = request.json['description']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        duration = request.json['duration']
        status = request.json['status']
    
        #program status: in_progress, closed

       #empty fields for validations
      
        if not name:
                 
          return jsonify({'error': 'Program name is required'}), 400 #bad request
          
        if not start_date:
            return jsonify({'error': 'Starting date is required'}), 400

        if not end_date:
            return jsonify({'error': 'Ending date is required'}), 400    
       
        if not duration:
                return jsonify({'error': 'Duration field is required'}), 400
        
        #checking if name exists
        if Program.query.filter_by(name=name).first():
                return jsonify({
                'error': 'Program name already exists'
            }), 409 #conflicts
      
           
        #For valid data
        #inserting values into the programs_list
        new_program = Program(name=name,description=description,start_date=start_date,end_date=end_date,status=status)
        db.session.add(new_program)
        db.session.commit()
        
         
  
    return jsonify({'message':'Added a new program','start_date':start_date,'name':name,'description':description,'user_id':user_id,'duration':duration,'status':status,'end_date':end_date}),200
    


 
# #deleting a question
@programs.route("/remove/<string:programId>", methods=['DELETE'])

def delete_programs(programId):
  

    program = Program.query.filter_by(user_id=current_user, id=programId).first()

    if not program:
        return jsonify({'message': 'program not found'}), 404

    db.session.delete(program)
    db.session.commit()

    return jsonify({}), 204

# #updating a program
# @programs.route("/remove/<string:programId>", methods=['DELETE'])
# @jwt_required()
# def update_programs(programId):
#     current_user = get_jwt_identity()

#     program = Program.query.filter_by(user_id=current_user, id=programId).first()

#     if request.method == "POST":
        
#         program.user_id = get_jwt_identity()
#         program.name = request.json['name']
#         program.description = request.json['description']
#         program.starting_date = request.json['starting_date']
#         program.end_date = request.json['end_date']
#         program.duration = request.json['duration']
#         program.status = request.json['status']
    
#         #program status: in_progress, closed

#        #empty fields for validations
      
#         if not program.name:
                 
#           return jsonify({'error': 'Program name is required'}), 400 #bad request
          
#         if not program.starting_date:
#             return jsonify({'error': 'Starting date is required'}), 400

#         if not program.end_date:
#             return jsonify({'error': 'Ending date is required'}), 400    
       
#         if not program.duration:
#                 return jsonify({'error': 'Duration field is required'}), 400
        
#         #checking if name exists
#         if Program.query.filter_by(name=name).first():
#                 return jsonify({
#                 'error': 'Program name already exists'
#             }), 409 #conflicts
      
           
#         #For valid data
#         #updating values into the programs_list
        
#         db.session.add(program)
#         db.session.commit()
        
         
  
#     return jsonify({'message':'Added a new program','starting_date':starting_date,'name':name,'description':description,'user_id':user_id,'duration':duration,'status':status,'end_date':end_date}),200
    

#     db.session.delete(program)
#     db.session.commit()

#     return jsonify({}), 204
    



