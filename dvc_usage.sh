DO_AWS_ACCESS_KEY_ID=DO00JVCF7VU9NR8R9KUC
DO_AWS_ACCESS_KEY=qw7fwzXbo90pYNVgybQbodide616IklbcR21y6G8EOI 


# Clone the repositroy containing dvc files
# git clone https://github.com/${DO_GITHUB_USERNAME}/MSSC_DVC_V2.git MSSC_DVC

export AWS_ACCESS_KEY_ID=${DO_AWS_ACCESS_KEY_ID}
export AWS_SECRET_ACCESS_KEY=${DO_AWS_ACCESS_KEY}
# Install the dvc python package and the S3 dependencies
# sudo apt remove python3.8 -y
# sudo apt install python3.8 -y
# sudo apt install python3-pip -y

/home/${DO_USERNAME}/dl-env/bin/pip install dvc
/home/${DO_USERNAME}/dl-env/bin/pip install dvc-s3

# pull files
# cd MSSC_DVC
source /home/${DO_USERNAME}/dl-env/bin/activate
dvc pull data.zip


