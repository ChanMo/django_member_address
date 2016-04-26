基于django_wechat_member的地址模块
=====================================

一个基于 `django_wechat_member <http://github.com/ChanMo/django_wechat_member/>`_ 的地址模块

同时使用了 `input_address <http://github.com/ChanMo/input_address/>`_ 的选址模块


功能说明：
----------

- 每个微信会员有多个地址
- 每个地址包含经纬度信息

快速开始:
---------

安装 *django_wechat_member* :

    `有关django_wechat_member的详细使用说明 <http://github.com/ChanMo/django_wechat_member.git/>`_ 

安装 *django_member_address* :

.. code-block::

    pip install git+https://github.com/ChanMo/django_member_address.git

修改 *settings.py* 文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'address',
        ...
    )

修改 *urls.py* 文件:

.. code-block::

    url(r'^address', include('address.urls')),

更新数据库:

.. code-block::

   python manage.py migrate

用户地址主页:

    http://yourdomain/address/


版本更改:
---------
- v0.1 第一版
