from flask import Flask, render_template, request
import pandas as pd
import datetime as dt
import pickle
import sklearn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
      df1=pd.DataFrame(index=[0])
      df1['DateofJourney']=request.values['DateofJourney']
      df1['Year'] = pd.DatetimeIndex(df1['DateofJourney']).year
      df1['Month'] = pd.DatetimeIndex(df1['DateofJourney']).month
      df1['Day'] = pd.DatetimeIndex(df1['DateofJourney']).day
      df1.drop(['DateofJourney'],axis=1,inplace=True)
      df1['Departure']=request.values['Departure']
      df1["Dep_hour"] = pd.to_datetime(df1["Departure"]).dt.hour
    
      # Extracting Minutes
      df1["Dep_min"] = pd.to_datetime(df1["Departure"]).dt.minute

    
      df1.drop(["Departure"], axis = 1, inplace = True)    
      df1['Arrival']=request.values['Arrival']           
      # Extracting Hours
      df1["Arrival_hour"] = pd.to_datetime(df1.Arrival).dt.hour
      df1["Arrival_min"] = pd.to_datetime(df1.Arrival).dt.minute
      df1.drop(["Arrival"], axis = 1, inplace = True) 
      Source = request.form["Source"]
      if (Source == 'Delhi'):
         s_Delhi = 1
         s_Kolkata = 0
         s_Mumbai = 0
         s_Chennai = 0
      elif (Source == 'Kolkata'):
         s_Delhi = 0
         s_Kolkata = 1
         s_Mumbai = 0
         s_Chennai = 0
      elif (Source == 'Mumbai'):
         s_Delhi = 0
         s_Kolkata = 0
         s_Mumbai = 1
         s_Chennai = 0
      elif (Source == 'Chennai'):
         s_Delhi = 0
         s_Kolkata = 0
         s_Mumbai = 0
         s_Chennai = 1
      else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0
    Source = request.form["Destination"]
    if (Source == 'Cochin'):
      d_Cochin = 1
      d_Delhi = 0
      d_New_Delhi = 0
      d_Hyderabad = 0
      d_Kolkata = 0
        
    elif (Source == 'Delhi'):
      d_Cochin = 0
      d_Delhi = 1
      d_New_Delhi = 0
      d_Hyderabad = 0
      d_Kolkata = 0

    elif (Source == 'New_Delhi'):
      d_Cochin = 0
      d_Delhi = 0
      d_New_Delhi = 1
      d_Hyderabad = 0
      d_Kolkata = 0
    elif (Source == 'Hyderabad'):
      d_Cochin = 0
      d_Delhi = 0
      d_New_Delhi = 0
      d_Hyderabad = 1
      d_Kolkata = 0

    elif (Source == 'Kolkata'):
      d_Cochin = 0
      d_Delhi = 0
      d_New_Delhi = 0
      d_Hyderabad = 0
      d_Kolkata = 1
    else:
      d_Cochin = 0
      d_Delhi = 0
      d_New_Delhi = 0
      d_Hyderabad = 0
      d_Kolkata = 0       
    
    df1['Total_Stops'] = int(request.form['Stopage'])
    airline=request.form['airline']
    if(airline=='Jet Airways'):
      Jet_Airways = 1
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0 

    elif (airline=='IndiGo'):
      Jet_Airways = 0
      IndiGo = 1
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0 
    elif (airline=='Air India'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 1
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0 
    elif (airline=='Multiple carriers'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 1
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0 
    elif (airline=='SpiceJet'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 1
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0 
    elif (airline=='Vistara'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 1
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0
    elif (airline=='GoAir'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 1
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0
    elif (airline=='Multiple carriers Premium economy'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 1
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0
    elif (airline=='Jet Airways Business'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 1
      Vistara_Premium_economy = 0
      Trujet = 0
    elif (airline=='Vistara Premium economy'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 1
      Trujet = 0
            
    elif (airline=='Trujet'):
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 1

    else:
      Jet_Airways = 0
      IndiGo = 0
      Air_India = 0
      Multiple_carriers = 0
      SpiceJet = 0
      Vistara = 0
      GoAir = 0
      Multiple_carriers_Premium_economy = 0
      Jet_Airways_Business = 0
      Vistara_Premium_economy = 0
      Trujet = 0
    df1['Duration'] = request.form['Duration']
    df1['TotalMinutes']=(pd.to_timedelta(df1['Duration']).dt.seconds // 60).astype(str) 
    h = df1['Duration'].str.extract('(\d+)h', expand=False).astype(float) 
    m = df1['Duration'].str.extract('(\d+)m', expand=False).astype(float)

    df1["Duration_hours"] = h
    df1["Duration_mins"] = m 
    df1.drop(['Duration'],axis=1,inplace=True)
    print(Jet_Airways,
            IndiGo,
            Air_India,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            GoAir,
            Multiple_carriers_Premium_economy,
            Jet_Airways_Business,
            Vistara_Premium_economy,
            Trujet)
    Year = df1['Year']
    print(Year)
    Month =df1['Month']
    print(Month)
    Day = df1['Day']
    print(Day)
    Dep_hour =df1['Dep_hour']
    print(Dep_hour)
    Dep_min = df1['Dep_min']
    print(Dep_min)
    Arrival_min = df1['Arrival_min']
    print(Arrival_min)
    Arrival_hour = df1['Arrival_hour']
    print(Arrival_hour)
    Total_Stops = df1['Total_Stops']
    print(Total_Stops)
    TotalMinutes = df1['TotalMinutes'].astype(int)
    print(TotalMinutes)
    Duration_hours = df1['Duration_hours']
    print(Duration_hours)
    Duration_mins = df1['Duration_mins']
    print(Duration_mins)



    print(df1.columns)
    with open('flightreg.pkl', 'rb') as f:
      dt1 = pickle.load(f)
    print("loading saved artifacts...done")
    value=dt1.predict([[
      Year,
      Month,
      Day,
      Dep_hour,
      Dep_min,
      Arrival_min,
      Arrival_hour,
      Total_Stops,
      TotalMinutes,
      Duration_hours,
      Duration_mins,
      Jet_Airways,
      IndiGo,
      Air_India,
      Multiple_carriers,
      SpiceJet,
      Vistara,
      GoAir,
      Multiple_carriers_Premium_economy,
      Jet_Airways_Business,
      Vistara_Premium_economy,
      Trujet,
      s_Chennai,
      s_Delhi,
      s_Kolkata,
      s_Mumbai,
      d_Cochin,
      d_Delhi,
      d_Hyderabad,
      d_Kolkata,
      d_New_Delhi
      ]])
    print(value)
    output=round(value[0],2)
    return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    
    return render_template("home.html")


app.run(host='0.0.0.0', port=8080)