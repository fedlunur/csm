import importlib
from django.apps import apps
from django.db.models.base import ModelBase

def import_all_models():
    """
    Dynamically import all models from all installed apps and return them as a dictionary.
    The keys are the model names and the values are the model classes.
    """
    models = {}
    for app_config in apps.get_app_configs():
        try:
            app_module = importlib.import_module(app_config.name + '.models')
        except ModuleNotFoundError:
            continue

        # Iterate over all attributes of the module
        for attr_name in dir(app_module):
            attr = getattr(app_module, attr_name)
            if isinstance(attr, ModelBase):
                models[attr_name] = attr

    return models
