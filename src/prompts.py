def calculate_min_max_section_count(char_length: int) -> tuple[int, int]:
    min_sections = max(int(char_length / 1000), 1)
    max_sections = max(int(char_length / 500), min_sections + 1)
    return min_sections, max_sections


def build_summary_request_prompt(text: str, max_length: int):
    min_sections, max_sections = calculate_min_max_section_count(max_length)
    return [
    {
        "role": "system",
        "content": ("You provide accurate information based on the input text. "
        "You preverve the style text based on the topic and tone of the input text. "
        "You skip any unrelevant parts such as advertisement or autopromotion."
    )
    },
    {
        "role": "user",
        "content": (
            "Summerize the input and be precise and on-point using at most"
            f"{max_length} characters. Skip any advertisement."
            f"Start with short numbered list of {str(min_sections)}-{str(max_sections)} main topics "
            "and after that provide more context for each topic in a visually separated section.\n\n"
            "Text: \"\"\" {text} \"\"\""
        )
                    },
]

