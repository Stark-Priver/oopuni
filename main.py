#!/usr/bin/env python3
"""
OOP UNI: The Journey Through MUST
A Story-Driven Educational Adventure Game for Learning Object-Oriented Programming

Copyright (c) 2026 Mbeya University of Science and Technology
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.engine.game import Game


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\nThanks for playing OOP UNI!")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
