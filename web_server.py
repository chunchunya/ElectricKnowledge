import web
import json
import GetData
import Delete2
import Change2

urls = (
    '/init(.*)', 'init',
    '/Delete(.*)', 'Del',
    '/Change(.*)', 'Cha',
)
app = web.application(urls, globals())

# {queryText: "123", category: 1}
# {data={links, nodes}}

class init:
    def GET(self, type):
        # 设置 hearder
        web.header("Access-Control-Allow-Origin", "*")
        web.header("Content-Type", "application/json")
        # 获取请求参数
        web_data = web.data()
        # 根据请求参数从图数据库获取数据 data
        # data = dict(nodes=[1,2,3,4], links=[dict(source=1, target=4)])
        getAllData = GetData.GetData()
        data1, data2 = getAllData.get_data()
        data = dict(nodes=data1, links=data2)
        # 返回 JSON 串
        # return json.dumps(dict(data=data, msg=type), ensure_ascii=False)

        return json.dumps(data, ensure_ascii=False)


class Del:
    def POST(self, type):
        # 设置 hearder
        web.header("Access-Control-Allow-Origin", "*")
        web.header("Content-Type", "application/json")
        user_data = web.input(del_data='{"nodes":{},"links":{}}')
        del_data = user_data.del_data
        delete = Delete2.Deleter()
        new_data = delete.delete(del_data)
        return json.dumps(new_data, ensure_ascii=False)

class Cha:
    def POST(self, type):
        # 设置 hearder
        web.header("Access-Control-Allow-Origin", "*")
        web.header("Content-Type", "application/json")
        user_data = web.input(cha_data='{"nodes":{},"links":{}}')
        cha_data = user_data.cha_datalashi
        change = Change2.Changer()
        new_data = change.change(cha_data)
        return json.dumps(new_data, ensure_ascii=False)

if __name__ == "__main__":
    app.run()
