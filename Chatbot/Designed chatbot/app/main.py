import sys
import os

# Add the parent directory to sys.path so 'ui' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.splash_screen import open_splash

if __name__ == "__main__":
    open_splash()