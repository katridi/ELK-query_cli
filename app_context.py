from typing import Dict
import json

from elasticsearch import Elasticsearch


class AppContext:
    __INDEX_PATH = 'index.json'

    def __init__(self, es: Elasticsearch) -> None:
        self.es = es
        self._check_connection()
        self.set_index(index_name=self._read_index_name())

    def search_in_index(self, body: Dict) -> Dict:
        return self.es.search(index=self.index, body=body)


    def set_index(self, index_name: str) -> None:
        if self.es.indices.exists(index=index_name):
            self._write_index_name(index_name=index_name)
            self.index = index_name
            print(f"Index set to {self.index}\n")
        else:
            raise ValueError(f"Index '{index_name}' doesn't exist.\n")


    def _check_connection(self) -> None:
        if not self.es.ping():
            raise ValueError(f"Connection failed to {self.es}")

    def _read_index_name(self) -> str:
        with open(self.__INDEX_PATH, 'r') as f:
            return json.load(f)['index']

    def _write_index_name(self, index_name: str):
        with open(self.__INDEX_PATH, 'w') as f:
            f.write(json.dumps({"index": index_name}, indent=4, ensure_ascii=False))



def create_es_client() -> Elasticsearch:
    # configure params
    return Elasticsearch(
        hosts=["https://localhost:9200"],
        http_auth=("admin", "admin"),
        verify_certs=False,
        use_ssl=True,
        ssl_show_warn=False
    )


def create_app_context():
    return AppContext(es=create_es_client())
