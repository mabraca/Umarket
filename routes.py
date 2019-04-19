import user, company, manufacturer, retail
@app.route('/')
def root_response():
    return jsonify({"Msj":"API REST UbiiMarket."})

@app.route('/users')
users()

@app.route('/user', methods=['POST'])
user()

@app.route('/user_login', methods=['POST'])
userLogin()

@app.route('/update', methods=['POST'])
updateUser()

@app.route('/delete/')
deleteUser()

@app.route('/token',methods=['POST'])
token()