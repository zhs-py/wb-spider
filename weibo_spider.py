import requests
import json
import datetime
class weibo_spider():
    def __init__(self):
        self.now_time = datetime.date.today()
        self.day30_time=self.now_time-datetime.timedelta(days=30)
        self.contents = []
        self.weibo(1)
        self.write()
    def weibo(self,page):
        break_num = 0
        url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076032183473425' + '_-_WEIBO_SECOND_PROFILE_WEIBO&page='+str(page)
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; X11)',
        }
        self.res = requests.get(url, headers=header)
        self.json_res = self.res.json()
        if page==1:
            for i in self.json_res['data']['cards'][1:]:
                content = {}
                content['created_at']=i['mblog']['created_at']
                content['text'] = i['mblog']['text']
                #点赞
                content['attitudes_sum'] =i['mblog']['attitudes_count']
                #评论
                content['comments_sum'] = i['mblog']['comments_count']
                #转发
                content['reposts_sum']= i['mblog']['reposts_count']
                #来源
                content['source'] = i['mblog']['source']
                self.contents.append(content)
            page+=1
            self.weibo(page)
        else:
            for i in self.json_res['data']['cards']:
                content = {}
                content['created_at'] = i['mblog']['created_at']
                content['text'] = i['mblog']['text']
                # 点赞
                content['attitudes_sum'] = i['mblog']['attitudes_count']
                # 评论
                content['comments_sum'] = i['mblog']['comments_count']
                # 转发
                content['reposts_sum'] = i['mblog']['reposts_count']
                # 来源
                content['source'] = i['mblog']['source']
                self.contents.append(content)
                if i['mblog']['created_at'] ==self.day30_time.strftime('%m-%d'):
                    break_num+=1
                    break
            if break_num==1:
                print('ok')
            else:
                page += 1
                self.weibo(page)
    def write(self):
        self.filename='weibo_spider.json'
        with open(self.filename,'w',encoding='utf-8') as f:
            json.dump(self.contents,f,ensure_ascii=False)
            print('存储成功')
if __name__=="__main__":
    weibo_spider()