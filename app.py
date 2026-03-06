from flask import Flask, render_template, request

app = Flask(__name__)
# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Campaign Generator
@app.route("/campaign", methods=["GET","POST"])
def campaign():

    result = None

    if request.method == "POST":

        product = request.form["product"]
        audience = request.form["audience"]
        platform = request.form["platform"]

        result = f"""
5 Content Ideas:

1. "Before and After" Transformation Story: Share a case study showing how {product} helped {audience}.

2. Educational Series: Tips and hacks for {audience} related to {product}.

3. Behind-the-scenes development story of {product}.

4. Customer Success Story highlighting real benefits.

5. Interactive Polls and Q&A on {platform} to engage users.
"""

    return render_template("campaign.html", result=result)



# Pitch Generator
@app.route("/pitch", methods=["GET","POST"])
def pitch():

    pitch_text = None

    if request.method == "POST":

        product = request.form["product"]
        persona = request.form["persona"]

        pitch_text = f"""
30-Second Pitch:

Scale your business using our {product}. Designed for {persona}, our solution improves efficiency,
reduces operational costs and provides real-time insights.

Value Proposition:

1. Improved operational accuracy
2. Data-driven decision making
3. Scalable architecture
4. Seamless integrations

Call to Action:

Schedule a personalized demo today and discover how {product}
can transform your business.
"""

    return render_template("pitch.html", pitch=pitch_text)



# Lead Qualifier
@app.route("/lead", methods=["GET","POST"])
def lead():

    analysis = None

    if request.method == "POST":

        name = request.form["name"]
        budget = request.form["budget"]
        need = request.form["need"]
        urgency = request.form["urgency"]

        score = 92

        analysis = f"""
Lead Qualification Score: {score}/100

Reasoning:

Budget: {budget}

Need: {need}

Urgency: {urgency}

Probability of Conversion: 85%

This lead has strong buying potential due to sufficient budget,
clear business needs and urgency for implementation.
"""

    return render_template("lead.html", result=analysis)



if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)
