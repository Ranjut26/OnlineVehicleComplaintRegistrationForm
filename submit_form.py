from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder='.')

# Define route for the homepage
@app.route('/', methods=['GET'])
def home():
    # Render the home template (Zotavehicles.html)
    return render_template('Zotavehicles.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Retrieve form data
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        custID = request.form.get('custID')
        phone = request.form.get('phone')
        address = request.form.get('address')
        email = request.form.get('mail')
        vehicle_files = request.files.getlist('vehiclefile')
        telephoneno = request.form.get('telephoneno')
        purchasedate = request.form.get('purchasedate')
        owner_image_file = request.files.get('ownerimagefile')
        vehicle_type = request.form.get('vehicles')
        insurance_details = request.files.get('insurancedetails')
        fuel_type = request.form.get('fuel')

        # Process the form data (e.g., store it in a database)
        # For demonstration purposes, let's print the data
        print("First Name:", fname)
        print("Last Name:", lname)
        print("Customer ID:", custID)
        print("Contact Number:", phone)
        print("Address:", address)
        print("Email:", email)
        print("Vehicle Files:", vehicle_files)
        print("Telephone Number:", telephoneno)
        print("Date of Vehicle Purchase:", purchasedate)
        print("Owner Image File:", owner_image_file)
        print("Vehicle Type:", vehicle_type)
        print("Insurance Details:", insurance_details)
        print("Fuel Type:", fuel_type)

        # Redirect user to a thank you page with a message
        return redirect(url_for('thank_you'))
    else:
        # Render the form template
        return render_template('Zotavehicles.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for registering your complaint on our website. We will get back to you as soon as possible."

if __name__ == '__main__':
    app.run(debug=True)
