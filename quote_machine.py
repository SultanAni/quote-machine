#!/usr/bin/env python3
"""Quote Machine — a tiny CLI that prints a random quote to brighten your day."""

import argparse
import random
import textwrap

# ANSI color codes (work in most modern terminals)
COLORS = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[93m", "\033[91m"]
RESET = "\033[0m"
BOLD = "\033[1m"

QUOTES = {
    "inspiration": [
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
        ("It always seems impossible until it's done.", "Nelson Mandela"),
        ("The future belongs to those who believe in their dreams.", "Eleanor Roosevelt"),
    ],
    "funny": [
        ("I'm not lazy, I'm on energy-saving mode.", "Anonymous"),
        ("I used to think I was indecisive, but now I'm not so sure.", "Anonymous"),
        ("My bed is a magical place where I suddenly remember everything I forgot.", "Anonymous"),
        ("I put the 'pro' in procrastinate.", "Anonymous"),
    ],
    "code": [
        ("Talk is cheap. Show me the code.", "Linus Torvalds"),
        ("First, solve the problem. Then, write the code.", "John Johnson"),
        ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
        ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ],
}


def pick_quote(category=None):
    if category and category in QUOTES:
        pool = QUOTES[category]
    else:
        pool = [q for quotes in QUOTES.values() for q in quotes]
    return random.choice(pool)


def render(quote, author):
    color = random.choice(COLORS)
    wrapped = textwrap.fill(f'"{quote}"', width=60)
    print()
    print(f"{color}{BOLD}{wrapped}{RESET}")
    print(f"{color}   — {author}{RESET}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Print a random quote.")
    parser.add_argument(
        "-c", "--category",
        choices=list(QUOTES.keys()),
        help="Pick a category: inspiration, funny, or code.",
    )
    parser.add_argument(
        "-n", "--number", type=int, default=1,
        help="How many quotes to print (default: 1).",
    )
    args = parser.parse_args()

    for _ in range(max(1, args.number)):
        quote, author = pick_quote(args.category)
        render(quote, author)


if __name__ == "__main__":
    main()
