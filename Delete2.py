import json
from py2neo import Graph


class Deleter:
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

    def delete(self, data):
        #del_data = json.dumps(data, ensure_ascii=False)
        del_data = data
        print(type(del_data))
        del_nodes = del_data['nodes']
        del_links = del_data['links']
        for k, v in del_links.items():
            query = "match(p)-[r]->(q) where id(r)=%s DELETE r" % (str(k))
            try:
                self.g.run(query)
            except Exception as e:
                print(e)

        for k, v in del_nodes.items():
            query = "match(p) where id(p)=%s DETACH DELETE p" % (str(k))
            try:
                self.g.run(query)
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
    de = Deleter()
    js = json.loads('{"42708": {"labels": "检修2222","attrs": {"end_time": "","start_time": "2019-11-02 00:06:00","end_plant_station": "-","department": "铁岭电厂","content": "备用11111","impact": "停机"}}}')
    js2 = json.loads('{}')
    data = dict(nodes=js, links=js2)
    json.dumps(data, ensure_ascii=False)
    de.delete(data)

