   
# sql语法与分类

## 1. 数据定义语言DDL

DDL((Data Definition Language)，用于定义/修改/删除数据对象(如表)的数据结构，或者说，DDL语言操作的对象是数据库中的对象而非对象所包含的数据。

DDL包含以下语句：
```
CREATE : 在数据库中创建新的数据对象
ALTER : 修改数据库中对象的数据结构
DROP : 删除数据库中的对象
DISABLE/ENABLE TRIGGER : 修改触发器的状态
UPDATE STATISTIC : 更新表/视图统计信息
TRUNCATE TABLE : 清空表中数据
COMMENT : 给数据对象添加注释
RENAME : 更改数据对象名称
```

## 2. 数据操作语言DML

DML(Data Manipulation Language)，用于添加/修改/查询数据库中数据。

DML包含以下语句：
```
INSERT ：将数据插入到表或视图
DELETE ：从表或视图删除数据
SELECT ：从表或视图中获取数据
UPDATE ：更新表或视图中的数据
MERGE ： 对数据进行合并操作(插入/更新/删除)
```


## 3. 数据控制语言DCL

DCL(Data Control Language)用来向用户赋予/取消对数据对象的控制权限。

DCL包含以下语句：
```
GRANT : 赋予用户某种控制权限
REVOKE ：取消用户某种控制权限
```

## 4. 事务控制语言(TCL)



TCL(Transaction Control Language)用来对事务进行管理。

TCL包含以下语句：
```
COMMIT : 保存已完成事务动作结果
SAVEPOINT : 保存事务相关数据和状态用以可能的回滚操作
ROLLBACK : 恢复事务相关数据至上一次COMMIT操作之后
SET TRANSACTION : 设置事务选项
根据语句操作目标的不同，还是很好区分这四种类型：DDL－数据对象; DML－数据; DCL－权限； TCL－事务。
```

唯一需要注意的是TRUNCATE，尽管从功能上看相当于DELETE表中所有数据，但由于它所操作的对象是table这个级别而非row（如由于某种原因不能立即删除表数据时，TRUNCATE会锁定整张表，而DELETE锁定的则是row)，所以归在DDL中。
