from flask import Flask, request, jsonify

app = Flask(__name__)

student_details = [
    {
        'id':1,
        'name':'Esther Adhiambo',
        'subject':'SPSS',
        'Duration':'1 month'
    },
    {
        'id':2,
        'name':'Brian Otieno',
        'subject':'Canva',
        'Duration':'1 month'
    },
    {
        'id':3,
        'name':'Rose Adhiambo',
        'subject':'R',
        'Duration':'2 months'
    }
]

@app.route('/students', methods = ['GET','POST'])
def students():
    if request.method == 'GET':
        if len(student_details) > 0:
            return jsonify(student_details)
    else:
        'Not Found', 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_subject = request.form['subject']
        new_duration = request.form['Duration']
        iD = student_details[-1]['id']+1
        
        
        new_obj = {
            'id':iD,
            'name':new_name,
            'subject':new_subject,
            'Duration':new_duration
        }

        student_details.append(new_obj)
        return jsonify(student_details), 201

@app.route('/student/<int:id>', methods=['GET','PUT','DELETE'])
def student(id):
    if request.method == 'GET':
        for student in student_details:
            if student['id'] == id:
                return jsonify(student)

    if request.method == 'PUT':
        for student in student_details:
            if student['id'] == id:
                student['name']:request.form['name']
                student['subject']:request.form['subject']
                student['Duration']:request.form['Duration']

                updated_student = {
                    'id':student['id'],
                    'subject':student['subject'],
                    'Duration':student['Duration']
                }

                student_details.append(updated_student)
                return jsonify(student_details)



if __name__ == '__main__':
    app.run()