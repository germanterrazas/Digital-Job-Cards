class JobcardsRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'adminsys':
            return 'jobcardsdb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'adminsys':
            return 'jobcardsdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'adminsys' and obj2._meta.app_label == 'adminsys':
            return True
        # Allow if neither is adminsys app
        elif 'adminsys' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'jobcardsdb' or model._meta.app_label == "adminsys":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True