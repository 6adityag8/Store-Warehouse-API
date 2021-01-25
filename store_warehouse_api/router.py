class DBRouter:
    """
    A router to control all database operations on models in the
    store and warehouse applications.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read store models go to db_store
        and warehouse models go to db_warehouse.
        """
        if model._meta.app_label == 'store':
            return 'db_store'
        elif model._meta.app_label == 'warehouse':
            return 'db_warehouse'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write store models go to db_store
        and warehouse models go to db_warehouse.
        """
        if model._meta.app_label == 'store':
            return 'db_store'
        elif model._meta.app_label == 'warehouse':
            return 'db_warehouse'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the store or warehouse apps is
        involved.
        """

        if obj1._meta.app_label == 'store' or obj2._meta.app_label == 'store':
            return True
        elif 'store' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'warehouse' or obj2._meta.app_label == 'warehouse':
            return True
        elif 'warehouse' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        return False


def allow_migrate(self, db, app_label, model_name=None, **hints):
    """
    Make sure the auth and contenttypes apps only appear in the
    'auth_db' database.
    """
    if app_label == 'store':
        return db == 'db_store'
    elif app_label == 'warehouse':
        return db == 'db_warehouse'
    return None
