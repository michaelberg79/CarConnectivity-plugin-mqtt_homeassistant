""" User interface for the MQTT Home Assistant plugin in the Car Connectivity application. """
from __future__ import annotations
from typing import TYPE_CHECKING

import os

import flask

from carconnectivity_plugins.base.plugin import BasePlugin
from carconnectivity_plugins.base.ui.plugin_ui import BasePluginUI

if TYPE_CHECKING:
    from typing import Optional, List, Dict, Union, Literal


class PluginUI(BasePluginUI):
    """
    A user interface class for the MQTT Home Assistant plugin in the Car Connectivity application.
    """
    def __init__(self, plugin: BasePlugin):
        blueprint: Optional[flask.Blueprint] = flask.Blueprint(name=plugin.id, import_name='carconnectivity-plugin-mqtt_homeassistant',
                                                               url_prefix=f'/{plugin.id}', template_folder=os.path.dirname(__file__) + '/templates')
        super().__init__(plugin, blueprint=blueprint)

    # pylint: disable=useless-parent-delegation
    def get_nav_items(self) -> List[Dict[Literal['text', 'url', 'sublinks', 'divider'], Union[str, List]]]:
        """
        Generates a list of navigation items for the MQTT Home Assistant plugin UI.
        """
        return super().get_nav_items()

    def get_title(self) -> str:
        """
        Returns the title of the plugin.

        Returns:
            str: The title of the plugin, which is "MQTT Home Assistant".
        """
        return "MQTT Home Assistant"
