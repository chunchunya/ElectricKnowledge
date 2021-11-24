import web
import json
import GetData

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

# {queryText: "123", category: 1}
# {data={links, nodes}}


class hello:
    def GET(self, type):
        # 设置 hearder
        web.header("Access-Control-Allow-Origin", "*")
        web.header("Content-Type", "application/json")
        # 获取请求参数
        web_data = web.data()
        # 根据请求参数从图数据库获取数据 data
        # data = dict(nodes=[1,2,3,4], links=[dict(source=1, target=4)])
        getAllData = GetData.GetData()
        data1,data2 = getAllData.get_data()
        data = dict(nodes=data1, links=data2)
        # 返回 JSON 串
        # return json.dumps(dict(data=data, msg=type), ensure_ascii=False)

        return json.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
    app.run()
