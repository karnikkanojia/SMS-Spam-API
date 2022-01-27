# SMS-Spam-API
## Steps to Access
To access our application you can either download the [android application]().

- [Backend API Postman Documentation](https://documenter.getpostman.com/view/18833270/UVeAtoRi)
- [Android App](https://github.com/ankithans/aadhaar-address-update/releases/download/v1.0.0/app-release.apk)
- [Google Slides Presentation](https://docs.google.com/presentation/d/1jLPull2oPpjYmqjZ3OYSywi6pUvDwz_kdRglHXa2vA0/edit?usp=sharing)
- [Video Demonstration](https://drive.google.com/file/d/1dfzlQbMaFiceaMA3m3UuaSNw_MhVyJiU/view?usp=sharing)

## Motivation 
Confidence in an online world
Our lives have been subjected to digital attacks more than ever before.

In recent times, during the lockdown period, a lot of citizens were victims of an SMS scam. 
The victim receives an SMS as below:

> "Dear customer, your xxx bank account will be suspended! Please Re KYC Verification Update click here link http://446bdf227fc4.ngrok.io/xxxbank".

Once a victim clicks on the link and logs in to the phishing website using internet banking credentials, the attacker generates OTP for 2FA or two factor authentication which is delivered to the victim's phone number. The victim then enters this OTP in the phishing site, which the attacker captures and Finally, the attacker gains access to the victim's account using the OTP and performs fraudulent transactions.

Use your creativity to design and develop a mobile app which can automatically scan through SMS texts and detect possible fraud and phishing attacks and suggest the user not to click on such a link. Additionally, the app can have a "Report This" option which submits the incident to Cyber Security Department (CERT-In) for further investigation. How will you detect false positives in reporting such incidents?

## ❓ Problem Statement
To design and develop a mobile app that can automatically scan through SMS texts to detect possible fraud and phishing attacks and suggest the user not to click on such a link.

## 👌 What it does/ Features:
- Spam and Malicious SMS Detection using BiLSTM Deep Learning Model with 98% Efficiency
- "Report This" option which submits the incident to Cyber Security Department (CERT-In) for further investigation
- User can see the SIM on which the spam message is coming
- Easy to understand Minimilastic and Interactive UI/UX Design 

## Proposed Approach:
<img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/hackathon.png" >



## Mockups
<table>
    <tr>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0001.jpg"></td>
<td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0002.jpg"></td>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0003.jpg"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0004.jpg"></td>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0005.jpg"></td>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0006.jpg"></td>
        <td><img src="https://github.com/eshaanagarwal/SMS-Spam-API/blob/documentation/Sms_page-0007.jpg"></td>
    </tr>
</table>

## Tech Stack
React Native, Python, Flask, Tensorflow, Heroku, Git, Numpy, Pandas, Scikit, Matplotlib
Technologies : Deep Learning, Bi-LSTM


## Steps to run loclly
Clone the repo in your local machine and setup python and flutter environment. Create .env file similar to .env.sample file with all the required fields.

### Mobile Application
1. Go into `app/` directory by doing `cd app` in terminal.
2. Configure firebase for android by folllowing the [doumentation](https://firebase.flutter.dev/docs/installation/android/).
3. Write `flutter run` in the terminal to start the application.

### Flask Server
1. Install all the required packages in python virtual enviroment `pip install requirements.txt`
2. Run `python app.py` in the root directory of the project.

## Contributors
- [Harsh Jadon](https://github.com/harshjadon9)
- [Karnik Kanojia](https://github.com/karnikkanojia)
- [Eshaan Agarwal](https://github.com/eshaanagarwal)
