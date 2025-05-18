from flask import Flask, render_template, request, flash
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

def is_valid_hex(hex_code):
    # Remove # if present
    hex_code = hex_code.lstrip('#')
    # Check if the hex code is valid (6 characters, hexadecimal)
    return bool(re.match(r'^[0-9A-Fa-f]{6}$', hex_code))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hex_code = request.form.get('hex_code', '').strip()
        
        if not hex_code:
            flash('Please enter a hex code', 'error')
        elif not is_valid_hex(hex_code):
            flash('Invalid hex code. Please enter a valid 6-digit hex code (e.g., #FF0000)', 'error')
        else:
            # Add # if not present
            if not hex_code.startswith('#'):
                hex_code = '#' + hex_code
            return render_template('index.html', hex_code=hex_code)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 