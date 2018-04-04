import os
import configparser

# 获取当前脚本所在的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "config.ini")
conf = configparser.ConfigParser()
conf.read(configPath)
smtp_server = conf.get("email", "smtp_server")
mail_sender = conf.get("email", "mail_sender")
mail_psw = conf.get("email", "mail_psw")
mail_receiver = conf.get("email", "mail_receiver")
mail_port = conf.get("email", "mail_port")