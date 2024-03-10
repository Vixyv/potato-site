from Link import Link


"""
This code lets you semiautomatically add
new entries into the main file
wow
"""

main_file = "index.html"
html_file_buffer = ["", "", ""]


# Returns the input object back. Returns None if it is identified as False
def false_like_to_none(obj):
    return obj if obj else None


def add_link_to_beginning(link: Link):

    with open(main_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_file_buffer[0])
        html_file.write(link.cast_to_html_link())
        html_file.write(html_file_buffer[1])
        html_file.write(html_file_buffer[2])


def add_link_to_end(link: Link):

    with open(main_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_file_buffer[0])
        html_file.write(html_file_buffer[1])
        html_file.write(link.cast_to_html_link())
        html_file.write(html_file_buffer[2])



# Reads data from the main.html
with open(main_file, "r", encoding="utf-8") as html_file:

    # defines where the new lines are added
    operating_mode = 0

    for line in html_file:

        html_file_buffer[operating_mode] += line

        if ("<!-- LINK BEGINNING TAG DO NOT REMOVE -->" in line or
                  "<!-- LINK END TAG DO NOT REMOVE -->" in line): operating_mode += 1
        

while True:

    constructor_type = input("Enter constructor type\n(full/fl, from name/fn, defaults/d. Empty for exit): ")

    match constructor_type:

        case "full" | "fl":
            link = Link(
                input("Enter link name: "),
                input("Enter path to html file (with file): "),
                false_like_to_none(
                    input("Enter path to picture (with file). Leave empty for no picture: ")
                )
            )

        case "from name" | "fn":
            link = Link.make_from_name(
                input("Enter link name"),
                input("Enter path to html file (with file): "),
                false_like_to_none(
                    input("Enter path to picture (with file). Leave empty for no picture: ")
                )
            )

        case "defaults" | "d":
            link = Link.make_with_defaults(
                input("Enter the link name: "),
                input("Enter the path w/o file name: "),
                not (input("Have picture? [Y/n] ") == "n")
            )

        case "":
            break

        case _:
            # Default
            print(f"Unrecognized constructor type: {constructor_type}")
            continue

    add_link_to_beginning(link)
