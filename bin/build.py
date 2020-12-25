from staticjinja import make_site
import json


if __name__ == "__main__":

    site = make_site(
        searchpath="/app/src/templates",
        outpath="/app/",
        env_globals=json.load(open('/app/src/data.json')),
    )

    # enable automatic reloading
    site.render(use_reloader=True)
