import requests
from cairosvg import svg2png

BADGE_HASHES = dict(
    hypesquad_brilliance="ec8e92568a7c8f19a052ef42f862ff18",
    hypesquad_bravery="efcc751513ec434ea4275ecda4f61136",
    hypesquad_balance="9f00b18e292e10fc0ae84ff5332e8b0b",
    hypesquad_events="e666a84a7a5ea2abbbfa73adf22e627b",

    staff="48d5bdcffe9e7848067c2e187f1ef951",
    certified_moderator="c981e58b5ea4b7fedd3a643cf0c60564",
    bug_hunter_level_1="8353d89b529e13365c415aef08d1d1f4",
    bug_hunter_level_2="f599063762165e0d23e8b11b684765a8",
    early_verified_developer="4441e07fe0f46b3cb41b79366236fca6",
    early_supporter="b802e9af134ff492276d94220e36ec5c",
    nitro="24d05f3b46a110e538674edbac0db4cd",
    partnered_server_owner="34306011e46e87f8ef25f3415d3b99ca",

    boosting_1_months="ca18353be0e57a2b3b3132fa1c08d6b4",
    boosting_2_months="22f99ed6e34eaca48950254c70f8fe8d",
    boosting_3_months="4a2618502278029ce88adeea179ed435",
    boosting_6_months="fbafa6adb7c49a6a2c3822521ff2af2f",
    boosting_9_months="0599f90e32c15b532647163edd72f70a",
    boosting_12_months="e07c08cdc72bcc78b69c76d2c7ceb344",
    boosting_15_months="c7f26927db5e7806790f4e968038630a",
    boosting_18_months="c6d88d1d12afe03bdc4ebb747f8d196b",
    boosting_24_months="d96ed283b74de75692487b7499fb8d09"
)

for name, hash in BADGE_HASHES.items():
    resp = requests.get(f"https://discord.com/assets/{hash}.svg")
    raw_svg = resp.text

    with open(f"SVG/{name}.svg", "w") as f:
        f.write(raw_svg)

    svg2png(bytestring=raw_svg, write_to=f"PNG/{name}.png", output_width=128, output_height=128)

    

