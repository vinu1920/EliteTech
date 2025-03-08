import random

random.randint(0,100)

# Lists of possible story elements
characters = ["a brave knight", "a clever detective", "a mischievous cat", "an adventurous astronaut",
              "a wise old wizard"]
settings = ["a haunted castle", "a distant planet", "a bustling city", "a hidden underground cave", "a magical forest"]
conflicts = ["had to solve a mysterious disappearance", "discovered a hidden treasure map", "was chased by a dragon",
             "found a secret passage", "got lost in a maze"]
outcomes = ["and became a hero of the land.", "but accidentally triggered a trap!", "and made a new unexpected friend.",
            "only to realize it was all a dream!", "and uncovered an ancient secret."]


def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    outcome = random.choice(outcomes)

    story = f"One day, {character} found themselves in {setting}. They {conflict} {outcome}"
    return story


# Generate and print a random story
if __name__ == "__main__":
    print(generate_story())
