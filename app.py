import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Dummy current telemetry values for judges demonstration
    current_telemetry = {
        "plot_id": "Zone_A_Plot_04",
        "cluster": "North Valley Sector (Lahore Cluster)",
        "moisture": 24.5,          # Percentage (%)
        "temperature": 26.2,       # Celsius (°C)
        "ph": 6.3,                 # pH scale
        "compaction": 1.1,         # MPa
        "nitrogen": 75,            # mg/kg
        "phosphorus": 50,          # mg/kg
        "potassium": 90,           # mg/kg
        "ec": 1.2,                 # dS/m (Salinity)
        "sbhi": 78.5,              # Soil Biological Health Index (%)
        "action": "Apply Compost Tea",
        "status": "ACTIVE_RESTORATION",
        "lat": 31.5497,            # Lahore coordinates reference
        "lng": 74.3436
    }
    
    # Historical data for time-series graphs
    chart_history = [
        {"time": "09:00 AM", "sbhi": 62.0, "moisture": 15.0, "ph": 5.4},
        {"time": "10:00 AM", "sbhi": 67.5, "moisture": 18.2, "ph": 5.7},
        {"time": "11:00 AM", "sbhi": 71.0, "moisture": 20.5, "ph": 5.9},
        {"time": "12:00 PM", "sbhi": 74.2, "moisture": 22.0, "ph": 6.1},
        {"time": "01:00 PM", "sbhi": 78.5, "moisture": 24.5, "ph": 6.3}
    ]

    return render_template("dashboard.html", data=current_telemetry, history=chart_history)

if __name__ == "__main__":
    # Dynamically bind to the port assigned by Render or default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)