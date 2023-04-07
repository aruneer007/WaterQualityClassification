from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application= Flask(__name__)

app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET', 'POST'])
def predict_datapoint():
    if request.method== 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            ph=float(request.form.get('ph')),
            iron= float(request.form.get('iron')),
            nitrate=float(request.form.get('nitrate')),
            chloride = float(request.form.get('chloride')),
            lead=float(request.form.get('lead')),
            zinc=float(request.form.get('zinc')),
            turbidity=float(request.form.get('turbidity')),
            fluoride=float(request.form.get('fluoride')),
            copper=float(request.form.get('copper')),
            odor=float(request.form.get('odor')),
            sulfate=float(request.form.get('sulfate')),
            conductivity=float(request.form.get('conductivity')),
            chlorine=float(request.form.get('chlorine')),
            manganese=float(request.form.get('manganese')),
            total_dissolved_solids=float(request.form.get('total_dissolved_solids')),
            color=request.form.get('color'),
            source=request.form.get('source')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline=PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(results)
        if results == 0:
            return render_template('home.html', results = "Safe to Drink")
        elif results == 1:
            return render_template('home.html', results = "UnSafe to Drink")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
