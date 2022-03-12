FROM registry.cn-hangzhou.aliyuncs.com/yyqq188/docker-python:latest
MAINTAINER yanghualei_1012@163.com
COPY download.py /
COPY upload.py /
COPY exec.sh /
COPY install.sh /
RUN chmod u+x /exec.sh
RUN /install.sh
ENV PATH /root/miniconda3/bin:$PATH