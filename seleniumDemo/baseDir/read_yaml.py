import yaml


class ReadYaml():
    def read(self, filename: str):
        fil = './data/'+filename
        with open(fil, 'r', encoding='utf8') as f:
            list1 = yaml.safe_load(f)
            return list1


