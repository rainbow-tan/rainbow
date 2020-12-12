/*
Navicat MySQL Data Transfer

Source Server         : rainbow
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : storemanagement

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-12-08 22:58:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `cangku`
-- ----------------------------
DROP TABLE IF EXISTS `cangku`;
CREATE TABLE `cangku` (
  `bianhao` varchar(10) NOT NULL,
  `mingchen` varchar(50) NOT NULL,
  `dizhi` varchar(100) DEFAULT '',
  `chengli` varchar(50) DEFAULT '',
  `guanliyuan` varchar(20) DEFAULT '',
  `lianxifangshi` varchar(20) DEFAULT '',
  PRIMARY KEY (`bianhao`,`mingchen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cangku
-- ----------------------------
INSERT INTO `cangku` VALUES ('1001', '海南青协管理库房', '海南协力大街102号', '2012/02/10', '李成', '15635214897');
INSERT INTO `cangku` VALUES ('1002', '鼓楼智能管理仓库', '鼓楼4层', '2015/01/03', '小李', '15425684589');
INSERT INTO `cangku` VALUES ('1003', '北海道火鸡库房管理', '北海道火鸡大街12-15号', '2015-12-03', '李琦', '15489759532');
INSERT INTO `cangku` VALUES ('1004', '太能制造仓库管理有限公司', '广东省合理县五大街12', '2014-1-3', '高瑞', '15478951254');
INSERT INTO `cangku` VALUES ('1045', '火星大数据管理中心', '火星大鹏街企划楼4楼', '1996-12-06', '李飞鱼', '0873-1258457');

-- ----------------------------
-- Table structure for `changjia`
-- ----------------------------
DROP TABLE IF EXISTS `changjia`;
CREATE TABLE `changjia` (
  `bianhao` varchar(20) NOT NULL,
  `mingchen` varchar(50) NOT NULL,
  `xingzhi` varchar(20) DEFAULT '',
  `dizhi` varchar(100) DEFAULT '',
  `lianxiren` varchar(20) DEFAULT '',
  `lianxifangshi` varchar(20) DEFAULT '',
  PRIMARY KEY (`bianhao`,`mingchen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of changjia
-- ----------------------------
INSERT INTO `changjia` VALUES ('1001', '湖南连衣帽供应商', '私人企业', '湖南省骆驼山乌龙大街123号', '皮卡丘', '15987456213');
INSERT INTO `changjia` VALUES ('1002', '青岛服装有限公司', '国企', '青岛四排街54号', '哈雷', '0862-5487512');
INSERT INTO `changjia` VALUES ('1003', '广东MM服饰有限责任公司', '台资', '广东省阿里县', '阿狸', '14857958523');
INSERT INTO `changjia` VALUES ('1004', '四舅妈西服供应商', '私企', '河北省大巴市龙街189号', '比利', '1258475954');
INSERT INTO `changjia` VALUES ('1005', '西风南开服饰专卖', '加盟店', '天津复烤厂大街45-96号', '韩梅梅', '0875-5487512');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('admin', 'admin');
INSERT INTO `user` VALUES ('nick', '123456');

-- ----------------------------
-- Table structure for `yifu`
-- ----------------------------
DROP TABLE IF EXISTS `yifu`;
CREATE TABLE `yifu` (
  `mingcheng` varchar(20) NOT NULL DEFAULT '',
  `jiage` float DEFAULT NULL,
  `jijie` varchar(20) DEFAULT '',
  `changjia` varchar(50) DEFAULT '',
  `yuangong` varchar(20) DEFAULT '',
  `canku` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mingcheng`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yifu
-- ----------------------------
INSERT INTO `yifu` VALUES ('17岁青少年夹克', '99', '春、夏', '广东MM服饰有限责任公司', '高丽', '北海道火鸡库房管理');
INSERT INTO `yifu` VALUES ('冬季保暖贴身羽绒服', '1200', '冬季', '广东MM服饰有限责任公司', '李明亮', '北海道火鸡库房管理');
INSERT INTO `yifu` VALUES ('贴心暖宝宝', '40', '冬季', '四舅妈西服供应商', '李明亮', '鼓楼智能管理仓库');
INSERT INTO `yifu` VALUES ('韩版潮流羊绒外套', '1200', '秋季', '广东MM服饰有限责任公司', '梨花', '鼓楼智能管理仓库');

-- ----------------------------
-- Table structure for `yuangong`
-- ----------------------------
DROP TABLE IF EXISTS `yuangong`;
CREATE TABLE `yuangong` (
  `bianhao` varchar(20) NOT NULL,
  `xingming` varchar(20) NOT NULL,
  `xingbie` varchar(10) DEFAULT '',
  `zhiwei` varchar(20) DEFAULT '',
  `xingzi` float DEFAULT NULL,
  `lianxifangshi` varchar(20) DEFAULT '',
  PRIMARY KEY (`bianhao`,`xingming`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yuangong
-- ----------------------------
INSERT INTO `yuangong` VALUES ('1025', '何怡情', '女', '导购员', '4021', '14875845962');
INSERT INTO `yuangong` VALUES ('125498', '李明亮', '男', '导购员', '3000', '1785412546');
INSERT INTO `yuangong` VALUES ('145845', '梨花', '女', '经理', '5000', '15487856584');
INSERT INTO `yuangong` VALUES ('1547', '高丽', '女', '经理', '8400', '15968457421');
INSERT INTO `yuangong` VALUES ('1548', '白鸽', '女', '普工', '5210', '154265877451');
