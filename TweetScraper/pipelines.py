from crawlab.utils import save_item_mongo
from crawlab.utils.config import get_task_id
class CustomMongoPipeline(object):
    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict['task_id'] = get_task_id()
        save_item_mongo(item_dict)

        # labeling data dari sini

        return item

