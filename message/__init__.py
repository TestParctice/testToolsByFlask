from flask import Blueprint

app_message = Blueprint('message', __name__,
                        static_url_path='./static',  # 访问静态资源的url前缀，默认值是当前包下的static
                        static_folder='/message/static',  # 静态文件的目录，默认是message/static
                        template_folder='./template'  # 模板文件的目录，默认是当前包下的template
                        )

from .views import get_message
