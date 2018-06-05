import json
import os
import subprocess
import sys

import requests
from PIL import Image

import secrets

image_size = 600
job_num = 5
url = 'https://mdma.vis.one'
base_folder = '/root/universal-style-transfer-pytorch'


def download_image(url, path):
    print('downloading...', url)
    media_res = requests.get(url)
    if not media_res.ok:
        raise Exception(media_res.status_code)
    with open(path, 'wb') as f:
        f.write(media_res.content)


def process_job(index, job):
    input_image_url = job['fields']['input_image']
    input_image_path = f"{base_folder}/images/content/in{str(index)}.jpg"
    download_image(input_image_url, input_image_path)

    style_image_url = job['fields']['style_image']
    style_image_path = f"{base_folder}/images/style/in{str(index)}.jpg"

    download_image(style_image_url, style_image_path)


def clean_folder(path):
    for file in os.scandir(path):
        os.unlink(file.path)


def upload_image(output_image_path, job_id):
    files = {'file': (output_image_path, open(output_image_path, 'rb'))}
    r = requests.post(url + '/upload_finished_job/' + str(job_id) + '/',
                      files=files, auth=(secrets.username, secrets.password))
    return r.status_code


def main():
    res_jobs = requests.get(url + '/get_jobs?num=' + str(job_num),
                            auth=(secrets.username, secrets.password))

    print(res_jobs.status_code)

    if not res_jobs.ok:
        sys.exit(1)

    res_jobs_json = res_jobs.json()

    jobs = json.loads(res_jobs_json['jobs'])
    print(jobs)

    if len(jobs) == 0:
        print('no jobs, thanks Obama!')
        sys.exit(0)

    clean_folder(f'{base_folder}/images/content/')
    clean_folder(f'{base_folder}/images/style/')
    clean_folder(f'{base_folder}/samples/')

    for i, j in enumerate(jobs):
        process_job(i, j)

    # subprocess.Popen("cd {base_folder} && python WCT.py")
    finished_proc = subprocess.run(
        f"cd {base_folder} && /usr/local/bin/pipenv run python WCT.py --fineSize {image_size}", shell=True, check=True,)
    if finished_proc.stdout != None:
        print(finished_proc.stdout)
    if finished_proc.stderr != None:
        print(finished_proc.stderr)
    if finished_proc.returncode != 0:
        sys.exit(1)

    for i, j in enumerate(jobs):
        output_image_path = f"{base_folder}/samples/in{str(i)}.jpg"

        status_code = upload_image(output_image_path, j['pk'])
        print(status_code)


if __name__ == '__main__':
    main()
