Django on App Engine
--------------------

Pyowa talk, October 9, 2014.

Demonstrates how to run a normal django app, then deploy it to
Google's App Engine. Converting to App Engine is pretty easy, just follow the steps below:

**Create New Project:**

`https://console.developers.google.com
<https://console.developers.google.com/>`_

**Create Cloud SQL Database**

- Storage -> Cloud SQL
- Enable Billing
- Create Instance
- Set Root Password
- Get IP Address
- `Create DB & Permissions <https://docs.google.com/document/d/1iq024XGIa9ffxHEnMuei0ydXR_WWyEu7BLGxWSUK5qc/edit?usp=sharing>`_

**Updating Existing Project for App Engine**

- Add `app.yaml`

  This is the main configuration file for App Engine. It specifies your settings & route handlers

- Add `django-appengine-utils` to project dependencies. This project is taken from the original django-nonrel. It provides an email backend, test runner, memcache stub, warmup request view, and a blobstore storage backend.

- add `appengine_config.py`

  This file is imported before anything else. Adding `lib` directory to path here.

**Update Settings:**

Base Settings: 

- Add `lib` dir to to path
- `SERVER_EMAIL` set to someone with permission to app
- `STATIC_ROOT = join(BASE_DIR, 'production_static')`

Dev Settings:

- `EMAIL_BACKEND = 'appengine_utils.mail.EmailBackend'`

Test Settings:

If you're using memcache, taskqueues, or other appengine apis, you'll need to initialize the testbed stubs. The below test runner makes that easy.

- `TEST_RUNNER = "appengine_utils.test_utils.AppEngineTestRunner"`

Remote Settings:

- Add remote settings to access production database locally

Production Settings:

- Update DB Credentials
- `EMAIL_BACKEND = 'appengine_utils.mail.AsyncEmailBackend'`
- `EMAIL_QUEUE_NAME = 'default'`
