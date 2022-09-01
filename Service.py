from SQL import DBUtil
import pygame


class MyService:
    def __init__(self):
        self.user = None

    # 用户登录
    def login(self, uname, passwords):
        sql = 'select * from TK_user where uname=%s and passwords=%s'
        self.user = DBUtil().query_one(sql, uname, passwords)
        if self.user:
            return True
        else:
            return False

            # 查询音乐id

    def music_id(self, music_name):
        sql = "select * from TK_music where music_name=%s"
        return DBUtil().query_one(sql, music_name)

    # 扫描t_music,将音乐名全部导出
    def find_mname(self):
        sql = "select m.music_name from TK_music m,TK_list t where m.id=t.mid and t.uid=%s"
        return DBUtil().query_all(sql, self.user[0])

    # 播放音乐
    def play_music(self, mname):
        # 查询音乐路径
        sql = 'select path from TK_music where music_name=%s'
        path = DBUtil().query_one(sql, mname)
        print(path)
        # 播放音乐
        pygame.mixer.init()
        pygame.mixer.music.load(path[0])
        pygame.mixer.music.play()

    # 加入音乐
    def add_music(self, files):
        # print('123')
        print(files)

        for f in files:
            start = f.rfind('/') + 1
            end = f.rfind('.mp3')
            music_name = f[start:end]
            path = f

            # sql = "select * from TL_music where music_name=%s"
            # music = DBUtil().query_one(sql,music_name)
            music = self.music_id(music_name)
            if music:
                print('音乐库已经有这首歌啦')
                sql = 'select * from TK_list where mid=%s and uid=%s'
                TK_list = DBUtil().query_one(sql, music[0], self.user[0])
                if not TK_list:
                    print('该用户还没有这首歌')
                    sql = 'insert into TK_list(mid,uid) values(%s,%s)'
                    DBUtil().exeDML(sql, music[0], self.user[0])
            else:
                # 导入音乐库没有的音乐
                print('音乐库里没有这首歌,写入开始')
                sql = 'insert into TK_music(music_name,path) values(%s,%s)'
                DBUtil().exeDML(sql, music_name, path)
                print('写入结束,开始写入关系表')
                # 导入关系表，用户添加记录
                music = self.music_id(music_name)
                sql = 'insert into TK_list(mid,uid) values(%s,%s)'
                print(music)
                print(self.user)
                DBUtil().exeDML(sql, music[0], self.user[0])
                print('结束')
        print('结束 ')

        # 删除音乐

    def del_list(self, mname):
        # 查询要删除的音乐
        music = self.music_id(mname)
        # 删除用户关系表
        sql = 'delete from TK_list where mid=%s and uid=%s'
        DBUtil().exeDML(sql, music[0], self.user[0])

        sql = 'select mid from TK_list where mid=%s'
        mid = DBUtil().query_one(sql, music[0])
        print('删除', mid)
        if mid == None:
            print('已无用户拥有这首歌，删除音乐表中该音乐')
            sql = 'delete from TK_music where id=%s'
            DBUtil().exeDML(sql, music[0])
