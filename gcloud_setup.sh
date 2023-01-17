
account="1058657454875-compute@developer.gserviceaccount.com" # find with sudo gcloud iam service-accounts list
keyfile_path="/Users/carlo/Projects/mlops/original-nomad-374513-b2fcf87a0b19.json"
project_id="original-nomad-374513"
image_name="app"

echo $account
echo $keyfile_path
echo $project_id

# Authenticate
sudo gcloud auth login
read -rsn1 -p"Press any key to continue";echo
sudo gcloud auth activate-service-account $account --key-file=$keyfile_path
sudo gcloud auth configure-docker

# Push image to registry
# sudo sh ./scripts/docker_app_build.sh
sudo docker tag $image_name gcr.io/$project_id/$image_name
sudo docker push gcr.io/$project_id/$image_name
