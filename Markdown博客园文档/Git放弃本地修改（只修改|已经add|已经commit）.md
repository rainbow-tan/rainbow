### 1、本地文件已经修改，但是没有使用git add .命令，此时通过git status查看（**只修改**）

<img src="/Users/tiger/Library/Application Support/typora-user-images/image-20210906154403084.png" alt="image-20210906154403084" style="zoom:50%;" />

可以通过以下命令放弃修改

- 放弃单个文件


```
git restore bootstrap表格/隔行变色的表格.html
```
- 放弃整个文件夹

```
git restore bootstrap表格
```
- 放弃所有修改

```
git restore .
```

### 2、本地代码修改后，使用了git add .命令，此时通过git status查看（**已经add**）

<img src="/Users/tiger/Library/Application Support/typora-user-images/image-20210906155202538.png" alt="image-20210906155202538" style="zoom:50%;" />

可以通过以下命令放弃修改，放弃后会回到第一步，修改的代码不会被删除。

- 放弃单个文件

```
git restore --staged bootstrap表格/隔行变色的表格.html
```
- 放弃整个文件夹

```
git restore --staged bootstrap表格
```
- 放弃所有修改

```
git restore --staged .
```

### 3、本地代码修改后，使用了git add .命令和git commit -m命令，此时通过git status查看（**已经commit**）<img src="/Users/tiger/Library/Application Support/typora-user-images/image-20210906161204390.png" alt="image-20210906161204390" style="zoom:50%;" />

可以通过以下命令放弃修改

```
git reset HEAD^
```

备注：此时仅保存了修改(恢复到了第一步)

<img src="/Users/tiger/Library/Application Support/typora-user-images/image-20210906162913566.png" alt="image-20210906162913566" style="zoom:50%;" />

