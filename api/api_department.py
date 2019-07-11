import api


class ApiDep(object):

    def __init__(self, session):
        self.session = session

    # 查询所有学院
    def api_get_all_dep(self):
        return self.session.get(api.url_department)

    # 查询指定学院
    def api_get_one_dep(self, dep_id):
        return self.session.get(api.url_department + dep_id + "/")

    # 新增学院
    def api_post_dep(self, data):
        return self.session.post(api.url_department, json=data)

    # 更新学院
    def api_put_dep(self, dep_id, data):
        return self.session.put(api.url_department + dep_id + "/", json=data)

    # 删除指定学院
    def api_delete_dep(self, dep_id):
        return self.session.delete(api.url_department + dep_id + "/")
