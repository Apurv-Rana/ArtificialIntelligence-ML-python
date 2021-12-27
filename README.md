PLease Read This For More details

# Virtual Assitant - Cookie

This a very basic virtual assistant which can do wiki search for you.

Text to speech framework used is  pyttsx3 
speech_recognition Library for performing speech recognition, with support for several engines and APIs, online and offline.

```
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
```


#### pyttsx3 
Text to speech framework

`pip install pyttsx3`

An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3

### PyWhatKit
PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Added support for youtbe queries and playing a song.

# Sketch Creator (No Ai just a python based image procesisng library)
Imageio is a Python library that provides a simple interface for reading and writing various image data such as animated images, volume data, and scientific formats.

![image](https://user-images.githubusercontent.com/29672909/147487659-f0cb3490-6def-4afb-bd04-0d66841cadf1.png)

####reading the images and displaying

```
img="https://i.pinimg.com/originals/e2/05/4b/e2054b0c108f943fa58d98b8a4d37cd5.png" 

dp.Image(requests.get(img).content)

source_img = imageio.imread(img) //displaying the image 

```
![image](https://user-images.githubusercontent.com/29672909/147487736-9cf4bb85-7d67-41c6-a56e-0a051fe6bd4b.png)


# Sonar Mine Predictor
The model is used for binary classification for a sonar device to predecity diffrence between rock and mine. The application of this can be in battle ships/sumbarines to safegaurd the Defence assets. The model used for predections is trained using Logisitc Regression model with a dataset obtained from kaggle. plese Find the dataset file at the root names as sonar_data and change the path accordingly in code.

# ChatBot
This is a simple framework which is used to train a neural network using tensorflow using university qustionaries intent. once the neural network is trained you can query come question related to university service and bot will provide a satidfactoy answer. predection can vary as on how the bot is trained.

`pip install tensorflow`


### Examples

`classify('What are you hours of operation?')`

####`response('openhouse timings') `

-- We're open Mon to Fri  day 9am-9pm and alternate sat from 9am to 12pm

####`response('how can i pay my fees')`

you can generate e-challan from nearest icici bank

####`response("can i study computer engineering")`
we provide a wide range of programmes, please visit programmes available section of the website

####`response('LOR document')`
we do provide LOR, please visit Head of the Department for more details, keep the Documents ready

