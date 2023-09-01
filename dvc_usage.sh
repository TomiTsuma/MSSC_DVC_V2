
DO_AWS_ACCESS_KEY_ID=DO00JVCF7VU9NR8R9KUC
DO_AWS_ACCESS_KEY=qw7fwzXbo90pYNVgybQbodide616IklbcR21y6G8EOI 


# Clone the repositroy containing dvc files
# git clone https://github.com/${DO_GITHUB_USERNAME}/MSSC_DVC_V2.git MSSC_DVC

# Install the dvc python package and the S3 dependencies
pip install dvc==3.15.3


# pull files
# cd MSSC_DVC
dvc pull data.zip
