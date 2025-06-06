"""
@author: da2el
@title: D2 Nodes
@description: A Collection of Handy Custom Nodes for ComfyUI
"""

import os
import server
from aiohttp import web
from .nodes.modules import util

from .nodes.d2_nodes import NODE_CLASS_MAPPINGS as D2_CLASS_MAPPIGS 
from .nodes.d2_size_nodes import NODE_CLASS_MAPPINGS as D2_SIZE_CLASS_MAPPIGS 
from .nodes.d2_xy_nodes import NODE_CLASS_MAPPINGS as D2_XY_CLASS_MAPPIGS 
from .nodes.d2_refiner_nodes import NODE_CLASS_MAPPINGS as D2_REFINER_CLASS_MAPPIGS 
from .nodes.d2_merge_nodes import NODE_CLASS_MAPPINGS as D2_MERGE_CLASS_MAPPIGS 
from .nodes.d2_text_nodes import NODE_CLASS_MAPPINGS as D2_TEXT_CLASS_MAPPIGS 
from .nodes.d2_image_nodes import NODE_CLASS_MAPPINGS as D2_IMAGE_CLASS_MAPPIGS 

WEB_DIRECTORY = "./web"
NODE_CLASS_MAPPINGS = {
    **D2_CLASS_MAPPIGS,
    **D2_SIZE_CLASS_MAPPIGS,
    **D2_XY_CLASS_MAPPIGS,
    **D2_REFINER_CLASS_MAPPIGS,
    **D2_MERGE_CLASS_MAPPIGS,
    **D2_TEXT_CLASS_MAPPIGS,
    **D2_IMAGE_CLASS_MAPPIGS
}
NODE_DISPLAY_NAME_MAPPINGS = []

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]


# css読み取り用のパスを設定
if os.path.exists(util.D2_WEB_PATH):
    server.PromptServer.instance.app.add_routes([
        web.static("/D2/assets/", str(util.D2_WEB_PATH))
    ])

