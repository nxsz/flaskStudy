import os

from flask import Flask


def create_app(test_config=None):

  #创建和配置应用
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )
  
  if test_config is None:
    #不测试时加载实例配置（如果存在）
    app.config.from_pyfile('config.py', silent=True)
  else:
    #如果传入， 则加载测试配置
    app.config.from_mapping(test_config)

  #确保实例文件存在
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  #一页简单的问候语
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  return app