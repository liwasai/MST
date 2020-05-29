1.django 中当一个用户登录 A 应用服务器（进入登录状态），然后下次请求被 nginx 代理到 B 应用服务器会出现什么影响？

如果用户在A应用服务器登陆的session数据没有共享到B应用服务器，纳米之前的登录状态就没有了。

2.跨域请求问题django怎么解决的（原理）

启用中间件

post请求

验证码

表单中添加{%csrf_token%}标签

3.请解释或描述一下Django的架构

对于Django框架遵循MVC设计，并且有一个专有名词：MVT

M全拼为Model，与MVC中的M功能相同，负责数据处理，内嵌了ORM框架

V全拼为View，与MVC中的C功能相同，接收HttpRequest，业务处理，返回HttpResponse

T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html，内嵌了模板引擎

4.django对数据查询结果排序怎么做，降序怎么做，查询大于某个字段怎么做

排序使用order_by()

降序需要在排序字段名前加-

查询字段大于某个值：使用filter(字段名_gt=值)

5.说一下Django，MIDDLEWARES中间件的作用？

答：中间件是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。