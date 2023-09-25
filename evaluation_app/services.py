import csv
import json
import os
import subprocess
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

