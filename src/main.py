from bigjpg import (
    Bigjpg,
    noices,
    styles,
    enlarge_values,
)
from urllib.request import urlretrieve
import pathutil
import time
import os

from config import CONFIG_JSON_FILE_PATH
from utils import json_file
from cli import CLI

from models.app_config import AppConfig

APP_CONFIG = AppConfig(**json_file.read(CONFIG_JSON_FILE_PATH))
OUT_DIR = "./.tmp"

def enlarge_dragon_image(image_url: str):
    bigjpg_api_token = APP_CONFIG.bigjpg.api_token
    enlarger = Bigjpg(bigjpg_api_token)

    image_info = enlarger.enlarge(
        styles.Art,
        noices._None,
        enlarge_values._4x,
        image_url
    )

    return image_info

def main():
    img_name = CLI.input_str("Dragon image name")
    phase = CLI.input_int("Dragon phase", 0, 3)
    skin = CLI.input_int("Dragon skin", 0, 5)
    use_2x_img = CLI.input_yes_no("Want to use 2x image")
    enlarge_image = CLI.input_yes_no("Want to enlarge the image")

    if skin:
        skin = f"_skin{skin}"
        phase = 3

    else:
        skin = ""

    if use_2x_img:
        image_url = f"https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/ui_{img_name}{skin}_{phase}@2x.png"
    
    else:
        image_url = f"https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/ui_{img_name}{skin}_{phase}.png"

    CLI.log(f"Original image URL: {image_url}")

    if enlarge_image:
        try:
            image_info = enlarge_dragon_image(image_url)
        except:
            CLI.error("Error trying to process the image! Trying to download the original...")

            try:
                filename = f"ui_{img_name}{skin}_{phase}_original.png"
                out_path = f"{OUT_DIR}/{filename}"

                if not os.path.exists(OUT_DIR):
                    pathutil.mktree(OUT_DIR)

                urlretrieve(image_url, out_path)

            except:
                CLI.error("Error trying to download the original image! Restarting session in 2 seconds")
                time.sleep(2)
                return main()

        filename = f"ui_{img_name}{skin}_{phase}_enlarged.png"
        out_path = f"{OUT_DIR}/{filename}"

        if not os.path.exists(OUT_DIR):
            pathutil.mktree(OUT_DIR)

        CLI.log("Downloading enlarged image of the dragon...")
        image_info.download(out_path)

    else:
        try:
            filename = f"ui_{img_name}{skin}_{phase}_original.png"
            out_path = f"{OUT_DIR}/{filename}"

            if not os.path.exists(OUT_DIR):
                pathutil.mktree(OUT_DIR)

            urlretrieve(image_url, out_path)

        except:
            CLI.error("Error trying to download the original image! Restarting session in 2 seconds")
            time.sleep(2)
            return main()

    return main()

if __name__ == "__main__":
    main()