import os
import ckanserviceprovider.web as web
import datapusher.jobs as jobs

# check whether jobs have been imported properly
assert(jobs.push_to_datastore)

if 'DATABASE_URL' in os.environ:
    web.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

web.configure()
app = web.app
print app.config.get('SQLALCHEMY_DATABASE_URI')

if __name__ == "__main__":
    import logging
    port = os.environ.get('PORT', 5000)
    debug = os.environ.get('DEBUG', False)
    host = os.environ.get('HOST', '0.0.0.0')
    logging.basicConfig(level=logging.NOTSET)
    app.run(host=host, port=port, debug=debug)

