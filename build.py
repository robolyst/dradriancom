from staticjinja import make_site
import json


if __name__ == "__main__":

    site = make_site(
        searchpath="site/templates",
        outpath="site/",
        env_globals=json.load(open('site/data.json')),
    )

    # enable automatic reloading
    site.render(use_reloader=True)
