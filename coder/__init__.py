from flask import Flask
from coder.openswg import opp
from importlib import import_module
from coder.settings import app_settings


def register_blueprints(fpp, blueprints):
    """蓝图注册"""
    for bp in blueprints:
        mod = import_module(f'coder.api.{bp}')
        fpp.register_blueprint(mod.bp)


def create_app():
    """coder 实例化"""
    fpp = Flask(__name__)
    fpp.settings = app_settings

    register_blueprints(fpp, app_settings.blueprints)
    opp.init_app(fpp)
    return fpp
