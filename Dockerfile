FROM python:3.8.10

ARG ImgHost=pypi.tuna.tsinghua.edu.cn

RUN mkdir -p /opt/deployments/coder

COPY ./requirements.txt /opt/deployments

RUN pip install --trusted-host=${ImgHost} --no-cache -r /opt/deployments/requirements.txt \
    -i https://${ImgHost}/simple

COPY ./coder /opt/deployments/coder

WORKDIR /opt/deployments/

ENV TZ=Asia/Shanghai

CMD ["uwsgi", "--ini", "coder/deploy/uwsgi.ini"]
