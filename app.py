
from flask import Flask, render_template, request

app = Flask(__name__)

schemes = [
    {
        "name": "PM Kisan Samman Nidhi",
        "category": "Farmers",
        "benefits": "Financial assistance to eligible farmer families.",
        "eligibility": "Eligible landholding farmer families, subject to scheme rules.",
        "website": "https://pmkisan.gov.in/"
    },
    {
        "name": "Ayushman Bharat PM-JAY",
        "category": "Healthcare",
        "benefits": "Health coverage for eligible families.",
        "eligibility": "Eligibility depends on government beneficiary records.",
        "website": "https://pmjay.gov.in/"
    },
    {
        "name": "PM Awas Yojana",
        "category": "Housing",
        "benefits": "Housing assistance for eligible beneficiaries.",
        "eligibility": "Depends on scheme rules and beneficiary category.",
        "website": "https://pmaymis.gov.in/"
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    results = schemes
    query = ""

    if request.method == "POST":
        query = request.form.get("search", "").lower()
        results = [
            s for s in schemes
            if query in s["name"].lower()
            or query in s["category"].lower()
        ]

    return render_template(
        "index.html",
        schemes=results,
        query=query
    )

if __name__ == "__main__":
    app.run(debug=True)
