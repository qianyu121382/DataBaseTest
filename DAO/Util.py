import json


# 负责格式化输出  父类
class ModelExt(object):

    def __repr__(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return json.dumps(fields)
