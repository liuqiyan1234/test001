import logging
from logging import handlers
import  os
# 框架规定的   静态属性、全局变量都保存在一个文件里，方便管理
headers = None
emp_id = None
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 创建初始化日志函数
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    st = logging.StreamHandler()
    # 作用是自动根据当前执行的py目录，定位到项目工程目录   也就是父目录
    filename = BASE_DIR+"/log/irhm.log"
    # ,interval=5  代表两次运行的时间间隔5秒以上打印日志
    fh = logging.handlers.TimedRotatingFileHandler(filename=filename,when='S',interval=5,backupCount=3,encoding="utf-8")
    fmt = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    fh.setFormatter(fmt)
    st.setFormatter(fmt)
    logger.addHandler(st)
    logger.addHandler(fh)
