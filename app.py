#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import json,time,requests


app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        body = json.dumps(
            {
                "version":"db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                "input":{
                    "prompt": q
                }
        
            }
        )
        headers = {
            "Authorization": "Token r8_Zlui36p8W22PTfNx3j57D8iw2PLIO8q2JBCzK",
            "Content-Type": "application/json"
        }
        output = requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]        
        return(render_template("index.html",result=get_result[0]))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()


# In[ ]:




