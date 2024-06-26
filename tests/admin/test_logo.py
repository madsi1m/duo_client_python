import json
from .base import TestAdmin
import os
import base64
import urllib.parse


class TestLogo(TestAdmin):

    def test_update_logo(self):
        # Get an image to upload:
        logo_path = os.path.join(self.TEST_RESOURCES_DIR, "barn-owl-small.png")
        with open(logo_path, "rb") as image_file:
            logo_file = image_file.read()

            # Call function in client:
            response = self.client.update_logo(logo_file)

            # Prep validation text:
            base64_logo = base64.b64encode(logo_file)
            base64_logo = urllib.parse.quote_plus(base64_logo)

            # Validate response:
            self.assertTrue(
                json.loads(response['body']).get('logo'),
                base64_logo
            )
