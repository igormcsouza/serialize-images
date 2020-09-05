import os


def run_tests():
    os.system('pytest -v --cov=serialize_images')

def open_web_coverage():
    os.system('coverage html')
    os.system(f"chrome {os.path.join('htmlcov', 'index.html')}")