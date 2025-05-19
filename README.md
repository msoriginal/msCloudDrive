☁️ msCloud Driver
msCloud Driver is a personal cloud storage demo built using Flask. It lets you upload, preview, and download files through a simple web interface. The server runs locally but is exposed to the internet using LocalTunnel, allowing you to access your files from anywhere.

🚀 Features
📤 Upload files with progress bar and percentage

📁 View and preview uploaded files

📥 Download files if preview isn’t supported

🧭 Simple navigation between pages

🗂️ Files stored locally in the FilesUploaded folder

🌍 Accessible online using LocalTunnel with a custom subdomain

🛠 Tech Stack
Backend: Python (Flask)

Frontend: HTML, CSS, JavaScript

Tunnel Service: LocalTunnel (via Node.js)

📂 Project Structure
php
Copy
Edit
msCloudDriver/
│
├── FilesUploaded/          # Uploaded files are stored here
├── templates/              # HTML templates
│
├── server.py               # Flask backend server
├── starttunnel.js          # Starts LocalTunnel with a custom subdomain
├── README.md               # Project documentation
🧑‍💻 Getting Started
1. Install Python dependencies
Make sure Flask is installed:

bash
Copy
Edit
pip install flask
2. Start the Flask server
bash
Copy
Edit
python server.py
This will start the local server on http://127.0.0.1:5000.

3. Start the Tunnel (in a separate terminal)
bash
Copy
Edit
node starttunnel.js
This will expose your local server to the internet via LocalTunnel. The public URL/subdomain is defined inside starttunnel.js.

🌐 Accessing the App
Once both the Flask server and tunnel are running, open the public URL (from LocalTunnel) in your browser to access the app from any device.

⚠️ Note
This is a demo project meant for educational and personal use. Do not use it in a production environment as-is.
