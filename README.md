# Django-Zappa
Thisproject is used to show how to deploy an django app on aws lambda using zappa 

# Stack
<ul>
<li>Django</li>
<li>Zapp </li>
<li>virtualenv </li>
<li>S3 </li>
</ul>

## Follow the following steps in order to deploy the app on aws lamba
### 1- Set your virtualmachine(Zappa required a virtual-enviroment in order to work)
<ol>
<li>pip3 install virtualenv</li>
<li>virtualenv -p python3 <desired-path> </li>
<li>source <desired-path>/bin/activate </li>
<li>deactivate </li>
</ol>

### 2-  before running zappa make sure that the following file exist on your machine 
<ul>
<li>vi ~/.aws/credentials </li>
</ul>
 
#### The file looks something like this" 
```bash
[default]
aws_access_key_id = some_public_key
aws_secret_access_key = some_secret_key
```

### Modify your settings.py  and install the following package to server static files" 
#### A- install the following package 
<ul>
<li>pip install django-s3-storage</li>
</ul>

#### B- On settings.py, add 'django_s3_storage' to install app 
```bash
INSTALLED_APPS = [
  ... 
'django_s3_storage'
]
```
#### B- On settings.py, add the followings variables 

```bash
S3_BUCKET_NAME = "zappatest-static-files"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET_NAME
# serve the static files directly from the specified s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % S3_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# if you have configured a custom domain for your static files use:
#AWS_S3_PUBLIC_URL_STATIC = "https://static.yourdomain.com/"
```



### C- on your S3 bucket, under 'permissions', edit your CORS rule in order to allow access to the static files   
```bash
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "MaxAgeSeconds": 3000
    }
]
```


### 3-  Zappa Deployment 
<ul>
<li>zappa init </li>
<li> zappa deploy dev </li>
<li> zappa update dev  </li>
</ul>


 


### 4- Modify your S3 bucket to handle   static files 
<ul>
<li>zappa init </li>
<li> zappa deploy dev </li>
<li> zappa update dev  </li>
</ul>