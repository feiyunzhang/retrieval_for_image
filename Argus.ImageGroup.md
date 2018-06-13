<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [API](#api)
  - [/image/group/new](#imagegroupnew)
  - [/image/group/remove](#imagegroupremove)
  - [/image/group/add](#imagegroupadd)
  - [/image/group/delete](#imagegroupdelete)
  - [/image/group](#imagegroup)
  - [/image/group/<id>](#imagegroupid)
  - [/image/group/search](#imagegroupsearch)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# API

| PATH | Note | Input | Response Type |
| :--- | :--- | :--- | :---: |
| [`/v1/image/group/<id>/new`](#/image/group/new) | 新建图片库 | image URI | Json |
| [`/v1/image/group/<id>/remove`](#/image/group/remove) | 删除图片库 | Json | Json |
| [`/v1/image/group/<id>/add`](#/image/group/add) | 图片库添加特征 | image URI | Json |
| [`/v1/image/group/<id>/del`](#/image/group/del) | 图片库删除特征 | Json | Json |
| [`/v1/image/group`](#/image/group) | 显示所有图片库 | GET | Json |
| [`/v1/image/group/<id>`](#/image/group/<id>) | 显示图片库特征 | GET | Json |
| [`/v1/image/group/<id>/search`](#/image/group/search) | 图片库搜索 | image URI | Json |


## /image/group/new

> 新建图片库

Request

```
POST /v1/image/group/<id>/new  Http/1.1
Content-Type: application/json
Authorization: Qiniu <AccessKey>:<Sign>

{
	"data": [
		{
			"uri": "http://xx.com/xxx",
			"attribute": {
				"id": <id>,
				"label": <label>
			}
		},
		{
			"uri": "http://xx.com/xxx",
			"attribute": {
				"id": <id>,
				"label": <label>
			}
		}
	]
}
```

Response

```
200 ok

{
	"images": ["",""...]
}
```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|
|uri|string|图片资源地址|
|attribute.id|string|图片唯一标识，可选|
|label|string|图片标识|


## /image/group/remove

> 删除图片库

Request

```
POST /v1/image/group/<id>/remove  Http/1.1
Authorization: Qiniu <AccessKey>:<Sign>

```

Response

```
200 ok

```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|


## /image/group/add

> 图片库新增特征

Request

```
POST /v1/image/group/<id>/add  Http/1.1
Content-Type: application/json
Authorization: Qiniu <AccessKey>:<Sign>

{
	"data": [
		{
			"uri": "http://xx.com/xxx",
			"attribute": {
				"id": <id>,
				"label": <label>
			}
		},
		{
			"uri": "http://xx.com/xxx",
			"attribute": {
				"id": <id>,
				"label": <label>
			}
		}
	]
}
```

Response

```
200 ok

{
	"images": ["",""...]
}
```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|
|uri|string|图片资源地址|
|attribute.id|string|图片唯一标识，可选|
|label|string|图片标识|


## /image/group/delete

> 删除图片库特征

Request

```
POST /v1/image/group/<id>/delete  Http/1.1
Content-Type: application/json
Authorization: Qiniu <AccessKey>:<Sign>

{
	"images":[
		<image_id>,
		...
	]
}

```

Response

```
200 ok

{
	"code": 0,
	"message": "",
}
```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|
|image_id|string|图片唯一标识|

返回字段说明：

|字段|取值|说明|
|:---|:---|:---|
|code|int|0:表示正确|
|message|string|结果描述信息|


## /image/group

> 显示所有的图片库

Request

```
GET /v1/image/group  Http/1.1
Authorization: Qiniu <AccessKey>:<Sign>

```

Response

```
200 ok

{
	"code": 0,
	"message": "",
	"result": [
		<id>,
		...
	]
}
```
返回字段说明：

|字段|取值|说明|
|:---|:---|:---|
|code|int|0:表示正确|
|message|string|结果描述信息|
|id|string|图片库唯一标识|

## /image/group/<id>

> 显示图片库

Request

```
GET /v1/image/group/<id>  Http/1.1
Authorization: Qiniu <AccessKey>:<Sign>

```

Response

```
200 ok

{
	"code": 0,
	"message": "",
	"result": [
		{
			"id": <id>,
			"value": {
				"label": "xx"
			}
		},
		...
	]
}
```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|

返回字段说明：

|字段|取值|说明|
|:---|:---|:---|
|code|int|0:表示正确|
|message|string|结果描述信息|
|id|string|生成的该图片的唯一标识|
|value.label|string|图片标识|

## /image/group/search

> 图片库搜索

Request

```
POST /v1/image/group/<id>/search Http/1.1
Content-Type: application/json
Authorization: Qiniu <AccessKey>:<Sign>

{
	"data": {
		"uri": "http://xx.com/xxx"
	},
	"params": {
		"limit": 1
	}
}
```

Response

```
200 ok

{
	"code": 0,
	"message": "",
	"result": [
		{
			"label": "xx",
			"score":0.9998
			"uri": "http://xxx/xxx"
		},
		...
	]
}
```
请求字段说明：

|字段|取值|说明|
|:---|:---|:---|
|id|string|图片库的唯一标识|
|uri|string|图片资源地址|
|params.limit|int|匹配图片TOPN，可选，默认为1|

返回字段说明：

|字段|取值|说明|
|:---|:---|:---|
|code|int|0:表示正确|
|message|string|结果描述信息|
|result.uri|string|检索得到的图片地址|
|result.label|string|检索得到的图片标识|
|result.score|float|0~1,检索结果的可信度，1为确定|