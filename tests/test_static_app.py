import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "mission-control-prompt-library.html"


class StaticAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = HTML_PATH.read_text(encoding="utf-8")
        cls.head = cls.html.partition("</head>")[0]

    def test_runtime_assets_are_local(self) -> None:
        remote_assets = re.findall(
            r"(?:src|href)=[\"']https?://[^\"']+|@import\s+url\([\"']?https?://",
            self.head,
            flags=re.IGNORECASE,
        )
        self.assertEqual(remote_assets, [])
        self.assertIn('href="assets/tailwind-3.4.17.css"', self.head)
        self.assertTrue((ROOT / "assets" / "tailwind-3.4.17.css").is_file())

    def test_mobile_cards_keep_favorite_control_visible(self) -> None:
        mobile_picker = self.head.partition(
            "/* Mobile prompt-picker mode: prioritize scanning payloads over decorative chrome. */"
        )[2]
        self.assertRegex(
            mobile_picker,
            r"\.prompt-card \.card-body > \.flex:first-child\s*\{\s*"
            r"display: flex !important;",
        )
        self.assertRegex(mobile_picker, r"\.fav-btn\s*\{\s*min-width: 32px;")

    def test_theme_controls_primary_text_color(self) -> None:
        themed_text_rule = re.search(
            r"body\[data-theme-palette\] \.hero-title,[\s\S]+?"
            r"\{\s*color: var\(--tear-text\);\s*\}",
            self.head,
        )
        self.assertIsNotNone(themed_text_rule)
        self.assertIn(
            "body[data-theme-palette] .text-zinc-100",
            themed_text_rule.group(0),
        )


if __name__ == "__main__":
    unittest.main()
