# backend/tools/__init__.py

import pkgutil
import importlib

TOOLS = {}

for loader, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")

    if hasattr(module, "main"):
        TOOLS[module_name] = module
