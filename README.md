# Python notebooks for reporting

## Setting up a reporting environment
To build a server, setup a [Ubuntu Pro LTS VM on azure](https://ubuntu.com/azure/pro), persistently mount at boot a datalake using [blobfuse](https://github.com/Azure/azure-storage-fuse) or [s3fs](https://github.com/s3fs-fuse/s3fs-fuse), and install [the littlest jupyter hub](https://tljh.jupyter.org/en/latest/install/custom-server.html). That will be sufficient for a shared environment with up to 100 users.

## Install and configuration
Open up port 80 and 443 from the internet, configure DNS to point at the VM's public IP, then run through the install and configuration:

```bash
sudo apt install python3 python3-dev git curl
curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin admin
sudo tljh-config set user_environment.default_app jupyterlab
sudo tljh-config set https.enabled true
sudo tljh-config set https.letsencrypt.email bob@bobs.burgers
sudo tljh-config add-item https.letsencrypt.domains jupyterlab.bobs.burgers
sudo tljh-config reload proxy
sudo tljh-config reload hub
./bootstrap.py # downloaded from this repo
```

## Improving security
It's best to configure federated authentication to improve security.
- [Authenticator Configuration](https://tljh.jupyter.org/en/latest/topic/authenticator-configuration.html)
- [Azure AD setup](https://oauthenticator.readthedocs.io/en/latest/getting-started.html#azure-ad-setup)

## Running reports
The `*.ipynb` files in this repo can be uploaded to the jupyterlab environment and run against datasets in your datalake, they may need some configuration to adjust locations of data sources etc. It can be convenient to use a support notebook like [generate-reports.ipynb](generate-reports.ipynb) to run through and generate reports in bulk, which can then be scheduled using a tool like [`jupyter nbconvert --execute`](https://nbconvert.readthedocs.io/en/latest/execute_api.html)