# Plant Diseases Detection
I have been taking a couple of deep learning classes at https://course.fast.ai and got inspired by some of the projects done by other students undertaking the same class. So, I decided to try out something cool but meaningful using what I had learned in the first couple lessons. 

So, Kudos to `fast.ai` team for making deep learning fun and easy! 

## Goal of Project 
The main idea is still very fuzzy, but I hope to build a tool that helps farmers in Kenya identify crop diseases by simply taking a photo of a diseased part of the plant. 
Hopefully, this can help farmers increase yield, reduce losses, detect diseases earlier, and seek help before it is too late. Maybe in future, this Project can evolve to recommend best treatment for specific diseases and so on. 

## Getting Started
I wouldn't recommend you run this model.. But, hell, who am I to stop you from doing so? 

### Pre-requisities
1. Google Cloud VM Instance or AWS or Azure. 
2. Basic Knowledge of Jupyter Notebooks
3. Basic Knowledge of Python

### Setting Up Google Cloud Instance 

1. Create your account on GCP. 

    Google Cloud Comes with free credits worth $300. Sign up for Google Cloud [Here](https://cloud.google.com).

2. Install Google CLI (For MacOS)
    ```
    curl https://sdk.cloud.google.com | bash
    exec -l $SHELL
    ```
    then
    ```
    gcloud init
    ```
    You will be prompted with the following message
    ```
    To continue, you must log in. Would you like to log in (Y/n)?
    ```
    Type Y and choose your Project

3. Create an Instance 
   
   Copy and Paste the following Command
   ```
   export IMAGE_FAMILY="pytorch-latest-gpu" # or "pytorch-latest-cpu" for non-GPU instances
    export ZONE="us-west1-b"
    export INSTANCE_NAME="my-deeplearning-instance"
    export INSTANCE_TYPE="n1-highmem-4"

    gcloud compute instances create $INSTANCE_NAME \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --accelerator="type=nvidia-tesla-k80,count=1" \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=200GB \
        --metadata="install-nvidia-driver=True" \
        --preemptible
   ```
   If you get an error saying: 
   ```
   ERROR: (gcloud.compute.instances.create) Could not fetch resource:
   - Quota 'GPUS_ALL_REGIONS' exceeded. Limit: 0.0 globally.
   ```

    You will need to adjust your GPU Quotas
    Go to Google [Cloud Quotas Page](https://console.cloud.google.com/iam-admin/quotas).

    If you signed up with a free tier account, you first need to upgrade to a paid account; do so by clicking the “Upgrade account” button at the top right of the page. This won’t affect your $300 credit.

    In filter type, select metric to be GPUs (all regions) and Location as Global.
    Click edit quotas and select the quota to edit (GPUs All Regions). Set the new quota limit to 1 or more. Your request may require confirmation, which Google claims typically takes two business days to get.
    
    You will have to wait a little bit until you see the text informing you the instance has been created. You can see the instance online [here](https://console.cloud.google.com) in your list of instances (note that this will be the page you have to go to later to stop your instance).

    Access your Instance on Terminal by typing: 
    ```gcloud compute ssh --zone=$ZONE jupyter@$INSTANCE_NAME -- -L 8080:localhost:8080```

4. Access Material / Create Your Own Material

   On terminal, ```mkdir deep_learning``` then ```cd deep_learning``` then ```http://localhost:8080/tree``` on browser then open your deep_learning folder then on right-top side of browser, click new then select Python 3 which will open a notebook which can be used to try out different models 


Remember to shut down your instance on Google Cloud after use. 

### Downloading Data. 
The Data used for this Project comes from [Kaggle](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset). Due to copyright restrictions, Kaggle requires users to sign up before downloading any datasets. 

To download Kaggle Datasets using Kaggle API: 
```
pip install kaggle --upgrade
mkdir -p ~/.kaggle/
mv /download/path/kaggle.json ~/.kaggle/
kaggle datasets download -d vipoooool/new-plant-diseases-dataset
Unzip dataset. 
```

### Testing

Guide Coming Soon
## Built With

1. [Python](https://www.python.org/) - Source language
2. [Jupyter](https://jupyter.org) - Notebooks
3. [Fast AI](https://www.fast.ai) - Deep Learning Framework

## Contributing

Guide Coming Soon
