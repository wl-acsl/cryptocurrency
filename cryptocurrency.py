import argparse
import requests
import json
from flask import Flask

node = Flask(__name__)
parser = argparse.ArgumentParser()
