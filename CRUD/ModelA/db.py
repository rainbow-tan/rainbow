def update(table, chejian, chezhan, xiangmu, fenlei, renwuliang):
    objs = table.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu, fenlei=fenlei)
    for obj in objs:
        obj.renwuliang = renwuliang
        obj.save()
