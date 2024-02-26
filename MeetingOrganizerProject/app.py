from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

users = {
    'admin': 'password',
    'user' : 'password'
}
meetings = []
meeting_counter = 0

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            return redirect(url_for('index'))
        else:
            error_message = "Yanlış kullanıcı adı veya şifre. Lütfen tekrar deneyin."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html', error_message=None)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/meetings', methods=['GET'])
def get_meetings():
  return jsonify(sorted(meetings, key=lambda meeting: meeting['id']))

@app.route('/api/meetings', methods=['POST'])
def create_meeting():
    global meeting_counter
    data = request.json
    data['id'] = meeting_counter
    meetings.append(data)
    meeting_counter += 1
    return jsonify(data), 201

@app.route('/api/meetings/<int:id>', methods=['PUT'])
def update_meeting(id):
    for meeting in meetings:
        if meeting['id'] == id:
            meeting.update(request.json)
            print("Meeting updated:", meeting)
            return jsonify(meeting)
    print("oplantı bulunamadı:", id)
    return jsonify({'message': 'Toplantı bulunamadı.'}), 404

@app.route('/api/meetings/<int:id>', methods=['DELETE'])
def delete_meeting(id):
    for meeting in meetings:
        if meeting['id'] == id:
            meetings.remove(meeting)
            return jsonify({'message': 'Toplantı silindi.'})
    return jsonify({'message': 'oplantı bulunamadı.'}), 404

@app.route('/update_form/<int:meeting_id>')
def update_form(meeting_id):
    meeting = next((m for m in meetings if m['id'] == meeting_id), None)

    if meeting:
        return render_template('update_form.html', meeting=meeting)
    else:
        return "Toplantı bulunamadı", 404

if __name__ == '__main__':
    app.run(debug=True)
