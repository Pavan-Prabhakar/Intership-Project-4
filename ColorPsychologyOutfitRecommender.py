def get_user_mood():
    print("Welcome to the Color Psychology Outfit Recommender!")
    print("How are you feeling today?")
    print("Options: happy, sad, angry, stressed, relaxed, energetic, serious, caring")
    mood = input("Enter your mood: ").strip().lower()
    return mood


def recommend_color(mood):
    mood_dict = {
        "happy": "yellow",
        "sad": "green",
        "angry": "black",
        "stressed": "blue",
        "relaxed": "green",
        "energetic": "red",
        "serious": "black",
        "caring": "pink"
    }
    return mood_dict.get(mood, None)


def suggest_outfit(color):
    outfit_dict = {
        "red": "red jacket or red sneakers",
        "blue": "blue denim jeans or blue hoodie",
        "yellow": "yellow t-shirt or yellow sundress",
        "green": "green sweater or green casual shirt",
        "black": "black blazer or black dress",
        "pink": "pink blouse or pink skirt"
    }
    return outfit_dict.get(color, "a stylish outfit in your favorite color")


def main():
    mood = get_user_mood()
    color = recommend_color(mood)

    if color:
        outfit = suggest_outfit(color)
        print(f"\nBased on your mood ({mood}), we recommend wearing {color.upper()}.")
        print(f"Suggested outfit: {outfit}.")
    else:
        print("\nSorry, we couldn't recognize your mood. Please try again with a valid mood.")


if __name__ == "__main__":
    main()
