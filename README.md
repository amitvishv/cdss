**Install Django within a Virtual Environment**
<br><br>
`sudo apt-get install python3-pip`
<br><br>
`sudo pip3 install virtualenv `
<br><br>
`virtualenv envOne`   `#It will create virtual environemnt`
<br><br>
`source envOne/bin/activate`
<br><br>
`pip install -r req.txt` `#Install all the dependency`
<br><br><br>
**Project Setups**
<br><br>
`take git pull using` `git pull gitlink`
<br><br>
`cd cdss`
<br><br>
`python manage.py migrate`
<br><br>
`python manage.py runserver`
<br><br>
`Open Browser Chrome or Firefox or anything`
<br><br>
`GET  http:/127.0.0.1:8000/admin`  `Provide Fincode in url bar`
<br><br>
`Username:`  `amit123`
<br>
`Password:`   `Amit0000`
<br><br>
`You can Create New User via clicking on Users Model `
<br>
`You can add Hopital in to Hospital Models`
<br>
`You can Add Medical History in to Medical History providing Adharno and File there`
<br><br>
#### Required API
`POST`  `http://127.0.0.1:8000/doctor/api/upload` # Provide Event Type, Description, File
<br><br>
`GET`   `http://127.0.0.1:8000/doctor/api/history?adharno=112233` # provide adharno into url
