

# Clone the repositroy containing dvc files
# git clone https://github.com/${DO_GITHUB_USERNAME}/MSSC_DVC_V2.git MSSC_DVC

# Install the dvc python package and the S3 dependencies
pip install dvc
pip install dvc[s3]


# pull files
cd MSSC_DVC
dvc pull data.zip
