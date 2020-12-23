/*
Navicat MySQL Data Transfer

Source Server         : rainbow
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : datacenter

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-12-22 20:22:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `employee`
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `hiredate` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `pay` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES ('1', '1001', '张良', '男', '2015-07-12', '策划师', '8000');
INSERT INTO `employee` VALUES ('16', '1002', '焰灵姬', '女', '2014-05-08', '销售经理', '6500');
INSERT INTO `employee` VALUES ('18', '1003', '卫庄', '男', '2015-01-04', '普工', '8600');
INSERT INTO `employee` VALUES ('20', '1004', '紫玉', '女', '2020-01-15', '项目经理', '8000');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('21', 'admin', 'admin');
INSERT INTO `user` VALUES ('32', 'root', 'root');
INSERT INTO `user` VALUES ('33', 'A', 'admin');
