"""
Initializes the 'game' directory as a Python package.

This file's presence allows Python to recognize the 'game' directory
as a package, enabling the import of its sub-modules (e.g., 'game.core',
'game.assets') by other parts of the application.

No specific modules or functions are actively exposed at the top-level
'game' package upon import by this __init__.py.
"""
# This file is intentionally left mostly empty, serving primarily
# as a package marker for the 'game' directory.

# Example of how you might expose sub-modules or their contents
# directly under the 'game' package if needed:
# from . import core
# from .core import GameEngine

# Or specifically expose certain functions/classes:
# from .assets.loader import load_asset