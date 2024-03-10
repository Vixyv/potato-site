class Link:

    """
    This is a class for workink with links.
    """

    def __init__(self, name: str, html_path: str, picture_path: str = None) -> None:
        self.name = name
        self.html_path = html_path
        self.picture_path = picture_path

    # Creates a Link from name and paths without file names.
    def make_from_name(name: str, headless_html_path: str, headless_picture_path: str = None, picture_type: str = "png"):
        return Link(
            name,
            headless_html_path + name + ".html",
            headless_picture_path if headless_picture_path is None else (headless_picture_path + name + "." + picture_type)
        )
    
    # Creates a Link with defaults: page is .html,
    # picture is .png, and they are located in the same forlder
    def make_with_defaults(name: str, headless_path: str, has_picture=True):
        return Link(
            name,
            headless_path + name + ".html",
            (headless_path + name + ".png") if has_picture else None
        )
    
    # def from_html_link(html_link: str):
    #     src_index = html_link.index("src=\"") + 4
    #     href_index = html_link.index("href=\"") + 5

    
    # Creates a Link that can be put into main.html
    def cast_to_html_link(self) -> str:
        return f'''
        <table><tr><th>
        <img src="{self.picture_path}" alt="WhErE ImAgE?" width="200" height="200">
        </th></tr><tr><th>
        <a href="{self.html_path}">{self.name}</a>
        </th></tr></table>
        ''' if self.picture_path is not None else f'''
        <table><tr><th>
        <a href="{self.html_path}">{self.name}</a>
        </th></tr></table>
        '''

    # Allows the Link objects to be nicely represented in the terminal
    def __repr__(self) -> str:
        return f"Link({self.name}, {self.html_path}, {self.picture_path})"
