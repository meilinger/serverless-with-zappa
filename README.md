# Going serverless with Zappa and Python

see http://slides.com/joemeilinger/going-serverless-with-zappa for accompanying slides

### Setup/running/deploying

#### Running locally

```
pip install -r requirements.txt
python app.py
```

#### Push to AWS Lambda

```
# Modify the `zappa_settings.json` to include your own s3 bucket name
zappa deploy
```
