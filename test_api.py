# @describe:本地测试接口调试

import flask
import json
from flask import request

# 通过flask提供的装饰器@server.route()将普通函数转换为服务
# 将当前python文件当作一个服务

server = flask.Flask(__name__)


@server.route('/query1', methods=['get', 'post'])
def search():
    key = request.values.get('key')
    postcode = request.values.get('postcode')
    if key and postcode:
        if key == '1' and postcode == '644000':
            resu = {'error_code': 0, 'reason': 'ok'}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'error_code': 1, 'reason': 'error postcode'}
            return json.dumps(resu, ensure_ascii=False)

    else:
        resu = {'error_code': 2, 'reason': 'error postcode'}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')
