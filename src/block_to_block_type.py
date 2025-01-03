def block_to_block_type(markdown):
    # Check for Heading
    if markdown.startswith("# "):
        return "heading"
    if markdown.startswith("## "):
        return "heading"
    if markdown.startswith("### "):
        return "heading"
    if markdown.startswith("#### "):
        return "heading"
    if markdown.startswith("##### "):
        return "heading"
    if markdown.startswith("###### "):
        return "heading"

    # Check for Code Block
    if markdown.startswith("```") and markdown.endswith("```"):
        return "code"

    # Check for Quote
    if all(line.startswith(">") for line in markdown.split("\n")):
        return "quote"

    # Check for Unordered List
    if all(line.startswith(("* ", "- ")) for line in markdown.split("\n")):
        return "unordered_list"

    # Check for Ordered List
    lines = markdown.split("\n")
    if all(
        line.startswith(f"{i+1}. ")
        for i, line in enumerate(lines)
    ):
        return "ordered_list"

    # Default to Paragraph
    return "paragraph"
