# -*- coding: utf-8 -*-

import json
from flask import url_for
from rmon.models import ServerList


class TestServerList:
    """
    测试Redis服务器列表API
    """
    endpoint = 'api.server_list'

    def test_get_servers(self, server, client):
        """
        获取Redis服务器列表
        """
        resp = client.get(url_for(self.endpoint))

        # RestView 视图基类会设置HTTP头部 Content-Type为json
        assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
        # 访问成功后返回状态码200 OK
        assert resp.status_code == 200

        servers = resp.get_json

        # 由于当前的测试环境中只有一个Redis服务器， 所以返回的数量为1
        assert len(servers) == 1

        h = servers[0]
        assert h['name'] == server.name
        assert h['description'] == server.description
        assert h['host'] == server.host
        assert h['port'] == server.port
        assert 'updated_at' in h
        assert 'created_at' in h

    def test_create_server_success(self, db, client):
        """
        测试创建Redis服务器成功
        """
        pass

    def test_create_server_failed_with_invalid_host(self, db, client):
        """
        无效的服务器地址导致创建Redis服务器失败
        """
        pass

    def test_create_server_failed_with_duplciate_server(self, server, client):
        """
        创建重复的服务器时将失败
        """
        pass
