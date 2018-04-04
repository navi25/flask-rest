from connexion.resolver import RestyResolver
import connexion
from injector import Binder
from flask_injector import FlaskInjector

from services.provider import ItemsProvider

#Adding Binding
def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )


if __name__ == '__main__':
    app = connexion.App(__name__, 9090, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()
