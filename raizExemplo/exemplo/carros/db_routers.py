class DBRouter():
    """
    A router to control all database operations on models in the
    carros application.
    """
    #route_app_labels = {'carros'}

    def db_for_read(self, model, **hints):
        """
        Direcionamento de leitura para o banco de dados MTCars quando a tabela for 'MTCars'.
        """
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write carros models go to DBMTCars.
        """
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the carros app is involved.
        """
        if (
            obj1._meta.db_table == 'MTCars' or \
            obj2._meta.db_table == 'MTCars'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the carros app only appears in the 'DBMTCars'
        database.
        """
        if app_label == 'exemplo':
            return db == 'DBMTCars'
        return None