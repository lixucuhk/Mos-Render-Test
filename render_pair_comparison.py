#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("pair_comparison.html.jinja2")

    html = template.render(
        page_title="語者判別實驗表單 1",
        form_url="http://localhost:8888",
        form_id=1,
        questions=[
            {
                "title": "Group１- Audio1",
                "audio_paths": [
                    "audios/2/JTAN_sing_15-chunk-11_ADIZ_18_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q2"
            },
            {
                "title": "Group１- Audio2",
                "audio_paths": [
                    "audios/12/ADIZ_18.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q0"
            },
            {
                "title": "Group１- Audio3",
                "audio_paths": [
                    "audios/3/NJAT_sing_15-chunk-20_ADIZ_18_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q3"
            },
            {
                "title": "Group１- Audio4",
                "audio_paths": [
                    "audios/4/JTAN_sing_15-chunk-11_ADIZ_18_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q4"
            },
            {
                "title": "Group１- Audio5",
                "audio_paths": [
                    "audios/5/NJAT_sing_15-chunk-20_ADIZ_18_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q5"
            },
            {
                "title": "Group１- Audio6",
                "audio_paths": [
                    "audios/1/NJAT_sing_15-chunk-20_ADIZ_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ADIZ_sing_01-chunk-05.wav"
                ],
                "name": "g1-q1"
            },
            

            {
                "title": "Group2 - Audio1",
                "audio_paths": [
                    "audios/2/SAMF_sing_13-chunk-01_JLEE_11_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q2"
            },
            {
                "title": "Group2 - Audio2",
                "audio_paths": [
                    "audios/3/JTAN_sing_15-chunk-11_JLEE_11_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q3"
            },
            {
                "title": "Group2 - Audio3",
                "audio_paths": [
                    "audios/4/MPUR_sing_06-chunk-20_JLEE_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q4"
            },
                        {
                "title": "Group2 - Audio4",
                "audio_paths": [
                    "audios/12/JLEE_11.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q0"
            },
            {
                "title": "Group2 - Audio5",
                "audio_paths": [
                    "audios/1/ADIZ_sing_01-chunk-05_JLEE_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q1"
            },
            {
                "title": "Group2- Audio6",
                "audio_paths": [
                    "audios/5/MCUR_sing_04-chunk-00_JLEE_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/JLEE_sing_08-chunk-17.wav"
                ],
                "name": "g2-q5"
            },

            {
                "title": "Group3 - Audio1",
                "audio_paths": [
                    "audios/3/ZHIY_sing_14-chunk-10-part-00_JTAN_07_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q3"
            },
            {
                "title": "Group3 - Audio2",
                "audio_paths": [
                    "audios/4/JLEE_sing_08-chunk-17_JTAN_07_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q4"
            },
            {
                "title": "Group3 - Audio3",
                "audio_paths": [
                    "audios/5/JLEE_sing_08-chunk-17_JTAN_07_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q5"
            },
            {
                "title": "Group3 - Audio4",
                "audio_paths": [
                    "audios/12/JTAN_07.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q0"
            },
            {
                "title": "Group3 - Audio5",
                "audio_paths": [
                    "audios/1/MPUR_sing_06-chunk-20_JTAN_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q1"
            },
            {
                "title": "Group3 - Audio6",
                "audio_paths": [
                    "audios/2/NJAT_sing_15-chunk-20_JTAN_07_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/JTAN_sing_15-chunk-11.wav"
                ],
                "name": "g3-q2"
            },

            {
                "title": "Group4 - Audio１",
                "audio_paths": [
                    "audios/12/KENN_10.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q0"
            },
            {
                "title": "Group4 - Audio2",
                "audio_paths": [
                    "audios/1/PMAR_sing_11-chunk-10-part-00_KENN_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q1"
            },
            {
                "title": "Group4 - Audio3",
                "audio_paths": [
                    "audios/2/MPOL_sing_11-chunk-12_KENN_10_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q2"
            },
            {
                "title": "Group4 - Audio4",
                "audio_paths": [
                    "audios/3/NJAT_sing_15-chunk-20_KENN_10_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q3"
            },
            {
                "title": "Group4 - Audio5",
                "audio_paths": [
                    "audios/4/JTAN_sing_15-chunk-11_KENN_10_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q4"
            },
            {
                "title": "Group4 - Audio6",
                "audio_paths": [
                    "audios/5/NJAT_sing_15-chunk-20_KENN_10_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/KENN_sing_17-chunk-15-part-00.wav"
                ],
                "name": "g4-q5"
            },

            {
                "title": "Group5 - Audio1",
                "audio_paths": [
                    "audios/2/VKOW_sing_19-chunk-24_MCUR_17_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q2"
            },
            {
                "title": "Group5 - Audio2",
                "audio_paths": [
                    "audios/3/VKOW_sing_19-chunk-24_MCUR_17_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q3"
            },
                        {
                "title": "Group5 - Audio3",
                "audio_paths": [
                    "audios/12/MCUR_17.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q0"
            },
            {
                "title": "Group5 - Audio4",
                "audio_paths": [
                    "audios/1/JLEE_sing_08-chunk-17_MCUR_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q1"
            },
            {
                "title": "Group5 - Audio5",
                "audio_paths": [
                    "audios/4/KENN_sing_17-chunk-15-part-00_MCUR_17_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q4"
            },
            {
                "title": "Group5 - Audio6",
                "audio_paths": [
                    "audios/5/PMAR_sing_11-chunk-10-part-00_MCUR_17_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MCUR_sing_04-chunk-00.wav"
                ],
                "name": "g5-q5"
            },

            {
                "title": "Group6 - Audio1",
                "audio_paths": [
                    "audios/1/KENN_sing_17-chunk-15-part-00_MPOL_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q1"
            },
            {
                "title": "Group6 - Audio2",
                "audio_paths": [
                    "audios/4/ADIZ_sing_01-chunk-05_MPOL_20_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q4"
            },
            {
                "title": "Group6 - Audio3",
                "audio_paths": [
                    "audios/5/NJAT_sing_15-chunk-20_MPOL_20_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q5"
            },
            {
                "title": "Group6 - Audio4",
                "audio_paths": [
                    "audios/12/MPOL_20.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q0"
            },
            {
                "title": "Group6 - Audio5",
                "audio_paths": [
                    "audios/2/MCUR_sing_04-chunk-00_MPOL_20_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q2"
            },
            {
                "title": "Group6 - Audio6",
                "audio_paths": [
                    "audios/3/ADIZ_sing_01-chunk-05_MPOL_20_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPOL_sing_11-chunk-12.wav"
                ],
                "name": "g6-q3"
            },

            {
                "title": "Group7 - Audio1",
                "audio_paths": [
                    "audios/1/SAMF_sing_13-chunk-01_MPUR_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q1"
            },
            {
                "title": "Group7 - Audio2",
                "audio_paths": [
                    "audios/2/PMAR_sing_11-chunk-10-part-00_MPUR_02_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q2"
            },
            {
                "title": "Group7 - Audio3",
                "audio_paths": [
                    "audios/12/MPUR_02.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q0"
            },
            {
                "title": "Group7 - Audio4",
                "audio_paths": [
                    "audios/3/JLEE_sing_08-chunk-17_MPUR_02_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q3"
            },
            {
                "title": "Group7 - Audio5",
                "audio_paths": [
                    "audios/5/PMAR_sing_11-chunk-10-part-00_MPUR_02_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q5"
            },
            {
                "title": "Group7 - Audio6",
                "audio_paths": [
                    "audios/4/PMAR_sing_11-chunk-10-part-00_MPUR_02_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/MPUR_sing_06-chunk-20.wav"
                ],
                "name": "g7-q4"
            },

            {
                "title": "Group8 - Audio1",
                "audio_paths": [
                    "audios/4/SAMF_sing_13-chunk-01_NJAT_16_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q4"
            },
            {
                "title": "Group8 - Audio2",
                "audio_paths": [
                    "audios/1/JTAN_sing_15-chunk-11_NJAT_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q1"
            },
            {
                "title": "Group8- Audio3",
                "audio_paths": [
                    "audios/2/PMAR_sing_11-chunk-10-part-00_NJAT_16_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q2"
            },
            {
                "title": "Group8 - Audio4",
                "audio_paths": [
                    "audios/12/NJAT_16.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q0"
            },
            {
                "title": "Group8 - Audio5",
                "audio_paths": [
                    "audios/3/ZHIY_sing_14-chunk-10-part-00_NJAT_16_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q3"
            },
            {
                "title": "Group8 - Audio6",
                "audio_paths": [
                    "audios/5/JTAN_sing_15-chunk-11_NJAT_16_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/NJAT_sing_15-chunk-20.wav"
                ],
                "name": "g8-q5"
            },

            {
                "title": "Group9 - Audio1",
                "audio_paths": [
                    "audios/1/MPUR_sing_06-chunk-20_PMAR_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q1"
            },
            {
                "title": "Group9 - Audio2",
                "audio_paths": [
                    "audios/12/PAMR_15.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q0"
            },
            {
                "title": "Group9 - Audio3",
                "audio_paths": [
                    "audios/2/NJAT_sing_15-chunk-20_PAMR_15_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q2"
            },
            {
                "title": "Group9 - Audio4",
                "audio_paths": [
                    "audios/4/KENN_sing_17-chunk-15-part-00_PAMR_15_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q4"
            },
            {
                "title": "Group9 - Audio5",
                "audio_paths": [
                    "audios/5/VKOW_sing_19-chunk-24_PAMR_15_f0factor1.8_ldfactor0.0.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q5"
            },
            {
                "title": "Group9 - Audio6",
                "audio_paths": [
                    "audios/3/MPOL_sing_11-chunk-12_PAMR_15_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/PMAR_sing_11-chunk-10-part-00.wav"
                ],
                "name": "g9-q3"
            },

            {
                "title": "Group10 - Audio1",
                "audio_paths": [
                    "audios/2/KENN_sing_17-chunk-15-part-00_SAMF_13_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q2"
            },
            {
                "title": "Group10 - Audio2",
                "audio_paths": [
                    "audios/5/MCUR_sing_04-chunk-00_SAMF_13_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q5"
            },
            {
                "title": "Group10 - Audio3",
                "audio_paths": [
                    "audios/12/SAMF_13.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q0"
            },
            {
                "title": "Group10 - Audio4",
                "audio_paths": [
                    "audios/1/PMAR_sing_11-chunk-10-part-00_SAMF_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q1"
            },
            {
                "title": "Group10 - Audio5",
                "audio_paths": [
                    "audios/3/NJAT_sing_15-chunk-20_SAMF_13_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q3"
            },
            {
                "title": "Group10 - Audio6",
                "audio_paths": [
                    "audios/4/ADIZ_sing_01-chunk-05_SAMF_13_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/SAMF_sing_13-chunk-01.wav"
                ],
                "name": "g10-q4"
            },

            {
                "title": "Group11 - Audio1",
                "audio_paths": [
                    "audios/3/PMAR_sing_11-chunk-10-part-00_VKOW_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q3"
            },
            {
                "title": "Group11 - Audio2",
                "audio_paths": [
                    "audios/4/MPUR_sing_06-chunk-20_VKOW_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q4"
            },
            {
                "title": "Group11 - Audio3",
                "audio_paths": [
                    "audios/5/MPOL_sing_11-chunk-12_VKOW_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q5"
            },
            {
                "title": "Group11 - Audio4",
                "audio_paths": [
                    "audios/12/VKOW_11.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q0"
            },
            {
                "title": "Group11 - Audio5",
                "audio_paths": [
                    "audios/1/MPOL_sing_11-chunk-12_VKOW_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q1"
            },
            {
                "title": "Group11 - Audio6",
                "audio_paths": [
                    "audios/2/MPOL_sing_11-chunk-12_VKOW_11_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/VKOW_sing_19-chunk-24.wav"
                ],
                "name": "g11-q2"
            },

            {
                "title": "Group12 - Audio1",
                "audio_paths": [
                    "audios/12/ZHIY_03.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q0"
            },
            {
                "title": "Group12 - Audio2",
                "audio_paths": [
                    "audios/3/JTAN_sing_15-chunk-11_ZHIY_03_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q3"
            },
            {
                "title": "Group12 - Audio3",
                "audio_paths": [
                    "audios/4/JLEE_sing_08-chunk-17_ZHIY_03_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q4"
            },
            {
                "title": "Group12 - Audio4",
                "audio_paths": [
                    "audios/1/KENN_sing_17-chunk-15-part-00_ZHIY_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q1"
            },
            {
                "title": "Group12 - Audio5",
                "audio_paths": [
                    "audios/2/VKOW_sing_19-chunk-24_ZHIY_03_f0factor1.0_ldfactor0.0.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q2"
            },
            {
                "title": "Group12 - Audio6",
                "audio_paths": [
                    "audios/5/MCUR_sing_04-chunk-00_ZHIY_03_f0factor0.6_ldfactor0.0.wav",
                    "audios/0/ZHIY_sing_14-chunk-10-part-00.wav"
                ],
                "name": "g12-q5"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
