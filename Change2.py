import json
from py2neo import Graph


class Changer:
    def __init__(self):
        self.g = Graph(
            host="localhost",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="123")

    def check_json(self, input_str):
        try:
            json.loads(input_str)
            return True
        except:
            return False

    def change(self, data):
        #del_data = json.dumps(data, ensure_ascii=False)
        cha_data = data
        cha_links = cha_data['links']
        cha_nodes = cha_data['nodes']
        for k, v in cha_links.items():
            query = "match(p)-[r]->(q) where id(r)=%s SET" % (str(k))
            for kk, vv in v['attrs'].items():
                query += ' p.' + str(kk) + '="' + str(vv) + '",'
            try:
                self.g.run(query.strip(','))
            except Exception as e:
                print(e)

        for k, v in cha_nodes.items():
            query = "match(p) where id(p)=%s SET" % (str(k))
            for kk, vv in v['attrs'].items():
                query += ' p.' + str(kk) + '="' + str(vv) + '",'
            try:
                self.g.run(query.strip(','))
            except Exception as e:
                print(e)

        sess = 'MATCH (n)-[r]->(m) RETURN id(n) as source, labels(n) as source_labels, ' \
               'properties(n) as source_attrs, id(m) as target, labels(m) as target_labels, ' \
               'properties(m) as target_attrs, id(r) as link, type(r) as r_type, properties(r) as r_attrs '
        result = self.g.run(sess)
        nodes = dict()
        links = dict()
        for re in result:
            # print(str(re['source']), re['source_labels'], re['source_attrs'])
            nodes[str(re['source'])] = {'labels': re['source_labels'][0], 'attrs': re['source_attrs']}
            nodes[str(re['target'])] = {'labels': re['target_labels'][0], 'attrs': re['target_attrs']}
            links[str(re['link'])] = {'type': re['r_type'], 'attrs': re['r_attrs'],
                                      'source': str(re['source']), 'target': str(re['target'])}
        data = dict(nodes=nodes, links=links)
        return data


if __name__ == '__main__':
    cg= Changer()
    js = json.loads('{"42709": {"labels": "检修","attrs": {"end_time": "","start_time": "2020-03-03 22:16:00","end_plant_station": "-","department": "铁岭电厂","content": "备用1111","impact": "停机"}}}')
    js2 = json.loads('{}')
    data = dict(nodes=js, links=js2)
    json.dumps(data, ensure_ascii=False)
    cg.change(data)
