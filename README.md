# Deploy-CNN-on-google-cloud
This project shows how to deploy a deep convolutional neural network (CNN) on google cloud (App Engine). This is an instruction for how to use Keras and Flask to deploy a CNN model (InceptionResNetV2) on GCP. 
Create a new python environment:

        pip install virtualenv
Once virtualenv is installed you should create and activate a new python environment:
        
        virtualenv <name_of_enviroment> (e.g. virtualenv web_app)
        source <directory_to_the_name_of_enviroment>/bin/activate (e.g. source web_app/bin/activate)
Clone to this GitHub and download the files:
        
         git clone https://github.com/sinaakbarian/Deploy-CNN-on-google-cloud.git
Install requirement packages:
        
         pip install -r requirements.txt 
Run the following code to download a pretrained weights of InceptionResNetV2 model:
         
         python download_model.py
To test the app on a local server:

         gunicorn -b :8889 app:app -t 120 --graceful-timeout 60
         
Then open a browser go to http://localhost:8889/ and use the app.
To deploy it on the GCP you need to install GCP SDK: https://cloud.google.com/sdk/install.
Once initialization is done:
                
                gcloud init
             
The app will be deployed with the following command:

                gcloud app deploy
                
The web will be open with:
                
                 gcloud app browse
         
          
          
 
         


        
