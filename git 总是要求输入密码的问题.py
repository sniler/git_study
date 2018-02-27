git 总是要求输入密码的问题
在github.com上 建立了一个小项目，可是在每次push 的时候，都要输入用户名和密码，很是麻烦

原因是使用了https方式 push

在termail里边 输入 Git remote -v

可以看到形如一下的返回结果

origin httpsgithub.comyuquan0821demo.git (fetch)

origin httpsgithub.comyuquan0821demo.git (push)

下面把它换成ssh方式的。

git remote rm origin
git remote add origin git@github.comyuquan0821demo.git
git push origin