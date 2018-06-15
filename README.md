# retrieval-group-test-v0.1
step1: 新建一个图片库

[new-group.py](./new_group.py)

usage: python2 new-group.py --ak access_key --sk secret_key

setp2:上传base库图片，url_list对应上传图片的链接,可以并发上传

[img_upload.py](./img_upload.py)

usage: python2 img_upload.py --ak access_key --sk secret_key --in url_list

step3:搜索图片库中是否有对应链接的图片，不可以并发（程序本身支持并发）

[search-group.py](./search_group.py)

usage: python2 new-group.py --ak access_key --sk secret_key --in url_list

step4:返回现有图片库中的所有图片及其相关信息

[summay-group.py](./summary_group.py)

usage: python2 summay-group.py --ak access_key --sk secret_key

step5:计算以图搜图算法的top5准确

[top5_correct.py](./top5_correct.py)

usage: python2 top5_correct.py --ak access_key --sk secret_key --in json_file
注意对应的关键字

step6:删除库

[delete_group.py](./delete_group.py)

usage: python2 delete_group.py --ak access_key --sk secret_key

[Argus.ImageGroup.md](./Argus.ImageGroup.md)

API文档说明




