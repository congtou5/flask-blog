# flask-blog
# 学习《Flask Web开发》的代码

#存在问题：点击邮件链接确认账号后，confirmed还是False，编辑的资料不能保存，数据库不知道哪里出问题了
解决：db.add后未加上db.commit，即数据添加后却没有提交，不过书籍上都没有db.commit却能提交数据， 有待解决
