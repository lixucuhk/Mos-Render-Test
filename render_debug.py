#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS 實驗表單 1",
        form_url="https://script.google.com/macros/s/AKfycbxTl5y0iFZ-PeE7n72ymIvikU3aHdHs0Xbsi1lJqIADHcJcEytzUyA2ZjcuX1HfygIU/exec",
        form_id=1,
        questions=[
            {
                "title": "Group１- Audio1",
                "audio_path": "audios/2/JTAN_sing_15-chunk-11_ADIZ_18_f0factor1.8_ldfactor0.0.wav",
                "name": "g1-q1"
            },
            {
                "title": "Group１- Audio2",
                "audio_path": "audios/3/NJAT_sing_15-chunk-20_ADIZ_18_f0factor1.0_ldfactor0.0.wav",
                "name": "g1-q0"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
